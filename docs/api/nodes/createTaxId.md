### createTaxId

Add a tax ID to a customer (POST /v1/customers/{customer}/tax_ids, 200), such as an eu_vat number. Its country comes from the value, and verification starts pending. A value the type rejects is 400 tax_id_invalid on param value. Cleanup deletes it.

**Adapter:** `createTaxId`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| type | string | yes | eu_vat | One of Stripe's tax ID types, such as eu_vat, us_ein, or gb_vat |
| value | string | yes | DE000000000 |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| taxId | string |  |
| type | string |  |
| value | string |  |
| country | string |  |
| verificationStatus | string | pending, verified, unverified, or unavailable |
| customerId | string |  |

