### createSepaPaymentIntent

Charge a SEPA bank account in euros (POST /v1/payment_intents, 200), with the IBAN sent as payment_method_data and mandate acceptance. Confirmed, it goes to processing at once and reaches succeeded in about 15 seconds; the failing test IBAN ends requires_payment_method with last_payment_error payment_intent_payment_attempt_failed, whose charge failed with incorrect_account_holder_name.

**Adapter:** `createSepaPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| amount | integer | yes | 1000 |  |
| currency | string | yes | eur |  |
| customerId | string | no | from: createCustomer.customerId |  |
| iban | string | yes | DE89370400440532013000 |  |
| billingName | string | yes | AAT Stripe |  |
| billingEmail | string | yes | aat-stripe@example.com |  |
| confirm | boolean | no | true |  |
| acceptanceType | string | no | online |  |
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
| mandateId | string |  |
| lastErrorType | string |  |
| lastErrorCode | string |  |
| lastDeclineCode | string |  |
| chargeFailureCode | string |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

