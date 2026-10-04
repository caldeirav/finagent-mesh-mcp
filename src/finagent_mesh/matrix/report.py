"""Comparative matrix report builder (JSON/CSV)."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from finagent_mesh.matrix.models import MatrixRun


def build_report(matrix: MatrixRun) -> dict[str, Any]:
    return {
        "matrix_run_id": matrix.matrix_run_id,
        "created_at": matrix.created_at,
        "dataset_path": matrix.dataset_path,
        "sample_seed": matrix.sample_seed,
        "sample_size": matrix.sample_size,
        "selected_example_ids": list(matrix.selected_example_ids),
        "partners": dict(matrix.partner_ids),
        "gemini_model": matrix.gemini_model,
        "systemone_mock": matrix.systemone_mock,
        "synthesis_enabled": matrix.synthesis_enabled,
        "rows": [r.to_dict() for r in matrix.rows],
    }


def write_report(matrix: MatrixRun, out: Path, *, fmt: str = "json") -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    report = build_report(matrix)
    if fmt == "json":
        out.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return out
    if fmt == "csv":
        fieldnames = [
            "variable_config_id",
            "pair_id",
            "eval_run_id",
            "stage1_engine_id",
            "stage2_engine_id",
            "status",
            "stage1_ndcg_at_5",
            "stage1_map_at_5",
            "stage1_mrr_at_5",
            "stage2_ndcg_at_5",
            "stage2_map_at_5",
            "stage2_mrr_at_5",
            "latency_ms_p50",
            "latency_ms_p95",
            "parse_failure_rate",
            "answer_normalized_em",
            "answer_token_f1",
            "n_examples",
            "n_synthesis_attempted",
            "n_synthesis_failed",
            "stage1_unsupported_reason",
            "stage2_unsupported_reason",
            "error",
        ]
        with out.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames)
            writer.writeheader()
            for row in report["rows"]:
                m = row.get("metrics") or {}
                out_row = {k: m.get(k) for k in fieldnames}
                out_row.update(
                    {
                        "variable_config_id": row["variable_config_id"],
                        "pair_id": row["variable_config_id"],
                        "eval_run_id": row["eval_run_id"],
                        "stage1_engine_id": row["stage1_engine_id"],
                        "stage2_engine_id": row["stage2_engine_id"],
                        "status": row["status"],
                        "error": row.get("error"),
                    }
                )
                writer.writerow(out_row)
        return out
    raise ValueError(f"Unsupported format {fmt}")
