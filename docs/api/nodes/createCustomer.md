### createCustomer

Create a customer (POST /v1/customers, 200). Every customer the package creates carries metadata[source]=aat-stripe and a fresh Idempotency-Key. Sending the key again with the same parameters answers with the first customer, with Idempotent-Replayed: true and Original-Request naming the first request; other parameters, or another endpoint, are 400 idempotency_error. Cleanup deletes the customer, except after a replay, whose customer the first request's cleanup deletes.

**Adapter:** `createCustomer`

**Inputs:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| email | string | yes | aat-stripe-{{random 10}}@example.com | A fresh address in a domain reserved for examples |
| name | string | yes | AAT Stripe customer |  |
| description | string | no |  |  |
| idempotencyKey | string | no | {{uuid}} | The Idempotency-Key header; a retried create answers with the first customer |

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| customerId | string |  |
| email | string |  |
| name | string |  |
| livemode | boolean |  |
| created | integer |  |
| source | string | metadata.source, aat-stripe for every customer the package creates |
| testClock | string | The test clock the customer runs on; "" for none |
| idempotentReplayed | boolean | The Idempotent-Replayed response header; false when Stripe sends none |
| requestId | string | The Request-Id response header, the req_ ID events name |
| originalRequest | string | The Original-Request header, the request that first sent the key; this request's own ID unless it is a replay |
| stripeVersion | string | The Stripe-Version response header, the API version Stripe answered at |

**Error Detection:**

| Path | Rule | Details |
|------|------|---------|
| `livemode` | equals true |  |

