### createPaymentMethod

Create a PaymentMethod (POST /v1/payment_methods, 200): a card from a test token such as tok_visa. Sending a raw card number instead is refused (402 invalid_request_error, "generally unsafe"). A new PaymentMethod belongs to no customer, and a PaymentMethod can't be deleted.

**Adapter:** `createPaymentMethod`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| type | string | yes | card |  |
| cardToken | string | no | tok_visa | A test card token, such as tok_visa or tok_mastercard |
| billingName | string | no |  |  |
| billingEmail | string | no |  |  |
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

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

