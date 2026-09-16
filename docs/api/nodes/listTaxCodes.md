### listTaxCodes

Page through Stripe Tax's product tax codes (GET /v1/tax_codes, 200), a fixed catalog of txcd_ codes. limit is 1 to 100.

**Adapter:** `listTaxCodes`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 100 | Codes per page, 1 to 100 | 1..100 |
| startingAfter | string | no |  | The previous page's lastId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| taxCodes | taxCode[] |  |
|   └ id | string | elementField |
|   └ name | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string | The last code on the page; "" on an empty page |

