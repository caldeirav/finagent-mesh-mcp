"""Typed records for Unsloth export / train / frozen Stage-1 (data-model.md)."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

TrainStatus = Literal["pending", "running", "completed", "failed"]

SCORE_CRITERIA = ("not relevant", "partially relevant", "highly relevant")
DEFAULT_BASE_MODEL = "unsloth/Qwen3.8-27B-unsloth-bnb-4bit"
DEFAULT_TEST_SOURCE = "paper-n200-full"


@dataclass
class SplitManifest:
    manifest_id: str
    created_at: str
    test_source: str
    test_ids: list[str]
    train_ids: list[str]
    val_ids: list[str]
    seed: int
    content_hash: str
    n_train: int = 0
    n_val: int = 0
    n_test: int = 0

    def __post_init__(self) -> None:
        self.n_train = len(self.train_ids)
        self.n_val = len(self.val_ids)
        self.n_test = len(self.test_ids)
        test, train, val = set(self.test_ids), set(self.train_ids), set(self.val_ids)
        if test & train:
            raise ValueError("SplitManifest leakage: test ∩ train non-empty")
        if test & val:
            raise ValueError("SplitManifest leakage: test ∩ val non-empty")
        if train & val:
            raise ValueError("SplitManifest leakage: train ∩ val non-empty")
        if self.test_source == DEFAULT_TEST_SOURCE and self.n_test != 200:
            # Soft warning only when source claims paper; builder enforces hard check
            pass

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ScoreTrainingRow:
    example_id: str
    query: str
    candidates: list[dict[str, Any]]
    score_criteria: list[str] = field(default_factory=lambda: list(SCORE_CRITERIA))
    labels: dict[str, int] = field(default_factory=dict)
    gold_doc_types: list[str] = field(default_factory=list)

    def validate(self) -> None:
        gold = set(self.gold_doc_types)
        for c in self.candidates:
            dt = str(c.get("doc_type") or "")
            if gold and dt not in gold:
                raise ValueError(
                    f"Candidate {c.get('id')} doc_type={dt!r} not in gold_doc_types={gold}"
                )

    def to_export_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "example_id": self.example_id,
            "query": self.query,
            "gold_doc_types": list(self.gold_doc_types),
            "candidates": list(self.candidates),
            "decision": {
                "type": "score",
                "instructions": "Rank passages for answering the query.",
                "criteria": list(self.score_criteria),
            },
            "labels": dict(self.labels),
        }


@dataclass
class UnslothTrainRun:
    train_run_id: str
    base_model_id: str
    checkpoint_dir: str
    split_manifest_id: str
    lora: dict[str, Any]
    seed: int
    status: TrainStatus = "pending"
    mlflow_run_id: str | None = None
    holdout_metrics: dict[str, Any] = field(default_factory=dict)
    split_content_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class FrozenStage1Record:
    example_id: str
    top1_doc_type: str | None
    empty_top1: bool
    source: str = "paper-n200-full:lux-lux"
    stage1_ordered_ids: list[str] = field(default_factory=list)
    stage1_scores: list[float] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
