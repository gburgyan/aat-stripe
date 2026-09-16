### updateCashBalance

Set how a customer's cash balance is applied (POST /v1/customers/{customer}/cash_balance, 200): reconciliation_mode automatic, manual, or merchant_default. Another value is 400 on param settings[reconciliation_mode], with no code.

**Adapter:** `updateCashBalance`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| reconciliationMode | string | yes | manual |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerId | string |  |
| reconciliationMode | string |  |
| usingMerchantDefault | boolean |  |
| availableUsd | integer |  |

