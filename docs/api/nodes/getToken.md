### getToken

Read a token by its ID (GET /v1/tokens/{token}, 200), which says whether it has been used. An unknown token is 400 resource_missing on param token, not 404. Stripe's test card tokens, such as tok_visa, read back as cards.

**Adapter:** `getToken`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| tokenId | string | yes | from: createToken.tokenId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| tokenId | string |  |
| type | string |  |
| used | boolean |  |
| livemode | boolean |  |
| bankLast4 | string |  |
| cardBrand | string |  |

