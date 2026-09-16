### cancelPaymentIntent

Cancel a PaymentIntent (POST /v1/payment_intents/{intent}/cancel, 200) while it is requires_payment_method, requires_confirmation, requires_action, or requires_capture; an uncaptured authorization is released. The cleanup for an open PaymentIntent.

**Adapter:** `cancelPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createPaymentIntent.paymentIntentId |  |
| cancellationReason | string | no |  | abandoned, duplicate, fraudulent, or requested_by_customer |

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

