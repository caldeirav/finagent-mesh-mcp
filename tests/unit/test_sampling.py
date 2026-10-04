from finagent_mesh.matrix.sampling import select_example_ids


def test_full_mode_returns_all() -> None:
    ids = ["a", "b"]
    sel = select_example_ids(ids, sample_size=None, sample_seed=None)
    assert sel.selected_example_ids == ids
