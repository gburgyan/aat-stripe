### searchCustomers

Search customers with Stripe's search language (GET /v1/customers/search, 200), such as email:'ada@example.com'. Search is eventually consistent: a new customer took 16 seconds and 8 reads to appear, so plans poll it; lists are up to date at once. A field customers can't be searched by is 400 with no code. Pages turn with page, the previous response's next_page.

**Adapter:** `searchCustomers`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| query | string | yes |  | A search query, such as email:'ada@example.com' |  |
| limit | integer | yes | 10 |  | 1..100 |
| page | string | no |  | The previous response's nextPage |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customers | customer[] |  |
|   └ id | string | elementField |
|   └ email | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| nextPage | string | The cursor for the next page; "" on the last |
| firstId | string | The first customer found; "" when none is |

