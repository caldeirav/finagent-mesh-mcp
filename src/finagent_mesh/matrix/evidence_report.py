"""P0 evidence pack: routing yield, strata, win/loss, bootstrap, multi-seed."""

from __future__ import annotations

from typing import Any

from finagent_mesh.matrix.metrics import (
    contributions_from_inspect_examples,
    pipeline_means_from_contributions,
    routing_classes_from_contributions,
)
from finagent_mesh.matrix.models import MatrixRun
from finagent_mesh.matrix.strata import build_strata, win_loss_vs_baseline
from finagent_mesh.matrix.uncertainty import (
    bootstrap_ci,
    bootstrap_delta_ci,
    metric_series,
    multi_seed_rollup,
)


CORE_PAIRS = ("lux-lux", "anyjev-l0-lux", "lux-e5", "lux-bm25")
BLOCK_B_SCORERS = ("lux-lux", "lux-bm25", "lux-e5", "lux-clm")


def build_p0_evidence(
    matrix: MatrixRun,
    *,
    inspect_examples: dict[str, list[dict[str, Any]]] | None = None,
    multi_seed_matrices: list[MatrixRun] | None = None,
) -> dict[str, Any]:
    by_pair_contrib: dict[str, list[dict[str, Any]]] = {}
    pipeline_yield: list[dict[str, Any]] = []
    routing_classes: list[dict[str, Any]] = []
    stage2_series: dict[str, Any] = {}

    for row in matrix.rows:
        pid = row.variable_config_id
        examples = (inspect_examples or {}).get(pid) or []
        contribs = contributions_from_inspect_examples(examples) if examples else []
        by_pair_contrib[pid] = contribs
        if contribs:
            pipe = pipeline_means_from_contributions(contribs)
            classes = routing_classes_from_contributions(contribs)
        else:
            # Fall back to row aggregates when inspect missing
            n = int(row.metrics.n_examples or 0)
            n_empty = int(row.metrics.n_empty_top1 or 0)
            n_scored = max(0, n - n_empty) if n else 0
            pipe = {
                "pipeline_yield": (n_scored / n) if n else 0.0,
                "n_scored": n_scored,
                "stage2_ndcg_at_5_pipeline": None,
                "stage2_mrr_at_5_pipeline": None,
            }
            classes = {
                "n_examples": n,
                "counts": {},
                "rates": {},
                "n_scored": n_scored,
                "pipeline_yield": pipe["pipeline_yield"],
            }
        pipeline_yield.append(
            {
                "pair_id": pid,
                "n_examples": classes.get("n_examples") or row.metrics.n_examples,
                "n_scored": pipe["n_scored"],
                "pipeline_yield": pipe["pipeline_yield"],
                "stage1_top1_recall": row.metrics.stage1_top1_recall,
                "empty_top1_chunk_rate": row.metrics.empty_top1_chunk_rate,
            }
        )
        routing_classes.append({"pair_id": pid, **classes})
        stage2_series[pid] = {
            "label_scored": "scored_only",
            "label_pipeline": "pipeline_averaged",
            "scored_mean": {
                "stage2_ndcg_at_5": row.metrics.stage2_ndcg_at_5,
                "stage2_mrr_at_5": row.metrics.stage2_mrr_at_5,
                "stage2_ndcg_at_5_given_top1": row.metrics.stage2_ndcg_at_5_given_top1,
                "stage2_mrr_at_5_given_top1": row.metrics.stage2_mrr_at_5_given_top1,
            },
            "pipeline_mean": {
                "stage2_ndcg_at_5": pipe["stage2_ndcg_at_5_pipeline"],
                "stage2_mrr_at_5": pipe["stage2_mrr_at_5_pipeline"],
            },
        }

    inspect_name = f"{matrix.matrix_run_id}.inspect.html"
    b_pairs = [p for p in BLOCK_B_SCORERS if p in by_pair_contrib]
    strata = build_strata(by_pair_contrib, pair_ids=b_pairs) if b_pairs else []

    win_loss: list[dict[str, Any]] = []
    lux_c = by_pair_contrib.get("lux-lux") or []
    for chal in ("lux-e5", "lux-bm25", "lux-clm"):
        if chal not in by_pair_contrib:
            continue
        win_loss.append(
            win_loss_vs_baseline(
                lux_c,
                by_pair_contrib[chal],
                baseline_pair_id="lux-lux",
                challenger_pair_id=chal,
                inspect_name=inspect_name,
            )
        )

    seed = int(matrix.sample_seed or 42)
    bootstrap: list[dict[str, Any]] = []
    for pid, contribs in by_pair_contrib.items():
        if not contribs:
            continue
        for metric, scored_only in (
            ("stage1_ndcg_at_5", False),
            ("stage2_ndcg_at_5", True),
            ("stage2_mrr_at_5", True),
        ):
            series = metric_series(contribs, metric, scored_only=scored_only)
            # For S1 use all examples with values
            if metric.startswith("stage1"):
                series = [c.get(metric) for c in contribs]
            ci = bootstrap_ci(series, seed=seed)
            bootstrap.append(
                {
                    "pair_id": pid,
                    "metric": metric + ("_scored" if scored_only and metric.startswith("stage2") else ""),
                    **ci,
                }
            )
        # Δ vs lux
        if pid != "lux-lux" and lux_c:
            for metric in ("stage1_ndcg_at_5", "stage2_ndcg_at_5"):
                a = [c.get(metric) for c in contribs]
                b = [c.get(metric) for c in lux_c]
                if metric.startswith("stage2"):
                    a = metric_series(contribs, metric, scored_only=True)
                    b = metric_series(lux_c, metric, scored_only=True)
                dci = bootstrap_delta_ci(a, b, seed=seed)
                bootstrap.append(
                    {
                        "pair_id": f"delta:{pid}-vs-lux-lux",
                        "metric": metric,
                        **dci,
                    }
                )

    multi_seed: list[dict[str, Any]] = []
    if multi_seed_matrices:
        # Group by seed → matrix
        by_seed: dict[int, MatrixRun] = {}
        for m in multi_seed_matrices:
            if m.sample_seed is not None:
                by_seed[int(m.sample_seed)] = m
        by_seed[int(matrix.sample_seed or 42)] = matrix
        for pid in CORE_PAIRS:
            for metric_attr in ("stage1_ndcg_at_5", "stage2_ndcg_at_5"):
                per: dict[int, float | None] = {}
                for s, mrun in by_seed.items():
                    row = next(
                        (r for r in mrun.rows if r.variable_config_id == pid),
                        None,
                    )
                    per[s] = getattr(row.metrics, metric_attr) if row else None
                roll = multi_seed_rollup(per)
                multi_seed.append({"pair_id": pid, "metric": metric_attr, **roll})

    # Synthesis reuse summary from row answer metrics
    synth_pairs = []
    for row in matrix.rows:
        if row.metrics.n_synthesis_attempted or row.metrics.answer_normalized_em is not None:
            synth_pairs.append(
                {
                    "pair_id": row.variable_config_id,
                    "answer_normalized_em": row.metrics.answer_normalized_em,
                    "answer_token_f1": row.metrics.answer_token_f1,
                    "n_synthesis_attempted": row.metrics.n_synthesis_attempted,
                    "n_synthesis_failed": row.metrics.n_synthesis_failed,
                }
            )
    synthesis_reuse = None
    if synth_pairs and matrix.synthesis_enabled:
        synthesis_reuse = {
            "run_id": matrix.matrix_run_id,
            "rankings_reused": True,
            "pairs": synth_pairs,
        }

    return {
        "pipeline_yield": pipeline_yield,
        "routing_classes": routing_classes,
        "stage2_series": stage2_series,
        "strata": strata,
        "win_loss": win_loss,
        "uncertainty": {"bootstrap": bootstrap, "multi_seed": multi_seed},
        "synthesis_reuse": synthesis_reuse,
        "_by_pair_contrib": by_pair_contrib,
    }


def render_p0_markdown_sections(payload: dict[str, Any]) -> list[str]:
    """Markdown fragments for P0 sections (inserted after Block B / routing)."""
    lines: list[str] = []

    lines.extend(["", "## Routing accounting", ""])
    lines.append(
        "Mutually exclusive classes reconcile Top-1 recall vs empty-Top-1. "
        "**Pipeline yield** = fraction of examples with a Stage-2 ranking list. "
        "Primary Stage-2 nDCG/MRR are **scored-only** means; "
        "**pipeline-averaged** treats empty/unscored as 0."
    )
    lines.append("")
    lines.append(
        "| Pair | N | Top-1 recall | Empty rate | Yield | "
        "correct_scored | correct_empty | wrong_scored | wrong_empty | missing/other |"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    yield_by = {r["pair_id"]: r for r in payload.get("pipeline_yield") or []}
    for rc in payload.get("routing_classes") or []:
        pid = rc["pair_id"]
        y = yield_by.get(pid) or {}
        c = rc.get("counts") or {}
        other = int(c.get("missing_top1") or 0) + int(c.get("other") or 0)
        lines.append(
            f"| {pid} | {rc.get('n_examples')} | "
            f"{_fmt(y.get('stage1_top1_recall'))} | {_fmt(y.get('empty_top1_chunk_rate'))} | "
            f"{_fmt(y.get('pipeline_yield'))} | "
            f"{c.get('correct_top1_scored', '—')} | {c.get('correct_top1_empty', '—')} | "
            f"{c.get('wrong_top1_scored', '—')} | {c.get('wrong_top1_empty', '—')} | {other} |"
        )

    lines.extend(["", "## Stage-2 metric series (scored vs pipeline)", ""])
    lines.append(
        "| Pair | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG\\|Top-1 | "
        "S2 nDCG (pipeline) | S2 MRR (pipeline) |"
    )
    lines.append("|---|---|---|---|---|---|")
    for pid, series in (payload.get("stage2_series") or {}).items():
        sm = series.get("scored_mean") or {}
        pm = series.get("pipeline_mean") or {}
        lines.append(
            f"| {pid} | {_fmt(sm.get('stage2_ndcg_at_5'))} | {_fmt(sm.get('stage2_mrr_at_5'))} | "
            f"{_fmt(sm.get('stage2_ndcg_at_5_given_top1'))} | "
            f"{_fmt(pm.get('stage2_ndcg_at_5'))} | {_fmt(pm.get('stage2_mrr_at_5'))} |"
        )
    lines.append("")
    lines.append(
        "_Footnote: **scored** = mean over examples with a Stage-2 ranking list; "
        "**pipeline** = mean over all N with empty/unscored as 0._"
    )

    strata = payload.get("strata") or []
    if strata:
        lines.extend(["", "## Strata (Block B)", ""])
        for axis in ("gold_type", "cand_size", "length"):
            rows = [s for s in strata if s.get("axis") == axis]
            if not rows:
                continue
            lines.append(f"### By {axis}")
            lines.append("")
            lines.append("| Bucket | Pair | N | S2 nDCG@5 |")
            lines.append("|---|---|---|---|")
            for s in rows:
                lines.append(
                    f"| {s.get('bucket')} | {s.get('pair_id')} | {s.get('n')} | "
                    f"{_fmt(s.get('stage2_ndcg_at_5'))} |"
                )
            lines.append("")

    wl = payload.get("win_loss") or []
    if wl:
        lines.extend(["", "## Win/tie/loss vs Lux Score", ""])
        lines.append("Decided by per-example Stage-2 **nDCG@5**; `|Δ| < 0.01` counts as tie.")
        lines.append("")
        lines.append("| Challenger | N compared | Wins | Ties | Losses |")
        lines.append("|---|---|---|---|---|")
        for w in wl:
            lines.append(
                f"| {w.get('challenger_pair_id')} | {w.get('n_compared')} | "
                f"{w.get('wins')} | {w.get('ties')} | {w.get('losses')} |"
            )
        lines.append("")
        for w in wl:
            lines.append(f"### Samples — `{w.get('challenger_pair_id')}`")
            lines.append("")
            for label, key in (("Wins", "sample_wins"), ("Losses", "sample_losses")):
                samples = w.get(key) or []
                if not samples:
                    continue
                lines.append(f"**{label}:**")
                for s in samples:
                    lines.append(
                        f"- `{s.get('example_id')}` Δ={_fmt(s.get('delta'))} "
                        f"([inspect]({s.get('href')}))"
                    )
                lines.append("")

    unc = payload.get("uncertainty") or {}
    boot = unc.get("bootstrap") or []
    if boot:
        lines.extend(["", "## Uncertainty (bootstrap 95% CI)", ""])
        lines.append("| Id | Metric | Point | CI low | CI high | N |")
        lines.append("|---|---|---|---|---|---|")
        # Prefer delta rows + lux / e5 / anyjev headlines
        priority = [
            b
            for b in boot
            if str(b.get("pair_id", "")).startswith("delta:")
            or b.get("pair_id") in {"lux-lux", "lux-e5", "anyjev-l0-lux", "lux-bm25"}
        ]
        for b in priority[:40]:
            lines.append(
                f"| {b.get('pair_id')} | {b.get('metric')} | {_fmt(b.get('point'))} | "
                f"{_fmt(b.get('ci_low'))} | {_fmt(b.get('ci_high'))} | {b.get('n')} |"
            )

    ms = unc.get("multi_seed") or []
    if ms:
        lines.extend(["", "## Multi-seed summary", ""])
        lines.append("Independent N draws per seed; across-seed = mean of seed means + min–max.")
        lines.append("")
        lines.append("| Pair | Metric | Per-seed | Mean | Min | Max |")
        lines.append("|---|---|---|---|---|---|")
        for r in ms:
            lines.append(
                f"| {r.get('pair_id')} | {r.get('metric')} | `{r.get('per_seed')}` | "
                f"{_fmt(r.get('mean_of_means'))} | {_fmt(r.get('min'))} | {_fmt(r.get('max'))} |"
            )
    elif boot:
        lines.extend(
            [
                "",
                "## Multi-seed summary",
                "",
                "_Pending: run core-subset seeds `{42,7,123}` "
                "(`lux-lux`, `anyjev-l0-lux`, `lux-e5`, `lux-bm25`) and rebuild analysis._",
                "",
            ]
        )

    synth = payload.get("synthesis_reuse")
    lines.extend(["", "## Answer metrics (synthesis reuse)", ""])
    if synth:
        lines.append(
            "Rankings were **reused** from the published matrix (no Choice/Score re-inference)."
        )
        lines.append("")
        lines.append("| Pair | EM | Token F1 | Attempted | Failed |")
        lines.append("|---|---|---|---|---|")
        for p in synth.get("pairs") or []:
            lines.append(
                f"| {p.get('pair_id')} | {_fmt(p.get('answer_normalized_em'))} | "
                f"{_fmt(p.get('answer_token_f1'))} | {p.get('n_synthesis_attempted')} | "
                f"{p.get('n_synthesis_failed')} |"
            )
    else:
        lines.append("Answer EM/F1 **not run** (ranking-only or synthesis reuse not attached).")

    return lines


def _fmt(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.4f}"
    return str(v)
