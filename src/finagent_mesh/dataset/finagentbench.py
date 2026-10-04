"""FinAgentBench dataset loader with subset sampling."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

from finagent_mesh.agent.state import BenchmarkExample, PassageChunk
from finagent_mesh.agent.types import DOC_TYPE_SET, DOC_TYPES


class DatasetError(RuntimeError):
    pass


def _validate_labels(stage1_labels: list[str]) -> None:
    bad = [x for x in stage1_labels if x not in DOC_TYPE_SET]
    if bad:
        raise DatasetError(f"Invalid stage1 label doc types {bad}; allowed={list(DOC_TYPES)}")


def load_examples(path: Path, *, limit: int | None = None) -> list[BenchmarkExample]:
    if not path.exists():
        raise DatasetError(f"FINAGENTBENCH_PATH not found: {path}")
    examples: list[BenchmarkExample] = []
    if path.is_file():
        examples.extend(_load_file(path))
    else:
        for fp in sorted(path.rglob("*.jsonl")):
            if fp.name.startswith("sample"):
                continue
            examples.extend(_load_file(fp))
        for fp in sorted(path.rglob("*.json")):
            if fp.name.endswith(".jsonl") or fp.name.startswith("sample"):
                continue
            examples.extend(_load_file(fp))
    if not examples:
        raise DatasetError(f"No FinAgentBench examples found under {path}")
    if limit is not None:
        examples = examples[:limit]
    return examples


def iter_examples(path: Path, *, limit: int | None = None) -> Iterator[BenchmarkExample]:
    yield from load_examples(path, limit=limit)


def _load_file(path: Path) -> list[BenchmarkExample]:
    # File iteration splits on LF only. str.splitlines() also splits on U+2028/U+2029,
    # which appear in SEC filings and would bisect JSON strings.
    if path.suffix == ".jsonl":
        rows: list[dict] = []
        with path.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip("\n\r")
                if line.strip():
                    rows.append(json.loads(line))
    else:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            rows = data
        elif isinstance(data, dict) and "examples" in data:
            rows = data["examples"]
        else:
            rows = [data]
    out: list[BenchmarkExample] = []
    for row in rows:
        stage1 = list(row.get("stage1_labels") or row.get("doc_type_labels") or [])
        # Preserve graded dict labels; validate underlying doc-type ids
        type_ids = [
            str(x) if not isinstance(x, dict) else str(x.get("doc_type", x.get("id")))
            for x in stage1
        ]
        _validate_labels(type_ids)
        norm_stage1: list = []
        for x in stage1:
            if isinstance(x, dict):
                cid = str(x.get("doc_type", x.get("id")))
                norm_stage1.append(
                    {
                        "id": cid,
                        "doc_type": cid,
                        "relevance": float(x.get("relevance", x.get("label", 1.0))),
                    }
                )
            else:
                norm_stage1.append(str(x))
        chunks_raw = row.get("chunks") or []
        chunks = [
            PassageChunk(
                chunk_id=str(c.get("chunk_id", c.get("id"))),
                doc_type=str(c.get("doc_type", "")),
                text=str(c.get("text", "")),
                is_table=bool(c.get("is_table", False)),
            )
            for c in chunks_raw
        ]
        out.append(
            BenchmarkExample(
                example_id=str(row.get("example_id") or row.get("id")),
                firm_id=str(row.get("firm_id") or row.get("ticker") or ""),
                query_text=str(row.get("query_text") or row.get("question") or ""),
                query_category=str(row.get("query_category") or row.get("category") or ""),
                stage1_labels=norm_stage1,
                stage2_labels=list(row.get("stage2_labels") or row.get("chunk_labels") or []),
                answer_label=row.get("answer_label") or row.get("answer"),
                chunks=chunks,
            )
        )
    return out
