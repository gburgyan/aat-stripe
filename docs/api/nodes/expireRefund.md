### expireRefund

Expire a refund that is waiting on the customer (POST /v1/test_helpers/refunds/{refund}/expire, 200), a test-mode helper for a refund in requires_action. A card refund is 400 with no code, pointing at the charge refund endpoint.

**Adapter:** `expireRefund`

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

