### getBalanceSettings

Read the balance settings (GET /v1/balance_settings, 200): whether a negative balance is debited from the bank account, the payout schedule, and how many days a charge takes to settle.

**Adapter:** `getBalanceSettings`

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| debitNegativeBalances | boolean |  |
| payoutInterval | string | manual, daily, weekly, or monthly; "" when no schedule is set |
| payoutStatus | string | enabled or disabled; "" when absent |
| settlementDelayDays | integer | Days before a charge's funds become available; 0 when absent |

