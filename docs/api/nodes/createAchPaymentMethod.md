### createAchPaymentMethod

Create a us_bank_account PaymentMethod from a routing and account number (POST /v1/payment_methods, 200). Stripe's test routing number is 110000000, and the account number chooses what the debit does later: 000123456789 succeeds, 000222222227 fails for insufficient funds, and 000111111113 for a closed account. The bank is "STRIPE TEST BANK", and the account is a checking account on the ach network.

**Adapter:** `createAchPaymentMethod`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| routingNumber | string | yes | 110000000 |  |
| accountNumber | string | yes | 000123456789 |  |
| accountHolderType | string | yes | individual |  |
| billingName | string | yes | AAT Stripe |  |
| billingEmail | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentMethodId | string |  |
| type | string |  |
| livemode | boolean |  |
| customerId | string |  |
| bankName | string |  |
| last4 | string |  |
| accountHolderType | string |  |
| accountType | string |  |
| preferredNetwork | string |  |
| billingName | string |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

