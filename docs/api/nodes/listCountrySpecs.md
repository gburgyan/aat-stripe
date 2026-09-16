### listCountrySpecs

Page through the country specs (GET /v1/country_specs, 200): one for each country a Stripe account can be in, with its default currency. limit is 1 to 100. A page of 100 has taken from 1 to 20 seconds.

**Adapter:** `listCountrySpecs`

**Inputs:**

| Name | Type | Required | Default | Description | Constraints |
|------|------|----------|---------|-------------|------------|
| limit | integer | yes | 100 | Countries per page, 1 to 100 | 1..100 |
| startingAfter | string | no |  | The previous page's lastId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| countries | countrySpec[] |  |
|   └ id | string | elementField |
|   └ defaultCurrency | string | elementField |
| count | integer |  |
| hasMore | boolean |  |
| lastId | string | The last country code on the page; "" on an empty page |

