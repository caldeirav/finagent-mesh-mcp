"""Paper-facing analysis report with Block A/B tables and inspect links."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from finagent_mesh.matrix.models import MatrixRun


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


def _fmt(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.4f}"
    return str(v)


def _rows_for_block(matrix: MatrixRun, block: str) -> list[Any]:
    out = []
    for r in matrix.rows:
        blocks = r.blocks or (r.metrics.blocks if r.metrics else []) or []
        if block in blocks or (not blocks and block == "?"):
            out.append(r)
        # lux-lux may only list both blocks on row; also include by pair id convention
        elif r.variable_config_id == "lux-lux" and block in {"A", "B"}:
            out.append(r)
    # Deduplicate by pair id
    seen: set[str] = set()
    uniq = []
    for r in out:
        if r.variable_config_id in seen:
            continue
        seen.add(r.variable_config_id)
        uniq.append(r)
    return uniq


def _guardrail_findings(matrix: MatrixRun) -> list[str]:
    findings: list[str] = []
    block_a = [r for r in _rows_for_block(matrix, "A") if r.status == "completed"]
    block_b = [
        r
        for r in _rows_for_block(matrix, "B")
        if r.status == "completed" and r.variable_config_id != "one-shot-ar"
    ]
    if block_a:
        s2s = {r.stage2_engine_id for r in block_a}
        if len(s2s) == 1:
            findings.append(
                f"Block A holds Stage-2 fixed at `{next(iter(s2s))}`; "
                "do not attribute Stage-2 nDCG differences across Block A rows to different scorers."
            )
        else:
            findings.append(
                f"WARNING: Block A Stage-2 engines differ: {sorted(s2s)} — check catalog."
            )
        s1_scores = [(r.variable_config_id, r.metrics.stage1_ndcg_at_5) for r in block_a]
        best = max(s1_scores, key=lambda x: (x[1] is not None, x[1] or -1))
        findings.append(
            f"Strongest Block A Stage-1 nDCG@5 among completed rows: `{best[0]}` ({_fmt(best[1])})."
        )
    if block_b:
        s1s = {r.stage1_engine_id for r in block_b}
        if len(s1s) == 1:
            findings.append(
                f"Block B holds Stage-1 fixed at `{next(iter(s1s))}`; "
                "compare Stage-2 overall vs conditional-on-Top-1 metrics."
            )
        s2_scores = [(r.variable_config_id, r.metrics.stage2_ndcg_at_5) for r in block_b]
        best2 = max(s2_scores, key=lambda x: (x[1] is not None, x[1] or -1))
        findings.append(
            f"Strongest Block B Stage-2 nDCG@5 (overall): `{best2[0]}` ({_fmt(best2[1])})."
        )
    if any(r.variable_config_id == "one-shot-ar" for r in matrix.rows):
        findings.append(
            "`one-shot-ar` collapses Stage 1+2 (baseline_collapsed); not a production pair."
        )
    if not matrix.synthesis_enabled:
        findings.append("Answer EM/F1: not run (ranking-only; synthesis disabled).")
    return findings


def build_analysis_payload(
    matrix: MatrixRun,
    *,
    inspect_examples: dict[str, list[dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    """Build machine-readable analysis index."""
    index: list[dict[str, Any]] = []
    inspect_name = f"{matrix.matrix_run_id}.inspect.html"
    for row in matrix.rows:
        examples = (inspect_examples or {}).get(row.variable_config_id) or []
        if not examples:
            index.append(
                {
                    "pair_id": row.variable_config_id,
                    "example_id": None,
                    "status": "trace_missing" if row.status == "completed" else row.status,
                    "href": f"{inspect_name}#pair-{row.variable_config_id}",
                }
            )
            continue
        for ex in examples:
            eid = ex.get("example_id") or "unknown"
            st = ex.get("ledger_state") or "unknown"
            if ex.get("error") == "empty_top1_chunks" or (ex.get("stage2") or {}).get(
                "skipped_reason"
            ) == "empty_top1_chunks":
                st = "empty_top1"
            index.append(
                {
                    "pair_id": row.variable_config_id,
                    "example_id": eid,
                    "status": st,
                    "href": f"{inspect_name}#pair-{row.variable_config_id}-ex-{eid}",
                }
            )
    return {
        "matrix_run_id": matrix.matrix_run_id,
        "n_examples": len(matrix.selected_example_ids),
        "sample_seed": matrix.sample_seed,
        "dataset_path": matrix.dataset_path,
        "synthesis_enabled": matrix.synthesis_enabled,
        "skip_records": list(matrix.skip_records),
        "deferred": DEFERRED_ISSUES,
        "findings": _guardrail_findings(matrix),
        "artifact_index": index,
        "rows": [r.to_dict() for r in matrix.rows],
    }


def build_analysis_markdown(matrix: MatrixRun, payload: dict[str, Any]) -> str:
    lines: list[str] = [
        f"# Paper analysis — {matrix.matrix_run_id}",
        "",
        "## Run facts",
        "",
        f"- **N**: {len(matrix.selected_example_ids)}",
        f"- **Seed**: {matrix.sample_seed}",
        f"- **Dataset**: `{matrix.dataset_path}`",
        f"- **Synthesis**: {'on' if matrix.synthesis_enabled else 'not run (ranking-only)'}",
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
        "| Pair | S1 | S2 | S1 nDCG@5 | Top-1 recall | OFR | Parse fail | S1 p50 ms |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in _rows_for_block(matrix, "A"):
        m = r.metrics
        lines.append(
            f"| {r.variable_config_id} | {r.stage1_engine_id} | {r.stage2_engine_id} | "
            f"{_fmt(m.stage1_ndcg_at_5)} | {_fmt(m.stage1_top1_recall)} | "
            f"{_fmt(m.option_flip_rate)} | {_fmt(m.parse_failure_rate)} | "
            f"{_fmt(m.latency_stage1_p50_ms)} |"
        )
    lines.extend(
        [
            "",
            "## Block B — Stage-2 Score (Lux Choice fixed)",
            "",
            "| Pair | S1 | S2 | S2 nDCG@5 | S2 nDCG@5\\|Top-1 | Empty Top-1 | S2 p50 ms |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for r in _rows_for_block(matrix, "B"):
        m = r.metrics
        lines.append(
            f"| {r.variable_config_id} | {r.stage1_engine_id} | {r.stage2_engine_id} | "
            f"{_fmt(m.stage2_ndcg_at_5)} | {_fmt(m.stage2_ndcg_at_5_given_top1)} | "
            f"{_fmt(m.empty_top1_chunk_rate)} | {_fmt(m.latency_stage2_p50_ms)} |"
        )
    lines.extend(
        [
            "",
            "## Routing vs scoring",
            "",
            "Wrong Top-1 filing type caps Stage-2 candidates (`empty_top1_chunks` / gold outside filter). "
            "Prefer **S2 nDCG@5|Top-1** when judging scorers; use overall S2 when judging the full pipeline.",
            "",
            "## Latency / resources",
            "",
            "| Pair | S1 p50/p95 | S2 p50/p95 | GPU high-water MB |",
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
    lines.extend(["", "## Findings", ""])
    for f in payload.get("findings") or []:
        lines.append(f"- {f}")
    lines.extend(
        [
            "",
            "## Limitations / threats to validity",
            "",
            "- Sample N may be below full FinAgentBench; seed and N are above.",
            "- CLM Stage-2 is zero-shot Action Cache (2k context) unless shortlist optional row ran.",
            "- E5 is general-domain, not finance-tuned.",
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
            f"- Interactive inspect: `{matrix.matrix_run_id}.inspect.html`",
            f"- Analysis JSON: `{matrix.matrix_run_id}.analysis.json`",
            "",
            "| Pair | Example | Status | Link |",
            "|---|---|---|---|",
        ]
    )
    for item in payload.get("artifact_index") or []:
        lines.append(
            f"| {item.get('pair_id')} | {item.get('example_id') or '—'} | "
            f"{item.get('status')} | [{item.get('href')}]({item.get('href')}) |"
        )
    lines.append("")
    return "\n".join(lines)


def write_analysis_reports(
    matrix: MatrixRun,
    *,
    out_md: Path,
    out_json: Path,
    inspect_payload: dict[str, Any] | None = None,
) -> tuple[Path, Path]:
    by_pair: dict[str, list[dict[str, Any]]] = {}
    if inspect_payload:
        for p in inspect_payload.get("pairs") or []:
            by_pair[str(p.get("pair_id"))] = list(p.get("examples") or [])
    payload = build_analysis_payload(matrix, inspect_examples=by_pair)
    md = build_analysis_markdown(matrix, payload)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md, encoding="utf-8")
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_md, out_json
