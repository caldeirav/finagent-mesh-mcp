from pathlib import Path

import pytest

from finagent_mesh.clients.engines.registry import load_registry
from finagent_mesh.matrix.partners import resolve_matrix_pairs


ROOT = Path(__file__).resolve().parents[2]


def test_default_pairs_match_architecture_set() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, repo_root=ROOT)
    ids = [p.pair_id for p in pairs]
    assert ids[0] == "lux-clm"
    lux = next(p for p in pairs if p.pair_id == "lux-clm")
    assert lux.stage1_config_id == "decision20-lux"
    assert lux.stage2_config_id == "clm-8b"
    assert "ar-clm" not in ids
    # L1 only if 200-id file exists
    cal = ROOT / "configs" / "calibration" / "anyjev_l1_heldout.json"
    if not cal.exists():
        assert "anyjev-l1-clm" not in ids


def test_include_baseline_adds_ar() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    ids = [p.pair_id for p in resolve_matrix_pairs(reg, include_baseline=True, repo_root=ROOT)]
    assert "ar-clm" in ids


def test_explicit_pair_ids() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    pairs = resolve_matrix_pairs(reg, pair_ids=["kai-clm", "lux-lux"], repo_root=ROOT)
    assert [p.pair_id for p in pairs] == ["kai-clm", "lux-lux"]
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
