"""Engine registry loader and adapter factory."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

import yaml


_ENV_PATTERN = re.compile(
    r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}"
)


def _expand_env(value: str) -> str:
    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        default = match.group(2) if match.group(2) is not None else ""
        env_val = os.getenv(name)
        if env_val is None or env_val.strip() == "":
            return default
        return env_val

    return _ENV_PATTERN.sub(repl, value)


@dataclass(frozen=True)
class EngineConfiguration:
    config_id: str
    family: str
    display_name: str
    primitives: list[str]
    primary_stages: list[str]
    base_url: str
    health_path: str = "/healthz"
    decide_path: str = "/v1/systemone"
    container_ref: str = ""
    weights_ref: str = ""
    calibration_ref: str | None = None
    is_heavy_gpu: bool = True
    is_light_edge: bool = False
    model_revision: str = ""
    backend: str = "sidecar"

    def decide_url(self) -> str:
        return f"{self.base_url.rstrip('/')}{self.decide_path}"

    def health_url(self) -> str:
        return f"{self.base_url.rstrip('/')}{self.health_path}"


@dataclass
class EngineRegistry:
    version: int
    partners: dict[str, str]
    engines: dict[str, EngineConfiguration]
    ports: dict[str, int] = field(default_factory=dict)

    def get(self, config_id: str) -> EngineConfiguration:
        if config_id not in self.engines:
            raise KeyError(f"Unknown engine config_id={config_id!r}")
        return self.engines[config_id]

    def all_ids(self) -> list[str]:
        return list(self.engines.keys())


def load_registry(path: Path | str | None = None) -> EngineRegistry:
    registry_path = Path(
        path or os.getenv("ENGINES_REGISTRY_PATH", "./configs/engines.yaml")
    )
    raw = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    engines: dict[str, EngineConfiguration] = {}
    for row in raw.get("engines") or []:
        cal = row.get("calibration_ref")
        weights = _expand_env(str(row.get("weights_ref") or ""))
        cfg = EngineConfiguration(
            config_id=str(row["config_id"]),
            family=str(row["family"]),
            display_name=str(row.get("display_name") or row["config_id"]),
            primitives=list(row.get("primitives") or []),
            primary_stages=list(row.get("primary_stages") or []),
            base_url=str(row["base_url"]).rstrip("/"),
            health_path=str(row.get("health_path") or "/healthz"),
            decide_path=str(row.get("decide_path") or "/v1/systemone"),
            container_ref=str(row.get("container_ref") or ""),
            weights_ref=weights,
            calibration_ref=str(cal) if cal else None,
            is_heavy_gpu=bool(row.get("is_heavy_gpu", True)),
            is_light_edge=bool(row.get("is_light_edge", False)),
            model_revision=str(row.get("model_revision") or row["config_id"]),
            backend=str(row.get("backend") or "sidecar"),
        )
        if cfg.config_id in engines:
            raise ValueError(f"Duplicate config_id={cfg.config_id}")
        engines[cfg.config_id] = cfg
    ports = {k: int(v) for k, v in (raw.get("ports") or {}).items()}
    partners = {
        "stage1_partner_id": str((raw.get("partners") or {}).get("stage1_partner_id", "anyjev-l0")),
        "stage2_partner_id": str((raw.get("partners") or {}).get("stage2_partner_id", "clm-8b")),
    }
    return EngineRegistry(
        version=int(raw.get("version") or 1),
        partners=partners,
        engines=engines,
        ports=ports,
    )


class DecisionAdapter(Protocol):
    engine_id: str
    model_revision: str

    def decide(
        self,
        primitive: str,
        query: str,
        candidates: list[dict[str, str]],
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]: ...

    def health(self) -> tuple[bool, str]: ...


def validate_calibration(cfg: EngineConfiguration, repo_root: Path | None = None) -> None:
    if not cfg.calibration_ref:
        return
    root = repo_root or Path.cwd()
    path = Path(cfg.calibration_ref)
    if not path.is_absolute():
        path = root / path
    if not path.exists():
        raise RuntimeError(
            f"Calibration missing for {cfg.config_id}: {path} (require exactly 200 example_ids)"
        )
    import json

    data = json.loads(path.read_text(encoding="utf-8"))
    ids = data.get("example_ids") or []
    if len(ids) != 200:
        raise RuntimeError(
            f"Calibration for {cfg.config_id} has {len(ids)} ids; require exactly 200"
        )


def create_adapter(config_id: str, registry: EngineRegistry | None = None) -> DecisionAdapter:
    reg = registry or load_registry()
    cfg = reg.get(config_id)
    family = cfg.family
    if family == "anyjev":
        from finagent_mesh.clients.engines.anyjev import AnyJevAdapter

        return AnyJevAdapter(cfg)
    if family == "clm":
        from finagent_mesh.clients.engines.clm8b import Clm8bAdapter

        return Clm8bAdapter(cfg)
    if family == "vllm-sr":
        from finagent_mesh.clients.engines.vllm_sr import VllmSrAdapter

        return VllmSrAdapter(cfg)
    if family == "laya":
        from finagent_mesh.clients.engines.laya import LayaAdapter

        return LayaAdapter(cfg)
    if family == "ar-baseline":
        from finagent_mesh.clients.engines.ar_baseline import ArBaselineAdapter

        return ArBaselineAdapter(cfg)
    raise ValueError(f"No adapter for family={family}")
