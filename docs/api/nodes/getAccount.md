### getAccount

Read the account the secret key belongs to (GET /v1/account, 200): its country, default currency, and type, whether it can take charges and pay out, and the state of the card_payments and transfers capabilities. The account object has no livemode field; the balance has one.

**Adapter:** `getAccount`

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| accountId | string |  |
| country | string |  |
| accountType | string | standard, express, custom, or none |
| defaultCurrency | string |  |
| chargesEnabled | boolean |  |
| payoutsEnabled | boolean |  |
| detailsSubmitted | boolean |  |
| cardPayments | string | The card_payments capability, such as active or pending; "" when the account has none |
| transfers | string | The transfers capability, such as active or pending; "" when the account has none |
| controllerType | string | account for an account that controls itself, application for a connected account; "" when absent |

