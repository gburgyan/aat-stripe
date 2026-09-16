### listPaymentIntents

Page through PaymentIntents (GET /v1/payment_intents, 200), newest first, narrowed to one customer or to those created at or after a Unix time. Each page counts the PaymentIntents this package created and those of them still open, and lists the open ones so a guard that fails can name them.

**Adapter:** `listPaymentIntents`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |
| customerId | string | no |  |  |  |
| createdGte | integer | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntents | paymentIntent[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ amount | integer | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |
| ourCount | integer |  |
| ourOpenCount | integer | The package's PaymentIntents in a requires_ state, which cleanup should have canceled |
| ourOpen | openPaymentIntent[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ created | integer | elementField |
| liveCount | integer |  |

