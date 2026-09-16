### getCashBalanceTransaction

Read one of a customer's cash balance transactions (GET /v1/customers/{customer}/cash_balance_transactions/{transaction}, 200).

**Adapter:** `getCashBalanceTransaction`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| cashBalanceTransactionId | string | yes | from: fundCashBalance.cashBalanceTransactionId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| cashBalanceTransactionId | string |  |
| type | string |  |
| netAmount | integer |  |
| endingBalance | integer |  |
| currency | string |  |
| customerId | string |  |
| reference | string |  |
| appliedPaymentIntentId | string |  |

