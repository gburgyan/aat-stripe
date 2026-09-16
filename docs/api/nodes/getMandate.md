### getMandate

Read a mandate (GET /v1/mandates/{mandate}, 200), the customer's authorization for a debit. A SetupIntent's is multi_use and active; a single payment's is single_use and inactive once it is used. It records how the customer accepted it, with the IP address and user agent sent as mandate_data. An unknown mandate is 404 resource_missing on param mandate.

**Adapter:** `getMandate`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| mandateId | string | yes | from: verifySetupIntentMicrodeposits.mandateId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| mandateId | string |  |
| type | string | multi_use or single_use |
| status | string | active, inactive, or pending |
| livemode | boolean |  |
| paymentMethodId | string |  |
| paymentMethodType | string |  |
| acceptanceType | string |  |
| acceptanceIp | string |  |
| acceptanceUserAgent | string |  |
| sepaReferenceSet | string | A SEPA mandate's reference; "" for other types |

