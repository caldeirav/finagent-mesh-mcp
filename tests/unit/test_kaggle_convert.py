import json
from pathlib import Path

from finagent_mesh.dataset.kaggle_convert import convert_kaggle_dir, extract_question, parse_chunks


def test_extract_question_and_chunks() -> None:
    content = (
        "Question: What is Apple revenue?\n\n"
        "[Chunk Index 0] First passage about revenue.\n"
        "[Chunk Index 2] Second passage.\n"
        "\nTask: Select and rank the chunks\nResponse Format: list\n"
    )
    assert extract_question(content).startswith("What is Apple")
    chunks, idxs = parse_chunks(content)
    assert idxs == [0, 2]
    assert "revenue" in chunks[0]


def test_convert_synthetic_kaggle(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    raw.mkdir()
    doc = {
        "_id": "q1",
        "messages": [{"role": "user", "content": "Question: Cash flow risks?\n\nMore"}],
        "qrel": {"0": 1, "1": 4, "2": 2, "3": 0, "4": 3},
    }
    chunk = {
        "_id": "q1",
        "messages": [
            {
                "role": "user",
                "content": (
                    "Question: Cash flow risks?\n\n"
                    "[Chunk Index 0] Risk factors mention liquidity.\n"
                    "[Chunk Index 1] Unrelated boilerplate.\n"
                ),
            }
        ],
        "qrel": {"0": 2, "1": 0},
    }
    (raw / "document_ranking_kaggle_dev.jsonl").write_text(json.dumps(doc) + "\n")
    (raw / "chunk_ranking_kaggle_dev.jsonl").write_text(json.dumps(chunk) + "\n")
    out = tmp_path / "out"
    n = convert_kaggle_dir(raw, out)
    assert n == 1
    lines = (out / "finagentbench_dev.jsonl").read_text().strip().splitlines()
    ex = json.loads(lines[0])
    assert ex["query_text"].startswith("Cash flow")
    assert any(x["doc_type"] == "10-K" for x in ex["stage1_labels"])
    assert ex["chunks"]
    assert ex["stage2_labels"]
