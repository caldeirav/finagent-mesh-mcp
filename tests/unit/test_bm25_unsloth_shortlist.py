"""BM25 → Unsloth shortlist hybrid tests."""

from __future__ import annotations

from pathlib import Path

from finagent_mesh.clients.engines.bm25_unsloth_shortlist import Bm25UnslothShortlistAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration


def test_shortlist_k_and_rerank(tmp_path: Path, monkeypatch):
    ckpt = tmp_path / "ckpt"
    ckpt.mkdir()
    (ckpt / "adapter_config.json").write_text("{}", encoding="utf-8")
    monkeypatch.setenv("UNSLOTH_SCORE_CHECKPOINT", str(ckpt))
    monkeypatch.setenv("UNSLOTH_SHORTLIST_K", "2")

    cfg = EngineConfiguration(
        config_id="bm25-unsloth-score-shortlist-32",
        family="hybrid-ir",
        display_name="hybrid",
        primitives=["score"],
        primary_stages=["stage2"],
        base_url="http://localhost:8711",
        backend="bm25_unsloth_shortlist",
        model_revision="test",
        is_heavy_gpu=True,
        is_light_edge=False,
    )
    ad = Bm25UnslothShortlistAdapter(cfg)
    # Inject score adapter without loading Unsloth
    from finagent_mesh.clients.engines.unsloth_score import UnslothScoreAdapter

    score = UnslothScoreAdapter(
        EngineConfiguration(
            config_id="unsloth-decision-score",
            family="unsloth-decision",
            display_name="u",
            primitives=["score"],
            primary_stages=["stage2"],
            base_url="http://localhost:8711",
            backend="unsloth_score",
            model_revision="t",
        )
    )
    score._inject_scores = lambda q, cands, meta: list(range(len(cands), 0, -1))
    ad._score = score

    cands = [
        {"id": f"c{i}", "text": f"apple banana {i} revenue growth" if i < 3 else f"zzz {i}"}
        for i in range(5)
    ]
    out = ad.decide("score", "revenue growth", cands)
    assert out["shortlist_k"] == 2
    assert out["n_shortlisted"] == 2
    assert out["backend"] == "bm25_unsloth_shortlist"
    assert len(out["ranking"]) == 5
