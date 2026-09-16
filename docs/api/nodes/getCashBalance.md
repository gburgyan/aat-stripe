### getCashBalance

Read a customer's cash balance (GET /v1/customers/{customer}/cash_balance, 200): what they have paid in by bank transfer, per currency, and how it is applied. reconciliation_mode is automatic by default, when a payment takes what it needs as soon as the money arrives, or manual, when apply_customer_balance does it. A customer with a positive cash balance can't be deleted.

**Adapter:** `getCashBalance`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerId | string |  |
| livemode | boolean |  |
| reconciliationMode | string |  |
| usingMerchantDefault | boolean |  |
| availableUsd | integer |  |
| availableEur | integer |  |
| currencyCount | integer |  |

