### getCharge

Read a charge by its ch_ or py_ ID (GET /v1/charges/{charge}, 200): its amounts captured and refunded, its card's brand, country, funding, and last four digits, and its outcome and risk level.

**Adapter:** `getCharge`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| chargeId | string | yes | from: getPaymentIntent.latestChargeId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| chargeId | string |  |
| status | string |  |
| amount | integer |  |
| amountCaptured | integer |  |
| amountRefunded | integer |  |
| currency | string |  |
| captured | boolean |  |
| refunded | boolean |  |
| paid | boolean |  |
| disputed | boolean |  |
| livemode | boolean |  |
| paymentIntentId | string |  |
| balanceTransactionId | string | The txn_ ID; "" before the charge has one |
| cardBrand | string |  |
| cardCountry | string |  |
| cardFunding | string |  |
| cardLast4 | string |  |
| outcomeType | string |  |
| riskLevel | string |  |
| networkStatus | string | approved_by_network, declined_by_network, not_sent_to_network, or reversed_after_approval |
| failureCode | string | "" for a charge that didn't fail |

