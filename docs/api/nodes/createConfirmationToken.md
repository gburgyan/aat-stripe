### createConfirmationToken

Create a ConfirmationToken (POST /v1/test_helpers/confirmation_tokens, 200), the test-mode stand-in for what Stripe.js collects: a payment method, what it may be saved for, and a return URL, gathered into one ctoken_ that confirms a PaymentIntent. It lasts 12 hours and previews the payment method. Confirming with it a second time is 400 payment_intent_confirmation_token_invalid.

**Adapter:** `createConfirmationToken`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| paymentMethod | string | no | pm_card_visa |  |
| setupFutureUsage | string | no |  | on_session or off_session; the PaymentIntent must ask for the same |
| returnUrl | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| confirmationTokenId | string |  |
| livemode | boolean |  |
| created | integer |  |
| expiresAt | integer |  |
| setupFutureUsage | string |  |
| previewType | string |  |
| previewBrand | string |  |
| previewLast4 | string |  |
| paymentIntentId | string | The PaymentIntent it confirmed; "" until it is used |
| setupIntentId | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

