"""Engine registry contract tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from finagent_mesh.clients.engines.registry import create_adapter, load_registry, validate_calibration
from finagent_mesh.matrix.partners import FixedStagePartners, bind_matrix_row


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "configs" / "engines.yaml"


def test_registry_loads_core_and_paper_ir_engines() -> None:
    reg = load_registry(REGISTRY)
    assert len(reg.engines) >= 11
    assert reg.partners["stage1_partner_id"] == "anyjev-l0"
    assert reg.partners["stage2_partner_id"] == "clm-8b"
    for eid in [
        "anyjev-l0",
        "anyjev-l1",
        "clm-8b",
        "decision20-kai",
        "decision20-lux",
        "laya-modernbert",
        "ar-qwen3-8b-instruct",
        "bm25-stage2",
        "e5-base",
        "clm-shortlist-32",
        "noop-choice",
    ]:
        assert eid in reg.engines


def test_adapters_construct_for_each_family() -> None:
    reg = load_registry(REGISTRY)
    for eid in reg.all_ids():
        adapter = create_adapter(eid, reg)
        assert adapter.engine_id == eid


def test_matrix_binding_stage1_only_uses_clm_partner() -> None:
    reg = load_registry(REGISTRY)
    partners = FixedStagePartners.from_registry(reg)
    binding = bind_matrix_row(reg.get("anyjev-l0"), partners)
    assert binding.stage1_config_id == "anyjev-l0"
    assert binding.stage2_config_id == "clm-8b"


def test_matrix_binding_stage2_only_uses_choice_partner() -> None:
    reg = load_registry(REGISTRY)
    partners = FixedStagePartners.from_registry(reg)
    binding = bind_matrix_row(reg.get("clm-8b"), partners)
    assert binding.stage1_config_id == "anyjev-l0"
    assert binding.stage2_config_id == "clm-8b"


def test_l1_calibration_gate_rejects_empty() -> None:
    reg = load_registry(REGISTRY)
    with pytest.raises(RuntimeError, match="200"):
        validate_calibration(reg.get("anyjev-l1"), ROOT)
