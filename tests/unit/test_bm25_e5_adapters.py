from finagent_mesh.clients.engines.bm25_score import Bm25ScoreAdapter
from finagent_mesh.clients.engines.noop_choice import NoopChoiceAdapter
from finagent_mesh.clients.engines.registry import EngineConfiguration


def _cfg(cid: str, family: str, backend: str) -> EngineConfiguration:
    return EngineConfiguration(
        config_id=cid,
        family=family,
        display_name=cid,
        primitives=["score"] if "bm25" in cid or "e5" in cid else ["choice"],
        primary_stages=["stage2"] if "bm25" in cid else ["stage1"],
        base_url="http://localhost:9",
        backend=backend,
        model_revision="test",
        is_heavy_gpu=False,
        is_light_edge=True,
    )


def test_bm25_ranks_relevant_chunk_first() -> None:
    adapter = Bm25ScoreAdapter(_cfg("bm25-stage2", "lexical-ir", "bm25_inprocess"))
    ok, _ = adapter.health()
    assert ok
    data = adapter.decide(
        "score",
        "revenue growth guidance",
        [
            {"id": "a", "text": "unrelated weather report"},
            {"id": "b", "text": "company revenue growth and guidance outlook"},
        ],
    )
    ordered = [r["id"] for r in sorted(data["ranking"], key=lambda r: r["rank"])]
    assert ordered[0] == "b"


def test_noop_choice_sentinel_top1() -> None:
    adapter = NoopChoiceAdapter(_cfg("noop-choice", "noop", "noop_inprocess"))
    data = adapter.decide(
        "choice",
        "q",
        [{"id": "10-K", "text": "t"}, {"id": "10-Q", "text": "t"}],
    )
    ordered = [r["id"] for r in sorted(data["ranking"], key=lambda r: r["rank"])]
    assert ordered[0] == "__all__"
