"""Build a detailed Markdown performance report with interpretation."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from finagent_mesh.matrix.models import MatrixRun


def _fmt(v: float | None, digits: int = 4) -> str:
    if v is None:
        return "—"
    return f"{v:.{digits}f}"


def _rank_rows(
    matrix: MatrixRun, key: str
) -> list[tuple[str, float | None]]:
    scored: list[tuple[str, float | None]] = []
    for row in matrix.rows:
        m = row.metrics.to_dict()
        scored.append((row.variable_config_id, m.get(key)))
    scored.sort(
        key=lambda x: (x[1] is None, -(x[1] or 0.0), x[0]),
    )
    return scored


def _best_label(ranked: list[tuple[str, float | None]]) -> str:
    if not ranked or ranked[0][1] is None:
        return "insufficient data"
    return f"{ranked[0][0]} ({_fmt(ranked[0][1])})"


def build_interpretation_markdown(matrix: MatrixRun) -> str:
    """Return a human-readable report with metrics tables and interpretation."""
    now = datetime.now(timezone.utc).isoformat()
    completed = [r for r in matrix.rows if r.status == "completed"]
    failed = [r for r in matrix.rows if r.status == "failed"]

    s1_ranked = _rank_rows(matrix, "stage1_ndcg_at_5")
    s2_ranked = _rank_rows(matrix, "stage2_ndcg_at_5")
    ans_ranked = _rank_rows(matrix, "answer_token_f1")

    lines: list[str] = [
        "# FinAgentBench Decision-Model Benchmark Report",
        "",
        f"**Generated**: {now}  ",
        f"**Matrix run ID**: `{matrix.matrix_run_id}`  ",
        f"**Dataset**: `{matrix.dataset_path}`  ",
        f"**Sample size**: {matrix.sample_size if matrix.sample_size is not None else 'full dataset'}  ",
        f"**Sample seed**: {matrix.sample_seed if matrix.sample_seed is not None else 'n/a'}  ",
        f"**Examples processed**: {len(matrix.selected_example_ids)}  ",
        f"**Gemini model**: `{matrix.gemini_model}`  ",
        f"**Synthesis enabled**: {matrix.synthesis_enabled}  ",
        f"**System-1 mock**: {matrix.systemone_mock}  ",
        f"**Overall status**: `{matrix.status}`  ",
        "",
        "## What this run did",
        "",
        "This benchmark evaluates **open System-1 decision engines** on FinAgentBench "
        "using the FinAgent Mesh agentic pipeline:",
        "",
        "1. **Stage 1 (Choice)** — rank document types for each query.",
        "2. **Stage 2 (Score / Action Cache)** — rank passage chunks from the Top-1 Stage-1 type.",
        "3. **System-2 (optional)** — Gemini synthesizes a final answer from top Stage-2 chunks "
        "(fail-closed; no extractive fallback).",
        "",
        "Each matrix row is an **architecture-true pair**: Stage 1 is a small-K **Choice** "
        "(five filing types) and Stage 2 is **Score** over long enumerated chunks. "
        "Default partners remain available for `--engines` ablation "
        f"(Stage-1 partner=`{matrix.partner_ids.get('stage1_partner_id', 'anyjev-l0')}`, "
        f"Stage-2 partner=`{matrix.partner_ids.get('stage2_partner_id', 'clm-8b')}`; "
        f"binding=`{matrix.partner_ids.get('binding', 'architecture-pairs')}`). "
        "Stage-1 metrics are attributed to the Stage-1 producer; Stage-2 metrics to the Stage-2 producer.",
        "",
        "## Metric definitions",
        "",
        "| Metric | Meaning |",
        "|--------|---------|",
        "| **nDCG@5** | Normalized discounted cumulative gain at 5 — ranking quality with position discount |",
        "| **MAP@5** | Mean average precision at 5 — precision across relevant ranks |",
        "| **MRR@5** | Mean reciprocal rank at 5 — how early the first relevant item appears |",
        "| **Answer EM / token-F1** | Exact-match and token overlap vs labeled answers (when synthesis ran) |",
        "| **Parse failure rate** | Share of AR baseline JSON parses that failed |",
        "| **Latency p50/p95** | Decision latency percentiles (when recorded by adapters) |",
        "",
        "Higher nDCG / MAP / MRR / answer scores are better. Lower parse-failure and latency are better.",
        "",
        "## Results by pair (Stage 1 × Stage 2)",
        "",
        "| Pair | Status | Stage-1 producer | Stage-2 producer | "
        "S1 nDCG@5 | S1 MAP@5 | S1 MRR@5 | S2 nDCG@5 | S2 MAP@5 | S2 MRR@5 | "
        "Ans EM | Ans F1 | Parse fail | N |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    for row in matrix.rows:
        m = row.metrics.to_dict()
        lines.append(
            "| `{vid}` | {st} | `{s1}` | `{s2}` | {s1n} | {s1m} | {s1r} | "
            "{s2n} | {s2m} | {s2r} | {em} | {f1} | {pf} | {n} |".format(
                vid=row.variable_config_id,
                st=row.status,
                s1=row.stage1_engine_id,
                s2=row.stage2_engine_id,
                s1n=_fmt(m.get("stage1_ndcg_at_5")),
                s1m=_fmt(m.get("stage1_map_at_5")),
                s1r=_fmt(m.get("stage1_mrr_at_5")),
                s2n=_fmt(m.get("stage2_ndcg_at_5")),
                s2m=_fmt(m.get("stage2_map_at_5")),
                s2r=_fmt(m.get("stage2_mrr_at_5")),
                em=_fmt(m.get("answer_normalized_em")),
                f1=_fmt(m.get("answer_token_f1")),
                pf=_fmt(m.get("parse_failure_rate")),
                n=m.get("n_examples") or 0,
            )
        )

    lines.extend(
        [
            "",
            "## Leaderboard (this sample)",
            "",
            f"- **Best Stage-1 ranking (nDCG@5)**: {_best_label(s1_ranked)}",
            f"- **Best Stage-2 ranking (nDCG@5)**: {_best_label(s2_ranked)}",
            f"- **Best answer quality (token-F1)**: {_best_label(ans_ranked) if matrix.synthesis_enabled else 'n/a (synthesis disabled)'}",
            "",
            "### Stage-1 ranking order",
            "",
        ]
    )
    for i, (eid, score) in enumerate(s1_ranked, 1):
        lines.append(f"{i}. `{eid}` — nDCG@5={_fmt(score)}")

    lines.extend(["", "### Stage-2 ranking order", ""])
    for i, (eid, score) in enumerate(s2_ranked, 1):
        lines.append(f"{i}. `{eid}` — nDCG@5={_fmt(score)}")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
        ]
    )

    if not completed and failed:
        lines.append(
            "All matrix rows **failed**. Check that System-1 engines are healthy "
            "(`./scripts/serve_engine.sh health <config_id>`), `SYSTEMONE_MOCK=0` "
            "(or pass `--allow-mock` only for debug), and that AnyJev L1 calibration "
            "has exactly 200 IDs if that engine was selected."
        )
    else:
        lines.append(
            f"{len(completed)} / {len(matrix.rows)} engine row(s) completed successfully."
        )
        if failed:
            lines.append("")
            lines.append("### Failures")
            lines.append("")
            for row in failed:
                lines.append(f"- `{row.variable_config_id}`: {row.error or 'unknown error'}")

        lines.append("")
        lines.append("### Reading the scores")
        lines.append("")
        if matrix.sample_size is not None and matrix.sample_size < 50:
            lines.append(
                f"- This run used a **small sample** (N={len(matrix.selected_example_ids)}). "
                "Treat rankings as an **integration / smoke signal**, not a publishable "
                "model comparison. Re-run with `--records 50` or omit `--records` for a fuller set."
            )
        else:
            lines.append(
                f"- Sample size N={len(matrix.selected_example_ids)} "
                f"(seed={matrix.sample_seed}). Re-run with the same seed to reproduce the example slice."
            )

        lines.append(
            "- Compare **pairs**, not isolated engines. Stage-1 nDCG judges the Choice "
            "model; Stage-2 nDCG judges the chunk scorer (and is bounded by Stage-1 recall)."
        )
        lines.append(
            "- `lux-clm` is the intended production pair (Lux Choice + CLM Action Cache). "
            "`lux-lux` tests long-context Score when chunks exceed CLM's 2,048-token window. "
            "`kai-clm` / `laya-clm` are latency/edge Stage-1 routers with a real Stage-2 scorer."
        )
        if matrix.partner_ids.get("binding") == "legacy-engines":
            lines.append(
                "- This run used **legacy `--engines` ablation** (one variable + fixed partner). "
                "Stage-2 numbers for Choice-only variables largely reflect "
                f"`{matrix.partner_ids.get('stage2_partner_id', 'clm-8b')}`."
            )
        if not matrix.synthesis_enabled:
            lines.append(
                "- **Synthesis was disabled** (`--skip-synthesis`). Answer EM/F1 are empty. "
                "Omit that flag (and set `GOOGLE_API_KEY`) for full pipeline scoring with Gemini."
            )
        else:
            lines.append(
                "- Synthesis used Gemini exclusively. Failures appear as synthesis-retriable "
                "in the ledger; extractive answers are never fabricated."
            )
        if matrix.systemone_mock:
            lines.append(
                "- **WARNING**: `SYSTEMONE_MOCK` was enabled. Results are **not** real-engine claims."
            )

        # Comparative narrative
        if len(completed) >= 2 and s1_ranked[0][1] is not None:
            top, top_s = s1_ranked[0]
            second = s1_ranked[1] if len(s1_ranked) > 1 else None
            lines.append("")
            lines.append("### Comparative takeaway")
            lines.append("")
            if second and second[1] is not None:
                delta = (top_s or 0) - (second[1] or 0)
                lines.append(
                    f"On Stage-1 nDCG@5, `{top}` leads `{second[0]}` by {_fmt(delta)}. "
                    "If the gap is small on a tiny sample, re-run with a larger `--records` "
                    "before drawing product conclusions."
                )
            else:
                lines.append(
                    f"`{top}` is the strongest Stage-1 configuration in this run "
                    f"(nDCG@5={_fmt(top_s)})."
                )

    lines.extend(
        [
            "",
            "## Selected example IDs",
            "",
            "```",
            ", ".join(matrix.selected_example_ids[:50])
            + (" ..." if len(matrix.selected_example_ids) > 50 else ""),
            "```",
            "",
            "## How to reproduce",
            "",
            "```bash",
            f"uv run python scripts/run_benchmark.py \\",
            f"  --run-id {matrix.matrix_run_id} \\",
            f"  --pairs {','.join(matrix.config_ids)} \\",
        ]
    )
    if matrix.sample_size is not None:
        lines.append(f"  --records {matrix.sample_size} \\")
    if matrix.sample_seed is not None:
        lines.append(f"  --seed {matrix.sample_seed} \\")
    if not matrix.synthesis_enabled:
        lines.append("  --skip-synthesis \\")
    lines.append(f"  --gemini-model {matrix.gemini_model}")
    lines.extend(
        [
            "```",
            "",
            "## Artifacts",
            "",
            f"- Interactive inspect (click pair → example: labels vs S1/S2/synthesis I/O): "
            f"`artifacts/benchmarks/{matrix.matrix_run_id}.inspect.html`",
            f"- Inspect JSON: `artifacts/benchmarks/{matrix.matrix_run_id}.inspect.json`",
            f"- Matrix JSON / CSV: `artifacts/benchmarks/{matrix.matrix_run_id}.json`, "
            f"`artifacts/benchmarks/{matrix.matrix_run_id}.csv`",
            f"- This report: `artifacts/benchmarks/{matrix.matrix_run_id}.md`",
            "",
            "---",
            "*Generated by `scripts/run_benchmark.py`*",
            "",
        ]
    )
    return "\n".join(lines)


def write_interpretation_report(matrix: MatrixRun, out: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_interpretation_markdown(matrix), encoding="utf-8")
    return out


def report_summary_dict(matrix: MatrixRun) -> dict[str, Any]:
    return {
        "matrix_run_id": matrix.matrix_run_id,
        "status": matrix.status,
        "n_rows": len(matrix.rows),
        "n_completed": sum(1 for r in matrix.rows if r.status == "completed"),
        "n_failed": sum(1 for r in matrix.rows if r.status == "failed"),
        "best_stage1_ndcg": _best_label(_rank_rows(matrix, "stage1_ndcg_at_5")),
        "best_stage2_ndcg": _best_label(_rank_rows(matrix, "stage2_ndcg_at_5")),
        "sample_size": matrix.sample_size,
        "sample_seed": matrix.sample_seed,
    }
