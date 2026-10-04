"""Domain types and LangGraph run state."""

from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

from finagent_mesh.agent.types import DOC_TYPES


class BenchmarkExample(BaseModel):
    example_id: str
    firm_id: str
    query_text: str
    query_category: str = ""
    # Strings (binary relevance) or {id|doc_type, relevance} graded labels
    stage1_labels: list[Any] = Field(default_factory=list)
    stage2_labels: list[dict[str, Any]] = Field(default_factory=list)
    answer_label: Optional[str] = None
    chunks: list["PassageChunk"] = Field(default_factory=list)


class DocumentTypeCandidate(BaseModel):
    doc_type: str
    score: float
    rank: int

    def model_post_init(self, __context: Any) -> None:
        if self.doc_type not in DOC_TYPES:
            raise ValueError(f"doc_type must be one of {DOC_TYPES}")


class PassageChunk(BaseModel):
    chunk_id: str
    doc_type: str
    text: str
    is_table: bool = False
    score: float = 0.0
    rank: int = 0


class StageRankingResult(BaseModel):
    stage: Literal["stage1", "stage2"]
    ordered_ids: list[str]
    scores: list[float]
    ndcg_at_5: float | None = None
    map_at_5: float | None = None
    mrr_at_5: float | None = None
    decision_distribution: dict[str, float] = Field(default_factory=dict)
    skipped_reason: str | None = None


class AnswerScore(BaseModel):
    prediction: str
    label: str | None
    normalized_em: float | None = None
    token_f1: float | None = None
    status: Literal["scored", "skipped_no_label"] = "skipped_no_label"


class AgentState(BaseModel):
    """Mutable per-example LangGraph state."""

    example: BenchmarkExample
    skip_synthesis: bool = False
    synthesis_k: int = 5
    top1_doc_type: str | None = None
    stage1: StageRankingResult | None = None
    stage2: StageRankingResult | None = None
    stage2_chunks: list[PassageChunk] = Field(default_factory=list)
    synthesized_answer: str | None = None
    answer_score: AnswerScore | None = None
    error: str | None = None
    tool_records: list[dict[str, Any]] = Field(default_factory=list)

    model_config = {"arbitrary_types_allowed": True}
