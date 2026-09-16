### getPaymentIntentForCleanup

Read a PaymentIntent's status for cleanup (GET /v1/payment_intents/{intent}, 200), so the cancel that follows runs only while it can: in requires_payment_method, requires_confirmation, requires_action, or requires_capture. A succeeded or canceled PaymentIntent is 400 payment_intent_unexpected_state to a cancel.

**Adapter:** `getPaymentIntentForCleanup`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createPaymentIntent.paymentIntentId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |

