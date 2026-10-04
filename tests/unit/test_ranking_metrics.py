from finagent_mesh.metrics.ranking import map_at_k, mrr_at_k, ndcg_at_k, stable_rank


def test_stable_rank_tie_break():
    ranked = stable_rank(["b", "a"], [1.0, 1.0])
    assert [r[0] for r in ranked] == ["a", "b"]


def test_metrics_deterministic():
    ordered = ["10-K", "10-Q", "8-K", "Earnings", "DEF14A"]
    labels = ["10-K", "8-K"]
    a = (ndcg_at_k(ordered, labels, 5), map_at_k(ordered, labels, 5), mrr_at_k(ordered, labels, 5))
    b = (ndcg_at_k(ordered, labels, 5), map_at_k(ordered, labels, 5), mrr_at_k(ordered, labels, 5))
    assert a == b
    assert a[2] == 1.0
