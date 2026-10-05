# finagent-mesh-mcp

Hybrid **financial agent** stack: LangGraph orchestration, open **System-1 decision models**, Gemini **System-2** synthesis, MCP tools, MLflow traces, and a **FinAgentBench** harness.

**Target hardware**: HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64, ~128GB unified memory). Engines are served **one heavy model at a time**.

---

## Why this benchmark exists

Two research threads meet here.

### 1. FinAgentBench: agentic retrieval in finance

Institutional questions over SEC filings are not a single embedding lookup. Accurate IR in finance needs **document structure** (which filing type?) and **passage-level evidence** (which chunks?), plus domain knowledge that sparse/dense retrievers miss.

[Choi et al., *FinAgentBench*, ACM ICAIF 2025](https://dl.acm.org/doi/10.1145/3768292.3770362) introduce the first large-scale **agentic retrieval** benchmark for that setting:

- **~26K expert-annotated examples** on S&P-500 firms (paper corpus).
- Each item is **two explicit reasoning steps** (so models are not asked to stuff an entire 10-K into one context):
  1. **Document-type ranking** among {DEF14A, 10-K, 10-Q, 8-K, Earnings}.
  2. **Chunk ranking** of passages inside the selected type.
- Metrics: **nDCG@5, MAP@5, MRR@5** at each stage.

The **ACM ICAIF’25 Agentic Retrieval Grand Challenge** shipped a competition slice (~2,400 analyst-curated 2023–2024 filings) on Kaggle. This repo downloads that dump (document + chunk ranking JSONL) and converts it to harness schema.

| Resource | Link |
|---|---|
| Paper (ACM DL) | [doi:10.1145/3768292.3770362](https://dl.acm.org/doi/10.1145/3768292.3770362) |
| UNIST record | [Scholarworks](http://scholarworks.unist.ac.kr/handle/201301/89409) |
| ICAIF’25 challenge brief | [ai4f.org/2025-challenge](https://ai4f.org/2025-challenge) |
| Kaggle data + API | [acm-icaif-25-ai-agentic-retrieval-grand-challenge](https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/data) |

This project’s extra claim is **pipeline-shaped**: Stage 1 and Stage 2 are bound to **typed System-1 primitives**, then Gemini Flash writes the answer from top chunks (**fail-closed** — no extractive fake answers if the API is down).

### 2. Open System-1 decision models (not “another LLM generating JSON”)

Agent control loops that ask a general LLM to *talk* its way into a tool pick or a rank list waste latency on chain-of-thought and JSON boilerplate, and they emit **uncalibrated verbal confidence** (“I am 90% sure”). Specialized **System-1** models instead score a shared *state* against an explicit schema and return a **probability vector in one (or few) forward passes**.

TypeSafe’s hosted **Jev** popularized the contract (`Choice` / `Noul` / `Score`). The open ecosystem that followed is surveyed in this repo’s [`Architectural Foundations for Open Decision Models.md`](Architectural%20Foundations%20for%20Open%20Decision%20Models.md) (taxonomy, failure modes, JevBench-style numbers, citations).

FinAgentBench maps onto that contract almost one-to-one:

| Pipeline stage | FinAgentBench job | System-1 primitive | Architectural implication |
|---|---|---|---|
| **Stage 1** | Rank 5 filing types | **Choice** (small *K*, mutually exclusive) | Calibrated categorical routing. Option-**order bias** is real on list-shaped Choice (AnyJev L0). Compact encoders have enough tokens for five short labels. **Wrong Top-1 is a recall ceiling**: Stage 2 never sees the right chunks ([pre-filtering recall](Architectural%20Foundations%20for%20Open%20Decision%20Models.md)). |
| **Stage 2** | Rank long enumerated passages | **Score** / metric matching | Dual-encoder **Action Cache** (CLM), BM25/E5 baselines, or Lux **ordinal Score** (2–10 relevance levels, pointwise over passages — Decision-2.0 Score is *not* a list of chunk texts). Lux’s 16k window is the long-context Score control. |
| **System 2** | Answer from evidence | Gemini Flash | Decision models do **not** write prose; synthesis stays generative and fail-closed. |

We are **not** trying to beat FinAgentBench with a giant instruct model doing both stages in one prompt. We are measuring whether **open decision architectures** — Choice heads, contrastive caches, bidirectional routers, training-free debiasing — actually fit this two-step financial IR loop.

Further reading from the survey: [Jev architecture probes](https://archerhume.com/posts/jevs-architecture-unmasked/), [Decision 1.0/2.0 (vLLM-sr)](https://vllm-sr.ai/blog/decision-models/), [CLM GitHub](https://github.com/Contrastive-LM/CLM), [AnyJev](https://github.com/nokia-applied-research/AnyJev) / [arXiv:2610.00831](https://arxiv.org/html/2610.00831v1), [JevBench](https://github.com/fstandhartinger/jevbench).

---

## Model architectures: selected vs not selected

Figures below are from the survey’s comparison table (JevBench / 54-task Decision suite / latency as published there — **not** FinAgentBench scores). Use them to understand *fit*, then run `--real` for this dataset.

### In the harness (and why)

| Model | Architecture | Params / context | Mechanism | Typical p50 | Survey composite | FinAgent Mesh role |
|---|---|---|---|---|---|---|
| **Decision-2.0 Lux-9B** | Qwen3.5 + Gated DeltaNet hybrid decoder | ~8B / **16,384** | Prompt candidate vectors + shared Choice/Score heads | ~18 ms | **76.94** (54-task) | Shared **Block A Stage-2 Score** and **Block B Stage-1 Choice** (`decision20-lux`). Stage-2 uses native ordinal Score (pointwise relevance), not chunk lists as criteria. Weights: [`vllm-sr/Decision-2.0-Lux-9B`](https://huggingface.co/vllm-sr/Decision-2.0-Lux-9B). |
| **Decision-2.0 Kai-0.6B** | Vela bidirectional encoder | 0.6B / **1,024** | Parallel Choice/Noul/Score heads | **~4.9 ms** | 53.52 (54-task) | **Latency Stage-1 only**. Five filing labels fit; long chunks do not. [`vllm-sr/Decision-2.0-Kai-0.6B`](https://huggingface.co/vllm-sr/Decision-2.0-Kai-0.6B). |
| **CLM-8B** | Frozen Qwen3-8B **dual encoder** + ~40M InfoNCE heads | 8B+heads / **2,048** | Hypersphere match; **Action Cache** of pre-embedded candidates | 15–40 ms cached | Strong on verifier benches (e.g. Terminal-Bench), not JevBench Choice | Default **Stage-2**. Enumerated chunks ≈ cached actions. Not a 5-way taxonomy Choice model. [`Contrastive-LM/CLM-v0.1-8B`](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B), [CLM](https://github.com/Contrastive-LM/CLM). |
| **AnyJev L0 / L1** | Wrapper on a Choice backbone | inherits base | L0: cyclic permutations + mean scores (kills additive **position bias**). L1: temperature scaling on ~200 labels | 150–400 ms (rotations) | Depends on base; L1 ECE ~0.036 on BANKING77 | **Stage-1 Choice** when *K*=5. Implemented as L0 cyclic permutations on the configured Lux backbone. L1 skipped until `configs/calibration/anyjev_l1_heldout.json`. [GitHub](https://github.com/nokia-applied-research/AnyJev). |
| **Laya (ModernBERT)** | Bidirectional MLM + task heads | **421M** / **512** | Full bidirectional attention, Choice/Noul/Score | 5–15 ms | **54.4** JevBench | **Edge Stage-1 only**. CPU-capable; truncates Stage-2 passages. [`ameerhmz5/laya-modernbert-decision-90pct`](https://huggingface.co/ameerhmz5/laya-modernbert-decision-90pct). |
| **Qwen3-8B** | Autoregressive chat | 8B / long | Generate JSON ranks | hundreds of ms–s | N/A (anti-pattern in the survey) | **Baseline** (`--include-baseline`): parse failures + verbal confidence. Hub id [`Qwen/Qwen3-8B`](https://huggingface.co/Qwen/Qwen3-8B) (there is no official `Qwen/Qwen3-8B-Instruct`). |

**Jev 1.x (hosted)** is the closed reference (~10B MoE-class, 64k context, ECE ~0.03, JevBench ~74.4). We do not call the TypeSafe API; open rows are compared against FinAgentBench labels, not against Jev’s black box.

### Out of the default matrix (and why)

| Model | Architecture | Why it is interesting | Why it is **not** a default FinAgentBench row |
|---|---|---|---|
| **Jev (TypeSafe)** | Causal prefill + parallel discriminative heads, RLCD | Defines the System-1 API and calibration bar | Proprietary hosted API; no local ARM64 weights; ordinal **scale compression** and order sensitivity documented in the survey. |
| **djev / DiffusionGemma** | 26B discrete diffusion, ~150 ms, native vision (≤8 frames) | JevBench ~73; multimodal UI/docs | 26B VRAM + specialized diffusion runtime; FinAgentBench here is **text SEC chunks**, not screenshots. |
| **Jeeves** | Chat-template reasoning rollout + pointer head | Hard-task accuracy via internal CoT (~400–1,200 ms) | Latency fights the System-1 pitch; not in `engines.yaml`. Revisit if we add a “slow reasoning Choice” row. |
| **SemIf / OpenJev** | Qwen3.5 causal + optional thinking | Drop-in `/v1/systemone`, consumer GPUs, JevBench ~73 | Overlaps Lux/AnyJev; extra serving stack. |
| **Solomon-27B** | Qwen + LoRA scoring heads | Document-routing calibration story | 27B vs 128GB sequential budget; no packaged adapter yet. |
| **Kev family** | Direct-decision heads on Qwen3.5 0.8B–9B | Open Jev-likes | We already cover the encoder (Kai) and hybrid-decoder (Lux) **Decision-2.0** tracks from the same product line. |
| **Decision-2.0 Lex / Eos / Sol / Nox / Vega** | Encoder (logs) or smaller/larger hybrids | Family completeness | Kai and Lux already span **fast short** vs **accurate long**. Vega-27B is a memory extra. |
| **CLM as Stage 1** | Same dual encoder | — | Five **type names** are Choice, not InfoNCE-over-rich-actions. |
| **Laya or Kai as Stage 2** | Short bidirectional | — | Chunk text exceeds 512 / 1,024 tokens; weak zero-shot vs Lux/CLM. |
| **AnyJev as Stage 2** | Permute every candidate | — | Cost scales with *K*; dozens of chunks undo the latency point. |
| **AR on both stages** | Generate two JSON lists | Easy to wire | Double the anti-pattern (parse + uncalibrated tokens). |

### Default pairs (`configs/engines.yaml` → `matrix_pairs`)

Paper matrix: **Block A** (Choice varies, Lux Score fixed) and **Block B** (Score varies, Lux Choice fixed). Not a CLM cross-product.

| Pair id | Block | Stage 1 | Stage 2 | Default |
|---|---|---|---|---|
| `lux-lux` | A+B | Lux | Lux | Required — shared physical run |
| `anyjev-l0-lux` | A | AnyJev L0 | Lux | Required — OFR reported |
| `kai-lux` / `laya-lux` | A | Kai / Laya | Lux | Required — latency/edge Choice |
| `ar-lux` | A | Qwen3-8B JSON | Lux | Required — generative Choice baseline |
| `lux-clm` / `lux-bm25` / `lux-e5` | B | Lux | CLM / BM25 / E5 | Required Score ablation |
| `lux-clm-shortlist` / `one-shot-ar` | B | Lux / noop | shortlist-CLM / AR | Optional (`--include-optional`) |

`--real` defaults: seeded **N=min(200, dataset)**, **ranking-only** (use `--with-synthesis` for Gemini). Artifacts include `*.analysis.md` (Block A/B + inspect links). Deferred train/CE: issues [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1), [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2).

GPU policy: **sequential exclusive** heavies; keep Lux warm across Block A (shared Score) and Block B (shared Choice).

---

## Production: real models × FinAgentBench

`scripts/run_benchmark.py --real` is the single command for a **publishable** multi-pair run.

### What it does

1. Resolves **Block A/B** pairs from `configs/engines.yaml` (not “one engine + dummy partner” unless you pass `--engines`).
2. Starts each needed engine with **`SYSTEMONE_BACKEND=real`** (HF / Decision-2.0 / CLM / AR / E5 weights — not the lexical sidecar).
3. Allocates ports so Block A can keep Lux Score warm on **:8001** while Stage-1 Choice variants swap on **:8000** (same-engine pairs stay on one port).
4. Runs FinAgentBench: Stage 1 → Stage 2; **ranking-only by default** (Gemini only with `--with-synthesis`).
5. Writes `artifacts/benchmarks/<run-id>.{json,csv,md,analysis.md,inspect.html}`.

`--real` **refuses** to start if `SYSTEMONE_MOCK=1` or FinAgentBench cannot be fetched/converted. Stage 2 CLM is **Qwen3-8B last-token pooling + Contrastive-LM heads** (not Decision-2.0 Kai). Lux Stage-2 Score uses Decision-2.0’s **ordinal** Score API (fixed 4-level relevance rubric per passage).

`--real` **force-restarts** System-1 sidecars (kills leftover processes on ports 8000/8001/8002). Pass `--keep-servers` to reuse a warm engine. You can also run `bash scripts/serve_engine.sh stop-all` by hand.

If `data/finagentbench/finagentbench_*.jsonl` is missing, `--real` **downloads from Kaggle and converts** (same as `scripts/download_finagentbench_kaggle.py`). Existing files are skipped. Pass `--no-fetch-data` to disable auto-fetch.

### Prerequisites

```bash
./scripts/prepare_real_stack.sh
# Optional: prefetch HF weights
./scripts/prepare_real_stack.sh --prefetch

# .env: SYSTEMONE_MOCK=0, SYSTEMONE_BACKEND=real, GOOGLE_API_KEY,
# KAGGLE_USERNAME / KAGGLE_KEY (first download only)
```

Accept Kaggle competition rules, then create an API token at [Kaggle settings](https://www.kaggle.com/settings).

### Run

```bash
# List Block A/B pairs
uv run python scripts/run_benchmark.py --list-pairs

# Default paper matrix (Block A Choice×Lux Score + Block B Lux Choice×Score)
# --real defaults to ranking-only N=min(200); add --with-synthesis for Gemini
uv run python scripts/run_benchmark.py --real --run-id paper-n200

# Smoke (10 examples, ranking-only)
uv run python scripts/run_benchmark.py --real --records 10 --seed 42 --run-id paper-smoke-10

# Highest-value rows if GPU time is scarce
uv run python scripts/run_benchmark.py --real --pairs lux-lux,lux-bm25,kai-lux --run-id paper-core

# Optional shortlist-CLM + one-shot AR stuffing baseline
uv run python scripts/run_benchmark.py --real --include-optional --run-id paper-opt

# Legacy one-variable ablation (fixed S2=clm-8b / S1=anyjev-l0)
uv run python scripts/run_benchmark.py --real --engines decision20-kai,clm-8b --run-id ablation
```

### Reports

```bash
less artifacts/benchmarks/paper-n200.analysis.md   # Block A/B tables + findings
less artifacts/benchmarks/paper-n200.md            # interpret summary
# Open inspect.html: pair → example → expected labels vs S1/S2 I/O
# Rebuild without engines:
#   uv run python scripts/run_benchmark.py --analysis-from paper-n200
#   uv run python scripts/run_benchmark.py --inspect-from paper-n200
```

---

## Python tooling

```bash
uv sync --extra real --group dev
```

## Layout

- `scripts/run_benchmark.py` — production pair matrix + reports (`--real`)
- `configs/engines.yaml` — engines, HF ids, **`matrix_pairs`**
- `scripts/download_finagentbench_kaggle.py` — fetch + convert ICAIF’25 FinAgentBench
- `scripts/prepare_real_stack.sh` — torch/transformers; optional HF prefetch
- `scripts/serve_engine.sh` — start/stop/restart/health/`stop-all` (`SYSTEMONE_BACKEND=real|lexical`)
- `src/finagent_mesh/matrix/inspect.py` — per-example inspect HTML/JSON (labels vs S1/S2 I/O)
- `src/finagent_mesh/clients/engines/real_infer.py` — Decision-2.0 / embed / AR / CLM inference
- `artifacts/benchmarks/` — JSON / CSV / Markdown outputs
- [`Architectural Foundations for Open Decision Models.md`](Architectural%20Foundations%20for%20Open%20Decision%20Models.md) — System-1 survey used above
- Spec & design: [`specs/003-choice-score-paper/`](specs/003-choice-score-paper/) (paper Block A/B); [`specs/002-decision-model-bench/`](specs/002-decision-model-bench/) (serving matrix)
