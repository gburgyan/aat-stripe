### listCharges

Page through charges (GET /v1/charges, 200), newest first, narrowed to one PaymentIntent or one customer.

**Adapter:** `listCharges`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |
| paymentIntentId | string | no |  |  |  |
| customerId | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| charges | charge[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ amount | integer | elementField |
|   └ refunded | boolean | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |

