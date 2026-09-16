### listTaxIds

Page through a customer's tax IDs (GET /v1/customers/{customer}/tax_ids, 200).

**Adapter:** `listTaxIds`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| customerId | string | yes | from: createCustomer.customerId |  |  |
| limit | integer | yes | 10 |  | 1..100 |
| startingAfter | string | no |  |  |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| taxIds | taxId[] |  |
|   └ id | string | elementField |
|   └ type | string | elementField |
|   └ value | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string |  |

