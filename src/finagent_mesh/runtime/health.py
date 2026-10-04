"""System-1 health checks (single URL or multi-engine)."""

from __future__ import annotations

import httpx


def check_healthz(base_url: str, *, health_path: str = "/healthz", timeout: float = 5.0) -> tuple[bool, str]:
    url = f"{base_url.rstrip('/')}{health_path}"
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


def require_engines_healthy(
    targets: list[tuple[str, str]],
    *,
    mock: bool,
) -> None:
    """targets: list of (base_url, health_path). Fail closed if any unhealthy when not mocking."""
    if mock:
        return
    failures: list[str] = []
    for base_url, health_path in targets:
        ok, msg = check_healthz(base_url, health_path=health_path)
        if not ok:
            failures.append(msg)
    if failures:
        raise RuntimeError(
            "Local System-1 unhealthy; fail closed (no cloud ranking). " + "; ".join(failures)
        )


def require_systemone_healthy(stage1_url: str, stage2_url: str, *, mock: bool) -> None:
    require_engines_healthy(
        [(stage1_url, "/healthz"), (stage2_url, "/healthz")],
        mock=mock,
    )
