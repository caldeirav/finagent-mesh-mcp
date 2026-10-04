"""Stdout progress for long matrix / harness runs (always flushed)."""

from __future__ import annotations

from datetime import datetime, timezone


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}Z] {msg}", flush=True)
