"""Resolver smoke: default paper set excludes optional rows."""

from pathlib import Path

from finagent_mesh.clients.engines.registry import load_registry
from finagent_mesh.matrix.partners import resolve_matrix_pairs


ROOT = Path(__file__).resolve().parents[2]


def test_default_real_pair_set_excludes_optional() -> None:
    reg = load_registry(ROOT / "configs" / "engines.yaml")
    ids = {p.pair_id for p in resolve_matrix_pairs(reg, repo_root=ROOT)}
    assert "lux-clm-shortlist" not in ids
    assert "one-shot-ar" not in ids
    # Required Block A + B
    assert {"lux-lux", "anyjev-l0-lux", "lux-clm", "lux-bm25", "lux-e5"} <= ids
