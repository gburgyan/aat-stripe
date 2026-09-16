### updateCharge

Update a charge's description and metadata note (POST /v1/charges/{charge}, 200).

**Adapter:** `updateCharge`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| chargeId | string | yes | from: getPaymentIntent.latestChargeId |  |
| description | string | no |  |  |
| note | string | no |  | Stored as metadata[note] |
| idempotencyKey | string | no | {{uuid}} |  |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| chargeId | string |  |
| description | string |  |
| note | string |  |

