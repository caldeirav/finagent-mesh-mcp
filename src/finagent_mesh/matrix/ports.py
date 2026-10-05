"""Runtime port allocation for sequential exclusive Stage-1 / Stage-2 sidecars.

Registry defaults often put several Choice engines on :8000. Block A pairs need
a different Stage-1 Choice engine alongside a warm Lux Score partner, so the
matrix runner rebinds Stage-1 → 8000 and Stage-2 → 8001 when both are sidecars.
"""

from __future__ import annotations

from finagent_mesh.clients.engines.registry import EngineRegistry
from finagent_mesh.matrix.partners import is_inprocess_engine

DEFAULT_STAGE1_PORT = 8000
DEFAULT_STAGE2_PORT = 8001


def registry_port(registry: EngineRegistry, config_id: str) -> int:
    cfg = registry.get(config_id)
    return int(cfg.base_url.rsplit(":", 1)[-1])


def plan_engine_ports(
    registry: EngineRegistry,
    stage1_config_id: str,
    stage2_config_id: str,
) -> dict[str, int]:
    """Return config_id → port for sidecar engines required by one pair."""
    s1_in = is_inprocess_engine(registry, stage1_config_id)
    s2_in = is_inprocess_engine(registry, stage2_config_id)

    if stage1_config_id == stage2_config_id:
        if s1_in:
            return {}
        return {stage1_config_id: registry_port(registry, stage1_config_id)}

    plan: dict[str, int] = {}
    if not s1_in:
        plan[stage1_config_id] = DEFAULT_STAGE1_PORT
    if not s2_in:
        s2_port = registry_port(registry, stage2_config_id)
        if s2_port == plan.get(stage1_config_id, -1):
            s2_port = DEFAULT_STAGE2_PORT
        # Prefer registry Stage-2 port when it does not collide (e.g. clm-8b :8001)
        if stage1_config_id in plan and s2_port == plan[stage1_config_id]:
            s2_port = DEFAULT_STAGE2_PORT
        if not s1_in and s2_port == DEFAULT_STAGE1_PORT:
            # Different engine still on :8000 in yaml → move Stage-2 to :8001
            s2_port = DEFAULT_STAGE2_PORT
        plan[stage2_config_id] = s2_port
    return plan


def base_url_for_port(port: int) -> str:
    return f"http://localhost:{int(port)}"
