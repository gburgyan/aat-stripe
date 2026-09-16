### listSetupAttempts

Page through a SetupIntent's attempts (GET /v1/setup_attempts, 200), newest first; setup_intent is required. A SetupIntent confirmed once has one attempt, with its status and usage.

**Adapter:** `listSetupAttempts`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| setupIntentId | string | yes | from: createSetupIntent.setupIntentId |  |  |
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| attempts | setupAttempt[] |  |
|   └ id | string | elementField |
|   └ status | string | elementField |
|   └ usage | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |
| latestStatus | string | The newest attempt's status; "" with none |

