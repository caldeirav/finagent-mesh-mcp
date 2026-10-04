"""Environment-backed harness settings."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def _int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return int(raw)


def _truthy(name: str, default: str = "0") -> bool:
    return os.getenv(name, default) in {"1", "true", "TRUE", "yes", "YES"}


@dataclass(frozen=True)
class Settings:
    finagentbench_path: Path | None
    eval_ledger_path: Path
    systemone_stage1_url: str
    systemone_stage2_url: str
    agent_gateway_url: str | None
    google_api_key: str | None
    gemini_model: str
    synthesis_k: int
    harness_max_attempts: int
    mlflow_tracking_uri: str
    podman_or_docker: str
    systemone_mock: bool
    engines_registry_path: Path

    @classmethod
    def from_env(cls) -> Settings:
        path = os.getenv("FINAGENTBENCH_PATH")
        return cls(
            finagentbench_path=Path(path) if path else None,
            eval_ledger_path=Path(os.getenv("EVAL_LEDGER_PATH", "./eval_ledger.db")),
            systemone_stage1_url=os.getenv("SYSTEMONE_STAGE1_URL", "http://localhost:8000"),
            systemone_stage2_url=os.getenv("SYSTEMONE_STAGE2_URL", "http://localhost:8001"),
            agent_gateway_url=os.getenv("AGENT_GATEWAY_URL"),
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
            synthesis_k=_int("SYNTHESIS_K", 5),
            harness_max_attempts=_int("HARNESS_MAX_ATTEMPTS", 3),
            mlflow_tracking_uri=os.getenv("MLFLOW_TRACKING_URI", "./mlruns"),
            podman_or_docker=os.getenv("PODMAN_OR_DOCKER", "podman"),
            systemone_mock=_truthy("SYSTEMONE_MOCK", "0"),
            engines_registry_path=Path(
                os.getenv("ENGINES_REGISTRY_PATH", "./configs/engines.yaml")
            ),
        )


def get_settings() -> Settings:
    return Settings.from_env()


def require_official_mock_policy(*, systemone_mock: bool, allow_mock: bool) -> None:
    """Refuse official starts when mock is enabled unless --allow-mock."""
    if systemone_mock and not allow_mock:
        raise RuntimeError(
            "SYSTEMONE_MOCK is enabled; refuse official run without --allow-mock "
            "(record allow_mock in config for debug-only)"
        )
