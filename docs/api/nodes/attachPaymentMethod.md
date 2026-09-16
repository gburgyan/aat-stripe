### attachPaymentMethod

Attach a PaymentMethod to a customer (POST /v1/payment_methods/{payment_method}/attach, 200). Attaching a test PaymentMethod such as pm_card_mastercard makes a new one with an ID of its own. A PaymentMethod that was detached, or used without a customer, can't be attached again (400, with no code).

**Adapter:** `attachPaymentMethod`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentMethodId | string | yes | from: createPaymentMethod.paymentMethodId |  |
| customerId | string | yes | from: createCustomer.customerId |  |
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

