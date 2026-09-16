# aat-stripe

Stripe's API in test mode as an [AAT](https://github.com/gburgyan/aat) package: an API graph, request templates, and
plans that prove what each operation does against the live test API, validated request by request against Stripe's
own OpenAPI spec.

**Status:** in progress. Covered so far:
- the account, its balance and balance settings, reference data, and events
- customers, with updates, search, balance transactions, and tax IDs, and idempotent requests
- card payments with PaymentIntents: every capture path, every decline, 3D Secure, and refunds
- saved cards: PaymentMethods, SetupIntents, and charging a saved card off session
- bank debits: ACH with microdeposit verification and mandates, and SEPA Direct Debit
- bank transfers into a customer's cash balance, reconciled as they arrive or by hand
- tokens, ConfirmationTokens, and search

Risk, Billing on test clocks, Checkout, Connect, Terminal, Issuing, Tax, and the rest of what test mode can drive come
next.

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
aat run plan drift/funding-instructions.yaml --env test-auto   # a response the spec doesn't describe
aat run show latest                        # what the last run sent and got back
```

### Environments

| Environment | What it does |
|---|---|
| `test` (default) | `Stripe-Version: 2026-08-26.dahlia`, the spec's version, and `oasValidation: strict`: a request or response the spec doesn't allow fails the step |
| `test-ci` | `test`, with request starts at least 60 ms apart for long batches |
| `test-auto` | `test`, with spec findings reported rather than failing a step, for [drift/funding-instructions](drift/funding-instructions.yaml), whose response Stripe's own spec doesn't describe |
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
- **Saved Card** ([workflow](workflows/saved-card.yaml)) saves a customer's card with a SetupIntent confirmed for
  off-session use. It checks the one setup attempt and the PaymentMethod the customer now holds, then charges that
  PaymentMethod with no customer present.
- **ACH Debit** ([workflow](workflows/ach-debit.yaml)) charges a US bank account given by its numbers. The `outcome`
  slot chooses the test account, which decides what the bank does: it pays, it has no money, or it is closed. Each
  verifies the microdeposits and then reads the payment until the bank has answered, about 20 seconds later.
- **Bank Transfer** ([workflow](workflows/bank-transfer.yaml)) pays out of a customer's cash balance. The
  `reconciliation` slot chooses automatic, where the payment takes the money as it arrives, or manual, where
  `apply_customer_balance` puts it toward the payment in two parts. Both end with the balance at zero.
- **Recipes:** the plans in [`plans/payments/`](plans/payments/), [`plans/declines/`](plans/declines/),
  [`plans/ach/`](plans/ach/), and [`plans/cash-balance/`](plans/cash-balance/) are mostly recipes of a few lines that
  choose a slot, and [saved-card](plans/setup-intents/saved-card.yaml) names its workflow.
- **Layers** ([`layers/`](layers/)) swap the card brand, the currency, or the amount without editing a plan.
- **Full plans:** refunds, 3D Secure, incremental authorization, updates, customer search, balances, and tax IDs,
  PaymentMethods, SetupIntents' states and refusals, ACH and SEPA, the cash balance, tokens, ConfirmationTokens,
  search, and the guards.

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
| `POST /v1/customers` | `createCustomer` | [lifecycle](plans/customers/lifecycle.yaml), [replay](plans/idempotency/replay.yaml), [conflict](plans/idempotency/conflict.yaml), every payment, PaymentMethod, and SetupIntent plan |
| `GET /v1/customers/{customer}` | `getCustomer` | [lifecycle](plans/customers/lifecycle.yaml), [conflict](plans/idempotency/conflict.yaml) |
| `POST /v1/customers/{customer}` | `updateCustomer` | [update-and-search](plans/customers/update-and-search.yaml) |
| `GET /v1/customers` | `listCustomers` | [lifecycle](plans/customers/lifecycle.yaml), [customers guard](plans/zz-guard/customers.yaml) |
| `GET /v1/customers/search` | `searchCustomers` | [update-and-search](plans/customers/update-and-search.yaml), polled |
| `DELETE /v1/customers/{customer}` | `deleteCustomer` | [lifecycle](plans/customers/lifecycle.yaml), and cleanup after every plan that creates a customer |
| `POST /v1/customers/{customer}/balance_transactions` | `createCustomerBalanceTransaction` | [balance-transactions](plans/customers/balance-transactions.yaml) |
| `GET /v1/customers/{customer}/balance_transactions/{transaction}` | `getCustomerBalanceTransaction` | [balance-transactions](plans/customers/balance-transactions.yaml) |
| `POST /v1/customers/{customer}/balance_transactions/{transaction}` | `updateCustomerBalanceTransaction` | [balance-transactions](plans/customers/balance-transactions.yaml) |
| `GET /v1/customers/{customer}/balance_transactions` | `listCustomerBalanceTransactions` | [balance-transactions](plans/customers/balance-transactions.yaml) |
| `POST /v1/customers/{customer}/tax_ids` | `createTaxId` | [tax-ids](plans/customers/tax-ids.yaml) |
| `GET /v1/customers/{customer}/tax_ids/{id}` | `getTaxId` | [tax-ids](plans/customers/tax-ids.yaml) |
| `GET /v1/customers/{customer}/tax_ids` | `listTaxIds` | [tax-ids](plans/customers/tax-ids.yaml) |
| `DELETE /v1/customers/{customer}/tax_ids/{id}` | `deleteTaxId` | [tax-ids](plans/customers/tax-ids.yaml), and cleanup |
| `POST /v1/payment_intents` | `createPaymentIntent` | every plan in [payments](plans/payments/), [declines](plans/declines/), and [refunds](plans/refunds/), [saved-card](plans/setup-intents/saved-card.yaml), [authentication](plans/setup-intents/authentication.yaml) |
| `GET /v1/payment_intents/{intent}` | `getPaymentIntent` | every Card Payment and Declined Card plan, [full-refund](plans/refunds/full-refund.yaml), and cleanup |
| `POST /v1/payment_intents/{intent}` | `updatePaymentIntent` | [update-and-list](plans/payments/update-and-list.yaml) |
| `POST /v1/payment_intents/{intent}/confirm` | `confirmPaymentIntent` | every plan in [declines](plans/declines/) |
| `POST /v1/payment_intents/{intent}/capture` | `capturePaymentIntent` | [manual-capture](plans/payments/manual-capture.yaml), [partial-capture](plans/payments/partial-capture.yaml), [three-d-secure](plans/payments/three-d-secure.yaml) |
| `POST /v1/payment_intents/{intent}/cancel` | `cancelPaymentIntent` | [cancel-authorization](plans/payments/cancel-authorization.yaml), [three-d-secure](plans/payments/three-d-secure.yaml), [increment-authorization](plans/payments/increment-authorization.yaml), [authentication](plans/setup-intents/authentication.yaml), and cleanup |
| `POST /v1/payment_intents/{intent}/increment_authorization` | `incrementAuthorization` | [increment-authorization](plans/payments/increment-authorization.yaml), refused |
| `GET /v1/payment_intents` | `listPaymentIntents` | [update-and-list](plans/payments/update-and-list.yaml), [three-d-secure](plans/payments/three-d-secure.yaml), [authentication](plans/setup-intents/authentication.yaml), [PaymentIntents guard](plans/zz-guard/payment-intents.yaml) |
| `POST /v1/refunds` | `createRefund` | every plan in [refunds](plans/refunds/) |
| `GET /v1/refunds/{refund}` | `getRefund` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `POST /v1/refunds/{refund}` | `updateRefund` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `GET /v1/refunds` | `listRefunds` | [partial-refund](plans/refunds/partial-refund.yaml), [refund-reads](plans/refunds/refund-reads.yaml) |
| `GET /v1/charges/{charge}` | `getCharge` | [partial-refund](plans/refunds/partial-refund.yaml), [refund-reads](plans/refunds/refund-reads.yaml) |
| `POST /v1/charges/{charge}` | `updateCharge` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `GET /v1/charges` | `listCharges` | [refund-reads](plans/refunds/refund-reads.yaml) |
| `POST /v1/payment_methods` | `createPaymentMethod` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml) |
| `GET /v1/payment_methods/{payment_method}` | `getPaymentMethod` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml) |
| `POST /v1/payment_methods/{payment_method}` | `updatePaymentMethod` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml) |
| `POST /v1/payment_methods/{payment_method}/attach` | `attachPaymentMethod` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml), [authentication](plans/setup-intents/authentication.yaml) |
| `POST /v1/payment_methods/{payment_method}/detach` | `detachPaymentMethod` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml) |
| `GET /v1/payment_methods` | `listPaymentMethods` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml) |
| `GET /v1/customers/{customer}/payment_methods` | `listCustomerPaymentMethods` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml) |
| `GET /v1/customers/{customer}/payment_methods/{payment_method}` | `getCustomerPaymentMethod` | [attach-and-detach](plans/payment-methods/attach-and-detach.yaml), [saved-card](plans/setup-intents/saved-card.yaml) |
| `POST /v1/setup_intents` | `createSetupIntent` | every plan in [setup-intents](plans/setup-intents/) |
| `GET /v1/setup_intents/{intent}` | `getSetupIntent` | [update-confirm-cancel](plans/setup-intents/update-confirm-cancel.yaml), and cleanup |
| `POST /v1/setup_intents/{intent}` | `updateSetupIntent` | [update-confirm-cancel](plans/setup-intents/update-confirm-cancel.yaml) |
| `POST /v1/setup_intents/{intent}/confirm` | `confirmSetupIntent` | [update-confirm-cancel](plans/setup-intents/update-confirm-cancel.yaml) |
| `POST /v1/setup_intents/{intent}/cancel` | `cancelSetupIntent` | [update-confirm-cancel](plans/setup-intents/update-confirm-cancel.yaml), [authentication](plans/setup-intents/authentication.yaml), and cleanup |
| `GET /v1/setup_intents` | `listSetupIntents` | [update-confirm-cancel](plans/setup-intents/update-confirm-cancel.yaml), [authentication](plans/setup-intents/authentication.yaml), [SetupIntents guard](plans/zz-guard/setup-intents.yaml) |
| `GET /v1/setup_attempts` | `listSetupAttempts` | [saved-card](plans/setup-intents/saved-card.yaml) |
| `POST /v1/payment_methods` (`us_bank_account`) | `createAchPaymentMethod` | every plan in [ach](plans/ach/) |
| `POST /v1/payment_intents` (`us_bank_account`) | `createAchPaymentIntent` | every plan in [ach](plans/ach/) |
| `POST /v1/payment_intents/{intent}/verify_microdeposits` | `verifyPaymentIntentMicrodeposits` | [microdeposit-refusals](plans/ach/microdeposit-refusals.yaml), the ACH Debit recipes |
| `POST /v1/setup_intents` (`us_bank_account`) | `createAchSetupIntent` | [saved-bank-account](plans/ach/saved-bank-account.yaml) |
| `POST /v1/setup_intents/{intent}/verify_microdeposits` | `verifySetupIntentMicrodeposits` | [saved-bank-account](plans/ach/saved-bank-account.yaml) |
| `GET /v1/mandates/{mandate}` | `getMandate` | [saved-bank-account](plans/ach/saved-bank-account.yaml), [direct-debit](plans/sepa/direct-debit.yaml) |
| `POST /v1/payment_methods` (`sepa_debit`) | `createSepaPaymentMethod` | [direct-debit](plans/sepa/direct-debit.yaml) |
| `POST /v1/payment_intents` (`sepa_debit`) | `createSepaPaymentIntent` | [direct-debit](plans/sepa/direct-debit.yaml) |
| `GET /v1/customers/{customer}/cash_balance` | `getCashBalance` | every plan in [cash-balance](plans/cash-balance/) |
| `POST /v1/customers/{customer}/cash_balance` | `updateCashBalance` | [apply-refusals](plans/cash-balance/apply-refusals.yaml), [manual-reconciliation](plans/cash-balance/manual-reconciliation.yaml) |
| `POST /v1/customers/{customer}/funding_instructions` | `createFundingInstructions` | [funding-instructions](drift/funding-instructions.yaml), under `auto` validation |
| `POST /v1/test_helpers/customers/{customer}/fund_cash_balance` | `fundCashBalance` | every plan in [cash-balance](plans/cash-balance/), [refund-gates](plans/refunds/refund-gates.yaml) |
| `GET /v1/customers/{customer}/cash_balance_transactions` | `listCashBalanceTransactions` | [funding-and-refusals](plans/cash-balance/funding-and-refusals.yaml), the Bank Transfer recipes |
| `GET /v1/customers/{customer}/cash_balance_transactions/{transaction}` | `getCashBalanceTransaction` | [funding-and-refusals](plans/cash-balance/funding-and-refusals.yaml) |
| `POST /v1/payment_intents` (`customer_balance`) | `createBankTransferPaymentIntent` | every plan in [cash-balance](plans/cash-balance/), [refund-gates](plans/refunds/refund-gates.yaml) |
| `POST /v1/payment_intents/{intent}/apply_customer_balance` | `applyCustomerBalance` | [apply-refusals](plans/cash-balance/apply-refusals.yaml), [manual-reconciliation](plans/cash-balance/manual-reconciliation.yaml) |
| `POST /v1/tokens` | `createToken` | [tokens](plans/tokens/tokens.yaml) |
| `GET /v1/tokens/{token}` | `getToken` | [tokens](plans/tokens/tokens.yaml) |
| `POST /v1/test_helpers/confirmation_tokens` | `createConfirmationToken` | [confirm-and-save](plans/confirmation-tokens/confirm-and-save.yaml) |
| `GET /v1/confirmation_tokens/{confirmation_token}` | `getConfirmationToken` | [confirm-and-save](plans/confirmation-tokens/confirm-and-save.yaml) |
| `GET /v1/payment_intents/search` | `searchPaymentIntents` | [payment-intents-and-charges](plans/search/payment-intents-and-charges.yaml) |
| `GET /v1/charges/search` | `searchCharges` | [payment-intents-and-charges](plans/search/payment-intents-and-charges.yaml) |
| `POST /v1/refunds/{refund}/cancel` | `cancelRefund` | [refund-gates](plans/refunds/refund-gates.yaml), refused |
| `POST /v1/test_helpers/refunds/{refund}/expire` | `expireRefund` | [refund-gates](plans/refunds/refund-gates.yaml), refused |

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
  `authentication_required` with decline code `authentication_not_handled`. Charged off session, a saved card that
  requires authentication is 402 `authentication_required` with decline code `authentication_required`.
  [three-d-secure](plans/payments/three-d-secure.yaml), [authentication](plans/setup-intents/authentication.yaml)
- **A refused create still makes an object.** Each of these leaves a PaymentIntent open in `requires_payment_method`:
  - the 3D Secure refusal
  - the incremental authorization refusal
  - the off-session authentication refusal

  A declined SetupIntent create leaves its SetupIntent open the same way. No success response names these objects.
  The plans find them under the customer and cancel them; the PaymentIntents guard caught the first one a plan missed.
  [three-d-secure](plans/payments/three-d-secure.yaml),
  [increment-authorization](plans/payments/increment-authorization.yaml),
  [authentication](plans/setup-intents/authentication.yaml)
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
- **Search lags behind lists.** A new customer took 16 to 20 seconds to appear in customer search in two runs, while a
  list shows it at once, so the plan polls with `repeat.until`. An update changes only the fields it sends. Searching
  by a field customers can't be searched by is 400 `invalid_request_error` with no `code` or `param`.
  [update-and-search](plans/customers/update-and-search.yaml)
  - *Probe:* at the moment a search by email alone found the new customer, one by email and `metadata['source']`
    together found nothing.
- **Customer balance.** A credit of 500 leaves a balance of −500, and a debit of 700 then leaves 200. Each is recorded
  as type `adjustment` with the balance after it as `ending_balance`, and the list comes newest first. A credit's
  description and note can change afterward. [balance-transactions](plans/customers/balance-transactions.yaml)
  - *Probe:* an adjustment in EUR on a USD customer was accepted.
- **Tax IDs.** A German `eu_vat` number takes its country from the value and starts with verification `pending`. A
  value that isn't a VAT number is 400 `tax_id_invalid` on param `value`, and deleting a deleted tax ID is 404
  `resource_missing` on param `id`. [tax-ids](plans/customers/tax-ids.yaml)
  - *Probe:* `DE000000000` and `DE111111111` were both still `pending` 3 seconds later.
- **PaymentMethods.** A card from `tok_visa` belongs to no customer until it is attached. Attaching the test ID
  `pm_card_mastercard` makes a new PaymentMethod with an ID of its own. Detaching is for good:
  - attaching it again is 400 `invalid_request_error` with no `code`
  - detaching it again is refused the same way
  - reading it under the customer is 404 on param `customer`

  [attach-and-detach](plans/payment-methods/attach-and-detach.yaml)
  - *Probe:* a raw card number is 402 `invalid_request_error` ("generally unsafe"). Without a customer, the
    PaymentMethods list is empty. A deleted customer's PaymentMethod still reads with the customer's ID.
- **SetupIntents.** Confirmed with a card for off-session use, a SetupIntent succeeds with one setup attempt. The
  customer then holds a new PaymentMethod that pays a PaymentIntent off session.
  - **Without a card,** it waits in `requires_payment_method`, can be updated, and succeeds when confirmed with one.
  - **Canceling works only while it is open.** A succeeded or canceled SetupIntent is 400
    `setup_intent_unexpected_state` with no `param`.
  - **A card that needs authentication on setup** stops it at `requires_action`, with a `redirect_to_url` next action.
  - **A declined card** is 402 `card_declined` / `generic_decline`, with no `param`.

  [saved-card](plans/setup-intents/saved-card.yaml),
  [update-confirm-cancel](plans/setup-intents/update-confirm-cancel.yaml),
  [authentication](plans/setup-intents/authentication.yaml)
- **ACH debits take a mandate, verification, and time.** A debit without `mandate_data` is refused, and still leaves a
  PaymentIntent in `requires_confirmation`. A bank account given by its numbers waits in `requires_action` for
  microdeposits, which on this account are verified by a descriptor code, `SM11AA` in test mode.
  - a wrong code is `payment_method_microdeposit_verification_descriptor_code_mismatch`
  - one amount instead of two is `payment_method_microdeposit_verification_amounts_invalid` on param `amounts`
  - verifying an intent that isn't waiting is `payment_intent_unexpected_state`, or `intent_invalid_state` on a
    SetupIntent

  Verified, the payment goes through `processing` and settles about 20 seconds later, or fails with
  `insufficient_funds` or `account_closed`. [ach](plans/ach/)
- **Mandates.** A SetupIntent's mandate is `multi_use` and stays `active`, and a later off-session debit reuses it with
  nothing to collect again. Stripe records how the customer accepted it, with the IP address and user agent sent as
  `mandate_data`. [saved-bank-account](plans/ach/saved-bank-account.yaml)
- **SEPA Direct Debit.** A euro debit from a test IBAN goes through `processing` and succeeds about 15 seconds later,
  with a mandate that carries a reference. The failing test IBAN is accepted the same way and fails afterward, with
  `payment_intent_payment_attempt_failed` and `incorrect_account_holder_name` on the charge.
  [direct-debit](plans/sepa/direct-debit.yaml)
- **Stripe's own spec doesn't describe one of its responses.** Funding instructions give a customer bank details to pay
  into, two of them for `us_bank_transfer`, `aba` and `swift`, and the same ones again for the same customer. The spec
  says that response's `bank_transfer.type` is `eu_bank_transfer` or `jp_bank_transfer`, so the `us_bank_transfer` the
  live API answers with fails strict validation. Those reads run in
  [drift/funding-instructions](drift/funding-instructions.yaml) under `auto` validation, which reports the finding
  without failing the step; everything else stays strict.
- **Bank transfers and the cash balance.** A test helper pretends a customer's transfer arrived.
  - **Automatic reconciliation** pays as the money is there, or takes part and waits with the `amount_remaining`.
  - **Manual reconciliation** waits for `apply_customer_balance`, which refuses more than remains, another currency, a
    payment already paid, and a payment that isn't a `customer_balance` one. Each application records its own
    `applied_to_payment` transaction, so a balance applied in two parts records two.
  - An amount below 1 is `parameter_invalid_integer`, and an unknown mode is refused on param
    `settings[reconciliation_mode]`.
  - **A customer with a positive cash balance can't be deleted,** so every plan spends it to zero first.

  [cash-balance](plans/cash-balance/)
- **Tokens hold one thing once.** A bank account, a PII number, or a CVC collected again. Naming none is
  `parameter_missing`, naming two is refused, and a raw card number is refused as it is on PaymentMethods. A CVC token
  spent on a payment reads back `used`, and using it again is `token_already_used`, which still leaves a PaymentIntent.
  An unknown token is 400 `resource_missing`, not 404. [tokens](plans/tokens/tokens.yaml)
- **ConfirmationTokens.** The test helper makes what Stripe.js would collect. One lasts 12 hours, previews its payment
  method, and confirms exactly one PaymentIntent: a second is `payment_intent_confirmation_token_invalid`, and a
  `setup_future_usage` that doesn't match the PaymentIntent's is refused on that param. A token that asks to save the
  card leaves the customer holding it. [confirm-and-save](plans/confirmation-tokens/confirm-and-save.yaml)
- **Search lags the lists, everywhere.** A new PaymentIntent took about 30 seconds to appear in search, while charges
  were in the index sooner. Queries compare amounts (`amount>1500`), read metadata, and page with the previous
  response's `next_page`. A field that can't be searched is 400 with no code, and no query at all is 400
  `parameter_missing` on param `query`. [payment-intents-and-charges](plans/search/payment-intents-and-charges.yaml)
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
| Strict OpenAPI validation | Every node names its operation in Stripe's own spec, and `test` checks each request and response against it: 200 requests and 516 responses in a full batch, with 1 violation — the step that sends a reconciliation mode the spec's enum doesn't allow, on purpose. A step that expects to fail never fails on a violation |
| Workflows, slots, and recipes | Card Payment's `capture` slot and Declined Card's `decline` slot, with most payment plans as recipes of a few lines |
| Layers | Card brands, currencies (yen is zero-decimal), and amounts, each changing only the inputs it names |
| Offsets on references | `amountToCapture: "{{authorize.amount - 500}}"`, a refund of `"{{pay.amount + 1}}"` to prove the limit, and `endingBalance == "{{credit.endingBalance + 700}}"` |
| Refusals checked in full | Every expected failure asserts `type`, `code`, `decline_code`, and `param`, exactly or with `fieldAbsent`, and a decline names its PaymentIntent |
| Cleanup chains with `when` and `releasedBy` | A PaymentIntent's or SetupIntent's cleanup reads its status and cancels it only while it is open; a plan's own cancel or delete releases it, and a replayed create registers no delete |
| Selection filters that read earlier steps | `filter: 'objectId == "{{create.customerId}}"'` finds the customer's event, and `id != "{{create.paymentIntentId}}"` the PaymentIntent a refused create left open |
| Inputs named for what they hold | `/v1/customers/{{customerId}}` fills the spec's `{customer}`, and `starting_after={{startingAfter}}` its query parameter |
| Headers as outputs | `createCustomer` reads `Idempotent-Replayed`, `Original-Request`, `Request-Id`, and `Stripe-Version` |
| Paging with `repeat.next` | Stripe lists page with `next: {startingAfter: lastId}` and stop on `until: hasMore == false` |
| Polling with `repeat.until` | Search, which lags behind lists, is read every 2 seconds `until: count >= 1`, and a bank debit every 3 seconds `until: status != "processing"` |
| Test helpers as nodes | `fund_cash_balance`, `confirmation_tokens`, and the refund `expire` helper are nodes like any other, so a plan drives what only test mode can do |
| Guards | [`zz-guard/`](plans/zz-guard/) reads every page since `packageEpoch` and fails on a customer, an open PaymentIntent, or an open SetupIntent of ours left behind |
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
  - refunds of bank transfer payments, which have to collect the customer's bank details by email: that needs a
    verified account email, so Stripe refuses them here. Refund cancel and the refund expire helper work only on those
    refunds, so both are covered by their refusals on a card refund
    ([refund-gates](plans/refunds/refund-gates.yaml))
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
workflows/           Card Payment, Declined Card, and Saved Card, and the slots
layers/              card brands, currencies, and amounts
domain.yaml          verified concepts, each naming its plans
plans/               plans the batch runs; zz-guard/ sorts last
drift/               plans for the account-default environment
openapi/spec3.json   Stripe's spec
```
