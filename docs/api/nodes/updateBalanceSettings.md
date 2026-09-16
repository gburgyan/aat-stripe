### updateBalanceSettings

Update the balance settings (POST /v1/balance_settings, 200). Only the fields given are sent; the payout interval defaults to the one getBalanceSettings read, so the node writes back what is there unless a plan says otherwise. An activated account can't change payments[debit_negative_balances] through the API at all: 400 invalid_request_error with that param, even when the value is unchanged. The response is the settings after the update.

**Adapter:** `updateBalanceSettings`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| debitNegativeBalances | boolean | no |  | Refused on an activated account |
| payoutInterval | string | no | from: getBalanceSettings.payoutInterval | manual, daily, weekly, or monthly |
| idempotencyKey | string | no | {{uuid}} | The Idempotency-Key header; a retried request answers with the first response |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| debitNegativeBalances | boolean |  |
| payoutInterval | string |  |
| payoutStatus | string |  |
| settlementDelayDays | integer |  |

