### deleteTaxId

Delete a customer's tax ID (DELETE /v1/customers/{customer}/tax_ids/{id}, 200, deleted: true). Deleting it again is 404 resource_missing on param id. The cleanup for createTaxId.

**Adapter:** `deleteTaxId`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| taxId | string | yes | from: createTaxId.taxId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| taxId | string |  |
| deleted | boolean |  |

