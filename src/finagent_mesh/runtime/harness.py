"""End-to-end evaluation harness with ledger resume and fail-closed local ranking."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from finagent_mesh.agent.graph import build_graph, run_example
from finagent_mesh.agent.state import AgentState
from finagent_mesh.clients.gemini import GeminiClient
from finagent_mesh.clients.open_decision import OpenDecisionClient, OpenDecisionError
from finagent_mesh.config import Settings, get_settings
from finagent_mesh.dataset.finagentbench import load_examples
from finagent_mesh.ledger.sqlite_ledger import TERMINAL_NO_RERANK, SqliteLedger
from finagent_mesh.runtime.health import require_systemone_healthy
from finagent_mesh.runtime import tracing
from finagent_mesh.scoring.run_aggregator import RunAggregator


class Harness:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.decision = OpenDecisionClient(
            self.settings.systemone_stage1_url,
            self.settings.systemone_stage2_url,
            mock=self.settings.systemone_mock,
        )
        self.gemini = GeminiClient(self.settings.google_api_key, self.settings.gemini_model)
        self.graph = build_graph(self.decision, self.gemini)

    def run(
        self,
        run_id: str,
        *,
        limit: int | None = None,
        dataset_path: Path | None = None,
        skip_synthesis: bool = False,
        synthesis_k: int | None = None,
    ) -> dict[str, Any]:
        settings = self.settings
        path = dataset_path or settings.finagentbench_path
        if path is None:
            raise RuntimeError("FINAGENTBENCH_PATH is required")
        require_systemone_healthy(
            settings.systemone_stage1_url,
            settings.systemone_stage2_url,
            mock=settings.systemone_mock,
        )
        examples = load_examples(Path(path), limit=limit)
        k = synthesis_k if synthesis_k is not None else settings.synthesis_k
        ledger = SqliteLedger(settings.eval_ledger_path)
        owner = SqliteLedger.default_owner()
        config = {
            "limit": limit,
            "skip_synthesis": skip_synthesis,
            "synthesis_k": k,
            "dataset_path": str(path),
        }
        try:
            ledger.ensure_run(run_id, config)
            ledger.acquire_lease(run_id, owner)
            ledger.ensure_examples(run_id, [e.example_id for e in examples])
            tracing.setup_mlflow(settings.mlflow_tracking_uri)
            agg = RunAggregator(run_id)
            import mlflow

            with mlflow.start_run(run_name=run_id):
                for example in examples:
                    entry = ledger.get_entry(run_id, example.example_id)
                    assert entry is not None
                    if entry.state == "completed":
                        if entry.ranking_payload_json:
                            agg.add_payload(
                                example.example_id,
                                entry.ranking_payload_json,
                                entry.synthesis_payload_json,
                            )
                        continue
                    if entry.state == "synthesis_retriable" and entry.ranking_payload_json:
                        self._resume_synthesis(
                            ledger, run_id, example.example_id, entry, skip_synthesis, k, agg
                        )
                        continue
                    if entry.state in TERMINAL_NO_RERANK and entry.state == "ranking_complete":
                        if skip_synthesis:
                            ledger.transition(run_id, example.example_id, "completed")
                            agg.add_payload(example.example_id, entry.ranking_payload_json, None)
                            continue
                        self._resume_synthesis(
                            ledger, run_id, example.example_id, entry, skip_synthesis, k, agg
                        )
                        continue
                    self._process_full(
                        ledger, run_id, example, skip_synthesis=skip_synthesis, k=k, agg=agg
                    )
            return {"status": ledger.status_counts(run_id), "lease": ledger.lease_info(run_id)}
        finally:
            ledger.release_lease(run_id, owner)
            ledger.close()

    def _process_full(
        self,
        ledger: SqliteLedger,
        run_id: str,
        example,
        *,
        skip_synthesis: bool,
        k: int,
        agg: RunAggregator,
    ) -> None:
        settings = self.settings
        ledger.transition(run_id, example.example_id, "in_progress")
        attempts = 0
        last_err: str | None = None
        state: AgentState | None = None
        while attempts < settings.harness_max_attempts:
            attempts += 1
            try:
                with tracing.example_run(run_id, example.example_id):
                    state = run_example(
                        self.graph,
                        example,
                        skip_synthesis=True,  # commit ranking first
                        synthesis_k=k,
                    )
                    tracing.log_agent_state(state)
                if state.error == "empty_top1_chunks":
                    ledger.transition(
                        run_id,
                        example.example_id,
                        "failed_retriable",
                        last_error=state.error,
                        inc_stage2=True,
                    )
                    return
                ranking_payload = {
                    "stage1": state.stage1.model_dump() if state.stage1 else None,
                    "stage2": state.stage2.model_dump() if state.stage2 else None,
                    "top1_doc_type": state.top1_doc_type,
                    "stage2_chunks": [c.model_dump() for c in state.stage2_chunks],
                }
                ledger.transition(
                    run_id,
                    example.example_id,
                    "ranking_complete",
                    ranking_payload=ranking_payload,
                    inc_stage1=True,
                    inc_stage2=True,
                )
                break
            except OpenDecisionError as exc:
                last_err = str(exc)
                if attempts >= settings.harness_max_attempts:
                    ledger.transition(
                        run_id,
                        example.example_id,
                        "failed_retriable",
                        last_error=last_err,
                        inc_stage1=True,
                    )
                    return
            except Exception as exc:  # noqa: BLE001
                last_err = str(exc)
                if attempts >= settings.harness_max_attempts:
                    ledger.transition(
                        run_id,
                        example.example_id,
                        "failed_retriable",
                        last_error=last_err,
                    )
                    return
        entry = ledger.get_entry(run_id, example.example_id)
        assert entry is not None
        if skip_synthesis:
            ledger.transition(run_id, example.example_id, "completed")
            agg.add_payload(example.example_id, entry.ranking_payload_json, None)
            return
        self._resume_synthesis(ledger, run_id, example.example_id, entry, False, k, agg)

    def _resume_synthesis(
        self,
        ledger: SqliteLedger,
        run_id: str,
        example_id: str,
        entry,
        skip_synthesis: bool,
        k: int,
        agg: RunAggregator,
    ) -> None:
        if skip_synthesis:
            ledger.transition(run_id, example_id, "completed")
            agg.add_payload(example_id, entry.ranking_payload_json, None)
            return
        settings = self.settings
        ranking = entry.ranking_payload_json or {}
        from finagent_mesh.agent.state import BenchmarkExample, PassageChunk, StageRankingResult

        # Rebuild minimal state for synthesis from durable ranking payload.
        # Example content reloaded lazily from ranking payload chunks.
        chunks = [PassageChunk.model_validate(c) for c in ranking.get("stage2_chunks") or []]
        example = BenchmarkExample(
            example_id=example_id,
            firm_id="",
            query_text="",
            chunks=chunks,
            answer_label=(entry.synthesis_payload_json or {}).get("label"),
        )
        # Prefer reloading full example from dataset if available.
        try:
            if settings.finagentbench_path:
                for ex in load_examples(Path(settings.finagentbench_path)):
                    if ex.example_id == example_id:
                        example = ex
                        break
        except Exception:  # noqa: BLE001
            pass

        attempts = entry.attempts_synthesis
        last_err = None
        while attempts < settings.harness_max_attempts:
            attempts += 1
            try:
                with tracing.example_run(run_id, example_id):
                    state = run_example(
                        self.graph,
                        example,
                        skip_synthesis=False,
                        synthesis_k=k,
                    )
                    # Preserve committed ranking metrics if re-rank differs; prefer durable.
                    if ranking.get("stage1"):
                        state.stage1 = StageRankingResult.model_validate(ranking["stage1"])
                    if ranking.get("stage2"):
                        state.stage2 = StageRankingResult.model_validate(ranking["stage2"])
                    tracing.log_agent_state(state)
                synth_payload = {
                    "answer": state.synthesized_answer,
                    "answer_score": state.answer_score.model_dump() if state.answer_score else None,
                    "label": example.answer_label,
                }
                ledger.transition(
                    run_id,
                    example_id,
                    "completed",
                    synthesis_payload=synth_payload,
                    inc_synthesis=True,
                )
                agg.add_payload(example_id, ranking, synth_payload)
                return
            except Exception as exc:  # noqa: BLE001
                last_err = str(exc)
                ledger.transition(
                    run_id,
                    example_id,
                    "synthesis_retriable",
                    last_error=last_err,
                    inc_synthesis=True,
                )
        # Exhausted
        ledger.transition(
            run_id,
            example_id,
            "synthesis_retriable",
            last_error=last_err or "synthesis_attempts_exhausted",
        )

    def status(self, run_id: str) -> dict[str, Any]:
        ledger = SqliteLedger(self.settings.eval_ledger_path)
        try:
            return {"counts": ledger.status_counts(run_id), "lease": ledger.lease_info(run_id)}
        finally:
            ledger.close()

    def export_metrics(self, run_id: str, out: Path | None = None) -> dict[str, Any]:
        ledger = SqliteLedger(self.settings.eval_ledger_path)
        agg = RunAggregator(run_id)
        try:
            rows = ledger._conn.execute(
                "SELECT example_id, ranking_payload_json, synthesis_payload_json "
                "FROM ledger_entries WHERE run_id=?",
                (run_id,),
            ).fetchall()
            for row in rows:
                ranking = json.loads(row["ranking_payload_json"]) if row["ranking_payload_json"] else None
                synthesis = (
                    json.loads(row["synthesis_payload_json"]) if row["synthesis_payload_json"] else None
                )
                agg.add_payload(row["example_id"], ranking, synthesis)
            return agg.export(out)
        finally:
            ledger.close()
