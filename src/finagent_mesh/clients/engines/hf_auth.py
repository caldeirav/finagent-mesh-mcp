"""Hugging Face Hub auth from .env (HF_TOKEN / HUGGING_FACE_HUB_TOKEN)."""

from __future__ import annotations

import os
from functools import lru_cache

from finagent_mesh.runtime.progress import log


def hf_token() -> str | None:
    """Return a Hub token from the environment, or None."""
    for key in ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
        raw = (os.getenv(key) or "").strip()
        if raw:
            return raw
    return None


@lru_cache(maxsize=1)
def ensure_hf_hub_auth() -> str | None:
    """Propagate token into both common env names so hub/transformers pick it up.

    Call once before downloads / ``from_pretrained``. Returns the token or None.
    Does not log the secret.
    """
    token = hf_token()
    if not token:
        log(
            "HF Hub: no HF_TOKEN / HUGGING_FACE_HUB_TOKEN in env "
            "(unauthenticated rate limits apply; set HF_TOKEN in .env)"
        )
        return None
    os.environ["HF_TOKEN"] = token
    os.environ["HUGGING_FACE_HUB_TOKEN"] = token
    log("HF Hub: authenticated via HF_TOKEN (higher rate limits)")
    return token
