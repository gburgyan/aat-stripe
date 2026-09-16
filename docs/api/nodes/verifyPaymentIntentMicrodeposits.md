### verifyPaymentIntentMicrodeposits

Verify the microdeposits of an ACH PaymentIntent (POST /v1/payment_intents/{intent}/verify_microdeposits, 200), which moves it from requires_action to processing. In test mode the descriptor code is SM11AA and the amounts are 32 and 45. A wrong code is 400 payment_method_microdeposit_verification_descriptor_code_mismatch, one amount is 400 payment_method_microdeposit_verification_amounts_invalid on param amounts, and verifying a PaymentIntent that isn't waiting is 400 payment_intent_unexpected_state.

**Adapter:** `verifyPaymentIntentMicrodeposits`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createAchPaymentIntent.paymentIntentId |  |
| descriptorCode | string | no | SM11AA |  |
| amounts | integer[] | no |  | The two deposit amounts, instead of a descriptor code |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |
| nextActionType | string |  |
| amountReceived | integer |  |
| lastErrorCode | string |  |

