### deleteCustomer

Delete a customer for good (DELETE /v1/customers/{customer}, 200, deleted: true). Deleting one already deleted is 404 resource_missing with param id. The cleanup for createCustomer.

**Adapter:** `deleteCustomer`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId | The cus_ ID |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerId | string |  |
| deleted | boolean |  |

