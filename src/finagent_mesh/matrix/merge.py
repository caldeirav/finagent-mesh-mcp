"""Merge matrix runs (e.g. primary + retry) into one reportable MatrixRun."""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone

from finagent_mesh.matrix.models import MatrixRowResult, MatrixRun


def merge_matrix_runs(
    *runs: MatrixRun,
    matrix_run_id: str,
    prefer_measured: bool = True,
) -> MatrixRun:
    """Overlay later runs onto earlier ones by ``variable_config_id``.

    When ``prefer_measured`` is true, a later row replaces an earlier one only if
    it has usable Stage-1 or Stage-2 nDCG (avoids clobbering good rows with
    null-metric placeholders).
    """
    if not runs:
        raise ValueError("merge_matrix_runs requires at least one MatrixRun")
    base = runs[0]
    by_id: dict[str, MatrixRowResult] = {
        r.variable_config_id: deepcopy(r) for r in base.rows
    }
    config_ids = list(base.config_ids)
    skip = list(base.skip_records or [])

    def _measured(row: MatrixRowResult) -> bool:
        m = row.metrics
        return (
            m.stage1_ndcg_at_5 is not None
            or m.stage2_ndcg_at_5 is not None
            or m.stage1_top1_recall is not None
        )

    for run in runs[1:]:
        for row in run.rows:
            prev = by_id.get(row.variable_config_id)
            if prev is None:
                by_id[row.variable_config_id] = deepcopy(row)
                if row.variable_config_id not in config_ids:
                    config_ids.append(row.variable_config_id)
                continue
            if prefer_measured and _measured(prev) and not _measured(row):
                continue
            if prefer_measured and not _measured(prev) and _measured(row):
                by_id[row.variable_config_id] = deepcopy(row)
                continue
            # Default: later run wins (retry supersedes).
            by_id[row.variable_config_id] = deepcopy(row)
        for s in run.skip_records or []:
            pid = s.get("pair_id")
            if pid and not any(x.get("pair_id") == pid for x in skip):
                skip.append(s)

    # Preserve base pair order, then append any new ids.
    order = [r.variable_config_id for r in base.rows]
    for cid in by_id:
        if cid not in order:
            order.append(cid)
    rows = [by_id[cid] for cid in order if cid in by_id]

    return MatrixRun(
        matrix_run_id=matrix_run_id,
        dataset_path=base.dataset_path,
        sample_size=base.sample_size,
        sample_seed=base.sample_seed,
        selected_example_ids=list(base.selected_example_ids),
        config_ids=config_ids,
        status="completed"
        if rows and all(r.status == "completed" for r in rows)
        else base.status,
        partner_ids=dict(base.partner_ids),
        gemini_model=base.gemini_model,
        systemone_mock=base.systemone_mock,
        synthesis_enabled=base.synthesis_enabled,
        rows=rows,
        skip_records=skip,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
