### createToken

Create a single-use token (POST /v1/tokens, 200): a bank account (btok_), a PII number (pii_), or a CVC collected again (cvctok_). Exactly one kind per request: none is 400 parameter_missing, and two at once is 400 with no code. A raw card number is refused as it is on PaymentMethods (402, "generally unsafe"). A token is used once, and reusing it is 400 token_already_used.

**Adapter:** `createToken`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| bankCountry | string | no |  |  |
| bankCurrency | string | no |  |  |
| routingNumber | string | no |  |  |
| accountNumber | string | no |  |  |
| accountHolderName | string | no |  |  |
| accountHolderType | string | no |  |  |
| idNumber | string | no |  | A PII number, such as a test SSN |
| cvc | string | no |  | A card's CVC, for a cvc_update token |
| cardNumber | string | no |  | A raw card number, which Stripe refuses |
| cardExpMonth | string | no |  |  |
| cardExpYear | string | no |  |  |
| cardCvc | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| tokenId | string |  |
| type | string | bank_account, pii, cvc_update, card, account, or person |
| used | boolean |  |
| livemode | boolean |  |
| clientIpSet | string |  |
| bankLast4 | string |  |
| bankStatus | string |  |
| bankName | string |  |
| bankCountry | string |  |
| cardBrand | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

