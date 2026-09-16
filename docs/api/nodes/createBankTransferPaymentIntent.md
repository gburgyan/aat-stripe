### createBankTransferPaymentIntent

Take a payment from a customer's cash balance (POST /v1/payment_intents, 200) with payment_method_types customer_balance. With automatic reconciliation and enough money it succeeds at once; with less it takes what there is and waits in requires_action with the amount_remaining, then succeeds when the rest arrives. With manual reconciliation it waits for apply_customer_balance instead.

**Adapter:** `createBankTransferPaymentIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| amount | integer | yes | 2000 |  |
| currency | string | yes | usd |  |
| customerId | string | yes | from: createCustomer.customerId |  |
| bankTransferType | string | yes | us_bank_transfer |  |
| euCountry | string | no |  |  |
| confirm | boolean | no | true |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentIntentId | string |  |
| status | string |  |
| amount | integer |  |
| currency | string |  |
| amountReceived | integer |  |
| livemode | boolean |  |
| customerId | string |  |
| latestChargeId | string |  |
| nextActionType | string |  |
| amountRemaining | integer |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

