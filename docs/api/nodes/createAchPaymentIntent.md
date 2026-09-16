### createAchPaymentIntent

Charge a US bank account (POST /v1/payment_intents, 200) with payment_method_types us_bank_account. It needs mandate acceptance: without mandate_data the create is 400 and still leaves a PaymentIntent in requires_confirmation. A bank account given by its numbers has to be verified first, so the PaymentIntent waits in requires_action with a verify_with_microdeposits next action, whose microdeposit_type on this account is descriptor_code. Verified, it goes to processing and reaches succeeded in about 20 seconds; a failing test account ends requires_payment_method with the reason as last_payment_error.

**Adapter:** `createAchPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| amount | integer | yes | 1500 |  |
| currency | string | yes | usd |  |
| customerId | string | no | from: createCustomer.customerId |  |
| paymentMethod | string | no | from: createAchPaymentMethod.paymentMethodId |  |
| confirm | boolean | no | true |  |
| offSession | boolean | no |  |  |
| verificationMethod | string | no |  | automatic (the default) or microdeposits |
| acceptanceType | string | no | online | How the customer accepted the mandate; {} sends none, which Stripe refuses |
| acceptanceIp | string | no | 203.0.113.10 |  |
| acceptanceUserAgent | string | no | aat-stripe |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |
| amount | integer |  |
| currency | string |  |
| amountReceived | integer |  |
| livemode | boolean |  |
| customerId | string |  |
| paymentMethodId | string |  |
| latestChargeId | string |  |
| chargeStatus | string |  |
| mandateId | string | The mandate the debit used; "" before the charge exists |
| nextActionType | string |  |
| microdepositType | string | descriptor_code or amounts, the way the deposits are verified |
| lastErrorType | string |  |
| lastErrorCode | string |  |
| lastDeclineCode | string |  |
| chargeFailureCode | string |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

