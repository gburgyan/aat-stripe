### createCustomerBalanceTransaction

Adjust a customer's balance (POST /v1/customers/{customer}/balance_transactions, 200). A negative amount is a credit the customer's next invoices use, and a positive one a debit added to what they owe; either is recorded as type adjustment, with the balance after it as ending_balance. Balance transactions can't be deleted.

**Adapter:** `createCustomerBalanceTransaction`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| amount | integer | yes |  | Negative for a credit, positive for a debit |
| currency | string | yes | usd |  |
| description | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerBalanceTransactionId | string |  |
| type | string | adjustment for a manual one; others come from invoices, credit notes, and Checkout |
| amount | integer |  |
| currency | string |  |
| endingBalance | integer |  |
| description | string |  |
| note | string |  |
| source | string |  |

