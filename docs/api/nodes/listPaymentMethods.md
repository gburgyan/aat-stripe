### listPaymentMethods

Page through a customer's PaymentMethods of one type (GET /v1/payment_methods, 200), newest first. Without a customer, the list is empty.

**Adapter:** `listPaymentMethods`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 |  | 1..100 |
| customerId | string | no |  |  |  |
| type | string | no | card |  |  |
| startingAfter | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentMethods | paymentMethod[] |  |
|   └ id | string | elementField |
|   └ type | string | elementField |
|   └ cardBrand | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |

