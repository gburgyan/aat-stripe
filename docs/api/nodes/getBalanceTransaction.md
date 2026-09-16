### getBalanceTransaction

Read one balance transaction by its txn_ ID (GET /v1/balance_transactions/{id}, 200). net is the amount less the fee, and source is the ID of the object that moved the balance, such as a ch_ charge or a re_ refund.

**Adapter:** `getBalanceTransaction`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| balanceTransactionId | string | yes | from: listBalanceTransactions.transactions | The txn_ ID |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| balanceTransactionId | string |  |
| transactionType | string |  |
| amount | integer |  |
| fee | integer |  |
| net | integer |  |
| currency | string |  |
| status | string | available or pending |
| reportingCategory | string |  |
| source | string | The ID of the object behind the transaction; "" when there is none |
| created | integer |  |
| availableOn | integer |  |

