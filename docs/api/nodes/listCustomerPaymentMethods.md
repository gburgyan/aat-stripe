### listCustomerPaymentMethods

Page through a customer's PaymentMethods (GET /v1/customers/{customer}/payment_methods, 200), newest first.

**Adapter:** `listCustomerPaymentMethods`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| customerId | string | yes | from: createCustomer.customerId |  |  |
| limit | integer | yes | 10 |  | 1..100 |
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

