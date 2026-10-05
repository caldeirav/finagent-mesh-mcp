"""Sequential exclusive matrix orchestration with fixed Stage partners."""

from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path
from typing import Any

from finagent_mesh.clients.engines.registry import EngineRegistry, load_registry
from finagent_mesh.config import Settings, get_settings, require_official_mock_policy
from finagent_mesh.dataset.finagentbench import load_examples
from finagent_mesh.matrix.metrics import aggregate_paper_metrics
from finagent_mesh.matrix.models import EngineMetricsRecord, MatrixRun, MatrixRowResult
from finagent_mesh.matrix.partners import (
    FixedStagePartners,
    deferred_skip_records,
    is_inprocess_engine,
    resolve_matrix_pairs,
)
from finagent_mesh.matrix.ports import plan_engine_ports
from finagent_mesh.matrix.report import write_report
from finagent_mesh.matrix.sampling import select_example_ids
from finagent_mesh.runtime.harness import Harness
from finagent_mesh.runtime.progress import log as progress_log
from finagent_mesh.scoring.run_aggregator import RunAggregator


class MatrixRunner:
    def __init__(
        self,
        settings: Settings | None = None,
        *,
        allow_mock: bool = False,
        manage_servers: bool = True,
        force_restart: bool = False,
        repo_root: Path | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.allow_mock = allow_mock
        self.manage_servers = manage_servers
        self.force_restart = force_restart
        self.repo_root = repo_root or Path.cwd()
        self.registry: EngineRegistry = load_registry(self.settings.engines_registry_path)
        self.partners = FixedStagePartners.from_registry(self.registry)
        self._state_path = self.repo_root / "artifacts" / "matrix_runs"
        self._state_path.mkdir(parents=True, exist_ok=True)
        self._active_variable: str | None = None

    def _state_file(self, matrix_run_id: str) -> Path:
        return self._state_path / f"{matrix_run_id}.json"

    def save(self, matrix: MatrixRun) -> None:
        self._state_file(matrix.matrix_run_id).write_text(
            json.dumps(matrix.to_dict(), indent=2), encoding="utf-8"
        )

    def load(self, matrix_run_id: str) -> MatrixRun:
        raw = json.loads(self._state_file(matrix_run_id).read_text(encoding="utf-8"))
        rows = []
        for r in raw.get("rows") or []:
            m = r.get("metrics") or {}
            metrics = EngineMetricsRecord(
                n_examples=int(m.get("n_examples") or 0),
                stage1_ndcg_at_5=m.get("stage1_ndcg_at_5"),
                stage1_map_at_5=m.get("stage1_map_at_5"),
                stage1_mrr_at_5=m.get("stage1_mrr_at_5"),
                stage2_ndcg_at_5=m.get("stage2_ndcg_at_5"),
                stage2_map_at_5=m.get("stage2_map_at_5"),
                stage2_mrr_at_5=m.get("stage2_mrr_at_5"),
                stage2_ndcg_at_5_given_top1=m.get("stage2_ndcg_at_5_given_top1"),
                stage2_map_at_5_given_top1=m.get("stage2_map_at_5_given_top1"),
                stage2_mrr_at_5_given_top1=m.get("stage2_mrr_at_5_given_top1"),
                stage1_top1_recall=m.get("stage1_top1_recall"),
                stage1_top5_recall=m.get("stage1_top5_recall"),
                empty_top1_chunk_rate=m.get("empty_top1_chunk_rate"),
                option_flip_rate=m.get("option_flip_rate"),
                parse_failure_rate=m.get("parse_failure_rate"),
                latency_ms_p50=m.get("latency_ms_p50"),
                latency_ms_p95=m.get("latency_ms_p95"),
                latency_stage1_p50_ms=m.get("latency_stage1_p50_ms"),
                latency_stage1_p95_ms=m.get("latency_stage1_p95_ms"),
                latency_stage2_p50_ms=m.get("latency_stage2_p50_ms"),
                latency_stage2_p95_ms=m.get("latency_stage2_p95_ms"),
                gpu_mem_high_water_mb=m.get("gpu_mem_high_water_mb"),
                answer_normalized_em=m.get("answer_normalized_em"),
                answer_token_f1=m.get("answer_token_f1"),
                n_synthesis_attempted=int(m.get("n_synthesis_attempted") or 0),
                n_synthesis_failed=int(m.get("n_synthesis_failed") or 0),
                n_empty_top1=int(m.get("n_empty_top1") or 0),
                blocks=list(m.get("blocks") or r.get("blocks") or []),
                stage1_unsupported_reason=m.get("stage1_unsupported_reason"),
                stage2_unsupported_reason=m.get("stage2_unsupported_reason"),
            )
            rows.append(
                MatrixRowResult(
                    variable_config_id=r["variable_config_id"],
                    eval_run_id=r["eval_run_id"],
                    stage1_engine_id=r["stage1_engine_id"],
                    stage2_engine_id=r["stage2_engine_id"],
                    status=r.get("status", "pending"),
                    error=r.get("error"),
                    metrics=metrics,
                    blocks=list(r.get("blocks") or []),
                    collapsed_stages=bool(r.get("collapsed_stages")),
                    role=str(r.get("role") or ""),
                )
            )
        return MatrixRun(
            matrix_run_id=raw["matrix_run_id"],
            dataset_path=raw["dataset_path"],
            sample_size=raw.get("sample_size"),
            sample_seed=raw.get("sample_seed"),
            selected_example_ids=list(raw.get("selected_example_ids") or []),
            config_ids=list(raw.get("config_ids") or []),
            status=raw.get("status", "pending"),
            partner_ids=dict(raw.get("partners") or raw.get("partner_ids") or {}),
            gemini_model=raw.get("gemini_model", "gemini-2.5-flash"),
            systemone_mock=bool(raw.get("systemone_mock")),
            synthesis_enabled=bool(raw.get("synthesis_enabled", True)),
            rows=rows,
            skip_records=list(raw.get("skip_records") or []),
            created_at=raw.get("created_at", ""),
        )

    def _serve(
        self,
        action: str,
        config_id: str | None = None,
        *,
        force: bool = False,
        port: int | None = None,
    ) -> None:
        if not self.manage_servers:
            return
        script = self.repo_root / "scripts" / "serve_engine.sh"
        env = {**dict(__import__("os").environ)}
        env.setdefault("SYSTEMONE_BACKEND", "lexical")
        if force:
            env["SYSTEMONE_FORCE_RESTART"] = "1"
        if port is not None:
            env["SYSTEMONE_PORT_OVERRIDE"] = str(port)
        elif "SYSTEMONE_PORT_OVERRIDE" in env:
            del env["SYSTEMONE_PORT_OVERRIDE"]
        cmd = ["bash", str(script), action]
        if config_id:
            cmd.append(config_id)
        subprocess.run(
            cmd,
            check=True,
            cwd=str(self.repo_root),
            env=env,
        )

    def _ensure_partner(self, partner_id: str) -> None:
        self._serve("start", partner_id)
        # brief wait for bind
        time.sleep(0.3)
        self._serve("health", partner_id)

    def run(
        self,
        matrix_run_id: str,
        *,
        engines: list[str] | None = None,
        pair_ids: list[str] | None = None,
        include_baseline: bool = False,
        include_optional: bool = False,
        sample_size: int | None = None,
        sample_seed: int | None = None,
        gemini_model: str | None = None,
        skip_synthesis: bool = False,
        dataset_path: Path | None = None,
    ) -> MatrixRun:
        require_official_mock_policy(
            systemone_mock=self.settings.systemone_mock, allow_mock=self.allow_mock
        )
        path = dataset_path or self.settings.finagentbench_path
        if path is None:
            raise RuntimeError("FINAGENTBENCH_PATH is required")
        pairs = resolve_matrix_pairs(
            self.registry,
            pair_ids=pair_ids,
            engines=engines,
            include_baseline=include_baseline,
            include_optional=include_optional,
            repo_root=self.repo_root,
        )
        if not pairs:
            raise RuntimeError(
                "No matrix pairs selected. Check configs/engines.yaml matrix_pairs "
                "or pass --pairs / --engines."
            )
        config_ids = [p.pair_id for p in pairs]
        progress_log(f"Loading FinAgentBench from {path} (full dump, then sample)…")
        all_examples = load_examples(Path(path))
        selection = select_example_ids(
            [e.example_id for e in all_examples],
            sample_size=sample_size,
            sample_seed=sample_seed,
        )
        skips = [s.to_dict() for s in deferred_skip_records(self.registry)]
        if not include_optional:
            from finagent_mesh.matrix.partners import pairs_from_registry

            for p in pairs_from_registry(self.registry):
                if p.optional and p.pair_id not in config_ids:
                    skips.append(
                        {
                            "pair_id": p.pair_id,
                            "reason": "optional_not_requested",
                            "issue_url": None,
                        }
                    )
        matrix = MatrixRun(
            matrix_run_id=matrix_run_id,
            dataset_path=str(path),
            sample_size=sample_size,
            sample_seed=sample_seed,
            selected_example_ids=selection.selected_example_ids,
            config_ids=config_ids,
            status="running",
            partner_ids={
                "stage1_partner_id": self.partners.stage1_partner_id,
                "stage2_partner_id": self.partners.stage2_partner_id,
                "block_a_stage2": self.registry.partners.get("block_a_stage2", "decision20-lux"),
                "block_b_stage1": self.registry.partners.get("block_b_stage1", "decision20-lux"),
                "binding": "architecture-pairs" if not engines else "legacy-engines",
            },
            gemini_model=gemini_model or self.settings.gemini_model,
            systemone_mock=self.settings.systemone_mock,
            synthesis_enabled=not skip_synthesis,
            skip_records=skips,
        )
        self.save(matrix)

        if self.force_restart and self.manage_servers:
            progress_log("force-restart: stopping all System-1 sidecars and listeners")
            self._serve("stop-all")

        progress_log(
            f"Matrix {matrix_run_id}: {len(pairs)} pair(s), "
            f"{len(matrix.selected_example_ids)} example(s), "
            f"synthesis={'off' if skip_synthesis else 'on'}"
        )
        for i, p in enumerate(pairs, 1):
            progress_log(
                f"  planned {i}/{len(pairs)} {p.pair_id}: "
                f"S1={p.stage1_config_id} S2={p.stage2_config_id}"
            )

        active_ports: dict[str, int] = {}
        n_pairs = len(pairs)
        for pair_i, pair in enumerate(pairs, 1):
            binding = pair.as_binding()
            port_plan = plan_engine_ports(
                self.registry, pair.stage1_config_id, pair.stage2_config_id
            )
            row = MatrixRowResult(
                variable_config_id=pair.pair_id,
                eval_run_id=f"{matrix_run_id}:{pair.pair_id}",
                stage1_engine_id=pair.stage1_config_id,
                stage2_engine_id=pair.stage2_config_id,
                status="running",
                blocks=list(pair.blocks),
                collapsed_stages=pair.collapsed_stages,
                role=pair.role,
            )
            matrix.rows.append(row)
            self.save(matrix)
            pair_t0 = time.perf_counter()
            progress_log(
                f"=== Pair {pair_i}/{n_pairs} {pair.pair_id} "
                f"S1={pair.stage1_config_id} S2={pair.stage2_config_id} "
                f"blocks={list(pair.blocks)} ==="
            )
            if pair.rationale.strip():
                progress_log(pair.rationale.strip().split("\n")[0][:200])
            try:
                # Stop engines that are no longer needed or must move ports.
                for eid, port in list(active_ports.items()):
                    if eid not in port_plan or port_plan[eid] != port:
                        progress_log(f"stopping {eid} (port {port})")
                        self._serve("stop", eid, port=port)
                        del active_ports[eid]
                # Free ports occupied by a different config_id.
                occupied = {p: e for e, p in active_ports.items()}
                for eid, port in port_plan.items():
                    holder = occupied.get(port)
                    if holder is not None and holder != eid:
                        progress_log(
                            f"stopping {holder} to free port {port} for {eid}"
                        )
                        self._serve("stop", holder, port=port)
                        del active_ports[holder]
                        occupied.pop(port, None)
                for eid, port in port_plan.items():
                    if eid in active_ports:
                        progress_log(f"reusing warm {eid} on port {port}")
                        continue
                    progress_log(
                        f"starting {eid} on port {port} "
                        f"(real weights load on first request)"
                    )
                    self._serve("start", eid, port=port, force=True)
                    time.sleep(0.3)
                    self._serve("health", eid, port=port)
                    active_ports[eid] = port
                # In-process engines need no sidecar.
                for eid in pair.unique_engines():
                    if is_inprocess_engine(self.registry, eid):
                        progress_log(f"in-process engine {eid} (no sidecar)")
                self._active_variable = pair.pair_id

                harness = Harness(
                    self.settings,
                    stage1_engine=binding.stage1_config_id,
                    stage2_engine=binding.stage2_config_id,
                    gemini_model=matrix.gemini_model,
                    allow_mock=self.allow_mock,
                    port_overrides=port_plan,
                )
                progress_log(
                    f"{pair.pair_id}: ranking {len(matrix.selected_example_ids)} example(s)…"
                )
                harness.run(
                    row.eval_run_id,
                    skip_synthesis=skip_synthesis,
                    example_ids=matrix.selected_example_ids,
                    dataset_path=Path(path),
                )
                row.metrics = self._metrics_for_run(
                    row.eval_run_id,
                    stage1_id=binding.stage1_config_id,
                    stage2_id=binding.stage2_config_id,
                    variable_id=pair.pair_id,
                    synthesis_enabled=matrix.synthesis_enabled,
                    blocks=list(pair.blocks),
                )
                row.status = "completed"
                elapsed = time.perf_counter() - pair_t0
                m = row.metrics
                progress_log(
                    f"{pair.pair_id} done in {elapsed:.1f}s  "
                    f"S1 nDCG@5={m.stage1_ndcg_at_5}  S2 nDCG@5={m.stage2_ndcg_at_5}  "
                    f"n={m.n_examples}"
                )
            except Exception as exc:  # noqa: BLE001
                row.status = "failed"
                row.error = str(exc)
                progress_log(f"{pair.pair_id} FAILED after {time.perf_counter() - pair_t0:.1f}s: {exc}")
            self.save(matrix)

        matrix.status = (
            "completed"
            if all(r.status == "completed" for r in matrix.rows)
            else "failed"
        )
        self.save(matrix)
        return matrix

    def _metrics_for_run(
        self,
        eval_run_id: str,
        *,
        stage1_id: str,
        stage2_id: str,
        variable_id: str,
        synthesis_enabled: bool,
        blocks: list[str] | None = None,
    ) -> EngineMetricsRecord:
        from finagent_mesh.ledger.sqlite_ledger import SqliteLedger

        ledger = SqliteLedger(self.settings.eval_ledger_path)
        agg = RunAggregator(eval_run_id)
        paper_recs: list[dict[str, Any]] = []
        try:
            rows = ledger._conn.execute(
                "SELECT example_id, ranking_payload_json, synthesis_payload_json, state "
                "FROM ledger_entries WHERE run_id=?",
                (eval_run_id,),
            ).fetchall()
            n_synth_attempted = 0
            n_synth_failed = 0
            for row in rows:
                ranking = json.loads(row["ranking_payload_json"]) if row["ranking_payload_json"] else None
                synthesis = (
                    json.loads(row["synthesis_payload_json"]) if row["synthesis_payload_json"] else None
                )
                agg.add_payload(row["example_id"], ranking, synthesis)
                if ranking:
                    paper_recs.append({"ranking": ranking})
                if synthesis_enabled:
                    if row["state"] in {"completed", "synthesis_retriable"}:
                        n_synth_attempted += 1
                    if row["state"] == "synthesis_retriable":
                        n_synth_failed += 1
            summary = agg.summary()
            paper = aggregate_paper_metrics(paper_recs)
        finally:
            ledger.close()

        gpu_mb: float | None = None
        try:
            import torch

            if torch.cuda.is_available():
                gpu_mb = float(torch.cuda.max_memory_allocated()) / (1024 * 1024)
        except Exception:  # noqa: BLE001
            gpu_mb = None

        metrics = EngineMetricsRecord(
            n_examples=summary["n_examples"],
            stage1_ndcg_at_5=paper.get("stage1_ndcg_at_5")
            or (summary.get("stage1") or {}).get("ndcg_at_5"),
            stage1_map_at_5=paper.get("stage1_map_at_5")
            or (summary.get("stage1") or {}).get("map_at_5"),
            stage1_mrr_at_5=paper.get("stage1_mrr_at_5")
            or (summary.get("stage1") or {}).get("mrr_at_5"),
            stage2_ndcg_at_5=paper.get("stage2_ndcg_at_5")
            or (summary.get("stage2") or {}).get("ndcg_at_5"),
            stage2_map_at_5=paper.get("stage2_map_at_5")
            or (summary.get("stage2") or {}).get("map_at_5"),
            stage2_mrr_at_5=paper.get("stage2_mrr_at_5")
            or (summary.get("stage2") or {}).get("mrr_at_5"),
            stage2_ndcg_at_5_given_top1=paper.get("stage2_ndcg_at_5_given_top1"),
            stage2_map_at_5_given_top1=paper.get("stage2_map_at_5_given_top1"),
            stage2_mrr_at_5_given_top1=paper.get("stage2_mrr_at_5_given_top1"),
            stage1_top1_recall=paper.get("stage1_top1_recall"),
            stage1_top5_recall=paper.get("stage1_top5_recall"),
            empty_top1_chunk_rate=paper.get("empty_top1_chunk_rate"),
            option_flip_rate=paper.get("option_flip_rate"),
            parse_failure_rate=paper.get("parse_failure_rate"),
            latency_ms_p50=paper.get("latency_stage1_p50_ms"),
            latency_ms_p95=paper.get("latency_stage1_p95_ms"),
            latency_stage1_p50_ms=paper.get("latency_stage1_p50_ms"),
            latency_stage1_p95_ms=paper.get("latency_stage1_p95_ms"),
            latency_stage2_p50_ms=paper.get("latency_stage2_p50_ms"),
            latency_stage2_p95_ms=paper.get("latency_stage2_p95_ms"),
            gpu_mem_high_water_mb=gpu_mb,
            answer_normalized_em=(summary.get("answer") or {}).get("normalized_em"),
            answer_token_f1=(summary.get("answer") or {}).get("token_f1"),
            n_synthesis_attempted=n_synth_attempted,
            n_synthesis_failed=n_synth_failed,
            n_empty_top1=int(paper.get("n_empty_top1") or 0),
            blocks=list(blocks or []),
        )
        _ = (stage1_id, stage2_id, variable_id)
        return metrics

    def export(
        self, matrix_run_id: str, *, out: Path | None = None, fmt: str = "json"
    ) -> Path:
        matrix = self.load(matrix_run_id)
        target = out or (self._state_path / f"{matrix_run_id}.report.{fmt}")
        return write_report(matrix, target, fmt=fmt)

    def status(self, matrix_run_id: str) -> dict[str, Any]:
        matrix = self.load(matrix_run_id)
        return {
            "matrix_run_id": matrix.matrix_run_id,
            "status": matrix.status,
            "partners": matrix.partner_ids,
            "rows": [
                {
                    "variable_config_id": r.variable_config_id,
                    "status": r.status,
                    "stage1_engine_id": r.stage1_engine_id,
                    "stage2_engine_id": r.stage2_engine_id,
                    "error": r.error,
                }
                for r in matrix.rows
            ],
        }
