### createRefund

Refund a payment (POST /v1/refunds, 200), in full or in part, by its PaymentIntent or charge. Card refunds in test mode succeed at once. Refunding more than remains is 400 invalid_request_error on param amount. Refunds can't be deleted.

**Adapter:** `createRefund`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | no | from: createPaymentIntent.paymentIntentId |  |
| chargeId | string | no |  |  |
| amount | integer | no |  | The amount to refund; the whole remaining amount when left out |
| reason | string | no |  | duplicate, fraudulent, or requested_by_customer |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| refundId | string |  |
| status | string |  |
| amount | integer |  |
| currency | string |  |
| paymentIntentId | string | "" for a refund without one |
| chargeId | string |  |
| reason | string | "" for none |
| failureReason | string | Why a failed refund failed; "" otherwise |
| pendingReason | string | Why a pending refund is pending; "" otherwise |
| source | string | metadata.source |

