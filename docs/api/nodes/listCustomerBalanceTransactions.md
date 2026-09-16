### listCustomerBalanceTransactions

Page through a customer's balance transactions (GET /v1/customers/{customer}/balance_transactions, 200), newest first.

**Adapter:** `listCustomerBalanceTransactions`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| customerId | string | yes | from: createCustomer.customerId |  |  |
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| transactions | customerBalanceTransaction[] |  |
|   └ id | string | elementField |
|   └ type | string | elementField |
|   └ amount | integer | elementField |
|   └ endingBalance | integer | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |
| latestEndingBalance | integer | The newest transaction's ending balance, the customer's balance now; 0 with none |

