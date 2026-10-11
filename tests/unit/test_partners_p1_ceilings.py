"""P1 catalog: champions, shortlist-Lux, CE ceiling (005)."""

from pathlib import Path

import pytest

from finagent_mesh.clients.engines.registry import load_registry
from finagent_mesh.matrix.partners import deferred_skip_records, resolve_matrix_pairs
from finagent_mesh.matrix.ports import plan_engine_ports


ROOT = Path(__file__).resolve().parents[2]


def test_default_excludes_p1_optionals() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    ids = {p.pair_id for p in resolve_matrix_pairs(reg, repo_root=ROOT)}
    assert "anyjev-l0-e5" not in ids
    assert "anyjev-l0-bm25" not in ids
    assert "lux-lux-shortlist" not in ids
    assert "lux-e5-ce" not in ids


def test_include_optional_adds_p1_pairs() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    ids = {
        p.pair_id
        for p in resolve_matrix_pairs(reg, include_optional=True, repo_root=ROOT)
    }
    assert "anyjev-l0-e5" in ids
    assert "anyjev-l0-bm25" in ids
    assert "lux-lux-shortlist" in ids
    assert "lux-e5-ce" in ids


def test_explicit_champion_pairs_not_deferred() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(
        reg, pair_ids=["anyjev-l0-e5", "anyjev-l0-bm25"], repo_root=ROOT
    )
    assert [p.pair_id for p in pairs] == ["anyjev-l0-e5", "anyjev-l0-bm25"]
    assert all(p.role == "champion" for p in pairs)
    assert all(not p.deferred for p in pairs)
    assert pairs[0].stage1_config_id == "anyjev-l0"
    assert pairs[0].stage2_config_id == "e5-base"
    assert pairs[1].stage2_config_id == "bm25-stage2"


def test_lux_e5_ce_runnable_not_deferred() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, pair_ids=["lux-e5-ce"], repo_root=ROOT)
    assert pairs[0].role == "ir_ceiling"
    assert pairs[0].stage2_config_id == "e5-ce-shortlist-32"
    skips = {s.pair_id for s in deferred_skip_records(reg)}
    assert "lux-e5-ce" not in skips
    assert "lux-clm-ft" in skips


def test_champion_ports_no_extra_score_sidecar() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    plan = plan_engine_ports(reg, "anyjev-l0", "e5-base")
    assert plan == {"anyjev-l0": 8000}
    plan_bm = plan_engine_ports(reg, "anyjev-l0", "bm25-stage2")
    assert plan_bm == {"anyjev-l0": 8000}


def test_lux_shortlist_reuses_lux_choice_sidecar() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    plan = plan_engine_ports(reg, "decision20-lux", "lux-score-shortlist-32")
    assert plan == {"decision20-lux": 8000}


def test_e5_ce_does_not_start_clm() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    plan = plan_engine_ports(reg, "decision20-lux", "e5-ce-shortlist-32")
    assert plan == {"decision20-lux": 8000}
    assert "clm-8b" not in plan
