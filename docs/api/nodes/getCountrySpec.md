### getCountrySpec

Read one country's spec by its two-letter code (GET /v1/country_specs/{country}, 200): its default currency, and how many currencies payments can be in, countries it can transfer to, and payment methods it lists.

**Adapter:** `getCountrySpec`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| country | string | yes | US | An ISO 3166-1 alpha-2 country code |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| country | string |  |
| defaultCurrency | string |  |
| paymentCurrencyCount | integer |  |
| transferCountryCount | integer |  |
| paymentMethodCount | integer |  |

