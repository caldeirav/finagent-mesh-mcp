# Quickstart: Decision Model Serving & Benchmark Matrix

**Feature**: `002-decision-model-bench` | **Date**: 2026-10-04

Operator validation on HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64). Implementation follows in `/speckit-tasks` + `/speckit-implement`.

Contracts: [contracts/](./contracts/) · Data model: [data-model.md](./data-model.md) · Research: [research.md](./research.md)

## Prerequisites

- uv + Python 3.12; Podman + `nvidia-container-toolkit`
- FinAgentBench: `run_benchmark.py --real` downloads from Kaggle and converts if `data/finagentbench` is missing (`KAGGLE_USERNAME` / `KAGGLE_KEY` in `.env`)
- `GOOGLE_API_KEY` for Gemini Flash synthesis (default)
- Engine weights paths set in `.env` / registry (`ANYJEV_WEIGHTS`, `CLM8B_WEIGHTS`, …)
- `SYSTEMONE_MOCK=0` for any official claim
- Calibration file for AnyJev L1: `configs/calibration/anyjev_l1_heldout.json` (exactly 200 example IDs)

## 1. Environment

```bash
cp .env.example .env
# FINAGENTBENCH_PATH, GOOGLE_API_KEY, AGENT_GATEWAY_URL, weight paths
# SYSTEMONE_MOCK=0
# GEMINI_MODEL=gemini-2.5-flash
uv sync
```

## 2. Registry and build

```bash
# Install configs/engines.yaml from contracts/engines-registry.yaml (or symlink/copy)
./scripts/build_containers.sh
```

**Expected**: Images for anyjev, clm-8b, vllm-sr, laya, ar-qwen3-instruct build on ARM64.

## 3. Single-engine health (SC-001)

```bash
./scripts/serve_engine.sh start anyjev-l0
./scripts/serve_engine.sh start clm-8b   # Stage-2 partner
./scripts/serve_engine.sh health anyjev-l0
./scripts/serve_engine.sh health clm-8b
curl -sf http://localhost:8000/healthz
curl -sf http://localhost:8001/healthz
```

**Expected**: HTTP 200, `status=ok`, `engine` matches config id.

## 4. Fail-closed Gemini (SC-004)

```bash
# With engines healthy, unset key and require synthesis
env -u GOOGLE_API_KEY uv run python scripts/run_harness.py run \
  --run-id fail-closed-gemini \
  --stage1-engine anyjev-l0 \
  --stage2-engine clm-8b \
  --sample-size 5 --sample-seed 1
```

**Expected**: Ranking may complete; synthesis fails / retriable; **zero** extractive fabricated answers.

## 5. Mock disabled (SC-003)

```bash
SYSTEMONE_MOCK=1 uv run python scripts/run_matrix.py run \
  --matrix-run-id mock-refuse --sample-size 5 --sample-seed 1
# should refuse without --allow-mock

SYSTEMONE_MOCK=0 uv run python scripts/run_harness.py run \
  --run-id real-e2e-20 \
  --stage1-engine anyjev-l0 \
  --stage2-engine clm-8b \
  --sample-size 20 --sample-seed 7
```

**Expected**: Official path rejects mock; real run traces show engine ids, not lexical mock rankings; ≥95% terminal (SC-008).

## 6. Seeded sample reproducibility (SC-005)

```bash
uv run python scripts/run_matrix.py run \
  --matrix-run-id sample-a \
  --engines anyjev-l0 \
  --sample-size 50 --sample-seed 42

uv run python scripts/run_matrix.py run \
  --matrix-run-id sample-b \
  --engines anyjev-l0 \
  --sample-size 50 --sample-seed 42
```

**Expected**: Identical `selected_example_ids` in both matrix configs/reports.

## 6. Paper Block A/B pairs (default production matrix)

The default matrix is no longer a CLM cross-product. See [003 quickstart](../003-choice-score-paper/quickstart.md) and [README.md](../../README.md).

```bash
uv run python scripts/run_benchmark.py --list-pairs
uv run python scripts/run_benchmark.py --real --records 50 --seed 42 --run-id paper-smoke-50
# Highest-value pairs:
uv run python scripts/run_benchmark.py --real --pairs lux-lux,lux-bm25,kai-lux --records 20 --seed 42 --run-id smoke-core
```

**Expected**: Block A (`*-lux` Choice variants) + Block B (`lux-*` Score variants). `--real` is ranking-only unless `--with-synthesis`. Legacy `--engines` ablation still uses fixed CLM/AnyJev partners.

## 7. Sample matrix (≥2 engines, SC-002 / SC-007 / SC-009)

```bash
uv run python scripts/run_matrix.py run \
  --matrix-run-id matrix-smoke-50 \
  --engines anyjev-l0,clm-8b,laya-modernbert \
  --sample-size 50 --sample-seed 42

uv run python scripts/run_matrix.py export \
  --matrix-run-id matrix-smoke-50 \
  --out ./artifacts/matrix-smoke-50.json
```

**Expected**:
- One variable engine under test at a time; partner co-runs
- Each example trace has Stage 1 + Stage 2 in one agentic execution
- Full pipeline attempts Gemini Flash synthesis by default
- Export has aligned metric columns per variable engine (attribution to producing engine ids)
- Flash model id recorded (SC-010)

## 8. AR baseline signals (SC-006)

```bash
uv run python scripts/run_matrix.py run \
  --matrix-run-id ar-smoke \
  --engines ar-qwen3-8b-instruct \
  --sample-size 20 --sample-seed 3
```

**Expected**: Report includes `parse_failure_rate` and latency for 100% of attempted examples.

## 9. AnyJev L1 calibration gate

```bash
# Missing/wrong calibration → start fails
./scripts/serve_engine.sh start anyjev-l1
```

**Expected**: Fail closed until `configs/calibration/anyjev_l1_heldout.json` has exactly 200 IDs.

## 10. Optional: ranking-only debug

```bash
uv run python scripts/run_matrix.py run \
  --matrix-run-id debug-rank \
  --engines anyjev-l0 \
  --sample-size 10 --sample-seed 1 \
  --skip-synthesis
```

**Expected**: `synthesis_enabled=false` recorded; no Gemini calls.

## Success checklist

| Check | Criterion |
|-------|-----------|
| SC-001 | Health path per engine config |
| SC-003 | Mock off → no lexical rankings |
| SC-004 | No extractive Gemini fallback |
| SC-005 | Same seed/size → same IDs |
| SC-008 | ≥20-ex smoke ≥95% terminal |
| SC-009 | Sequential variable + partner; e2e Stage 1+2 |
| SC-010 | Default Flash unless overridden |
