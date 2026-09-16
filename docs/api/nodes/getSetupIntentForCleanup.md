### getSetupIntentForCleanup

Read a SetupIntent's status for cleanup (GET /v1/setup_intents/{intent}, 200), so the cancel that follows runs only while it can: in requires_payment_method, requires_confirmation, or requires_action. A succeeded or canceled SetupIntent is 400 setup_intent_unexpected_state to a cancel.

**Adapter:** `getSetupIntentForCleanup`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| setupIntentId | string | yes | from: createSetupIntent.setupIntentId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| setupIntentId | string |  |
| status | string |  |

