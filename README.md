# aat-stripe

Stripe's API in test mode as an [AAT](https://github.com/gburgyan/aat) package: an API graph, request templates, and
plans that prove what each operation does against the live test API, validated request by request against Stripe's
own OpenAPI spec.

**Status:** in progress. The account, its balance and balance settings, reference data, events, customers, and
idempotent requests are covered. Payments, risk, Billing on test clocks, Checkout, Connect, Terminal, Issuing, Tax, and
the rest of what test mode can drive come next.

## Getting started

### What you need

- **`aat` built from source.** The package uses features that aren't in a release yet:
  - path and query inputs named apart from the spec's parameters (gburgyan/aat#21)
  - the `fieldAbsent` assertion (gburgyan/aat#22)
  - selection filters that read an earlier step's output
- **A Stripe account in test mode,** based in the US, with a test secret key (`sk_test_…`).
  - Every node that creates an object fails a response whose `livemode` is true, so a live key stops at its first
    object.
  - Every object the package creates carries `metadata[source]=aat-stripe`.
- **In the Dashboard,** for the phases that need them: Connect (a platform profile), Issuing, and Tax (a head office
  address, which can't be removed once set).

### Run it

```bash
export STRIPE_API_KEY=sk_test_...        # the variable the Stripe CLI reads
aat validate --strict                    # graph, templates, plans, and the spec, without a request
aat run batch --env test-ci              # every plan, paced, with the guard last
aat run plan account/account-and-balance # one plan
aat run plan drift/account-default.yaml --env account-default
aat run show latest                      # what the last run sent and got back
```

### Environments

| Environment | What it does |
|---|---|
| `test` (default) | `Stripe-Version: 2026-08-26.dahlia`, the spec's version, and `oasValidation: strict`: a request or response the spec doesn't allow fails the step |
| `test-ci` | `test`, with request starts at least 60 ms apart for long batches |
| `account-default` | No `Stripe-Version`, so Stripe answers at the account's default API version; spec findings are reported without failing a step |

`packageEpoch` (a var) is when the package started; the guard plans look at objects created since then.
`webhookUrl` is where webhook plans point, `https://example.com/aat-stripe/webhooks` unless `--var webhookUrl=…` says
otherwise.

## What's exercised

### Operations

| Operation | Node | Plans |
|---|---|---|
| `GET /v1/account` | `getAccount` | [account-and-balance](plans/account/account-and-balance.yaml) |
| `GET /v1/balance` | `getBalance` | [account-and-balance](plans/account/account-and-balance.yaml), [account-default](drift/account-default.yaml) |
| `GET /v1/balance_transactions` | `listBalanceTransactions` | [balance-transactions](plans/account/balance-transactions.yaml) |
| `GET /v1/balance_transactions/{id}` | `getBalanceTransaction` | [balance-transactions](plans/account/balance-transactions.yaml) |
| `GET /v1/balance_settings` | `getBalanceSettings` | [balance-settings](plans/account/balance-settings.yaml), [conflict](plans/idempotency/conflict.yaml) |
| `POST /v1/balance_settings` | `updateBalanceSettings` | [balance-settings](plans/account/balance-settings.yaml), [conflict](plans/idempotency/conflict.yaml) |
| `GET /v1/country_specs` | `listCountrySpecs` | [country-specs](plans/reference/country-specs.yaml) |
| `GET /v1/country_specs/{country}` | `getCountrySpec` | [country-specs](plans/reference/country-specs.yaml) |
| `GET /v1/tax_codes` | `listTaxCodes` | [tax-codes](plans/reference/tax-codes.yaml) |
| `GET /v1/tax_codes/{id}` | `getTaxCode` | [tax-codes](plans/reference/tax-codes.yaml) |
| `GET /v1/events` | `listEvents` | [events](plans/account/events.yaml), [account-default](drift/account-default.yaml) |
| `GET /v1/events/{id}` | `getEvent` | [events](plans/account/events.yaml), [account-default](drift/account-default.yaml) |
| `POST /v1/customers` | `createCustomer` | [lifecycle](plans/customers/lifecycle.yaml), [replay](plans/idempotency/replay.yaml), [conflict](plans/idempotency/conflict.yaml), [events](plans/account/events.yaml) |
| `GET /v1/customers/{customer}` | `getCustomer` | [lifecycle](plans/customers/lifecycle.yaml), [conflict](plans/idempotency/conflict.yaml) |
| `GET /v1/customers` | `listCustomers` | [lifecycle](plans/customers/lifecycle.yaml), [customers guard](plans/zz-guard/customers.yaml) |
| `DELETE /v1/customers/{customer}` | `deleteCustomer` | [lifecycle](plans/customers/lifecycle.yaml), and cleanup after every plan that creates a customer |

## What Stripe does in test mode

Each item names the plan that asserts it. Items marked *probe* were seen in one-off requests and aren't asserted yet.

- **Idempotent replays.** A create sent again with the same `Idempotency-Key` and parameters answers with the first
  customer, with `Idempotent-Replayed: true` and `Original-Request` naming the first request, under a request ID of its
  own. On a first request, `Original-Request` names the request itself. [replay](plans/idempotency/replay.yaml)
- **A reused key is refused.** The same key with other parameters, or on another endpoint, is 400 `idempotency_error`
  with no `code`, `param`, or `decline_code`, and changes nothing. [conflict](plans/idempotency/conflict.yaml)
  - *Probe:* a replay still answers after its customer is deleted, and a replay without the `Stripe-Version` header
    still replays.
- **Balance settings.** An activated account can't change `payments[debit_negative_balances]` through the API, even to
  the value it already has: 400 `invalid_request_error` on that param. The payout interval is accepted.
  [balance-settings](plans/account/balance-settings.yaml)
- **Deleted customers.** A deleted customer drops out of the list but still reads 200, with only `id`, `object`, and
  `deleted: true`; deleting it again is 404 `resource_missing` on param `id`. [lifecycle](plans/customers/lifecycle.yaml)
- **Events and API versions.** A new customer's `customer.created` event names the customer and the request that
  created it. Events are rendered at the account's default API version even when the request pinned another, and
  without a `Stripe-Version` header the response header names that same default. [events](plans/account/events.yaml),
  [account-default](drift/account-default.yaml)
  - *Probe:* an unknown version is 400 `invalid_request_error` with no `code` or `param`; an old one such as
    `2020-08-27` is accepted and echoed.
- **Paging.** `has_more` is false on a last page that still holds items. There are 677 tax codes over 7 pages of 100,
  and 121 country specs. [tax-codes](plans/reference/tax-codes.yaml), [country-specs](plans/reference/country-specs.yaml)
- **Slow reference data.** A page of 100 country specs has taken from under a second to about 20 seconds; the slow
  pages came first after a pause. [country-specs](plans/reference/country-specs.yaml)

## AAT features on display

| Feature | In this package |
|---|---|
| Strict OpenAPI validation | Every node names its operation in Stripe's own spec, and `test` checks each request and response against it |
| Inputs named for what they hold | `/v1/customers/{{customerId}}` fills the spec's `{customer}`, and `starting_after={{startingAfter}}` its query parameter |
| Headers as outputs | `createCustomer` reads `Idempotent-Replayed`, `Original-Request`, `Request-Id`, and `Stripe-Version` |
| Cleanup with `when` | A replayed create registers no delete, so a customer is deleted once |
| Paging with `repeat.next` | Stripe lists page with `next: {startingAfter: lastId}` and stop on `until: hasMore == false` |
| Selection filters that read earlier steps | `filter: 'objectId == "{{create.customerId}}"'` finds the event about the customer a plan created |
| `fieldAbsent` | A refusal asserts the fields Stripe leaves out of its error, such as `code` |
| Guards | [`zz-guard/customers`](plans/zz-guard/customers.yaml) reads every page since `packageEpoch` and fails on a customer of ours left behind |
| Environments | `_stripe` → `_pinned` → `test` → `test-ci`, and `account-default` beside them without the version header |
| Error detection | A create answered with `livemode: true` fails the step |

## Not covered

- **Treasury:** the account isn't onboarded, so its endpoints answer 400 "Unrecognized request URL".
- **Sigma:** closed in test mode.
- **Legacy aliases:** Sources; a customer's `sources`, `cards`, `bank_accounts`, and `subscriptions`; Plans;
  `linked_accounts`; an account's `bank_accounts` and `people`; `/v1/balance/history`, the old name of
  `/v1/balance_transactions`; and Exchange Rates, deprecated for FX Quotes and answering 404.

## The spec

`openapi/spec3.json` is Stripe's published spec, vendored verbatim from
[stripe/openapi](https://github.com/stripe/openapi) at `2828026bc62e318ed475f0c770e10a07e835ea9e` (2026-09-14), API
version `2026-08-26.dahlia`: git blob `622c8d69a50f470944ab6713c7f27e216cb45d97`, SHA-256
`f0e0fc8fffbffda45bf5f3df59846443c1d47a3cfcbfae232eedf4743124ebee`.

## Repository layout

```
aat-project.yaml     manifest
env.yaml             environments
graph.yaml           nodes, one per operation
templates/           one request template per node
domain.yaml          verified concepts, each naming its plans
plans/               plans the batch runs; zz-guard/ sorts last
drift/               plans for the account-default environment
openapi/spec3.json   Stripe's spec
```
