from finagent_mesh.matrix.strata import win_loss_vs_baseline


def test_win_loss_epsilon() -> None:
    base = [
        {"example_id": "a", "scored": True, "stage2_ndcg_at_5": 0.20},
        {"example_id": "b", "scored": True, "stage2_ndcg_at_5": 0.50},
        {"example_id": "c", "scored": True, "stage2_ndcg_at_5": 0.30},
    ]
    chal = [
        {"example_id": "a", "scored": True, "stage2_ndcg_at_5": 0.40},  # win
        {"example_id": "b", "scored": True, "stage2_ndcg_at_5": 0.505},  # tie
        {"example_id": "c", "scored": True, "stage2_ndcg_at_5": 0.10},  # loss
    ]
    out = win_loss_vs_baseline(
        base,
        chal,
        baseline_pair_id="lux-lux",
        challenger_pair_id="lux-e5",
        inspect_name="x.inspect.html",
    )
    assert out["wins"] == 1
    assert out["ties"] == 1
    assert out["losses"] == 1
    assert out["n_compared"] == 3
