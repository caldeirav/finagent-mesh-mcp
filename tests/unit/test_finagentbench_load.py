from pathlib import Path

from finagent_mesh.dataset.finagentbench import load_examples


def test_load_jsonl_with_unicode_line_separator(tmp_path: Path) -> None:
    line_sep = "\u2028"
    row = {
        "example_id": "e1",
        "firm_id": "",
        "query_text": "q",
        "stage1_labels": ["10-K"],
        "stage2_labels": [],
        "chunks": [
            {
                "chunk_id": "c1",
                "doc_type": "10-K",
                "text": f"before{line_sep}after",
                "is_table": False,
            }
        ],
    }
    import json

    (tmp_path / "finagentbench_dev.jsonl").write_text(
        json.dumps(row, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    examples = load_examples(tmp_path)
    assert len(examples) == 1
    assert "after" in examples[0].chunks[0].text


def test_skips_sample_jsonl(tmp_path: Path) -> None:
    import json

    good = {
        "example_id": "e1",
        "firm_id": "",
        "query_text": "q",
        "stage1_labels": ["10-K"],
        "stage2_labels": [],
        "chunks": [],
    }
    (tmp_path / "finagentbench_dev.jsonl").write_text(json.dumps(good) + "\n")
    (tmp_path / "sample.jsonl").write_text("{not json\n")
    examples = load_examples(tmp_path)
    assert len(examples) == 1
