### listCustomers

Page through the customers (GET /v1/customers, 200), newest first. limit is 1 to 100, and filters narrow the list to one email or to customers created at or after a Unix time. A deleted customer is no longer listed. Each page counts the customers this package created (metadata.source aat-stripe), and lists them so a guard that fails can name them.

**Adapter:** `listCustomers`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 10 | Customers per page, 1 to 100 | 1..100 |
| startingAfter | string | no |  | The previous page's lastId |  |
| email | string | no |  | Only customers with exactly this email |  |
| createdGte | integer | no |  | Only customers created at or after this Unix time |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customers | customer[] |  |
|   └ id | string | elementField |
|   └ email | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string | The oldest ID on the page; "" on an empty page |
| ourCount | integer | Customers on the page this package created |
| ourCustomers | ourCustomer[] | The package's customers on the page, when there are any |
|   └ id | string | elementField |
|   └ email | string | elementField |
|   └ created | integer | elementField |
| liveCount | integer | Customers in live mode on the page; 0 for a test key |

