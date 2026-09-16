### confirmSetupIntent

Confirm a SetupIntent with a payment method (POST /v1/setup_intents/{intent}/confirm, 200). A card succeeds, and the customer gets a new PaymentMethod for it.

**Adapter:** `confirmSetupIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| setupIntentId | string | yes | from: createSetupIntent.setupIntentId |  |
| paymentMethod | string | no |  |  |
| returnUrl | string | no |  |  |
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

