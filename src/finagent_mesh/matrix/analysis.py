"""Paper-facing analysis report with Block A/B tables and inspect links."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from finagent_mesh.matrix.evidence_report import build_p0_evidence, render_p0_markdown_sections
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRowResult, MatrixRun


DEFERRED_ISSUES = [
    {
        "pair_id": "lux-clm-ft",
        "issue": "https://github.com/caldeirav/finagent-mesh-mcp/issues/1",
        "rationale": "Trained dual-encoder heads on held-out split",
    },
    {
        "pair_id": "lux-e5-ce",
        "issue": "https://github.com/caldeirav/finagent-mesh-mcp/issues/2",
        "rationale": "Dense shortlist then cross-encoder ceiling",
    },
]


def _fmt(v: Any, *, pct: bool = False) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        if pct:
            return f"{100.0 * v:.1f}%"
        return f"{v:.4f}"
    return str(v)


def _delta(cur: float | None, base: float | None) -> str:
    if cur is None or base is None:
        return "—"
    d = cur - base
    sign = "+" if d >= 0 else ""
    return f"{sign}{d:.4f}"


def _rows_for_block(matrix: MatrixRun, block: str) -> list[MatrixRowResult]:
    out = []
    for r in matrix.rows:
        blocks = r.blocks or (r.metrics.blocks if r.metrics else []) or []
        if block in blocks or (not blocks and block == "?"):
            out.append(r)
        elif r.variable_config_id == "lux-lux" and block in {"A", "B"}:
            out.append(r)
    seen: set[str] = set()
    uniq = []
    for r in out:
        if r.variable_config_id in seen:
            continue
        seen.add(r.variable_config_id)
        uniq.append(r)
    return uniq


def _measured(row: MatrixRowResult) -> bool:
    m = row.metrics
    return (
        m.stage1_ndcg_at_5 is not None
        or m.stage2_ndcg_at_5 is not None
        or m.stage1_top1_recall is not None
    )


def _find_row(matrix: MatrixRun, pair_id: str) -> MatrixRowResult | None:
    for r in matrix.rows:
        if r.variable_config_id == pair_id:
            return r
    return None


def _pair_outcome_summaries(
    matrix: MatrixRun,
    inspect_examples: dict[str, list[dict[str, Any]]] | None,
) -> list[dict[str, Any]]:
    """Per-pair counts for the analysis summary table (not every example)."""
    out: list[dict[str, Any]] = []
    inspect_name = f"{matrix.matrix_run_id}.inspect.html"
    for row in matrix.rows:
        examples = (inspect_examples or {}).get(row.variable_config_id) or []
        n_completed = n_empty = n_other = 0
        for ex in examples:
            err = ex.get("error")
            skipped = (ex.get("stage2") or {}).get("skipped_reason")
            st = ex.get("ledger_state") or ""
            if err == "empty_top1_chunks" or skipped == "empty_top1_chunks":
                n_empty += 1
            elif st in {"completed", "synthesis_retriable"} or (
                not err and st not in {"failed", "failed_retriable"}
            ):
                if st in {"failed", "failed_retriable"}:
                    n_other += 1
                else:
                    n_completed += 1
            else:
                n_other += 1
        if not examples:
            status = "measured" if _measured(row) else (
                "null_metrics" if row.status == "completed" else row.status
            )
        elif n_other and not n_completed and not n_empty:
            status = "failed"
        elif _measured(row):
            status = "measured"
        else:
            status = "null_metrics"
        out.append(
            {
                "pair_id": row.variable_config_id,
                "status": status,
                "n_examples": row.metrics.n_examples or len(examples) or 0,
                "n_completed": n_completed or (
                    (row.metrics.n_examples - row.metrics.n_empty_top1)
                    if examples == [] and _measured(row) and row.metrics.n_examples
                    else n_completed
                ),
                "n_empty_top1": n_empty
                if examples
                else int(row.metrics.n_empty_top1 or 0),
                "n_other_fail": n_other,
                "measured": _measured(row),
                "href": f"{inspect_name}#pair-{row.variable_config_id}",
            }
        )
    return out


def _build_findings(
    matrix: MatrixRun,
    *,
    pair_summaries: list[dict[str, Any]],
) -> dict[str, Any]:
    """Structured findings for JSON + narrative Markdown sections."""
    block_a = [r for r in _rows_for_block(matrix, "A") if r.status == "completed"]
    block_b = [
        r
        for r in _rows_for_block(matrix, "B")
        if r.status == "completed" and r.variable_config_id != "one-shot-ar"
    ]
    measured_a = [r for r in block_a if _measured(r)]
    measured_b = [r for r in block_b if _measured(r)]
    lux = _find_row(matrix, "lux-lux")
    lux_s1 = lux.metrics.stage1_ndcg_at_5 if lux else None
    lux_s2 = lux.metrics.stage2_ndcg_at_5 if lux else None
    lux_s2_cond = lux.metrics.stage2_ndcg_at_5_given_top1 if lux else None

    null_pairs = [
        r.variable_config_id
        for r in matrix.rows
        if r.status == "completed" and not _measured(r)
    ]
    failed_pairs = [r.variable_config_id for r in matrix.rows if r.status == "failed"]

    executive: list[str] = []
    bullets: list[str] = []
    block_a_notes: list[str] = []
    block_b_notes: list[str] = []
    routing_notes: list[str] = []
    latency_notes: list[str] = []
    takeaways: list[str] = []

    # --- Block A Choice ranking ---
    if measured_a:
        s2s = {r.stage2_engine_id for r in measured_a}
        if len(s2s) == 1:
            bullets.append(
                f"Block A holds Stage-2 fixed at `{next(iter(s2s))}` — Stage-2 "
                "nDCG differences across these rows reflect routing quality, not a different scorer."
            )
        else:
            bullets.append(
                f"WARNING: Block A Stage-2 engines differ: {sorted(s2s)} — check catalog."
            )

        ranked_a = sorted(
            measured_a,
            key=lambda r: (r.metrics.stage1_ndcg_at_5 is not None, r.metrics.stage1_ndcg_at_5 or -1),
            reverse=True,
        )
        best_a = ranked_a[0]
        executive.append(
            f"**Best Choice router (Block A):** `{best_a.variable_config_id}` with "
            f"Stage-1 nDCG@5 = {_fmt(best_a.metrics.stage1_ndcg_at_5)} "
            f"(Top-1 filing-type recall {_fmt(best_a.metrics.stage1_top1_recall, pct=True)})."
        )
        block_a_notes.append(
            "Ranked by Stage-1 nDCG@5 (filing-type ranking quality). "
            f"Lux Choice baseline (`lux-lux`) is {_fmt(lux_s1)}."
        )
        for i, r in enumerate(ranked_a, start=1):
            m = r.metrics
            ofr = (
                f", option-flip rate {_fmt(m.option_flip_rate, pct=True)}"
                if m.option_flip_rate is not None
                else ""
            )
            block_a_notes.append(
                f"{i}. **`{r.variable_config_id}`** (`{r.stage1_engine_id}`) — "
                f"nDCG@5 {_fmt(m.stage1_ndcg_at_5)} "
                f"({_delta(m.stage1_ndcg_at_5, lux_s1)} vs Lux), "
                f"Top-1 recall {_fmt(m.stage1_top1_recall, pct=True)}, "
                f"S1 p50 {_fmt(m.latency_stage1_p50_ms)} ms{ofr}."
            )
        anyjev = _find_row(matrix, "anyjev-l0-lux")
        if anyjev and anyjev.metrics.option_flip_rate is not None:
            block_a_notes.append(
                f"AnyJev L0 reports order sensitivity: OFR = "
                f"{_fmt(anyjev.metrics.option_flip_rate, pct=True)} "
                "(fraction of examples whose top Choice flips when options are permuted)."
            )
        kai = _find_row(matrix, "kai-lux")
        if kai and _measured(kai) and lux and _measured(lux):
            block_a_notes.append(
                f"Kai is much faster than Lux Choice "
                f"({_fmt(kai.metrics.latency_stage1_p50_ms)} vs "
                f"{_fmt(lux.metrics.latency_stage1_p50_ms)} ms p50) but trails on "
                f"nDCG@5 ({_fmt(kai.metrics.stage1_ndcg_at_5)} vs {_fmt(lux_s1)})."
            )

    # --- Block B Score ranking ---
    if measured_b:
        s1s = {r.stage1_engine_id for r in measured_b}
        if len(s1s) == 1:
            bullets.append(
                f"Block B holds Stage-1 fixed at `{next(iter(s1s))}` — compare Stage-2 "
                "overall nDCG vs **nDCG@5|Top-1** (scorer quality when routing was correct)."
            )
        ranked_b = sorted(
            measured_b,
            key=lambda r: (r.metrics.stage2_ndcg_at_5 is not None, r.metrics.stage2_ndcg_at_5 or -1),
            reverse=True,
        )
        best_b = ranked_b[0]
        executive.append(
            f"**Best passage scorer (Block B, overall S2 nDCG@5):** "
            f"`{best_b.variable_config_id}` = {_fmt(best_b.metrics.stage2_ndcg_at_5)} "
            f"(conditional-on-Top-1 {_fmt(best_b.metrics.stage2_ndcg_at_5_given_top1)})."
        )
        block_b_notes.append(
            "Ranked by overall Stage-2 nDCG@5 (full pipeline after Lux Choice). "
            f"Lux Score baseline (`lux-lux`) is {_fmt(lux_s2)} "
            f"(conditional {_fmt(lux_s2_cond)})."
        )
        for i, r in enumerate(ranked_b, start=1):
            m = r.metrics
            block_b_notes.append(
                f"{i}. **`{r.variable_config_id}`** (`{r.stage2_engine_id}`) — "
                f"S2 nDCG@5 {_fmt(m.stage2_ndcg_at_5)} "
                f"({_delta(m.stage2_ndcg_at_5, lux_s2)} vs Lux), "
                f"S2|Top-1 {_fmt(m.stage2_ndcg_at_5_given_top1)}, "
                f"empty-Top-1 {_fmt(m.empty_top1_chunk_rate, pct=True)}, "
                f"S2 p50 {_fmt(m.latency_stage2_p50_ms)} ms."
            )
        clm = _find_row(matrix, "lux-clm")
        if clm and _measured(clm):
            block_b_notes.append(
                f"CLM zero-shot Action Cache is weakest on this sample "
                f"(S2 nDCG@5 {_fmt(clm.metrics.stage2_ndcg_at_5)}) and slowest "
                f"(p50 {_fmt(clm.metrics.latency_stage2_p50_ms)} ms) — treat as a "
                "stress baseline, not a production scorer, until shortlist/FT variants run."
            )
        e5 = _find_row(matrix, "lux-e5")
        bm25 = _find_row(matrix, "lux-bm25")
        if e5 and _measured(e5) and lux_s2 is not None and (e5.metrics.stage2_ndcg_at_5 or 0) > lux_s2:
            block_b_notes.append(
                "E5 (general-domain dense) and/or BM25 beat Lux Score on overall "
                "passage nDCG here — surprising for a finance-specialized ordinal Score "
                "head; confirm on full FinAgentBench and with finance-tuned dense/CE ceilings."
            )
        if bm25 and e5 and _measured(bm25) and _measured(e5):
            latency_notes.append(
                f"BM25 is essentially free (p50 {_fmt(bm25.metrics.latency_stage2_p50_ms)} ms) "
                f"vs E5 ({_fmt(e5.metrics.latency_stage2_p50_ms)} ms) vs Lux Score "
                f"({_fmt(lux.metrics.latency_stage2_p50_ms) if lux else '—'} ms)."
            )

    # --- Routing ceiling ---
    empty_rates = [
        (r.variable_config_id, r.metrics.empty_top1_chunk_rate, r.metrics.n_empty_top1)
        for r in matrix.rows
        if _measured(r) and r.metrics.empty_top1_chunk_rate is not None
    ]
    if empty_rates:
        # Lux-backed Block B rows share Choice → same empty rate; Choice-varying Block A differ.
        routing_notes.append(
            "When Stage-2 has no type-filtered candidates (`empty_top1_chunks`), those "
            "examples are **omitted** from primary (scored-only) S2 nDCG/MRR and count as "
            "**0** in the secondary **pipeline-averaged** series. See Routing accounting "
            "for class counts — empty is not always “wrong Top-1 type.”"
        )
        for pid, rate, n in empty_rates:
            row = _find_row(matrix, pid)
            n_ex = row.metrics.n_examples if row else None
            suffix = f" ({n} / {n_ex} examples)" if n and n_ex else ""
            routing_notes.append(f"- `{pid}`: empty-Top-1 rate {_fmt(rate, pct=True)}{suffix}")
        if lux and lux.metrics.empty_top1_chunk_rate:
            executive.append(
                f"**Routing ceiling:** ~{_fmt(lux.metrics.empty_top1_chunk_rate, pct=True)} of "
                "examples under Lux Choice yield empty Stage-2 candidate sets — passage "
                "scoring cannot recover those misses."
            )

    # --- Data quality / nulls ---
    if null_pairs:
        bullets.append(
            "Pairs with completed status but **null metrics** (engine load / all-example "
            f"failures): {', '.join(f'`{p}`' for p in null_pairs)}."
        )
    if failed_pairs:
        bullets.append(
            f"Failed pairs: {', '.join(f'`{p}`' for p in failed_pairs)}."
        )
    measured_n = sum(1 for s in pair_summaries if s.get("measured"))
    executive.append(
        f"**Coverage:** {measured_n}/{len(matrix.rows)} matrix pairs have measurable "
        f"ranking metrics on N={len(matrix.selected_example_ids)} (seed={matrix.sample_seed})."
    )

    if not matrix.synthesis_enabled:
        bullets.append(
            "Answer EM/F1 were **not** collected (ranking-only; Gemini synthesis off)."
        )

    # --- Takeaways ---
    if measured_a:
        ranked_a = sorted(
            measured_a,
            key=lambda r: (r.metrics.stage1_ndcg_at_5 is not None, r.metrics.stage1_ndcg_at_5 or -1),
            reverse=True,
        )
        takeaways.append(
            f"For typed Choice routing, prefer `{ranked_a[0].variable_config_id}` "
            "on this sample; cite OFR when claiming AnyJev robustness."
        )
    if measured_b:
        ranked_b = sorted(
            measured_b,
            key=lambda r: (r.metrics.stage2_ndcg_at_5 is not None, r.metrics.stage2_ndcg_at_5 or -1),
            reverse=True,
        )
        takeaways.append(
            f"For Stage-2 passage scoring after Lux Choice, `{ranked_b[0].variable_config_id}` "
            "leads on overall nDCG@5; also report conditional-on-Top-1 and latency."
        )
    takeaways.append(
        "Always separate **router quality** (Block A / empty-Top-1 rate) from **scorer "
        "quality** (Block B S2|Top-1); overall S2 mixes both."
    )
    if not matrix.synthesis_enabled:
        takeaways.append(
            "Re-run with `--with-synthesis` when answer-span EM/F1 are needed for the paper."
        )

    # Flat list kept for backward-compatible JSON consumers / tests.
    flat = list(bullets)
    if measured_a:
        best = max(
            measured_a,
            key=lambda r: (r.metrics.stage1_ndcg_at_5 is not None, r.metrics.stage1_ndcg_at_5 or -1),
        )
        flat.append(
            f"Strongest Block A Stage-1 nDCG@5 among completed rows: "
            f"`{best.variable_config_id}` ({_fmt(best.metrics.stage1_ndcg_at_5)})."
        )
    if measured_b:
        best2 = max(
            measured_b,
            key=lambda r: (r.metrics.stage2_ndcg_at_5 is not None, r.metrics.stage2_ndcg_at_5 or -1),
        )
        flat.append(
            f"Strongest Block B Stage-2 nDCG@5 (overall): "
            f"`{best2.variable_config_id}` ({_fmt(best2.metrics.stage2_ndcg_at_5)})."
        )

    return {
        "executive_summary": executive,
        "guardrails": bullets,
        "block_a": block_a_notes,
        "block_b": block_b_notes,
        "routing": routing_notes,
        "latency": latency_notes,
        "takeaways": takeaways,
        "findings": flat,
    }


def build_analysis_payload(
    matrix: MatrixRun,
    *,
    inspect_examples: dict[str, list[dict[str, Any]]] | None = None,
    multi_seed_matrices: list[MatrixRun] | None = None,
) -> dict[str, Any]:
    """Build machine-readable analysis index."""
    pair_summaries = _pair_outcome_summaries(matrix, inspect_examples)
    structured = _build_findings(matrix, pair_summaries=pair_summaries)
    p0 = build_p0_evidence(
        matrix,
        inspect_examples=inspect_examples,
        multi_seed_matrices=multi_seed_matrices,
    )
    # Drop internal contrib cache from JSON
    p0_public = {k: v for k, v in p0.items() if not k.startswith("_")}

    # Compact artifact index: one row per pair (full example drill-down lives in inspect HTML).
    artifact_index = [
        {
            "pair_id": s["pair_id"],
            "example_id": None,
            "status": s["status"],
            "n_completed": s["n_completed"],
            "n_empty_top1": s["n_empty_top1"],
            "n_other_fail": s["n_other_fail"],
            "href": s["href"],
        }
        for s in pair_summaries
    ]
    return {
        "matrix_run_id": matrix.matrix_run_id,
        "n_examples": len(matrix.selected_example_ids),
        "sample_seed": matrix.sample_seed,
        "dataset_path": matrix.dataset_path,
        "synthesis_enabled": matrix.synthesis_enabled,
        "skip_records": list(matrix.skip_records),
        "deferred": DEFERRED_ISSUES,
        "executive_summary": structured["executive_summary"],
        "findings": structured["findings"],
        "findings_detail": {
            "guardrails": structured["guardrails"],
            "block_a": structured["block_a"],
            "block_b": structured["block_b"],
            "routing": structured["routing"],
            "latency": structured["latency"],
            "takeaways": structured["takeaways"],
        },
        "pair_outcomes": pair_summaries,
        "artifact_index": artifact_index,
        "rows": [r.to_dict() for r in matrix.rows],
        **p0_public,
    }


def build_analysis_markdown(matrix: MatrixRun, payload: dict[str, Any]) -> str:
    detail = payload.get("findings_detail") or {}
    lines: list[str] = [
        f"# Paper analysis — {matrix.matrix_run_id}",
        "",
        "## Executive summary",
        "",
    ]
    for item in payload.get("executive_summary") or []:
        lines.append(f"- {item}")
    if not payload.get("executive_summary"):
        lines.append("- No measured pairs yet.")

    lines.extend(
        [
            "",
            "## How to read this report",
            "",
            "1. **Block A** varies the Stage-1 **Choice** router; Stage-2 Score stays Lux. "
            "Higher S1 nDCG@5 / Top-1 recall = better filing-type routing.",
            "2. **Block B** varies the Stage-2 **Score** (or dense/lexical) head; Stage-1 "
            "Choice stays Lux. Compare overall S2 nDCG@5 (full pipeline) and "
            "**S2 nDCG@5|Top-1** (scorer only, when Top-1 type was correct).",
            "3. **`empty_top1_chunks`** means no type-filtered Stage-2 candidates "
            "(see Routing accounting — not always wrong Top-1). Primary S2 metrics are "
            "**scored-only**; **pipeline-averaged** treats empties as 0.",
            "",
            "## Run facts",
            "",
            f"- **N**: {len(matrix.selected_example_ids)}",
            f"- **Seed**: {matrix.sample_seed}",
            f"- **Dataset**: `{matrix.dataset_path}`",
            f"- **Synthesis**: {'on (reuse rankings if synthesis_reuse present)' if matrix.synthesis_enabled else 'not run (ranking-only)'}",
            f"- **Status**: {matrix.status}",
            "",
            "## Research questions",
            "",
            "1. Which Choice head routes SEC filing types well (Block A)?",
            "2. How should agents score long passages after type routing (Block B)?",
            "3. Does typed Choice→Score beat one-shot stuffing (optional baseline)?",
            "",
            "## Block A — Stage-1 Choice (Lux Score fixed)",
            "",
            "| Pair | S1 engine | S1 nDCG@5 | Δ vs Lux | Top-1 recall | OFR | Parse fail | S1 p50 ms |",
            "|---|---|---|---|---|---|---|---|",
        ]
    )
    lux = _find_row(matrix, "lux-lux")
    lux_s1 = lux.metrics.stage1_ndcg_at_5 if lux else None
    for r in _rows_for_block(matrix, "A"):
        m = r.metrics
        lines.append(
            f"| {r.variable_config_id} | {r.stage1_engine_id} | "
            f"{_fmt(m.stage1_ndcg_at_5)} | {_delta(m.stage1_ndcg_at_5, lux_s1)} | "
            f"{_fmt(m.stage1_top1_recall)} | {_fmt(m.option_flip_rate)} | "
            f"{_fmt(m.parse_failure_rate)} | {_fmt(m.latency_stage1_p50_ms)} |"
        )
    if detail.get("block_a"):
        lines.extend(["", "### Block A findings", ""])
        for note in detail["block_a"]:
            lines.append(f"- {note}")

    lux_s2 = lux.metrics.stage2_ndcg_at_5 if lux else None
    series = payload.get("stage2_series") or {}
    lines.extend(
        [
            "",
            "## Block B — Stage-2 Score (Lux Choice fixed)",
            "",
            "| Pair | S2 engine | S2 nDCG (scored) | S2 MRR (scored) | Δ nDCG vs Lux | "
            "S2 nDCG\\|Top-1 | S2 nDCG (pipeline) | Empty Top-1 | S2 p50 ms |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
    )
    for r in _rows_for_block(matrix, "B"):
        m = r.metrics
        pm = (series.get(r.variable_config_id) or {}).get("pipeline_mean") or {}
        lines.append(
            f"| {r.variable_config_id} | {r.stage2_engine_id} | "
            f"{_fmt(m.stage2_ndcg_at_5)} | {_fmt(m.stage2_mrr_at_5)} | "
            f"{_delta(m.stage2_ndcg_at_5, lux_s2)} | "
            f"{_fmt(m.stage2_ndcg_at_5_given_top1)} | {_fmt(pm.get('stage2_ndcg_at_5'))} | "
            f"{_fmt(m.empty_top1_chunk_rate)} | {_fmt(m.latency_stage2_p50_ms)} |"
        )
    if detail.get("block_b"):
        lines.extend(["", "### Block B findings", ""])
        for note in detail["block_b"]:
            lines.append(f"- {note}")

    # P0 sections: routing accounting, dual series detail, strata, win/loss, CIs, synth
    lines.extend(render_p0_markdown_sections(payload))

    lines.extend(["", "## Routing vs scoring (narrative)", ""])
    routing = detail.get("routing") or []
    if routing:
        lines.append(routing[0])
        lines.append("")
        for note in routing[1:]:
            lines.append(note if note.startswith("- ") else f"- {note}")
    else:
        lines.append(
            "See Routing accounting. Prefer **S2 nDCG@5|Top-1** and scored-only means when "
            "judging scorers; use pipeline-averaged S2 for end-to-end agent yield."
        )

    lines.extend(
        [
            "",
            "## Latency / resources",
            "",
            "| Pair | S1 p50/p95 (ms) | S2 p50/p95 (ms) | GPU high-water MB |",
            "|---|---|---|---|",
        ]
    )
    for r in matrix.rows:
        m = r.metrics
        lines.append(
            f"| {r.variable_config_id} | {_fmt(m.latency_stage1_p50_ms)}/{_fmt(m.latency_stage1_p95_ms)} | "
            f"{_fmt(m.latency_stage2_p50_ms)}/{_fmt(m.latency_stage2_p95_ms)} | "
            f"{_fmt(m.gpu_mem_high_water_mb)} |"
        )
    if detail.get("latency"):
        lines.extend(["", "### Latency notes", ""])
        for note in detail["latency"]:
            lines.append(f"- {note}")

    lines.extend(["", "## Guardrails", ""])
    for f in detail.get("guardrails") or payload.get("findings") or []:
        lines.append(f"- {f}")

    lines.extend(["", "## Takeaways", ""])
    for t in detail.get("takeaways") or []:
        lines.append(f"- {t}")
    if not detail.get("takeaways"):
        lines.append("- See Block A/B findings above.")

    lines.extend(
        [
            "",
            "## Pair outcomes",
            "",
            "| Pair | Status | Completed | Empty Top-1 | Other fail | Inspect |",
            "|---|---|---|---|---|---|",
        ]
    )
    for s in payload.get("pair_outcomes") or payload.get("artifact_index") or []:
        lines.append(
            f"| {s.get('pair_id')} | {s.get('status')} | "
            f"{s.get('n_completed', '—')} | {s.get('n_empty_top1', '—')} | "
            f"{s.get('n_other_fail', '—')} | "
            f"[open]({s.get('href')}) |"
        )

    lines.extend(
        [
            "",
            "## Limitations / threats to validity",
            "",
            "- Sample N may be below full FinAgentBench; seed and N are recorded above.",
            "- CLM Stage-2 is zero-shot Action Cache (2k context) unless shortlist optional row ran.",
            "- E5 is general-domain, not finance-tuned; BM25 is lexical only.",
            "- Empty-Top-1 rates depend on the Stage-1 engine — Block A rows are not "
            "comparable on Stage-2 overall nDCG without conditioning on Top-1.",
            "- Deferred trained heads: "
            "[#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1).",
            "- Deferred cross-encoder ceiling: "
            "[#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2).",
            "",
            "## Skipped / deferred pairs",
            "",
        ]
    )
    for s in matrix.skip_records or []:
        lines.append(
            f"- `{s.get('pair_id')}` — {s.get('reason')}"
            + (f" ([issue]({s.get('issue_url')}))" if s.get("issue_url") else "")
        )
    for d in DEFERRED_ISSUES:
        if not any(s.get("pair_id") == d["pair_id"] for s in (matrix.skip_records or [])):
            lines.append(f"- `{d['pair_id']}` — deferred_issue ([issue]({d['issue']}))")
    lines.extend(
        [
            "",
            "## Artifact index",
            "",
            f"- Interactive inspect (per-example): `{matrix.matrix_run_id}.inspect.html`",
            f"- Analysis JSON: `{matrix.matrix_run_id}.analysis.json`",
            f"- Matrix JSON / CSV: `{matrix.matrix_run_id}.json`, `{matrix.matrix_run_id}.csv`",
            "",
        ]
    )
    return "\n".join(lines)


def write_analysis_reports(
    matrix: MatrixRun,
    *,
    out_md: Path,
    out_json: Path,
    inspect_payload: dict[str, Any] | None = None,
    multi_seed_matrices: list[MatrixRun] | None = None,
) -> tuple[Path, Path]:
    by_pair: dict[str, list[dict[str, Any]]] = {}
    if inspect_payload:
        for p in inspect_payload.get("pairs") or []:
            by_pair[str(p.get("pair_id"))] = list(p.get("examples") or [])
    payload = build_analysis_payload(
        matrix,
        inspect_examples=by_pair,
        multi_seed_matrices=multi_seed_matrices,
    )
    md = build_analysis_markdown(matrix, payload)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md, encoding="utf-8")
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_md, out_json
