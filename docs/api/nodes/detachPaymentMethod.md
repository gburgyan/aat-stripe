### detachPaymentMethod

Detach a PaymentMethod from its customer (POST /v1/payment_methods/{payment_method}/detach, 200), for good: it can't be attached again. Detaching one that isn't attached is 400 with no code.

**Adapter:** `detachPaymentMethod`

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

