### getBalance

Read the balance (GET /v1/balance, 200), per currency, as available (ready to pay out) and pending. Amounts are integers in the currency's smallest unit. livemode is false for a test key, so a plan can check it before anything is created.

**Adapter:** `getBalance`

**Outputs:**

| Name | Type | Description |
|------|------|-------------|
| livemode | boolean |  |
| availableUsd | integer | The available USD amount in cents; 0 when the balance has no USD entry |
| pendingUsd | integer | The pending USD amount in cents; 0 when the balance has no USD entry |
| currencyCount | integer | How many currencies the available balance lists |

