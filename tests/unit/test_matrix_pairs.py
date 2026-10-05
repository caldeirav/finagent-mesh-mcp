from pathlib import Path

import pytest

from finagent_mesh.clients.engines.registry import load_registry
from finagent_mesh.matrix.partners import deferred_skip_records, resolve_matrix_pairs


ROOT = Path(__file__).resolve().parents[2]


def test_default_pairs_are_block_ab_required() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, repo_root=ROOT)
    ids = [p.pair_id for p in pairs]
    assert "lux-lux" in ids
    assert "anyjev-l0-lux" in ids
    assert "kai-lux" in ids
    assert "laya-lux" in ids
    assert "ar-lux" in ids
    assert "lux-clm" in ids
    assert "lux-bm25" in ids
    assert "lux-e5" in ids
    assert "lux-clm-shortlist" not in ids
    assert "one-shot-ar" not in ids
    lux = next(p for p in pairs if p.pair_id == "lux-lux")
    assert set(lux.blocks) == {"A", "B"}
    assert lux.stage1_config_id == lux.stage2_config_id == "decision20-lux"


def test_include_optional_adds_shortlist_and_oneshot() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    ids = [
        p.pair_id
        for p in resolve_matrix_pairs(reg, include_optional=True, repo_root=ROOT)
    ]
    assert "lux-clm-shortlist" in ids
    assert "one-shot-ar" in ids
    oneshot = next(
        p
        for p in resolve_matrix_pairs(reg, include_optional=True, repo_root=ROOT)
        if p.pair_id == "one-shot-ar"
    )
    assert oneshot.collapsed_stages is True


def test_explicit_pair_ids() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, pair_ids=["kai-lux", "lux-lux"], repo_root=ROOT)
    assert [p.pair_id for p in pairs] == ["kai-lux", "lux-lux"]
    assert pairs[1].stage1_config_id == pairs[1].stage2_config_id == "decision20-lux"


def test_legacy_engines_uses_fixed_partners() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, engines=["decision20-kai", "clm-8b"], repo_root=ROOT)
    assert pairs[0].stage1_config_id == "decision20-kai"
    assert pairs[0].stage2_config_id == "clm-8b"
    assert pairs[1].stage1_config_id == "anyjev-l0"
    assert pairs[1].stage2_config_id == "clm-8b"


def test_unknown_pair_raises() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    with pytest.raises(KeyError, match="Unknown matrix pair"):
        resolve_matrix_pairs(reg, pair_ids=["not-a-pair"], repo_root=ROOT)


def test_deferred_skip_records() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    skips = deferred_skip_records(reg)
    ids = {s.pair_id for s in skips}
    assert "lux-clm-ft" in ids
    assert "lux-e5-ce" in ids
