from pathlib import Path

from finagent_mesh.dataset.kaggle_fetch import EXPECTED_RAW, ensure_local_finagentbench

FIXTURE_LINE = (
    '{"example_id":"q","firm_id":"","query_text":"t","query_category":"dev",'
    '"stage1_labels":[{"id":"10-K","doc_type":"10-K","relevance":1}],'
    '"stage2_labels":[],"chunks":[]}\n'
)


def test_ensure_skips_download_when_raw_and_harness_present(tmp_path: Path, monkeypatch) -> None:
    raw = tmp_path / "raw"
    out = tmp_path / "out"
    raw.mkdir()
    out.mkdir()
    for name in EXPECTED_RAW:
        (raw / name).write_text("{}\n")
    (out / "finagentbench_dev.jsonl").write_text(FIXTURE_LINE * 120)

    def boom(*_a, **_k):
        raise AssertionError("download should not run")

    monkeypatch.setattr("finagent_mesh.dataset.kaggle_fetch.download_kaggle_files", boom)
    monkeypatch.setattr("finagent_mesh.dataset.kaggle_fetch.convert_kaggle_dir", boom)

    n = ensure_local_finagentbench(harness_out=out, raw_dir=raw, min_examples=100)
    assert n >= 100


def test_ensure_converts_when_harness_missing(tmp_path: Path, monkeypatch) -> None:
    raw = tmp_path / "raw"
    out = tmp_path / "out"
    raw.mkdir()
    for name in EXPECTED_RAW:
        (raw / name).write_text("{}\n")

    called = {"convert": False}

    def fake_convert(raw_dir, harness_out):
        called["convert"] = True
        harness_out.mkdir(parents=True, exist_ok=True)
        (harness_out / "finagentbench_dev.jsonl").write_text(FIXTURE_LINE * 120)
        return 120

    monkeypatch.setattr("finagent_mesh.dataset.kaggle_fetch.download_kaggle_files", lambda *a, **k: [])
    monkeypatch.setattr("finagent_mesh.dataset.kaggle_fetch.convert_kaggle_dir", fake_convert)

    n = ensure_local_finagentbench(harness_out=out, raw_dir=raw, min_examples=100)
    assert called["convert"]
    assert n >= 100


def test_ensure_downloads_when_raw_missing(tmp_path: Path, monkeypatch) -> None:
    raw = tmp_path / "raw"
    out = tmp_path / "out"
    downloaded = {"n": 0}

    def fake_download(raw_dir, *, force=False):
        downloaded["n"] += 1
        raw_dir.mkdir(parents=True, exist_ok=True)
        for name in EXPECTED_RAW:
            (raw_dir / name).write_text("{}\n")
        return list(raw_dir.glob("*.jsonl"))

    def fake_convert(raw_dir, harness_out):
        harness_out.mkdir(parents=True, exist_ok=True)
        (harness_out / "finagentbench_dev.jsonl").write_text(FIXTURE_LINE * 120)
        return 120

    monkeypatch.setattr("finagent_mesh.dataset.kaggle_fetch.download_kaggle_files", fake_download)
    monkeypatch.setattr("finagent_mesh.dataset.kaggle_fetch.convert_kaggle_dir", fake_convert)

    n = ensure_local_finagentbench(harness_out=out, raw_dir=raw, min_examples=100)
    assert downloaded["n"] == 1
    assert n >= 100
