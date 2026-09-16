### getPaymentIntent

Read a PaymentIntent with its latest charge expanded (GET /v1/payment_intents/{intent}, 200): its status and amounts, the charge's card brand, country, and funding, the charge's outcome and risk level, and what was refunded. A declined confirmation leaves it requires_payment_method with last_payment_error set; a successful one leaves last_payment_error null.

**Adapter:** `getPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createPaymentIntent.paymentIntentId | The pi_ ID |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |
| amount | integer |  |
| currency | string |  |
| amountCapturable | integer |  |
| amountReceived | integer |  |
| captureMethod | string |  |
| livemode | boolean |  |
| customerId | string |  |
| paymentMethodId | string |  |
| latestChargeId | string |  |
| cardBrand | string |  |
| cardCountry | string | The card's issuing country; "" without a card charge |
| cardFunding | string | credit, debit, prepaid, or unknown; "" without a card charge |
| chargeStatus | string | succeeded, pending, or failed; "" before a charge |
| captured | boolean |  |
| amountRefunded | integer |  |
| refunded | boolean | Whether the latest charge is refunded in full |
| outcomeType | string | authorized, manual_review, issuer_declined, blocked, or invalid; "" before a charge |
| riskLevel | string | normal, elevated, or highest; "" before a charge |
| nextActionType | string |  |
| lastErrorType | string | The last payment error's type, such as card_error; "" for none |
| lastErrorCode | string |  |
| lastDeclineCode | string |  |
| cancellationReason | string |  |
| expectedBrand | string |  |
| source | string |  |

