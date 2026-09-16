### getRefund

Read a refund by its re_ ID (GET /v1/refunds/{refund}, 200), to follow one that is pending.

**Adapter:** `getRefund`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| refundId | string | yes | from: createRefund.refundId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| refundId | string |  |
| status | string |  |
| amount | integer |  |
| currency | string |  |
| paymentIntentId | string | "" for a refund without one |
| chargeId | string |  |
| reason | string | "" for none |
| failureReason | string | Why a failed refund failed; "" otherwise |
| pendingReason | string | Why a pending refund is pending; "" otherwise |
| source | string | metadata.source |

