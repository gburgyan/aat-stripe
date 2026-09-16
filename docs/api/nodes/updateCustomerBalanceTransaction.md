### updateCustomerBalanceTransaction

Update a customer balance transaction's description and metadata note (POST /v1/customers/{customer}/balance_transactions/{transaction}, 200); its amount can't change.

**Adapter:** `updateCustomerBalanceTransaction`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| customerBalanceTransactionId | string | yes | from: createCustomerBalanceTransaction.customerBalanceTransactionId |  |
| description | string | no |  |  |
| note | string | no |  |  |

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

