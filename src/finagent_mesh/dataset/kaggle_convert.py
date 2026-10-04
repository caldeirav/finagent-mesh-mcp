"""Convert ACM-ICAIF '25 Kaggle FinAgentBench JSONL into harness BenchmarkExample JSONL."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterator

# Competition document-type index order (from challenge / public solutions)
KAGGLE_DOC_INDEX = {
    0: "DEF14A",
    1: "10-K",
    2: "10-Q",
    3: "8-K",
    4: "Earnings",
}


def _query_id(item: dict[str, Any]) -> str:
    for key in ("uuid", "_id", "record_id", "query_id", "id"):
        if key in item and item[key] is not None:
            return str(item[key])
    raise ValueError("No query id field")


def _message_content(item: dict[str, Any]) -> str:
    messages = item.get("messages") or []
    if not messages:
        raise ValueError("No messages")
    # Prefer user content; fall back to first message
    for m in messages:
        if m.get("role") == "user" and m.get("content"):
            return str(m["content"])
    return str(messages[0].get("content") or "")


def extract_question(content: str) -> str:
    for pattern in (
        r"Question:\s*(.+?)(?:\n|$)",
        r"###QUESTION###\s*(.+?)(?:\n|$)",
    ):
        match = re.search(pattern, content, re.DOTALL)
        if match:
            question = match.group(1).strip()
            cut = question.find("\n\n")
            if cut != -1:
                question = question[:cut].strip()
            if question:
                return question
    raise ValueError("Question not found in message content")


def parse_chunks(content: str) -> tuple[list[str], list[int]]:
    task_pattern = r"\n+Task:\s+Select and rank.*?Response Format:.*?$"
    cleaned = re.sub(task_pattern, "", content, flags=re.DOTALL | re.IGNORECASE)
    pattern = r"\[Chunk Index (\d+)\]\s*(.+?)(?=\n\[Chunk Index |\n*$)"
    matches = re.findall(pattern, cleaned, re.DOTALL)
    if not matches:
        raise ValueError("No chunks found")
    chunks: list[str] = []
    indices: list[int] = []
    for idx_str, text in matches:
        text = text.strip()
        if text:
            chunks.append(text)
            indices.append(int(idx_str))
    if not chunks:
        raise ValueError("Empty chunks")
    return chunks, indices


def _iter_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def load_document_rows(path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    for item in _iter_jsonl(path):
        qid = _query_id(item)
        content = _message_content(item)
        question = extract_question(content)
        qrel = item.get("qrel") or {}
        # Normalize qrel keys to int
        grades: dict[int, float] = {}
        for k, v in qrel.items():
            grades[int(k)] = float(v)
        stage1_labels: list[dict[str, Any]] = []
        for idx, grade in grades.items():
            if idx in KAGGLE_DOC_INDEX and grade > 0:
                stage1_labels.append(
                    {"id": KAGGLE_DOC_INDEX[idx], "doc_type": KAGGLE_DOC_INDEX[idx], "relevance": grade}
                )
        top1 = None
        if grades:
            top_idx = max(grades.items(), key=lambda kv: (kv[1], -kv[0]))[0]
            top1 = KAGGLE_DOC_INDEX.get(top_idx)
        rows[qid] = {
            "query_id": qid,
            "question": question,
            "stage1_labels": stage1_labels,
            "top1_doc_type": top1,
            "has_qrel": bool(grades),
        }
    return rows


def load_chunk_rows(path: Path) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return rows
    for item in _iter_jsonl(path):
        qid = _query_id(item)
        content = _message_content(item)
        question = extract_question(content)
        chunks, indices = parse_chunks(content)
        qrel = item.get("qrel") or {}
        grades = {int(k): float(v) for k, v in qrel.items()}
        stage2_labels = [
            {"chunk_id": f"chunk-{idx}", "relevance": grades.get(idx, 0.0)}
            for idx in indices
            if grades.get(idx, 0.0) > 0
        ]
        # Keep all chunks; labels only for positive grades
        if not stage2_labels and grades:
            # eval sets hide qrel — leave empty labels
            stage2_labels = []
        rows[qid] = {
            "query_id": qid,
            "question": question,
            "chunks_text": chunks,
            "chunk_indices": indices,
            "stage2_labels": stage2_labels,
            "has_qrel": bool(grades),
        }
    return rows


def _by_question(rows: dict[str, dict[str, Any]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for qid, row in rows.items():
        key = re.sub(r"\s+", " ", row["question"].strip().lower())
        out.setdefault(key, qid)
    return out


def merge_to_examples(
    doc_rows: dict[str, dict[str, Any]],
    chunk_rows: dict[str, dict[str, Any]],
    *,
    split: str,
) -> list[dict[str, Any]]:
    """Join document + chunk rows into harness examples."""
    examples: list[dict[str, Any]] = []
    used_chunks: set[str] = set()
    chunk_by_q = _by_question(chunk_rows)

    for qid, drow in doc_rows.items():
        crow = chunk_rows.get(qid)
        if crow is None:
            qkey = re.sub(r"\s+", " ", drow["question"].strip().lower())
            alt = chunk_by_q.get(qkey)
            crow = chunk_rows.get(alt) if alt else None
        if crow:
            used_chunks.add(crow["query_id"])
        top1 = drow.get("top1_doc_type") or "10-K"
        chunks = []
        stage2_labels = []
        if crow:
            for text, idx in zip(crow["chunks_text"], crow["chunk_indices"], strict=True):
                cid = f"{qid}:chunk-{idx}"
                chunks.append(
                    {
                        "chunk_id": cid,
                        "doc_type": top1,
                        "text": text,
                        "is_table": False,
                    }
                )
            # Remap stage2 label ids to namespaced chunk ids
            for lab in crow["stage2_labels"]:
                raw = str(lab["chunk_id"]).replace("chunk-", "")
                stage2_labels.append(
                    {
                        "chunk_id": f"{qid}:chunk-{raw}",
                        "relevance": lab["relevance"],
                    }
                )
        examples.append(
            {
                "example_id": f"{split}:{qid}",
                "firm_id": "",
                "query_text": drow["question"],
                "query_category": split,
                "stage1_labels": drow["stage1_labels"],
                "stage2_labels": stage2_labels,
                "answer_label": None,
                "chunks": chunks,
            }
        )

    # Chunk-only rows (no document join): duplicate chunks under all doc types
    # so Stage-2 still has candidates regardless of Stage-1 Top-1.
    from finagent_mesh.agent.types import DOC_TYPES

    for qid, crow in chunk_rows.items():
        if qid in used_chunks:
            continue
        chunks = []
        for dt in DOC_TYPES:
            for text, idx in zip(crow["chunks_text"], crow["chunk_indices"], strict=True):
                chunks.append(
                    {
                        "chunk_id": f"{qid}:{dt}:chunk-{idx}",
                        "doc_type": dt,
                        "text": text,
                        "is_table": False,
                    }
                )
        stage2_labels = []
        for lab in crow["stage2_labels"]:
            raw = str(lab["chunk_id"]).replace("chunk-", "")
            # Grade applies for whichever Top-1 is chosen; label all doc-type variants
            for dt in DOC_TYPES:
                stage2_labels.append(
                    {
                        "chunk_id": f"{qid}:{dt}:chunk-{raw}",
                        "relevance": lab["relevance"],
                    }
                )
        examples.append(
            {
                "example_id": f"{split}:chunk-only:{qid}",
                "firm_id": "",
                "query_text": crow["question"],
                "query_category": f"{split}-chunk",
                "stage1_labels": [],
                "stage2_labels": stage2_labels,
                "answer_label": None,
                "chunks": chunks,
            }
        )
    return examples


def convert_kaggle_dir(raw_dir: Path, out_dir: Path) -> int:
    """Convert all available Kaggle JSONL splits into harness JSONL files."""
    out_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    pairs = [
        ("dev", "document_ranking_kaggle_dev.jsonl", "chunk_ranking_kaggle_dev.jsonl"),
        ("eval", "document_ranking_kaggle_eval.jsonl", "chunk_ranking_kaggle_eval.jsonl"),
    ]
    for split, doc_name, chunk_name in pairs:
        docs = load_document_rows(raw_dir / doc_name)
        chunks = load_chunk_rows(raw_dir / chunk_name)
        if not docs and not chunks:
            continue
        examples = merge_to_examples(docs, chunks, split=split)
        out_path = out_dir / f"finagentbench_{split}.jsonl"
        with out_path.open("w", encoding="utf-8") as fh:
            for ex in examples:
                fh.write(json.dumps(ex, ensure_ascii=False) + "\n")
        total += len(examples)
        print(f"Wrote {len(examples)} examples → {out_path}")
    # Prefer keeping sample.jsonl aside; harness loads all json/jsonl under path
    return total
