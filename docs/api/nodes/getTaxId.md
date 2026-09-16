### getTaxId

Read one of a customer's tax IDs (GET /v1/customers/{customer}/tax_ids/{id}, 200).

**Adapter:** `getTaxId`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| taxId | string | yes | from: createTaxId.taxId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| taxId | string |  |
| type | string |  |
| value | string |  |
| country | string |  |
| verificationStatus | string | pending, verified, unverified, or unavailable |
| customerId | string |  |

