"""Matrix / pipeline binding domain models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal

Status = Literal["pending", "running", "completed", "failed"]


@dataclass
class PipelineBinding:
    run_id: str
    stage1_config_id: str
    stage2_config_id: str
    variable_config_id: str | None = None
    gemini_model: str = "gemini-2.5-flash"
    synthesis_enabled: bool = True
    systemone_mock: bool = False


@dataclass
class EngineMetricsRecord:
    n_examples: int = 0
    stage1_ndcg_at_5: float | None = None
    stage1_map_at_5: float | None = None
    stage1_mrr_at_5: float | None = None
    stage2_ndcg_at_5: float | None = None
    stage2_map_at_5: float | None = None
    stage2_mrr_at_5: float | None = None
    latency_ms_p50: float | None = None
    latency_ms_p95: float | None = None
    parse_failure_rate: float | None = None
    answer_normalized_em: float | None = None
    answer_token_f1: float | None = None
    n_synthesis_attempted: int = 0
    n_synthesis_failed: int = 0
    stage1_unsupported_reason: str | None = None
    stage2_unsupported_reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "n_examples": self.n_examples,
            "stage1_ndcg_at_5": self.stage1_ndcg_at_5,
            "stage1_map_at_5": self.stage1_map_at_5,
            "stage1_mrr_at_5": self.stage1_mrr_at_5,
            "stage2_ndcg_at_5": self.stage2_ndcg_at_5,
            "stage2_map_at_5": self.stage2_map_at_5,
            "stage2_mrr_at_5": self.stage2_mrr_at_5,
            "latency_ms_p50": self.latency_ms_p50,
            "latency_ms_p95": self.latency_ms_p95,
            "parse_failure_rate": self.parse_failure_rate,
            "answer_normalized_em": self.answer_normalized_em,
            "answer_token_f1": self.answer_token_f1,
            "n_synthesis_attempted": self.n_synthesis_attempted,
            "n_synthesis_failed": self.n_synthesis_failed,
            "stage1_unsupported_reason": self.stage1_unsupported_reason,
            "stage2_unsupported_reason": self.stage2_unsupported_reason,
        }


@dataclass
class MatrixRowResult:
    variable_config_id: str
    eval_run_id: str
    stage1_engine_id: str
    stage2_engine_id: str
    status: Status = "pending"
    error: str | None = None
    metrics: EngineMetricsRecord = field(default_factory=EngineMetricsRecord)

    def to_dict(self) -> dict[str, Any]:
        return {
            "variable_config_id": self.variable_config_id,
            "eval_run_id": self.eval_run_id,
            "stage1_engine_id": self.stage1_engine_id,
            "stage2_engine_id": self.stage2_engine_id,
            "status": self.status,
            "error": self.error,
            "metrics": self.metrics.to_dict(),
        }


@dataclass
class MatrixRun:
    matrix_run_id: str
    dataset_path: str
    sample_size: int | None = None
    sample_seed: int | None = None
    selected_example_ids: list[str] = field(default_factory=list)
    config_ids: list[str] = field(default_factory=list)
    status: Status = "pending"
    partner_ids: dict[str, str] = field(default_factory=dict)
    gemini_model: str = "gemini-2.5-flash"
    systemone_mock: bool = False
    synthesis_enabled: bool = True
    rows: list[MatrixRowResult] = field(default_factory=list)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "matrix_run_id": self.matrix_run_id,
            "created_at": self.created_at,
            "dataset_path": self.dataset_path,
            "sample_seed": self.sample_seed,
            "sample_size": self.sample_size,
            "selected_example_ids": list(self.selected_example_ids),
            "config_ids": list(self.config_ids),
            "status": self.status,
            "partners": dict(self.partner_ids),
            "gemini_model": self.gemini_model,
            "systemone_mock": self.systemone_mock,
            "synthesis_enabled": self.synthesis_enabled,
            "rows": [r.to_dict() for r in self.rows],
        }
