### listBalanceTransactions

Page through the balance transactions (GET /v1/balance_transactions, 200), newest first: each charge, refund, fee, payout, and transfer that moved the balance. limit is 1 to 100, and filters narrow the list to one type (charge, refund, payout, ...) or to transactions created at or after a Unix time. The older path /v1/balance/history answers the same list and isn't used.

**Adapter:** `listBalanceTransactions`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 | Transactions per page, 1 to 100 | 1..100 |
| startingAfter | string | no |  | The previous page's lastId |  |
| transactionType | string | no |  | Only transactions of this type, such as charge or refund |  |
| createdGte | integer | no |  | Only transactions created at or after this Unix time |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| transactions | balanceTransaction[] |  |
|   └ id | string | elementField |
|   └ type | string | elementField |
|   └ amount | integer | elementField |
|   └ currency | string | elementField |
|   └ status | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| firstId | string | The newest ID on the page; "" on an empty page |
| lastId | string | The oldest ID on the page, which the next page starts after; "" on an empty page |

