### searchPaymentIntents

Search PaymentIntents (GET /v1/payment_intents/search, 200) by customer, status, metadata, or amount, with comparisons such as amount>1500. Like every Stripe search it lags: new PaymentIntents took about 30 seconds to appear, while the list has them at once. A field that can't be searched is 400 with no code, and no query at all is 400 parameter_missing on param query.

**Adapter:** `searchPaymentIntents`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| query | string | no |  | A search query; {} sends none, which Stripe refuses |  |
| limit | integer | yes | 20 |  | 1..100 |
| page | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntents | paymentIntent[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ amount | integer | elementField |
| count | integer |  |
| hasMore | boolean |  |
| nextPage | string |  |
| firstId | string |  |
| statuses | string[] |  |

