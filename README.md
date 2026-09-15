# aat-stripe

Stripe's API in test mode as an [AAT](https://github.com/gburgyan/aat) package: an API graph, request templates, and
plans that prove what each operation does against the live test API, validated request by request against Stripe's
own OpenAPI spec.

**Status:** in progress. Covered so far:
- the account, its balance and balance settings, reference data, and events
- customers, and idempotent requests
- card payments with PaymentIntents: every capture path, every decline, 3D Secure, and refunds

Customers' balances, saved payment methods, SetupIntents, ACH, risk, Billing on test clocks, Checkout, Connect,
Terminal, Issuing, Tax, and the rest of what test mode can drive come next.

## Getting started

### What you need

- **`aat` built from source.** The package uses features that aren't in a release yet:
  - path and query inputs named apart from the spec's parameters (gburgyan/aat#21)
  - the `fieldAbsent` assertion (gburgyan/aat#22)
  - selection filters that read an earlier step's output (gburgyan/aat#23)
  - offsets on references, and step values that read an earlier step's output (gburgyan/aat#24)
- **A Stripe account in test mode,** based in the US, with a test secret key (`sk_test_…`).
  - Every node that creates an object fails a response whose `livemode` is true, so a live key stops at its first
    object.
  - Every object the package creates carries `metadata[source]=aat-stripe`.
- **In the Dashboard,** for the phases that need them:
  - Connect, with a platform profile
  - Issuing
  - Tax, with a head office address, which can't be removed once set
  - a Radar rule that sends elevated-risk payments to review

### Run it

```bash
export STRIPE_API_KEY=sk_test_...          # the variable the Stripe CLI reads
aat validate --strict                      # graph, templates, workflows, plans, and the spec, without a request
aat run batch --env test-ci                # every plan, paced, with the guards last
aat run plan payments/partial-capture      # one plan
aat run plan payments/manual-capture --layer card-amex --layer currency-jpy
aat run plan drift/account-default.yaml --env account-default
aat run show latest                        # what the last run sent and got back
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

## How the plans fit together

- **Card Payment** ([workflow](workflows/card-payment.yaml)) reads the balance first, which must be in test mode, and
  creates a customer. The `capture` slot pays: Automatic Capture, Manual Capture, Partial Capture, or Cancel
  Authorization. Then the PaymentIntent is read back, and its charge must have the card brand the plan expected.
- **Declined Card** ([workflow](workflows/declined-card.yaml)) creates a PaymentIntent without a card. The `decline`
  slot confirms it with a card that fails, and asserts Stripe's exact error. The PaymentIntent stays open with the
  decline recorded, and a working card pays it.
- **Recipes:** the plans in [`plans/payments/`](plans/payments/) and [`plans/declines/`](plans/declines/) are mostly
  recipes of a few lines that choose a slot.
- **Layers** ([`layers/`](layers/)) swap the card brand, the currency, or the amount without editing a plan.
- **Full plans:** refunds, 3D Secure, incremental authorization, updates, and the guards.

## What's exercised

### Operations

| Operation | Node | Plans |
|---|---|---|
| `GET /v1/account` | `getAccount` | [account-and-balance](plans/account/account-and-balance.yaml) |
| `GET /v1/balance` | `getBalance` | [account-and-balance](plans/account/account-and-balance.yaml), every Card Payment and Declined Card plan |
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
| `POST /v1/customers` | `createCustomer` | [lifecycle](plans/customers/lifecycle.yaml), [replay](plans/idempotency/replay.yaml), [conflict](plans/idempotency/conflict.yaml), every payment plan |
| `GET /v1/customers/{customer}` | `getCustomer` | [lifecycle](plans/customers/lifecycle.yaml), [conflict](plans/idempotency/conflict.yaml) |
| `GET /v1/customers` | `listCustomers` | [lifecycle](plans/customers/lifecycle.yaml), [customers guard](plans/zz-guard/customers.yaml) |
| `DELETE /v1/customers/{customer}` | `deleteCustomer` | [lifecycle](plans/customers/lifecycle.yaml), and cleanup after every plan that creates a customer |
| `POST /v1/payment_intents` | `createPaymentIntent` | every plan in [payments](plans/payments/), [declines](plans/declines/), and [refunds](plans/refunds/) |
| `GET /v1/payment_intents/{intent}` | `getPaymentIntent` | every Card Payment and Declined Card plan, [full-refund](plans/refunds/full-refund.yaml), and cleanup |
| `POST /v1/payment_intents/{intent}` | `updatePaymentIntent` | [update-and-list](plans/payments/update-and-list.yaml) |
| `POST /v1/payment_intents/{intent}/confirm` | `confirmPaymentIntent` | every plan in [declines](plans/declines/) |
| `POST /v1/payment_intents/{intent}/capture` | `capturePaymentIntent` | [manual-capture](plans/payments/manual-capture.yaml), [partial-capture](plans/payments/partial-capture.yaml), [three-d-secure](plans/payments/three-d-secure.yaml) |
| `POST /v1/payment_intents/{intent}/cancel` | `cancelPaymentIntent` | [cancel-authorization](plans/payments/cancel-authorization.yaml), [three-d-secure](plans/payments/three-d-secure.yaml), [increment-authorization](plans/payments/increment-authorization.yaml), and cleanup |
| `POST /v1/payment_intents/{intent}/increment_authorization` | `incrementAuthorization` | [increment-authorization](plans/payments/increment-authorization.yaml), refused |
| `GET /v1/payment_intents` | `listPaymentIntents` | [update-and-list](plans/payments/update-and-list.yaml), [three-d-secure](plans/payments/three-d-secure.yaml), [PaymentIntents guard](plans/zz-guard/payment-intents.yaml) |
| `POST /v1/refunds` | `createRefund` | every plan in [refunds](plans/refunds/) |
| `GET /v1/refunds/{refund}` | `getRefund` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `POST /v1/refunds/{refund}` | `updateRefund` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `GET /v1/refunds` | `listRefunds` | [partial-refund](plans/refunds/partial-refund.yaml), [refund-reads](plans/refunds/refund-reads.yaml) |
| `GET /v1/charges/{charge}` | `getCharge` | [partial-refund](plans/refunds/partial-refund.yaml), [refund-reads](plans/refunds/refund-reads.yaml) |
| `POST /v1/charges/{charge}` | `updateCharge` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `GET /v1/charges` | `listCharges` | [refund-reads](plans/refunds/refund-reads.yaml) |

## What Stripe does in test mode

Each item names the plan that asserts it. Items marked *probe* were seen in one-off requests and aren't asserted yet.

- **Declines, exactly.** Each is 402 `card_error` naming the PaymentIntent, which stays `requires_payment_method` with
  the error recorded, and a working card then pays it.

  | Test card | `code` | `decline_code` | `param` | `advice_code` |
  |---|---|---|---|---|
  | `pm_card_visa_chargeDeclined` | `card_declined` | `generic_decline` | — | `try_again_later` |
  | `pm_card_visa_chargeDeclinedInsufficientFunds` | `card_declined` | `insufficient_funds` | — | `try_again_later` |
  | `pm_card_visa_chargeDeclinedLostCard` | `card_declined` | `lost_card` | — | `do_not_try_again` |
  | `pm_card_visa_chargeDeclinedStolenCard` | `card_declined` | `stolen_card` | — | `do_not_try_again` |
  | `pm_card_chargeDeclinedExpiredCard` | `expired_card` | `expired_card` | `exp_month` | `confirm_card_data` |
  | `pm_card_chargeDeclinedIncorrectCvc` | `incorrect_cvc` | `incorrect_cvc` | `cvc` | `confirm_card_data` |
  | `pm_card_chargeDeclinedProcessingError` | `processing_error` | `processing_error` | — | `try_again_later` |
  | `pm_card_chargeDeclinedFraudulent` | `card_declined` | `fraudulent` | — | — |

  [declines](plans/declines/)
- **Capture.** A manual-capture PaymentIntent waits in `requires_capture` with its whole amount capturable. Capturing
  all but 500 receives that much, releases the rest, and ends `succeeded` with nothing left to capture. Canceling
  instead ends `canceled` with the reason given.
  [manual-capture](plans/payments/manual-capture.yaml), [partial-capture](plans/payments/partial-capture.yaml),
  [cancel-authorization](plans/payments/cancel-authorization.yaml)
- **3D Secure.** A card that requires it stops at `requires_action` with a `redirect_to_url` next action, and capturing
  it then is 400 `payment_intent_unexpected_state`. With `error_on_requires_action`, the create is 402
  `authentication_required` with decline code `authentication_not_handled`.
  [three-d-secure](plans/payments/three-d-secure.yaml)
- **A refused create still makes a PaymentIntent.** The 3D Secure refusal and the incremental authorization refusal
  each leave one open in `requires_payment_method`, and no success response names it. The plans find it under the
  customer and cancel it; the PaymentIntents guard caught the first one a plan missed.
  [three-d-secure](plans/payments/three-d-secure.yaml),
  [increment-authorization](plans/payments/increment-authorization.yaml)
- **Refunds.** Card refunds succeed at once. Two partial refunds add up to the payment and leave the charge refunded.
  Stripe refuses:
  - more than was paid: 400 on param `amount`, with no code
  - a second full refund: 400 `charge_already_refunded`
  - an authorization that wasn't captured: 400 with no code or param, telling you to cancel the PaymentIntent

  [full-refund](plans/refunds/full-refund.yaml), [partial-refund](plans/refunds/partial-refund.yaml),
  [refund-limits](plans/refunds/refund-limits.yaml)
- **Incremental authorization is gated on this account.** Asking for it is 400 `payment_intent_invalid_parameter`
  ("not eligible for the requested card features"). Incrementing an authorization that didn't ask for it is 400 with
  no code. [increment-authorization](plans/payments/increment-authorization.yaml)
- **Idempotent replays.** A create sent again with the same `Idempotency-Key` and parameters answers with the first
  customer, with `Idempotent-Replayed: true` and `Original-Request` naming the first request, under a request ID of its
  own. On a first request, `Original-Request` names the request itself. [replay](plans/idempotency/replay.yaml)
- **A reused key is refused.** The same key with other parameters, or on another endpoint, is 400 `idempotency_error`
  with no `code`, `param`, or `decline_code`, and changes nothing. [conflict](plans/idempotency/conflict.yaml)
  - *Probe:* a replay still answers after its customer is deleted, and a replay without the `Stripe-Version` header
    still replays.
- **Balance settings.** An activated account can't change `payments[debit_negative_balances]` through the API, even to
  the value it already has: 400 on that param, with no code. The payout interval is accepted.
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
| Strict OpenAPI validation | Every node names its operation in Stripe's own spec, and `test` checks each request and response against it: 88 requests and 199 responses in a full batch, with 0 violations |
| Workflows, slots, and recipes | Card Payment's `capture` slot and Declined Card's `decline` slot, with most payment plans as recipes of a few lines |
| Layers | Card brands, currencies (yen is zero-decimal), and amounts, each changing only the inputs it names |
| Offsets on references | `amountToCapture: "{{authorize.amount - 500}}"`, and a refund of `"{{pay.amount + 1}}"` to prove the limit |
| Refusals checked in full | Every expected failure asserts `type`, `code`, `decline_code`, and `param`, exactly or with `fieldAbsent`, and a decline names its PaymentIntent |
| Cleanup chains with `when` and `releasedBy` | A PaymentIntent's cleanup reads its status and cancels it only while it is open; a plan's own cancel releases it, and a replayed create registers no delete |
| Selection filters that read earlier steps | `filter: 'objectId == "{{create.customerId}}"'` finds the customer's event, and `id != "{{create.paymentIntentId}}"` the PaymentIntent a refused create left open |
| Inputs named for what they hold | `/v1/customers/{{customerId}}` fills the spec's `{customer}`, and `starting_after={{startingAfter}}` its query parameter |
| Headers as outputs | `createCustomer` reads `Idempotent-Replayed`, `Original-Request`, `Request-Id`, and `Stripe-Version` |
| Paging with `repeat.next` | Stripe lists page with `next: {startingAfter: lastId}` and stop on `until: hasMore == false` |
| Guards | [`zz-guard/`](plans/zz-guard/) reads every page since `packageEpoch` and fails on a customer or open PaymentIntent of ours left behind |
| Environments | `_stripe` → `_pinned` → `test` → `test-ci`, and `account-default` beside them without the version header |
| Error detection | A create answered with `livemode: true` fails the step |

## Not covered

- **Treasury:** the account isn't onboarded, so its endpoints answer 400 "Unrecognized request URL".
- **Sigma:** closed in test mode.
- **Legacy aliases:**
  - Sources; a customer's `sources`, `cards`, `bank_accounts`, and `subscriptions`
  - Plans; `linked_accounts`; an account's `bank_accounts` and `people`
  - `/v1/balance/history`, the old name of `/v1/balance_transactions`
  - Exchange Rates, deprecated for FX Quotes and answering 404
  - a charge's nested `refund`, `refunds`, and `dispute` paths, which the Refunds and Disputes APIs replace
- **Gated on this account:**
  - incremental authorization (above)
  - Issuing cards, which need a v2 financial account (`financial_account_v2`) that the pinned spec doesn't describe
  - Forwarding (`forwarding_api_inactive`)
  - Radar payment evaluations (404)

## The spec

`openapi/spec3.json` is Stripe's published spec, vendored verbatim from
[stripe/openapi](https://github.com/stripe/openapi) at `2828026bc62e318ed475f0c770e10a07e835ea9e` (2026-09-14), API
version `2026-08-26.dahlia`: git blob `622c8d69a50f470944ab6713c7f27e216cb45d97`, SHA-256
`f0e0fc8fffbffda45bf5f3df59846443c1d47a3cfcbfae232eedf4743124ebee`.

## Repository layout

```
aat-project.yaml     manifest
env.yaml             environments
graph.yaml           nodes, one per operation, and the workflow registry
templates/           one request template per node
workflows/           Card Payment and Declined Card, and their slots
layers/              card brands, currencies, and amounts
domain.yaml          verified concepts, each naming its plans
plans/               plans the batch runs; zz-guard/ sorts last
drift/               plans for the account-default environment
openapi/spec3.json   Stripe's spec
```
