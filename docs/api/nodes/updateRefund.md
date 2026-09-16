### updateRefund

Update a refund's metadata note (POST /v1/refunds/{refund}, 200); nothing else of a refund changes.

**Adapter:** `updateRefund`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| refundId | string | yes | from: createRefund.refundId |  |
| note | string | yes |  | Stored as metadata[note] |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| refundId | string |  |
| note | string |  |

