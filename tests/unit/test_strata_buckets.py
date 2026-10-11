from finagent_mesh.matrix.strata import build_strata, cand_size_bucket, quartile_cuts


def test_cand_buckets() -> None:
    assert cand_size_bucket(3) == "1-8"
    assert cand_size_bucket(20) == "9-32"
    assert cand_size_bucket(100) == "33-128"
    assert cand_size_bucket(200) == "129+"


def test_build_strata_has_cells() -> None:
    by_pair = {
        "lux-lux": [
            {
                "example_id": "1",
                "scored": True,
                "stage2_ndcg_at_5": 0.2,
                "gold_type": "10-K",
                "cand_size": 10,
                "length_chars": 100,
            }
        ],
        "lux-e5": [
            {
                "example_id": "1",
                "scored": True,
                "stage2_ndcg_at_5": 0.4,
                "gold_type": "10-K",
                "cand_size": 10,
                "length_chars": 100,
            }
        ],
    }
    cells = build_strata(by_pair, pair_ids=["lux-lux", "lux-e5"])
    assert any(c["axis"] == "gold_type" for c in cells)
    assert quartile_cuts([1, 2, 3, 4, 5, 6, 7, 8])
