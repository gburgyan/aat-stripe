### getCustomerBalanceTransaction

Read one of a customer's balance transactions (GET /v1/customers/{customer}/balance_transactions/{transaction}, 200).

**Adapter:** `getCustomerBalanceTransaction`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| customerBalanceTransactionId | string | yes | from: createCustomerBalanceTransaction.customerBalanceTransactionId |  |

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

