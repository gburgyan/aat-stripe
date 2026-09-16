### confirmPaymentIntent

Confirm a PaymentIntent with a payment method (POST /v1/payment_intents/{intent}/confirm, 200). Allowed while it is requires_payment_method, requires_confirmation, or requires_action. A declined card is 402 card_error with code and decline_code, and leaves the PaymentIntent requires_payment_method, ready to confirm again with another card.

**Adapter:** `confirmPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createPaymentIntent.paymentIntentId |  |
| paymentMethod | string | no |  |  |
| returnUrl | string | no |  |  |
| errorOnRequiresAction | boolean | no |  |  |
| offSession | boolean | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

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
| customerId | string | The customer's cus_ ID; "" for none |
| paymentMethodId | string | The pm_ ID of the payment method; "" for none |
| latestChargeId | string | The ch_ or py_ ID of the latest charge; "" before a charge |
| cardBrand | string | The latest charge's card brand, such as visa; "" without a card charge |
| nextActionType | string | What the customer must do next, such as redirect_to_url; "" for nothing |
| lastErrorCode | string | The last payment error's code, such as card_declined; "" for none |
| lastDeclineCode | string | The last payment error's decline code, such as insufficient_funds; "" for none |
| cancellationReason | string | Why it was canceled; "" while it isn't |
| expectedBrand | string | metadata.expected_brand; "" when the plan named none |
| source | string | metadata.source, aat-stripe for every PaymentIntent the package creates |

