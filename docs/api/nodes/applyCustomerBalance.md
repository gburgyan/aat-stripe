### applyCustomerBalance

Put a customer's cash balance toward a payment waiting for it (POST /v1/payment_intents/{intent}/apply_customer_balance, 200), which manual reconciliation needs. Part of the amount leaves the rest as amount_remaining; the rest succeeds it. More than remains is 400 with no code, as is a currency that isn't the payment's, and applying to a succeeded payment is 400 payment_intent_unexpected_state.

**Adapter:** `applyCustomerBalance`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentIntentId | string | yes | from: createBankTransferPaymentIntent.paymentIntentId |  |
| amount | integer | no |  | How much to apply; all that is needed when left out |
| currency | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |
| amount | integer |  |
| amountReceived | integer |  |
| nextActionType | string |  |
| amountRemaining | integer |  |

