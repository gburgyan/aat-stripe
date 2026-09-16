### createSetupIntent

Create a SetupIntent (POST /v1/setup_intents, 200), which saves a payment method for later without charging it. Confirmed with a card for off_session usage it succeeds, and the customer gets a new PaymentMethod, its own copy of a test card, that then pays off session. A card that needs authentication on setup stops it at requires_action with a redirect_to_url next action. A declined card is 402 card_error and still leaves the SetupIntent open in requires_payment_method. Cleanup reads it and cancels it while it is open.

**Adapter:** `createSetupIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| paymentMethod | string | no | pm_card_visa | A payment method ID, or a test one such as pm_card_visa; {} for none yet |
| paymentMethodTypes | string[] | yes | [card] |  |
| confirm | boolean | no |  |  |
| usage | string | no |  | on_session or off_session (the default) |
| returnUrl | string | no |  |  |
| description | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| setupIntentId | string |  |
| status | string |  |
| usage | string |  |
| livemode | boolean |  |
| customerId | string |  |
| paymentMethodId | string | The saved PaymentMethod; "" before one is set |
| latestAttemptId | string | The setatt_ ID of the latest attempt; "" before one |
| nextActionType | string |  |
| lastSetupErrorCode | string |  |
| lastSetupErrorDeclineCode | string |  |
| cancellationReason | string |  |
| description | string |  |
| note | string |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

