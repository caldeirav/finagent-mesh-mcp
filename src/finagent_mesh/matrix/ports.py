"""Runtime port allocation for sequential exclusive Stage-1 / Stage-2 sidecars.

Registry defaults often put several Choice engines on :8000. Block A pairs need
a different Stage-1 Choice engine alongside a warm Lux Score partner, so the
matrix runner rebinds Stage-1 → 8000 and Stage-2 → 8001 when both are sidecars.

Hybrid Stage-2 adapters (e.g. ``clm-shortlist-32``) are in-process orchestrators
but still require a real GPU sidecar dependency (``clm-8b``) to be started.
"""

from __future__ import annotations

from finagent_mesh.clients.engines.registry import EngineRegistry
from finagent_mesh.matrix.partners import is_inprocess_engine

DEFAULT_STAGE1_PORT = 8000
DEFAULT_STAGE2_PORT = 8001


def registry_port(registry: EngineRegistry, config_id: str) -> int:
    cfg = registry.get(config_id)
    return int(cfg.base_url.rsplit(":", 1)[-1])


def sidecar_dependencies(registry: EngineRegistry, config_id: str) -> list[str]:
    """Extra GPU sidecars needed by an in-process / hybrid engine."""
    if not config_id:
        return []
    cfg = registry.get(config_id)
    if cfg.backend == "clm_shortlist":
        return ["clm-8b"]
    if cfg.backend == "lux_shortlist":
        return ["decision20-lux"]
    if cfg.backend == "e5_ce_shortlist":
        return []
    return []


def _allocate_free_port(plan: dict[str, int], preferred: int) -> int:
    occupied = set(plan.values())
    if preferred not in occupied:
        return preferred
    for port in (DEFAULT_STAGE2_PORT, DEFAULT_STAGE1_PORT, 8002, 8003):
        if port not in occupied:
            return port
    return preferred + 1


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
            plan: dict[str, int] = {}
        else:
            plan = {stage1_config_id: registry_port(registry, stage1_config_id)}
    else:
        plan = {}
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

    # Hybrid in-process Stage-2 (BM25→CLM shortlist) still needs the CLM sidecar.
    for stage_id in (stage1_config_id, stage2_config_id):
        for dep in sidecar_dependencies(registry, stage_id):
            if dep in plan or is_inprocess_engine(registry, dep):
                continue
            preferred = registry_port(registry, dep)
            plan[dep] = _allocate_free_port(plan, preferred)
    return plan


def base_url_for_port(port: int) -> str:
    return f"http://localhost:{int(port)}"
