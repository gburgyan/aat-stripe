### searchCharges

Search charges (GET /v1/charges/search, 200) by customer, status, refunded, metadata, or amount. Charges were in the index sooner than PaymentIntents, though a search still lags a list.

**Adapter:** `searchCharges`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| query | string | yes |  |  |  |
| limit | integer | yes | 20 |  | 1..100 |
| page | string | no |  |  |  |

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
| nextPage | string |  |
| firstId | string |  |

