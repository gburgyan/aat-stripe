### createAchSetupIntent

Save a US bank account for later debits (POST /v1/setup_intents, 200) with payment_method_types us_bank_account and mandate acceptance. The mandate is recorded as the SetupIntent is created, and it waits in requires_action for microdeposit verification; verified, it succeeds with that mandate now multi_use and active, and the PaymentMethod is attached to the customer. A later off-session PaymentIntent on that PaymentMethod reuses the same mandate.

**Adapter:** `createAchSetupIntent`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| customerId | string | yes | from: createCustomer.customerId |  |
| paymentMethod | string | no | from: createAchPaymentMethod.paymentMethodId |  |
| confirm | boolean | no | true |  |
| usage | string | no |  |  |
| acceptanceType | string | no | online |  |
| acceptanceIp | string | no | 203.0.113.10 |  |
| acceptanceUserAgent | string | no | aat-stripe |  |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| setupIntentId | string |  |
| status | string |  |
| usage | string |  |
| livemode | boolean |  |
| customerId | string |  |
| paymentMethodId | string |  |
| mandateId | string |  |
| latestAttemptId | string |  |
| nextActionType | string |  |
| microdepositType | string |  |
| lastSetupErrorCode | string |  |
| source | string |  |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

