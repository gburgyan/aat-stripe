### updateCustomer

Update a customer (POST /v1/customers/{customer}, 200): its name, email, description, phone, preferred locales, and metadata note. Only the fields given change.

**Adapter:** `updateCustomer`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| name | string | no |  |  |
| email | string | no |  |  |
| description | string | no |  |  |
| phone | string | no |  |  |
| preferredLocales | string[] | no |  |  |
| note | string | no |  | Stored as metadata[note] |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerId | string |  |
| name | string |  |
| email | string |  |
| description | string |  |
| phone | string |  |
| note | string |  |
| balance | integer | The customer's balance in the smallest currency unit; negative is a credit |
| preferredLocaleCount | integer |  |

