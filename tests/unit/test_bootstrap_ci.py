import pytest

from finagent_mesh.matrix.uncertainty import bootstrap_ci, bootstrap_delta_ci, multi_seed_rollup


def test_bootstrap_ci_point() -> None:
    ci = bootstrap_ci([0.2, 0.4, 0.6], n_resamples=200, seed=1)
    assert ci["point"] == pytest.approx(0.4)
    assert ci["ci_low"] is not None and ci["ci_high"] is not None
    assert ci["ci_low"] <= ci["point"] <= ci["ci_high"]


def test_bootstrap_delta() -> None:
    a = [0.3, 0.4, 0.5]
    b = [0.1, 0.2, 0.3]
    d = bootstrap_delta_ci(a, b, n_resamples=200, seed=2)
    assert d["point"] is not None and d["point"] > 0


def test_multi_seed_rollup() -> None:
    r = multi_seed_rollup({42: 0.2, 7: 0.4, 123: 0.6})
    assert r["mean_of_means"] == pytest.approx(0.4)
    assert r["min"] == 0.2
    assert r["max"] == 0.6
