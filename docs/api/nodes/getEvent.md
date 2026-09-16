### getEvent

Read one event by its evt_ ID (GET /v1/events/{id}, 200): its type, the API version its data is rendered at, the object it is about, and the request that caused it.

**Adapter:** `getEvent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| eventId | string | yes | from: listEvents.events | The evt_ ID |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| eventId | string |  |
| eventType | string |  |
| apiVersion | string |  |
| livemode | boolean |  |
| created | integer |  |
| objectId | string | The ID of the object the event is about; "" when it has none |
| objectType | string | The object's type, such as customer; "" when absent |
| requestId | string | The req_ ID of the API request behind the event; "" for an event nothing requested |
| idempotencyKey | string | That request's Idempotency-Key; "" when it sent none |

