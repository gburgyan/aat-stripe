### cancelRefund

Cancel a refund that is waiting on the customer (POST /v1/refunds/{refund}/cancel, 200), which only a refund in requires_action allows. A card refund, which succeeds at once, is 400 with no code ("Canceling this refund is unsupported"). Refunds of bank transfer payments, the ones that can wait, are gated on this account.

**Adapter:** `cancelRefund`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| refundId | string | yes | from: createRefund.refundId |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| refundId | string |  |
| status | string |  |
| failureReason | string |  |

