### fundCashBalance

Pretend money arrived by bank transfer (POST /v1/test_helpers/customers/{customer}/fund_cash_balance, 200), a test-mode helper. It records a funded cash balance transaction with the balance after it, and the reference the sender gave. An amount below 1 is 400 parameter_invalid_integer on param amount.

**Adapter:** `fundCashBalance`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| amount | integer | yes | 5000 |  |
| currency | string | yes | usd |  |
| reference | string | no | aat-stripe |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| cashBalanceTransactionId | string |  |
| type | string | funded, applied_to_payment, refunded_from_payment, and others |
| netAmount | integer |  |
| endingBalance | integer |  |
| currency | string |  |
| customerId | string |  |
| livemode | boolean |  |
| bankTransferType | string |  |
| reference | string |  |

