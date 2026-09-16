### getCustomer

Read a customer by its cus_ ID (GET /v1/customers/{customer}, 200). A deleted customer still answers 200, with only id, object, and deleted: true; an ID that never existed is 404 resource_missing with param id.

**Adapter:** `getCustomer`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId | The cus_ ID |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerId | string |  |
| deleted | boolean | true for a deleted customer; false otherwise |
| email | string | "" for a deleted customer or one without an email |
| name | string |  |
| livemode | boolean |  |
| source | string | metadata.source; "" when absent |
| testClock | string | The test clock the customer runs on; "" for none |

