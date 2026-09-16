### getConfirmationToken

Read a ConfirmationToken (GET /v1/confirmation_tokens/{confirmation_token}, 200), which names the PaymentIntent it confirmed once it is used. An unknown one is 404 resource_missing on param confirmation_token.

**Adapter:** `getConfirmationToken`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| confirmationTokenId | string | yes | from: createConfirmationToken.confirmationTokenId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| confirmationTokenId | string |  |
| livemode | boolean |  |
| created | integer |  |
| expiresAt | integer |  |
| previewType | string |  |
| previewBrand | string |  |
| setupFutureUsage | string |  |
| paymentIntentId | string |  |
| setupIntentId | string |  |

