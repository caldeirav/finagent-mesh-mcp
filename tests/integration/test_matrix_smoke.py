"""Matrix orchestration smoke with fake/local constraints (no GPU)."""

from __future__ import annotations

from pathlib import Path

import pytest

from finagent_mesh.config import require_official_mock_policy
from finagent_mesh.matrix.partners import FixedStagePartners, bind_matrix_row
from finagent_mesh.matrix.sampling import select_example_ids
from finagent_mesh.clients.engines.registry import load_registry


ROOT = Path(__file__).resolve().parents[2]


def test_mock_refused_without_allow_mock() -> None:
    with pytest.raises(RuntimeError, match="SYSTEMONE_MOCK"):
        require_official_mock_policy(systemone_mock=True, allow_mock=False)


def test_mock_allowed_with_flag() -> None:
    require_official_mock_policy(systemone_mock=True, allow_mock=True)


def test_seeded_sample_reproducible() -> None:
    ids = [f"ex-{i}" for i in range(100)]
    a = select_example_ids(ids, sample_size=50, sample_seed=42)
    b = select_example_ids(ids, sample_size=50, sample_seed=42)
    assert a.selected_example_ids == b.selected_example_ids
    assert len(a.selected_example_ids) == 50


def test_sample_capped_when_larger_than_dataset() -> None:
    ids = ["a", "b", "c"]
    sel = select_example_ids(ids, sample_size=10, sample_seed=1)
    assert sel.capped is True
    assert len(sel.selected_example_ids) == 3


def test_sequential_binding_varies_one_engine() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    partners = FixedStagePartners.from_registry(reg)
    rows = [bind_matrix_row(reg.get(eid), partners) for eid in ("anyjev-l0", "clm-8b")]
    assert rows[0].variable_config_id == "anyjev-l0"
    assert rows[1].variable_config_id == "clm-8b"
    # Partner co-runs: stage2 of first row is partner clm; stage1 of second is partner anyjev
    assert rows[0].stage2_config_id == "clm-8b"
    assert rows[1].stage1_config_id == "anyjev-l0"


def test_architecture_default_pairs_exclude_baseline() -> None:
    from finagent_mesh.matrix.partners import resolve_matrix_pairs

    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, repo_root=ROOT)
    ids = [p.pair_id for p in pairs]
    assert "lux-lux" in ids
    assert "kai-lux" in ids
    assert "laya-lux" in ids
    assert "anyjev-l0-lux" in ids
    assert "lux-clm" in ids
    assert "lux-bm25" in ids
    assert "lux-e5" in ids
    assert "ar-lux" in ids
    assert "kai-clm" not in ids
    lux_lux = next(p for p in pairs if p.pair_id == "lux-lux")
    assert lux_lux.unique_engines() == ["decision20-lux"]
