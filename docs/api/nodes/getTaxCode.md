### getTaxCode

Read one product tax code by its txcd_ ID (GET /v1/tax_codes/{id}, 200). txcd_10000000 is the general code for electronically supplied services, the account's default.

**Adapter:** `getTaxCode`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| taxCodeId | string | yes | txcd_10000000 | The txcd_ ID |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| taxCodeId | string |  |
| name | string |  |
| description | string |  |

