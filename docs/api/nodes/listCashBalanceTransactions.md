### listCashBalanceTransactions

Page through a customer's cash balance transactions (GET /v1/customers/{customer}/cash_balance_transactions, 200), newest first: what arrived, and what each payment took.

**Adapter:** `listCashBalanceTransactions`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| customerId | string | yes | from: createCustomer.customerId |  |  |
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| transactions | cashBalanceTransaction[] |  |
|   └ id | string | elementField |
|   └ type | string | elementField |
|   └ netAmount | integer | elementField |
|   └ endingBalance | integer | elementField |
|   └ currency | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |
| latestType | string |  |
| latestEndingBalance | integer |  |

