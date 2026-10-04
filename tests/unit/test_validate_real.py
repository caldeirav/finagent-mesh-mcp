from pathlib import Path

import pytest

from finagent_mesh.dataset.validate_real import RealRunError, assert_real_dataset, assert_real_runtime


def test_sample_dataset_rejected_for_real(tmp_path: Path) -> None:
    sample = tmp_path / "finagentbench"
    sample.mkdir()
    # Wiring-only dump: few labeled rows under a non-sample filename
    (sample / "tiny.jsonl").write_text(
        '{"example_id":"a","firm_id":"","query_text":"q","stage1_labels":["10-K"],'
        '"stage2_labels":[],"chunks":[]}\n'
        '{"example_id":"b","firm_id":"","query_text":"q2","stage1_labels":["10-Q"],'
        '"stage2_labels":[],"chunks":[]}\n'
    )
    with pytest.raises(RealRunError, match="only"):
        assert_real_dataset(sample, min_examples=100)


def test_mock_rejected() -> None:
    with pytest.raises(RealRunError, match="SYSTEMONE_MOCK"):
        assert_real_runtime(systemone_mock=True, backend="real")


def test_lexical_backend_rejected() -> None:
    with pytest.raises(RealRunError, match="SYSTEMONE_BACKEND"):
        assert_real_runtime(systemone_mock=False, backend="lexical")
