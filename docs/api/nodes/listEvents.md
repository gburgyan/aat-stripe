### listEvents

Page through the account's events (GET /v1/events, 200), newest first, going back 30 days. eventType takes one type, or a group with a wildcard such as customer.*, and createdGte a Unix time. Each event names the object it is about, the API request that caused it, and that request's Idempotency-Key. An event is rendered at the account's default API version, even when the request that caused it pinned another.

**Adapter:** `listEvents`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 | Events per page, 1 to 100 | 1..100 |
| startingAfter | string | no |  | The previous page's lastId |  |
| eventType | string | no |  | Only events of this type, such as customer.created, or a group such as customer.* |  |
| createdGte | integer | no |  | Only events created at or after this Unix time |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| events | event[] |  |
|   └ id | string | elementField |
|   └ type | string | elementField |
|   └ objectId | string | elementField |
|   └ requestId | string | elementField |
|   └ apiVersion | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string | The oldest ID on the page; "" on an empty page |

