#!/usr/bin/env python3
"""Remove response-borne credentials from run archives before they are published.

AAT redacts the credentials it *sends*: the API key, every configured secret,
and the well-known credential headers. It cannot redact a credential an API
*hands back*, because nothing marks the value as one -- see the archive section
of AAT's SECURITY.md. For this project that gap is one shape.

Stripe returns a client secret on every PaymentIntent and SetupIntent. On the
intents a plan creates it is harmless by the end of the run: they finish
`succeeded` or `canceled`, and a terminal intent's secret can retrieve the
object but not act on it. The problem is the list reads. `listSetupIntents` and
`listPaymentIntents` return intents this project never created, some still
`requires_payment_method`, and those secrets are live: they can confirm or
cancel that intent. Nothing in a run cleans them up, because the run does not
own them. The nightly artifact is public, so they come out here.

Single-use token ids (btok_, cvctok_, ctoken_, tok_) are deliberately left in.
Each is consumed by the run that created it, and they read like every other
Stripe object id the archive is worth opening for.

The archive text is rewritten in place rather than reparsed, so a body stays
byte-for-byte what went over the wire apart from the redacted value.
"""

import re
import sys
from pathlib import Path

REDACTED = "[REDACTED]"

# "pi_XXX_secret_YYY" / "seti_XXX_secret_YYY", wherever it appears -- including
# inside the 3D Secure redirect_to_url query string, where it rides along as
# payment_intent_client_secret.
CLIENT_SECRET = re.compile(r"\b(?:pi|seti)_[A-Za-z0-9]+_secret_[A-Za-z0-9]+")

# A run must never carry a live-mode key. If one appears, fail the job rather
# than publish it: this artifact is public.
FORBIDDEN = re.compile(r"\b(?:sk_live_|rk_live_|pk_live_\w)")


def main(root: str) -> int:
    archives = sorted(Path(root).rglob("*.json"))
    if not archives:
        # The batch may have failed before it wrote anything. That is the run's
        # signal to give, not this script's.
        print(f"no archives under {root}; nothing to scrub")
        return 0

    redacted = 0
    for path in archives:
        text = path.read_text()
        if FORBIDDEN.search(text):
            print(f"live-mode key in {path} -- refusing to publish", file=sys.stderr)
            return 2
        scrubbed, n = CLIENT_SECRET.subn(REDACTED, text)
        if n:
            path.write_text(scrubbed)
            redacted += n

    print(f"{len(archives)} archives, {redacted} client secret(s) redacted")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "_output/runs"))
