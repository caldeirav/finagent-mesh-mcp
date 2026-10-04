# Quickstart: FinAgentBench Hybrid Evaluation Harness

**Feature**: `001-finagentbench-harness` | **Date**: 2026-10-04

Validation guide for operators on HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64). Implementation details live in later tasks—not here.

## Prerequisites

- uv + Python 3.12 (repo `.python-version`)
- Podman (preferred) or Docker with `nvidia-container-toolkit`
- FinAgentBench dataset available locally
- Google AI Studio API key (for synthesis)
- AgentGateway reachable for MCP + System-1 mediation
- GPU capacity for AnyJev / vLLM-sr / CLM-8B containers

Contracts: [contracts/](./contracts/) · Data model: [data-model.md](./data-model.md) · Research: [research.md](./research.md)

## 1. Environment

```bash
cp .env.example .env
# set FINAGENTBENCH_PATH, GOOGLE_API_KEY, AGENT_GATEWAY_URL, optional overrides
uv sync
```

## 2. Build and start local System-1 engines

```bash
./scripts/build_containers.sh
# start engines so health endpoints answer on :8000 and :8001
curl -sf http://localhost:8000/healthz
curl -sf http://localhost:8001/healthz
```

**Expected**: HTTP 200 with `status=ok` for both ports.

## 3. Start MCP tools behind AgentGateway

Ensure `mcp-sec-edgar` and `mcp-financial-calculator` are registered and reachable only through the gateway (no direct bypass from the harness).

**Expected**: Gateway lists both servers; sample `ratio_analysis` / `list_document_types` calls succeed.

## 4. Smoke ranking-only run (no synthesis)

```bash
uv run python scripts/run_harness.py run \
  --run-id smoke-rank-001 \
  --limit 20 \
  --skip-synthesis
```

**Expected**:
- Ledger entries reach `ranking_complete` or `skipped_invalid` / failed-with-reason
- Stage-1 and Stage-2 nDCG@5 / MAP@5 / MRR@5 persisted for labeled examples
- No Gemini calls occur
- MLflow traces include Stage 1/2 distributions

## 5. Smoke end-to-end run (with synthesis + answer score)

```bash
uv run python scripts/run_harness.py run \
  --run-id smoke-e2e-001 \
  --limit 100
```

**Expected** (SC-008 / SC-009 / SC-010):
- ≥95% examples in a terminal ledger state
- Synthesis uses top-5 chunks by default
- Answer scores present when labels exist; explicit skip when missing
- Traces reconstruct rankings, tools, synthesis, scores

## 6. Crash-resume check

1. Start a run with `--limit 30`.
2. Interrupt mid-run (SIGINT/SIGKILL after several completes).
3. Re-run the same `--run-id`.

**Expected** (SC-002 / FR-019):
- Completed / ranking-complete examples are not re-ranked
- `synthesis_retriable` retries synthesis only
- No duplicate terminal success rows

## 7. Fail-closed local ranking

Stop System-1 on `:8000` or `:8001`, then process one pending example.

**Expected** (SC-003 / FR-018): example fails closed; no cloud-only Stage-1/Stage-2 ranking.

## 8. Deterministic metrics golden

```bash
uv run python scripts/run_harness.py run --run-id golden-a --limit 50 --skip-synthesis
uv run python scripts/run_harness.py run --run-id golden-b --limit 50 --skip-synthesis
uv run python scripts/run_harness.py export-metrics --run-id golden-a
uv run python scripts/run_harness.py export-metrics --run-id golden-b
```

**Expected** (SC-005): identical Stage-1/Stage-2 metric triples for the same fixed subset and rankings.

## 9. Export

```bash
uv run python scripts/run_harness.py export-metrics --run-id smoke-e2e-001 --out /tmp/metrics.json
uv run python scripts/run_harness.py status --run-id smoke-e2e-001
```

**Expected**: JSON summary with Stage-1/2 aggregates and answer-score summary; status shows ledger counts.
