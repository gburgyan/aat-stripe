### getPaymentMethod

Read a PaymentMethod by its pm_ ID (GET /v1/payment_methods/{payment_method}, 200).

**Adapter:** `getPaymentMethod`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentMethodId | string | yes | from: createPaymentMethod.paymentMethodId |  |

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

