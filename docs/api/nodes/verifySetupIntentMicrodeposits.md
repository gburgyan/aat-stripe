### verifySetupIntentMicrodeposits

Verify the microdeposits of an ACH SetupIntent (POST /v1/setup_intents/{intent}/verify_microdeposits, 200), which succeeds it and records its mandate. Verifying one that already succeeded is 400 intent_invalid_state, where a PaymentIntent says payment_intent_unexpected_state.

**Adapter:** `verifySetupIntentMicrodeposits`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| setupIntentId | string | yes | from: createAchSetupIntent.setupIntentId |  |
| descriptorCode | string | no | SM11AA |  |
| amounts | integer[] | no |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| setupIntentId | string |  |
| status | string |  |
| mandateId | string |  |
| paymentMethodId | string |  |
| nextActionType | string |  |
| lastSetupErrorCode | string |  |

