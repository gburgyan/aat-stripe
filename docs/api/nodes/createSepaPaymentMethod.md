### createSepaPaymentMethod

Create a sepa_debit PaymentMethod from an IBAN (POST /v1/payment_methods, 200). Stripe's test IBAN DE89370400440532013000 succeeds, and DE62370400440532013001 fails after the charge is made. The country and bank code come from the IBAN. A PaymentMethod used once without a customer can't be attached later.

**Adapter:** `createSepaPaymentMethod`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| iban | string | yes | DE89370400440532013000 |  |
| billingName | string | yes | AAT Stripe |  |
| billingEmail | string | yes | aat-stripe@example.com |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| paymentMethodId | string |  |
| type | string |  |
| livemode | boolean |  |
| customerId | string |  |
| country | string |  |
| last4 | string |  |
| bankCode | string |  |
| billingName | string |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

