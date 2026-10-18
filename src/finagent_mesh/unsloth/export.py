"""Gold-type FinAgentBench → Unsloth Score row export."""

from __future__ import annotations

from typing import Any, Iterable

from finagent_mesh.agent.state import BenchmarkExample
from finagent_mesh.unsloth.types import SCORE_CRITERIA, ScoreTrainingRow


def _gold_doc_types(example: BenchmarkExample) -> list[str]:
    out: list[str] = []
    for x in example.stage1_labels or []:
        if isinstance(x, dict):
            out.append(str(x.get("doc_type") or x.get("id") or ""))
        else:
            out.append(str(x))
    return [t for t in out if t]


def _relevance_map(example: BenchmarkExample) -> dict[str, int]:
    labels: dict[str, int] = {}
    for row in example.stage2_labels or []:
        if isinstance(row, dict):
            cid = str(row.get("chunk_id") or row.get("id") or "")
            if not cid:
                continue
            rel = int(float(row.get("relevance", row.get("label", 0))))
            labels[cid] = max(0, min(2, rel))
    return labels


def build_score_row(
    example: BenchmarkExample,
    *,
    max_candidates: int | None = None,
    max_text_chars: int | None = 4000,
) -> ScoreTrainingRow | None:
    """Build one Score training row with gold-type candidates only.

    Returns None when the gold-type pool is empty (caller must count skips).
    """
    gold = _gold_doc_types(example)
    gold_set = set(gold)
    rel = _relevance_map(example)
    candidates: list[dict[str, Any]] = []
    for chunk in example.chunks:
        if gold_set and chunk.doc_type not in gold_set:
            continue
        text = chunk.text or ""
        if max_text_chars is not None and len(text) > max_text_chars:
            text = text[:max_text_chars]
        candidates.append(
            {
                "id": chunk.chunk_id,
                "text": text,
                "doc_type": chunk.doc_type,
                "relevance": rel.get(chunk.chunk_id, 0),
            }
        )
    if not candidates:
        return None
    if max_candidates is not None and len(candidates) > max_candidates:
        # Prefer higher relevance then stable id
        candidates.sort(key=lambda c: (-int(c["relevance"]), str(c["id"])))
        candidates = candidates[:max_candidates]
    labels = {str(c["id"]): int(c["relevance"]) for c in candidates}
    row = ScoreTrainingRow(
        example_id=example.example_id,
        query=example.query_text,
        candidates=candidates,
        score_criteria=list(SCORE_CRITERIA),
        labels=labels,
        gold_doc_types=gold,
    )
    row.validate()
    return row


def export_score_rows(
    examples: Iterable[BenchmarkExample],
    *,
    allowed_ids: set[str] | None = None,
    max_candidates: int | None = None,
    max_text_chars: int | None = 4000,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    rows: list[dict[str, Any]] = []
    stats = {"n_input": 0, "n_exported": 0, "n_empty_gold_pool": 0, "n_skipped_id": 0}
    for ex in examples:
        stats["n_input"] += 1
        if allowed_ids is not None and ex.example_id not in allowed_ids:
            stats["n_skipped_id"] += 1
            continue
        built = build_score_row(
            ex, max_candidates=max_candidates, max_text_chars=max_text_chars
        )
        if built is None:
            stats["n_empty_gold_pool"] += 1
            continue
        rows.append(built.to_export_dict())
        stats["n_exported"] += 1
    return rows, stats
