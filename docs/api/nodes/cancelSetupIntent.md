### cancelSetupIntent

Cancel a SetupIntent (POST /v1/setup_intents/{intent}/cancel, 200) while it is requires_payment_method, requires_confirmation, or requires_action. A succeeded or canceled one is 400 setup_intent_unexpected_state. The cleanup for an open SetupIntent.

**Adapter:** `cancelSetupIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| setupIntentId | string | yes | from: createSetupIntent.setupIntentId |  |
| cancellationReason | string | no |  | abandoned, duplicate, or requested_by_customer |

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

