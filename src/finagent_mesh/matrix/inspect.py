"""Per-example inspect reports: expected labels vs Stage-1/2 I/O vs synthesis."""

from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path
from typing import Any

from finagent_mesh.dataset.finagentbench import load_examples
from finagent_mesh.ledger.sqlite_ledger import SqliteLedger
from finagent_mesh.matrix.models import MatrixRun


def _gold_s1(labels: list[Any]) -> list[str]:
    out: list[str] = []
    for item in labels or []:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict):
            out.append(str(item.get("id") or item.get("doc_type") or item))
        else:
            out.append(str(item))
    return out


def _gold_s2_map(labels: list[Any]) -> dict[str, float]:
    mapped: dict[str, float] = {}
    for item in labels or []:
        if isinstance(item, dict):
            cid = str(item.get("id") or item.get("chunk_id") or "")
            rel = item.get("relevance", item.get("label", 1))
            try:
                mapped[cid] = float(rel)
            except (TypeError, ValueError):
                mapped[cid] = 1.0
        elif isinstance(item, str):
            mapped[item] = 1.0
    return mapped


def _example_card(
    pair_id: str,
    example_id: str,
    entry_state: str,
    last_error: str | None,
    ranking: dict[str, Any] | None,
    synthesis: dict[str, Any] | None,
    dataset_ex: Any | None,
) -> dict[str, Any]:
    ranking = ranking or {}
    expected = ranking.get("expected") or {}
    if dataset_ex is not None:
        expected = {
            "example_id": dataset_ex.example_id,
            "firm_id": dataset_ex.firm_id,
            "query_text": dataset_ex.query_text,
            "query_category": dataset_ex.query_category,
            "stage1_labels": dataset_ex.stage1_labels,
            "stage2_labels": dataset_ex.stage2_labels,
            "answer_label": dataset_ex.answer_label,
            "n_chunks": len(dataset_ex.chunks),
            "chunks_by_doc_type": dict(Counter(c.doc_type for c in dataset_ex.chunks)),
        }
    s1 = ranking.get("stage1") or {}
    s2 = ranking.get("stage2") or {}
    gold1 = _gold_s1(expected.get("stage1_labels") or [])
    gold2 = _gold_s2_map(expected.get("stage2_labels") or [])
    top1 = ranking.get("top1_doc_type")
    ordered1 = list(s1.get("ordered_ids") or [])
    ordered2 = list(s2.get("ordered_ids") or [])
    chunk_by_id = {c.get("chunk_id"): c for c in (ranking.get("stage2_chunks") or []) if c.get("chunk_id")}
    s2_rows = []
    for i, cid in enumerate(ordered2[:15]):
        ch = chunk_by_id.get(cid) or {}
        s2_rows.append(
            {
                "rank": i + 1,
                "chunk_id": cid,
                "score": (s2.get("scores") or [None] * len(ordered2))[i] if i < len(s2.get("scores") or []) else None,
                "gold_relevance": gold2.get(cid),
                "text": (ch.get("text") or "")[:400],
            }
        )
    return {
        "example_id": example_id or expected.get("example_id") or "",
        "pair_id": pair_id,
        "ledger_state": entry_state,
        "error": last_error or ranking.get("error"),
        "expected": expected,
        "stage1": {
            "engine": ranking.get("stage1_engine"),
            "top1": top1,
            "top1_in_gold": (top1 in gold1) if top1 else False,
            "gold": gold1,
            "ordered_ids": ordered1,
            "scores": s1.get("scores"),
            "distribution": s1.get("decision_distribution") or s1.get("distribution"),
            "ndcg_at_5": s1.get("ndcg_at_5"),
            "map_at_5": s1.get("map_at_5"),
            "mrr_at_5": s1.get("mrr_at_5"),
            "skipped_reason": s1.get("skipped_reason"),
        },
        "stage2": {
            "engine": ranking.get("stage2_engine"),
            "skipped_reason": s2.get("skipped_reason"),
            "ndcg_at_5": s2.get("ndcg_at_5"),
            "map_at_5": s2.get("map_at_5"),
            "mrr_at_5": s2.get("mrr_at_5"),
            "n_scored": len(ordered2),
            "gold_ids": list(gold2.keys())[:20],
            "rows": s2_rows,
        },
        "io_traces": ranking.get("io_traces") or [],
        "synthesis": synthesis,
    }


def build_inspect_payload(
    matrix: MatrixRun,
    *,
    ledger_path: Path,
    dataset_path: Path | None = None,
) -> dict[str, Any]:
    examples_by_id: dict[str, Any] = {}
    path = Path(dataset_path or matrix.dataset_path)
    if path.exists():
        try:
            for ex in load_examples(path):
                examples_by_id[ex.example_id] = ex
        except Exception:  # noqa: BLE001
            examples_by_id = {}

    ledger = SqliteLedger(ledger_path)
    pairs: list[dict[str, Any]] = []
    try:
        for row in matrix.rows:
            entries = ledger.list_entries(row.eval_run_id)
            cards = []
            n_ok = n_fail = 0
            for ent in entries:
                if ent.state == "completed":
                    n_ok += 1
                elif ent.state == "failed_retriable":
                    n_fail += 1
                cards.append(
                    _example_card(
                        row.variable_config_id,
                        ent.example_id,
                        ent.state,
                        ent.last_error,
                        ent.ranking_payload_json,
                        ent.synthesis_payload_json,
                        examples_by_id.get(ent.example_id),
                    )
                )
            m = row.metrics.to_dict()
            pairs.append(
                {
                    "pair_id": row.variable_config_id,
                    "eval_run_id": row.eval_run_id,
                    "stage1_engine_id": row.stage1_engine_id,
                    "stage2_engine_id": row.stage2_engine_id,
                    "row_status": row.status,
                    "row_error": row.error,
                    "metrics": m,
                    "n_completed": n_ok,
                    "n_failed_retriable": n_fail,
                    "examples": cards,
                }
            )
    finally:
        ledger.close()

    return {
        "matrix_run_id": matrix.matrix_run_id,
        "dataset_path": matrix.dataset_path,
        "sample_size": matrix.sample_size,
        "sample_seed": matrix.sample_seed,
        "synthesis_enabled": matrix.synthesis_enabled,
        "gemini_model": matrix.gemini_model,
        "status": matrix.status,
        "pairs": pairs,
    }


def _esc(v: Any) -> str:
    return html.escape("" if v is None else str(v))


def render_inspect_html(payload: dict[str, Any]) -> str:
    """Standalone HTML: pair summary + per-example expected vs model I/O."""
    parts: list[str] = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'/>",
        f"<title>Inspect {html.escape(str(payload.get('matrix_run_id')))}</title>",
        "<style>",
        "body{font-family:ui-sans-serif,system-ui,sans-serif;margin:24px;line-height:1.4;max-width:1200px}",
        "table{border-collapse:collapse;width:100%;font-size:14px;margin:12px 0}",
        "th,td{border:1px solid #ccc;padding:6px 8px;text-align:left;vertical-align:top}",
        "th{background:#f4f4f4}",
        "details{margin:8px 0;border:1px solid #ddd;padding:8px 12px}",
        "summary{cursor:pointer;font-weight:600}",
        "pre{white-space:pre-wrap;background:#f7f7f7;padding:8px;overflow:auto;max-height:320px}",
        ".ok{color:#0a6}.fail{color:#a30}.muted{color:#666;font-size:13px}",
        "</style></head><body>",
        f"<h1>Benchmark inspect — {_esc(payload.get('matrix_run_id'))}</h1>",
        "<p class='muted'>Each pair is a Stage-1 × Stage-2 combination. Open a pair, then an example, "
        "to compare labels (expected) with engine inputs/outputs and optional Gemini synthesis.</p>",
        "<h2>All combinations</h2>",
        "<table><thead><tr><th>Pair</th><th>S1 engine</th><th>S2 engine</th>"
        "<th>S1 nDCG@5</th><th>S2 nDCG@5</th><th>Completed</th><th>Failed</th><th>Row</th></tr></thead><tbody>",
    ]
    for p in payload.get("pairs") or []:
        m = p.get("metrics") or {}
        parts.append(
            "<tr>"
            f"<td><a href='#pair-{_esc(p['pair_id'])}'>{_esc(p['pair_id'])}</a></td>"
            f"<td>{_esc(p.get('stage1_engine_id'))}</td>"
            f"<td>{_esc(p.get('stage2_engine_id'))}</td>"
            f"<td>{_esc(m.get('stage1_ndcg_at_5'))}</td>"
            f"<td>{_esc(m.get('stage2_ndcg_at_5'))}</td>"
            f"<td>{_esc(p.get('n_completed'))}</td>"
            f"<td>{_esc(p.get('n_failed_retriable'))}</td>"
            f"<td>{_esc(p.get('row_status'))}</td>"
            "</tr>"
        )
    parts.append("</tbody></table>")

    for p in payload.get("pairs") or []:
        parts.append(f"<h2 id='pair-{_esc(p['pair_id'])}'>{_esc(p['pair_id'])}</h2>")
        parts.append(
            f"<p class='muted'>eval_run_id=<code>{_esc(p.get('eval_run_id'))}</code> · "
            f"S1={_esc(p.get('stage1_engine_id'))} · S2={_esc(p.get('stage2_engine_id'))}</p>"
        )
        for ex in p.get("examples") or []:
            eid = ex.get("example_id") or "unknown"
            st = ex.get("ledger_state")
            cls = "ok" if st == "completed" else "fail"
            exp = ex.get("expected") or {}
            s1 = ex.get("stage1") or {}
            s2 = ex.get("stage2") or {}
            anchor = f"pair-{p['pair_id']}-ex-{eid}"
            parts.append(f"<details id='{_esc(anchor)}'>")
            parts.append(
                f"<summary><span class='{cls}'>{_esc(st)}</span> · "
                f"<a href='#{_esc(anchor)}'>{_esc(eid)}</a> · "
                f"S1 nDCG={_esc(s1.get('ndcg_at_5'))} · S2 nDCG={_esc(s2.get('ndcg_at_5'))}"
                f"{' · ' + _esc(ex.get('error')) if ex.get('error') else ''}</summary>"
            )
            parts.append("<h3>Expected (benchmark)</h3>")
            parts.append(f"<p><strong>Query</strong>: {_esc(exp.get('query_text'))}</p>")
            parts.append(
                f"<p>firm={_esc(exp.get('firm_id'))} · chunks={_esc(exp.get('n_chunks'))} · "
                f"by type={_esc(exp.get('chunks_by_doc_type'))}</p>"
            )
            parts.append(f"<p><strong>Stage-1 gold types</strong>: {_esc(s1.get('gold'))}</p>")
            parts.append(f"<p><strong>Stage-2 gold chunk ids</strong> (first 20): {_esc(s2.get('gold_ids'))}</p>")
            if exp.get("answer_label"):
                parts.append(f"<p><strong>Answer label</strong>: {_esc(exp.get('answer_label'))}</p>")

            parts.append("<h3>Stage 1 output</h3>")
            parts.append(
                f"<p>engine={_esc(s1.get('engine'))} · top1=<strong>{_esc(s1.get('top1'))}</strong> "
                f"in gold={_esc(s1.get('top1_in_gold'))}</p>"
            )
            parts.append(f"<p>ordered: {_esc(s1.get('ordered_ids'))}</p>")
            parts.append(f"<p>scores: {_esc(s1.get('scores'))}</p>")

            parts.append("<h3>Stage 2 output</h3>")
            parts.append(
                f"<p>engine={_esc(s2.get('engine'))} · skipped={_esc(s2.get('skipped_reason'))} · "
                f"n_scored={_esc(s2.get('n_scored'))}</p>"
            )
            parts.append(
                "<table><thead><tr><th>Rank</th><th>Chunk</th><th>Score</th>"
                "<th>Gold rel</th><th>Text</th></tr></thead><tbody>"
            )
            for r in s2.get("rows") or []:
                parts.append(
                    "<tr>"
                    f"<td>{_esc(r.get('rank'))}</td>"
                    f"<td><code>{_esc(r.get('chunk_id'))}</code></td>"
                    f"<td>{_esc(r.get('score'))}</td>"
                    f"<td>{_esc(r.get('gold_relevance'))}</td>"
                    f"<td>{_esc(r.get('text'))}</td>"
                    "</tr>"
                )
            parts.append("</tbody></table>")

            syn = ex.get("synthesis")
            if syn:
                parts.append("<h3>Synthesis (Gemini)</h3>")
                parts.append(f"<p>model={_esc(syn.get('gemini_model'))}</p>")
                parts.append(f"<p><strong>Answer</strong>: {_esc(syn.get('answer'))}</p>")
                parts.append(f"<p><strong>Label</strong>: {_esc(syn.get('label'))}</p>")
                parts.append(f"<pre>{_esc(json.dumps(syn.get('answer_score'), indent=2))}</pre>")
                if syn.get("prompt"):
                    parts.append("<details><summary>Gemini prompt</summary>")
                    parts.append(f"<pre>{_esc(syn.get('prompt'))}</pre></details>")

            traces = ex.get("io_traces") or []
            if traces:
                parts.append("<h3>Model I/O traces</h3>")
                for i, tr in enumerate(traces, 1):
                    parts.append(
                        f"<details><summary>Call {i}: {_esc(tr.get('primitive'))} "
                        f"engine={_esc(tr.get('engine'))} n_cand={_esc(tr.get('n_candidates'))}"
                        f"{' ERROR' if tr.get('error') else ''}</summary>"
                    )
                    parts.append(f"<pre>{_esc(json.dumps(tr, indent=2)[:20000])}</pre></details>")
            parts.append("</details>")

    parts.append("</body></html>")
    return "".join(parts)


def write_inspect_reports(
    matrix: MatrixRun,
    *,
    ledger_path: Path,
    out_json: Path,
    out_html: Path,
    dataset_path: Path | None = None,
) -> tuple[Path, Path]:
    payload = build_inspect_payload(matrix, ledger_path=ledger_path, dataset_path=dataset_path)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    out_html.write_text(render_inspect_html(payload), encoding="utf-8")
    return out_json, out_html
