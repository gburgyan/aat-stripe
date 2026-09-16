### updateSetupIntent

Update a SetupIntent's description and metadata note (POST /v1/setup_intents/{intent}, 200).

**Adapter:** `updateSetupIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| setupIntentId | string | yes | from: createSetupIntent.setupIntentId |  |
| description | string | no |  |  |
| note | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| setupIntentId | string |  |
| status | string |  |
| usage | string |  |
| livemode | boolean |  |
| customerId | string |  |
| paymentMethodId | string | The saved PaymentMethod; "" before one is set |
| latestAttemptId | string | The setatt_ ID of the latest attempt; "" before one |
| nextActionType | string |  |
| lastSetupErrorCode | string |  |
| lastSetupErrorDeclineCode | string |  |
| cancellationReason | string |  |
| description | string |  |
| note | string |  |
| source | string |  |

