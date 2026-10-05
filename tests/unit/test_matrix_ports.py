"""Port allocation for Block A dual-sidecar pairs."""

from __future__ import annotations

from pathlib import Path

from finagent_mesh.clients.engines.registry import load_registry
from finagent_mesh.matrix.ports import plan_engine_ports


def test_same_engine_uses_registry_port() -> None:
    reg = load_registry(Path("configs/engines.yaml"))
    assert plan_engine_ports(reg, "decision20-lux", "decision20-lux") == {
        "decision20-lux": 8000
    }


def test_block_a_moves_lux_score_to_8001() -> None:
    reg = load_registry(Path("configs/engines.yaml"))
    plan = plan_engine_ports(reg, "decision20-kai", "decision20-lux")
    assert plan == {"decision20-kai": 8000, "decision20-lux": 8001}


def test_block_b_keeps_clm_on_8001() -> None:
    reg = load_registry(Path("configs/engines.yaml"))
    plan = plan_engine_ports(reg, "decision20-lux", "clm-8b")
    assert plan == {"decision20-lux": 8000, "clm-8b": 8001}


def test_inprocess_stage2_only_starts_choice() -> None:
    reg = load_registry(Path("configs/engines.yaml"))
    plan = plan_engine_ports(reg, "decision20-lux", "bm25-stage2")
    assert plan == {"decision20-lux": 8000}
