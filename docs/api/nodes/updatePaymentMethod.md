### updatePaymentMethod

Update a PaymentMethod (POST /v1/payment_methods/{payment_method}, 200): its billing name, whether it may be shown again to its customer, and its metadata note.

**Adapter:** `updatePaymentMethod`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentMethodId | string | yes | from: createPaymentMethod.paymentMethodId |  |
| billingName | string | no |  |  |
| allowRedisplay | string | no |  |  |
| note | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentMethodId | string |  |
| type | string |  |
| livemode | boolean |  |
| customerId | string | The customer it is attached to; "" for none |
| cardBrand | string |  |
| cardLast4 | string |  |
| cardCountry | string |  |
| cardFunding | string |  |
| billingName | string |  |
| allowRedisplay | string | always, limited, or unspecified |
| note | string |  |
| source | string |  |

