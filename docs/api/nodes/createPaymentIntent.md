### createPaymentIntent

Create a PaymentIntent (POST /v1/payment_intents, 200), the object that tracks one payment from creation to capture. Amounts are integers in the currency's smallest unit (cents, or whole yen for jpy). With confirm true it is confirmed at once with the payment method; with capture_method manual a successful confirmation stops at requires_capture. A decline on a confirming create is 402 and leaves no PaymentIntent ID in a success response, so decline plans create first and confirm after. Every PaymentIntent the package creates carries metadata[source]=aat-stripe, and metadata[expected_brand] when a plan names the brand its card should have. Cleanup reads it and cancels it while it is still open.

**Adapter:** `createPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| amount | integer | yes | 2000 | The amount in the currency's smallest unit |
| currency | string | yes | usd |  |
| customerId | string | no | from: createCustomer.customerId |  |
| paymentMethod | string | no | pm_card_visa | A payment method ID, or a test one such as pm_card_visa; {} for none yet |
| paymentMethodTypes | string[] | yes | [card] | The payment method types it accepts |
| captureMethod | string | no |  | automatic (the default), automatic_async, or manual |
| confirm | boolean | no |  |  |
| returnUrl | string | no |  | Where a customer returns after authentication, for redirect-based next actions |
| errorOnRequiresAction | boolean | no |  |  |
| offSession | boolean | no |  |  |
| setupFutureUsage | string | no |  | on_session or off_session, to save the payment method for later |
| confirmationToken | string | no |  | A ctoken_ ID, which carries the payment method instead of paymentMethod |
| cvcToken | string | no |  | A cvctok_ ID, the CVC collected again for a saved card |
| requestIncrementalAuthorization | string | no |  | if_available or never, for a card authorization that may be incremented |
| description | string | no |  |  |
| expectedBrand | string | no | visa | The card brand the plan expects, stored as metadata[expected_brand]; the default card's is visa |
| idempotencyKey | string | no | {{uuid}} | The Idempotency-Key header |

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

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

