### updatePaymentIntent

Update a PaymentIntent (POST /v1/payment_intents/{intent}, 200): its amount, while it isn't yet captured, and its description and metadata note.

**Adapter:** `updatePaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createPaymentIntent.paymentIntentId |  |
| amount | integer | no |  |  |
| description | string | no |  |  |
| note | string | no |  | Stored as metadata[note] |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |
| amount | integer |  |
| description | string | "" for none |
| note | string | metadata.note; "" for none |

