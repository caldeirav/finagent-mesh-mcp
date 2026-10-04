# finagent-mesh-mcp

Hybrid financial agent architecture and benchmark harness: LangGraph agentic pipeline, open System-1 decision models, Gemini System-2, MCP tools, MLflow traces, FinAgentBench.

**Target**: HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64, ~128GB unified memory).

## Production: real models × FinAgentBench

`scripts/run_benchmark.py --real` is the single command for a **publishable** multi-engine run.

### What it does

1. Loads HF model ids from `configs/engines.yaml` (Decision-2.0 Kai/Lux, CLM-8B, Laya, Qwen3-8B-Instruct, AnyJev slot).
2. Starts each engine with **`SYSTEMONE_BACKEND=real`** (loads real weights via `torch`/`transformers` — not the lexical sidecar).
3. Runs FinAgentBench end-to-end: Stage 1 → Stage 2 → Gemini Flash synthesis (unless `--skip-synthesis`).
4. Evaluates engines **one variable at a time** with fixed partners (Stage-2=`clm-8b`, Stage-1=`anyjev-l0`).
5. Writes `artifacts/benchmarks/<run-id>.{json,csv,md}` — metrics + interpretation.

`--real` **refuses** to start if:

- `SYSTEMONE_MOCK=1`
- FinAgentBench cannot be fetched or converted (Kaggle credentials / competition rules)

If `data/finagentbench/finagentbench_*.jsonl` is missing, `--real` **downloads from Kaggle and converts** automatically (same as `scripts/download_finagentbench_kaggle.py`). Existing files are skipped. Pass `--no-fetch-data` to disable auto-fetch.

### Prerequisites

```bash
# 1) Real Python stack
./scripts/prepare_real_stack.sh
# Optional: prefetch all HF weights (large)
./scripts/prepare_real_stack.sh --prefetch

# 2) Kaggle credentials in .env (one-time; required the first time data is not local)
#    https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/data
#    Accept rules, then API token: https://www.kaggle.com/settings
# KAGGLE_USERNAME=...
# KAGGLE_KEY=...          # KGAT_ access token is supported

# Optional: prefetch dataset only (idempotent — skips files already on disk)
uv run python scripts/download_finagentbench_kaggle.py

# 3) Configure .env
cp .env.example .env
# FINAGENTBENCH_PATH=./data/finagentbench
# SYSTEMONE_MOCK=0
# SYSTEMONE_BACKEND=real
# GOOGLE_API_KEY=...          # required for Gemini answer scoring
```

### Run (full dataset)

```bash
uv run python scripts/run_benchmark.py --real --run-id prod-full
```

### Run (reproducible subset of the real dump)

Still real models + real labels; only fewer examples:

```bash
uv run python scripts/run_benchmark.py --real --records 200 --seed 42 --run-id prod-200
```

### Engine subset

```bash
uv run python scripts/run_benchmark.py --real \
  --engines decision20-kai,decision20-lux,clm-8b \
  --run-id prod-decision20
```

### Reports

```bash
less artifacts/benchmarks/prod-full.md
```

---

## Python tooling

```bash
uv sync --extra real --group dev
```

## Layout

- `scripts/run_benchmark.py` — production multi-engine benchmark + reports (`--real`)
- `scripts/download_finagentbench_kaggle.py` — fetch + convert ICAIF’25 Kaggle FinAgentBench
- `scripts/convert_kaggle_finagentbench.py` — convert already-downloaded Kaggle JSONL
- `scripts/prepare_real_stack.sh` — install torch/transformers; optional HF prefetch
- `scripts/serve_engine.sh` — start/stop/health (`SYSTEMONE_BACKEND=real|lexical`)
- `configs/engines.yaml` — engine ports, partners, HF model ids
- `src/finagent_mesh/clients/engines/real_infer.py` — Decision-2.0 / embed / AR / CLM inference
- `artifacts/benchmarks/` — JSON / CSV / Markdown outputs

Spec & design: [`specs/002-decision-model-bench/`](specs/002-decision-model-bench/).
