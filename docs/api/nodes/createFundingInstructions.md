### createFundingInstructions

Ask for the bank details a customer pays into (POST /v1/customers/{customer}/funding_instructions, 200). A us_bank_transfer gives two financial addresses, aba and swift, and the same customer gets the same details again. A eu_bank_transfer needs its country, and euros.

**Adapter:** `createFundingInstructions`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| fundingType | string | yes | bank_transfer |  |
| currency | string | yes | usd |  |
| bankTransferType | string | yes | us_bank_transfer | us_bank_transfer, eu_bank_transfer, gb_bank_transfer, jp_bank_transfer, or mx_bank_transfer |
| euCountry | string | no |  | The country of a eu_bank_transfer, such as DE |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| currency | string |  |
| fundingType | string |  |
| livemode | boolean |  |
| bankTransferType | string |  |
| addressCount | integer |  |
| addressTypes | string[] |  |
| firstAddressType | string |  |

