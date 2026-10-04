"""System-1 health checks."""

from __future__ import annotations

import httpx


def check_healthz(base_url: str, *, timeout: float = 5.0) -> tuple[bool, str]:
    url = f"{base_url.rstrip('/')}/healthz"
    try:
        with httpx.Client(timeout=timeout) as client:
            resp = client.get(url)
            if resp.status_code != 200:
                return False, f"{url} status={resp.status_code}"
            data = resp.json()
            if data.get("status") != "ok":
                return False, f"{url} unexpected body={data}"
            return True, "ok"
    except Exception as exc:  # noqa: BLE001 — surface any transport failure
        return False, f"{url} error={exc}"


def require_systemone_healthy(stage1_url: str, stage2_url: str, *, mock: bool) -> None:
    if mock:
        return
    ok1, msg1 = check_healthz(stage1_url)
    ok2, msg2 = check_healthz(stage2_url)
    if not ok1 or not ok2:
        raise RuntimeError(
            "Local System-1 unhealthy; fail closed (no cloud ranking). "
            f"stage1={msg1}; stage2={msg2}"
        )
