### listSetupIntents

Page through SetupIntents (GET /v1/setup_intents, 200), newest first, narrowed to one customer or to those created at or after a Unix time. Each page counts the SetupIntents this package created and those of them still open, and lists the open ones.

**Adapter:** `listSetupIntents`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 |  | 1..100 |
| customerId | string | no |  |  |  |
| createdGte | integer | no |  |  |  |
| startingAfter | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| setupIntents | setupIntent[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |
| ourCount | integer |  |
| ourOpenCount | integer |  |
| ourOpen | openSetupIntent[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ created | integer | elementField |
| liveCount | integer |  |

