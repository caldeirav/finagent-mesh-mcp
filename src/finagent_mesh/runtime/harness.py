"""End-to-end evaluation harness with ledger resume and fail-closed local ranking."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from finagent_mesh.agent.graph import build_graph, run_example
from finagent_mesh.agent.state import AgentState
from finagent_mesh.clients.gemini import GeminiClient, GeminiError
from finagent_mesh.clients.open_decision import OpenDecisionClient, OpenDecisionError, bind_from_registry
from finagent_mesh.config import Settings, get_settings, require_official_mock_policy
from finagent_mesh.dataset.finagentbench import load_examples
from finagent_mesh.ledger.sqlite_ledger import TERMINAL_NO_RERANK, SqliteLedger
from finagent_mesh.matrix.metrics import top1_correct as _top1_correct
from finagent_mesh.matrix.partners import is_inprocess_engine
from finagent_mesh.matrix.sampling import select_example_ids
from finagent_mesh.runtime.health import require_engines_healthy, require_systemone_healthy
from finagent_mesh.runtime.progress import log as progress_log
from finagent_mesh.runtime import tracing
from finagent_mesh.scoring.run_aggregator import RunAggregator


def expected_snapshot(example) -> dict[str, Any]:
    by_type: dict[str, int] = {}
    for c in example.chunks:
        by_type[c.doc_type] = by_type.get(c.doc_type, 0) + 1
    return {
        "example_id": example.example_id,
        "firm_id": example.firm_id,
        "query_text": example.query_text,
        "query_category": getattr(example, "query_category", "") or "",
        "stage1_labels": example.stage1_labels,
        "stage2_labels": example.stage2_labels,
        "answer_label": example.answer_label,
        "n_chunks": len(example.chunks),
        "chunks_by_doc_type": by_type,
    }


def _ranking_payload(
    example,
    state: AgentState | None,
    decision: OpenDecisionClient,
    stage1_engine: str | None,
    stage2_engine: str | None,
    *,
    error: str | None = None,
) -> dict[str, Any]:
    s1 = state.stage1.model_dump() if state and state.stage1 else None
    s2 = state.stage2.model_dump() if state and state.stage2 else None
    chunks = []
    if state:
        for c in state.stage2_chunks:
            d = c.model_dump()
            d["text"] = (d.get("text") or "")[:500]
            chunks.append(d)
    expected = expected_snapshot(example)
    top1 = state.top1_doc_type if state else None
    empty = bool(
        (error or (state.error if state else None)) == "empty_top1_chunks"
        or (state and state.error == "empty_top1_chunks")
    )
    correct = _top1_correct(top1, expected.get("stage1_labels") or [])
    # Collapsed one-shot: Top-1 sentinel is not a filing-type routing success
    if top1 == "__all__":
        correct = False
    return {
        "stage1": s1,
        "stage2": s2,
        "top1_doc_type": top1,
        "stage2_chunks": chunks,
        "stage1_engine": stage1_engine or decision.stage1_engine_id,
        "stage2_engine": stage2_engine or decision.stage2_engine_id,
        "expected": expected,
        "io_traces": list(decision.io_traces),
        "error": error or (state.error if state else None),
        "top1_correct": correct,
        "empty_top1_chunks": empty,
        "eligible_for_conditional_s2": bool(correct) and not empty,
        "collapsed_stages": top1 == "__all__",
        "parse_failure": bool(
            error and "parse" in str(error).lower()
        ),
    }


class Harness:
    def __init__(
        self,
        settings: Settings | None = None,
        *,
        stage1_engine: str | None = None,
        stage2_engine: str | None = None,
        gemini_model: str | None = None,
        allow_mock: bool = False,
        port_overrides: dict[str, int] | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.allow_mock = allow_mock
        self.stage1_engine = stage1_engine
        self.stage2_engine = stage2_engine
        self.port_overrides = dict(port_overrides or {})
        self.gemini_model = gemini_model or self.settings.gemini_model
        require_official_mock_policy(
            systemone_mock=self.settings.systemone_mock, allow_mock=allow_mock
        )
        if stage1_engine and stage2_engine and not self.settings.systemone_mock:
            self.decision = bind_from_registry(
                stage1_engine,
                stage2_engine,
                mock=False,
                registry_path=str(self.settings.engines_registry_path),
                port_overrides=self.port_overrides,
            )
        else:
            self.decision = OpenDecisionClient(
                self.settings.systemone_stage1_url,
                self.settings.systemone_stage2_url,
                mock=self.settings.systemone_mock,
            )
        self.gemini = GeminiClient(self.settings.google_api_key, self.gemini_model)
        self.graph = build_graph(self.decision, self.gemini)

    def run(
        self,
        run_id: str,
        *,
        limit: int | None = None,
        dataset_path: Path | None = None,
        skip_synthesis: bool = False,
        synthesis_k: int | None = None,
        sample_size: int | None = None,
        sample_seed: int | None = None,
        example_ids: list[str] | None = None,
    ) -> dict[str, Any]:
        settings = self.settings
        path = dataset_path or settings.finagentbench_path
        if path is None:
            raise RuntimeError("FINAGENTBENCH_PATH is required")

        if self.stage1_engine and self.stage2_engine and not settings.systemone_mock:
            from finagent_mesh.clients.engines.registry import load_registry

            from finagent_mesh.matrix.ports import base_url_for_port

            reg = load_registry(settings.engines_registry_path)
            targets: list[tuple[str, str]] = []
            for eid in (self.stage1_engine, self.stage2_engine):
                if is_inprocess_engine(reg, eid):
                    continue
                cfg = reg.get(eid)
                url = (
                    base_url_for_port(self.port_overrides[eid])
                    if eid in self.port_overrides
                    else cfg.base_url
                )
                targets.append((url, cfg.health_path))
            if targets:
                require_engines_healthy(targets, mock=False)
        else:
            require_systemone_healthy(
                settings.systemone_stage1_url,
                settings.systemone_stage2_url,
                mock=settings.systemone_mock,
            )

        progress_log(f"Harness {run_id}: loading FinAgentBench from {path}…")
        all_examples = load_examples(Path(path), limit=None if sample_size or example_ids else limit)
        if example_ids is not None:
            id_set = set(example_ids)
            examples = [e for e in all_examples if e.example_id in id_set]
            # Preserve sample order
            order = {eid: i for i, eid in enumerate(example_ids)}
            examples.sort(key=lambda e: order.get(e.example_id, 10**9))
            selected_ids = list(example_ids)
            capped = False
        elif sample_size is not None:
            selection = select_example_ids(
                [e.example_id for e in all_examples],
                sample_size=sample_size,
                sample_seed=sample_seed,
            )
            id_set = set(selection.selected_example_ids)
            examples = [e for e in all_examples if e.example_id in id_set]
            order = {eid: i for i, eid in enumerate(selection.selected_example_ids)}
            examples.sort(key=lambda e: order.get(e.example_id, 10**9))
            selected_ids = selection.selected_example_ids
            capped = selection.capped
        else:
            examples = all_examples[:limit] if limit is not None else all_examples
            selected_ids = [e.example_id for e in examples]
            capped = False

        progress_log(
            f"Harness {run_id}: {len(examples)} example(s)  "
            f"S1={self.stage1_engine} S2={self.stage2_engine}  "
            f"synthesis={'off' if skip_synthesis else 'on'}"
        )

        k = synthesis_k if synthesis_k is not None else settings.synthesis_k
        ledger = SqliteLedger(settings.eval_ledger_path)
        owner = SqliteLedger.default_owner()
        config = {
            "limit": limit,
            "skip_synthesis": skip_synthesis,
            "synthesis_enabled": not skip_synthesis,
            "synthesis_k": k,
            "dataset_path": str(path),
            "stage1_engine": self.stage1_engine,
            "stage2_engine": self.stage2_engine,
            "gemini_model": self.gemini_model,
            "systemone_mock": settings.systemone_mock,
            "allow_mock": self.allow_mock,
            "sample_size": sample_size,
            "sample_seed": sample_seed,
            "selected_example_ids": selected_ids,
            "sample_capped": capped,
        }
        try:
            ledger.ensure_run(run_id, config)
            ledger.acquire_lease(run_id, owner)
            ledger.ensure_examples(run_id, [e.example_id for e in examples])
            tracing.setup_mlflow(settings.mlflow_tracking_uri)
            agg = RunAggregator(run_id)
            import mlflow

            with mlflow.start_run(run_name=run_id):
                mlflow.set_tags(
                    {
                        "stage1_engine": self.stage1_engine or "",
                        "stage2_engine": self.stage2_engine or "",
                        "gemini_model": self.gemini_model,
                        "systemone_mock": str(settings.systemone_mock),
                    }
                )
                n_ex = len(examples)
                for idx, example in enumerate(examples, 1):
                    entry = ledger.get_entry(run_id, example.example_id)
                    assert entry is not None
                    short_id = example.example_id
                    if entry.state == "completed":
                        progress_log(f"  [{idx}/{n_ex}] {short_id} skip (already completed)")
                        if entry.ranking_payload_json:
                            agg.add_payload(
                                example.example_id,
                                entry.ranking_payload_json,
                                entry.synthesis_payload_json,
                            )
                        continue
                    t0 = time.perf_counter()
                    was = entry.state
                    if was == "failed_retriable":
                        progress_log(
                            f"  [{idx}/{n_ex}] {short_id} retry ranking "
                            f"(ledger leftover from an earlier failed attempt)"
                        )
                    else:
                        progress_log(f"  [{idx}/{n_ex}] {short_id} ranking…")
                    if entry.state == "synthesis_retriable" and entry.ranking_payload_json:
                        self._resume_synthesis(
                            ledger, run_id, example.example_id, entry, skip_synthesis, k, agg
                        )
                        progress_log(
                            f"  [{idx}/{n_ex}] {short_id} synthesis resume "
                            f"{time.perf_counter() - t0:.1f}s"
                        )
                        continue
                    if entry.state in TERMINAL_NO_RERANK and entry.state == "ranking_complete":
                        if skip_synthesis:
                            ledger.transition(run_id, example.example_id, "completed")
                            agg.add_payload(example.example_id, entry.ranking_payload_json, None)
                            progress_log(f"  [{idx}/{n_ex}] {short_id} ranking already complete")
                            continue
                        self._resume_synthesis(
                            ledger, run_id, example.example_id, entry, skip_synthesis, k, agg
                        )
                        progress_log(
                            f"  [{idx}/{n_ex}] {short_id} synthesis resume "
                            f"{time.perf_counter() - t0:.1f}s"
                        )
                        continue
                    self._process_full(
                        ledger, run_id, example, skip_synthesis=skip_synthesis, k=k, agg=agg
                    )
                    done = ledger.get_entry(run_id, example.example_id)
                    st = done.state if done else "?"
                    err = (done.last_error if done else None) or ""
                    extra = f"  error={err[:300]}" if err else ""
                    progress_log(
                        f"  [{idx}/{n_ex}] {short_id} → {st} "
                        f"({time.perf_counter() - t0:.1f}s){extra}"
                    )
            return {
                "status": ledger.status_counts(run_id),
                "lease": ledger.lease_info(run_id),
                "config": config,
            }
        finally:
            ledger.release_lease(run_id, owner)
            ledger.close()

    def _maybe_attach_ofr(self, example, state: AgentState | None, ranking_payload: dict[str, Any]) -> None:
        """Option-flip rate: AnyJev L0 Top-1 change under reversed type order."""
        if not state or self.stage1_engine != "anyjev-l0":
            return
        if state.top1_doc_type in (None, "__all__"):
            return
        try:
            from finagent_mesh.agent.types import DOC_TYPES

            candidates = [
                {"id": dt, "text": f"Document type {dt} for firm {example.firm_id}"}
                for dt in DOC_TYPES
            ]
            flipped = list(reversed(candidates))
            resp = self.decision.decide(
                "choice",
                example.query_text,
                flipped,
                {"firm_id": example.firm_id, "ofr_probe": True},
            )
            ranking = sorted(resp.get("ranking") or [], key=lambda r: r["rank"])
            top_rev = ranking[0]["id"] if ranking else None
            ranking_payload["option_flipped"] = bool(
                top_rev is not None and top_rev != state.top1_doc_type
            )
            ranking_payload["ofr_top1_reversed"] = top_rev
        except Exception:  # noqa: BLE001
            ranking_payload["option_flipped"] = None

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
                    tracing.log_binding(
                        stage1_engine=self.stage1_engine,
                        stage2_engine=self.stage2_engine,
                        gemini_model=self.gemini_model,
                    )
                    self.decision.reset_traces()
                    state = run_example(
                        self.graph,
                        example,
                        skip_synthesis=True,
                        synthesis_k=k,
                    )
                    tracing.log_agent_state(state, decision_meta=self.decision.last_response_meta)
                ranking_payload = _ranking_payload(
                    example, state, self.decision, self.stage1_engine, self.stage2_engine
                )
                self._maybe_attach_ofr(example, state, ranking_payload)
                if state.error == "empty_top1_chunks":
                    ledger.transition(
                        run_id,
                        example.example_id,
                        "failed_retriable",
                        last_error=state.error,
                        ranking_payload=ranking_payload,
                        inc_stage2=True,
                    )
                    agg.add_payload(example.example_id, ranking_payload, None)
                    return
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
                ranking_payload = _ranking_payload(
                    example,
                    state,
                    self.decision,
                    self.stage1_engine,
                    self.stage2_engine,
                    error=last_err,
                )
                if attempts >= settings.harness_max_attempts:
                    ledger.transition(
                        run_id,
                        example.example_id,
                        "failed_retriable",
                        last_error=last_err,
                        ranking_payload=ranking_payload,
                        inc_stage1=True,
                    )
                    agg.add_payload(example.example_id, ranking_payload, None)
                    return
            except Exception as exc:  # noqa: BLE001
                last_err = str(exc)
                ranking_payload = _ranking_payload(
                    example,
                    state,
                    self.decision,
                    self.stage1_engine,
                    self.stage2_engine,
                    error=last_err,
                )
                if attempts >= settings.harness_max_attempts:
                    ledger.transition(
                        run_id,
                        example.example_id,
                        "failed_retriable",
                        last_error=last_err,
                        ranking_payload=ranking_payload,
                    )
                    agg.add_payload(example.example_id, ranking_payload, None)
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

        chunks = [PassageChunk.model_validate(c) for c in ranking.get("stage2_chunks") or []]
        example = BenchmarkExample(
            example_id=example_id,
            firm_id="",
            query_text="",
            chunks=chunks,
            answer_label=(entry.synthesis_payload_json or {}).get("label"),
        )
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
                    tracing.log_binding(
                        stage1_engine=self.stage1_engine,
                        stage2_engine=self.stage2_engine,
                        gemini_model=self.gemini_model,
                    )
                    state = run_example(
                        self.graph,
                        example,
                        skip_synthesis=False,
                        synthesis_k=k,
                    )
                    if ranking.get("stage1"):
                        state.stage1 = StageRankingResult.model_validate(ranking["stage1"])
                    if ranking.get("stage2"):
                        state.stage2 = StageRankingResult.model_validate(ranking["stage2"])
                    tracing.log_agent_state(state)
                synth_payload = {
                    "answer": state.synthesized_answer,
                    "answer_score": state.answer_score.model_dump() if state.answer_score else None,
                    "label": example.answer_label,
                    "gemini_model": self.gemini_model,
                    "prompt": self.gemini.last_prompt,
                    "passages": [
                        {"chunk_id": c.chunk_id, "text": (c.text or "")[:800]}
                        for c in (state.stage2_chunks or chunks)[:k]
                    ],
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
            except GeminiError as exc:
                last_err = str(exc)
                ledger.transition(
                    run_id,
                    example_id,
                    "synthesis_retriable",
                    last_error=last_err,
                    inc_synthesis=True,
                )
            except Exception as exc:  # noqa: BLE001
                last_err = str(exc)
                ledger.transition(
                    run_id,
                    example_id,
                    "synthesis_retriable",
                    last_error=last_err,
                    inc_synthesis=True,
                )
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
