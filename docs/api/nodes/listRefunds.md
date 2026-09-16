### listRefunds

Page through refunds (GET /v1/refunds, 200), newest first, narrowed to one PaymentIntent or one charge.

**Adapter:** `listRefunds`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |
| paymentIntentId | string | no |  |  |  |
| chargeId | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| refunds | refund[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ amount | integer | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |
| totalAmount | integer | The refunds' amounts added up |

