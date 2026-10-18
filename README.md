# finagent-mesh-mcp

Hybrid **financial agent** stack for evaluating open **System-1 decision models** on [FinAgentBench](https://dl.acm.org/doi/10.1145/3768292.3770362): typed **Choice** (which SEC filing type?) then **Score** / dense / lexical ranking (which passages?), with optional Gemini **System-2** answer synthesis, MCP tools, and MLflow Runs/Traces.

**Target hardware**: HP ZGX Nano / NVIDIA DGX Spark (Grace Blackwell ARM64, ~128GB unified memory). Heavy engines are served **one at a time** (sequential exclusive GPU ports).

---

## What this repo does

Institutional questions over SEC filings need **document structure** and **passage evidence**. This harness:

1. Samples FinAgentBench examples (document-type + chunk labels).
2. Runs a LangGraph agent: Stage-1 Choice → Stage-2 Score → nDCG@5 / MAP@5 / MRR@5 → optional Gemini synthesis + answer EM/F1.
3. Sweeps a **Choice × Score** paper matrix (Block A / Block B) across open decision models and strong baselines.
4. Writes paper-facing analysis, CSV/JSON tables, and per-example inspect HTML, with nested MLflow Runs/Traces for debugging.

**Reading order for the “why”:**

| Doc | Audience | Contents |
|---|---|---|
| [`Decision Models for Enterprise Agentic Architecture.md`](Decision%20Models%20for%20Enterprise%20Agentic%20Architecture.md) | Developers & architects | Short note: agent shape, FinAgentBench, MCP, performance/safety — takeaways from `paper-n200-full` + P1 ceilings |
| [`Tuning Decision Models for Enterprise Agents.md`](Tuning%20Decision%20Models%20for%20Enterprise%20Agents.md) | Developers & architects | Continuation: why/how we specialized Stage-2 Score (006), results vs paper baselines, next steps |
| [`Architectural Foundations for Open Decision Models.md`](Architectural%20Foundations%20for%20Open%20Decision%20Models.md) | Deeper survey | System-1 landscape, trade-offs, failure modes |

---

## Why FinAgentBench

[Choi et al., *FinAgentBench*, ACM ICAIF 2025](https://dl.acm.org/doi/10.1145/3768292.3770362) provide ~26K annotated examples with two explicit retrieval steps and nDCG@5 / MAP@5 / MRR@5. This repo uses the ICAIF’25 challenge dump (~2.4K) from Kaggle.

| Resource | Link |
|---|---|
| Paper (ACM DL) | [doi:10.1145/3768292.3770362](https://dl.acm.org/doi/10.1145/3768292.3770362) |
| UNIST record | [Scholarworks](http://scholarworks.unist.ac.kr/handle/201301/89409) |
| ICAIF’25 challenge | [ai4f.org/2025-challenge](https://ai4f.org/2025-challenge) |
| Kaggle data | [competition data](https://www.kaggle.com/competitions/acm-icaif-25-ai-agentic-retrieval-grand-challenge/data) |

| Pipeline stage | Job | Primitive |
|---|---|---|
| Stage 1 | Rank 5 filing types `{DEF14A, 10-K, 10-Q, 8-K, Earnings}` | **Choice** |
| Stage 2 | Rank passages inside the Top-1 type | **Score** / Action Cache / BM25 / E5 |
| System 2 (optional) | Answer from top-K evidence | Gemini Flash (fail-closed) |

Further reading: [Jev architecture probes](https://archerhume.com/posts/jevs-architecture-unmasked/), [Decision 1.0/2.0](https://vllm-sr.ai/blog/decision-models/), [CLM](https://github.com/Contrastive-LM/CLM), [AnyJev](https://github.com/nokia-applied-research/AnyJev) / [arXiv:2610.00831](https://arxiv.org/html/2610.00831v1), [JevBench](https://github.com/fstandhartinger/jevbench).

---

## How the benchmark is built

**Block A** — Stage-1 **Choice** varies; Stage-2 Lux Score is fixed. Differences in Stage-1 nDCG@5 / Top-1 recall measure routing quality.

**Block B** — Stage-1 Lux Choice is fixed; Stage-2 **Score** (or BM25 / E5 / CLM) varies. Compare overall Stage-2 nDCG@5 (full pipeline) and **S2 nDCG@5|Top-1** (scorer quality when the filing type was correct).

Wrong Top-1 type yields `empty_top1_chunks` — a **routing** failure, not a scorer bug. Those examples contribute 0 to overall S2 nDCG and are excluded from conditional-on-Top-1 metrics.

Default matrix = required pairs in `configs/engines.yaml` (`optional: false`). `--real` defaults to **ranking-only** and **N = min(200, dataset size)**.

```text
MLflow parent Run (matrix run_id)
└─ nested Run (run_id:example_id)
   └─ Trace: finagent_example
      ├─ stage1 Choice → stage2 Score → metrics
      └─ (optional) gemini_synthesize → answer_score
```

---

## Models selected

Survey latency / composite figures are **not** FinAgentBench scores — they guide architectural fit; run `--real` for numbers.

### In the harness

| Model | Architecture | Params / context | FinAgent Mesh role |
|---|---|---|---|
| **Decision-2.0 Lux-9B** | Qwen3.5 + Gated DeltaNet | ~8B / 16k | Shared Block A Score + Block B Choice (`decision20-lux`). [HF](https://huggingface.co/vllm-sr/Decision-2.0-Lux-9B) |
| **Decision-2.0 Kai-0.6B** | Vela encoder | 0.6B / 1k | Fast Stage-1 Choice. [HF](https://huggingface.co/vllm-sr/Decision-2.0-Kai-0.6B) |
| **CLM-8B** | Frozen Qwen3-8B dual encoder + InfoNCE | 8B+ / 2k | Stage-2 Action Cache. [HF](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B) |
| **AnyJev L0** | Cyclic permutations on Lux Choice | inherits | Stage-1 order-bias control. [GitHub](https://github.com/nokia-applied-research/AnyJev) |
| **Laya (ModernBERT)** | Bidirectional MLM heads | 421M / 512 | Edge Stage-1. [HF](https://huggingface.co/ameerhmz5/laya-modernbert-decision-90pct) |
| **Qwen3-8B AR** | Autoregressive JSON | 8B | Generative baseline (`ar-lux`). [HF](https://huggingface.co/Qwen/Qwen3-8B) |
| **BM25 / E5-base** | Lexical / dense | — | Strong Stage-2 baselines |

### Default pairs (`configs/engines.yaml` → `matrix_pairs`)

| Pair id | Block | Stage 1 | Stage 2 | Default |
|---|---|---|---|---|
| `lux-lux` | A+B | Lux | Lux | Required — shared physical run |
| `anyjev-l0-lux` | A | AnyJev L0 | Lux | Required |
| `kai-lux` / `laya-lux` | A | Kai / Laya | Lux | Required |
| `ar-lux` | A | Qwen3-8B JSON | Lux | Required baseline |
| `lux-clm` / `lux-bm25` / `lux-e5` | B | Lux | CLM / BM25 / E5 | Required |
| `lux-clm-shortlist` / `one-shot-ar` | B | Lux / noop | shortlist-CLM / AR | Optional (`--include-optional`) |
| `anyjev-l0-e5` / `anyjev-l0-bm25` | champion | AnyJev L0 | E5 / BM25 | Opt-in P1 (S8) |
| `lux-lux-shortlist` | B optional | Lux | BM25→Lux Score (k=32) | Opt-in P1 (S2b) |
| `lux-e5-ce` | B baseline | Lux | E5→CrossEncoder (k=32) | Opt-in P1 (S7; [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)) |
| `lux-unsloth-score` | trained | frozen Lux | BM25→Unsloth Score (k=32) | Parallel 006 track (`run_unsloth_eval.py`) |
| `lux-lux-yield` / `lux-unsloth-score-yield` | yield | Lux / frozen Lux | Lux / BM25→Unsloth + first-non-empty | Opt-in 007 (`yield_recovery: true`) |

Deferred trained CLM heads: issue [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1).
P1 Stage-2 ceilings (champions, shortlist→Lux, E5→CE): feature [`005-s2-approach-ceilings`](specs/005-s2-approach-ceilings/); measured in `paper-p1-ceilings-n200` (see below).
Trained Score track (Unsloth): feature [`006-unsloth-decision-track`](specs/006-unsloth-decision-track/); measured in `unsloth-score-paper-n200` (see below).

### Out of the default matrix

| Model | Why interesting | Why not default |
|---|---|---|
| Jev (TypeSafe) | Defines the System-1 bar | Hosted / proprietary |
| djev / DiffusionGemma | Multimodal | VRAM + not text-SEC chunks |
| Other Decision-2.0 sizes / Jeeves / SemIf / … | Family completeness | Overlap or memory vs sequential budget |
| CLM as Stage 1 / Laya·Kai as Stage 2 | — | Wrong primitive or context/cost fit |
| **Unsloth Qwen3.8 Decision Score** (006 / [#5](https://github.com/caldeirav/finagent-mesh-mcp/issues/5)) | Trainable Score head comparable to paper matrix | **Parallel stack** — not a Decision-2.0 Lux drop-in; optional `uv` extra + dedicated CLIs |

### Unsloth Score track (006) — high level

After the zero-shot matrix showed **Stage-2 Score** (not Choice) as the weaker hop, feature **006** adds a **parallel trained Score path** that does **not** overwrite paper baselines:

1. **Export** a leakage-safe split: paper N=200 ids are **test-only**; train/val come from the rest of FinAgentBench.
2. **Train** a QLoRA Score head (Unsloth `FastDecisionModel` / `DecisionTrainer` on Qwen3.8-27B) — supervised relevance grades, **not** RL in v1.
3. **Eval** with frozen Lux Choice from `paper-n200-full` + BM25 shortlist k=32 + the trained head (`lux-unsloth-score`), writing only `unsloth-*` artifacts.

Operator guide: [`specs/006-unsloth-decision-track/quickstart.md`](specs/006-unsloth-decision-track/quickstart.md). Architect narrative: [`Tuning Decision Models for Enterprise Agents.md`](Tuning%20Decision%20Models%20for%20Enterprise%20Agents.md). Plain-language vs paper numbers: [`unsloth-score-paper-n200-comparison.md`](artifacts/benchmarks/unsloth-score-paper-n200-comparison.md). Choice train and AnyJev×Unsloth compounds remain deferred past v1.

```bash
# Unsloth fine-tune stack — all deps via uv (pyproject [unsloth] extra):
uv sync --extra real --extra unsloth
# or: bash scripts/install_unsloth_zgx.sh --with-real

uv run python scripts/export_unsloth_dataset.py
uv run python scripts/train_unsloth_score.py --max-train-rows 1000 --dry-run   # or full GPU train
uv run python scripts/run_unsloth_eval.py --real --pairs lux-unsloth-score \
  --checkpoint artifacts/unsloth/checkpoints/<run> --records 20 --run-id unsloth-score-smoke20
```

---

## Results: paper-n200-full (N=200, seed=42)

Merged primary + retry matrix: **8/8 required pairs measured**, ranking-only. Published analysis under `artifacts/benchmarks/` includes **P0 evidence** (routing audit, dual S2, strata, win/loss, bootstrap CIs, multi-seed rollup).

For a **non-metrics walkthrough** of what these numbers mean for agent design (routing vs yield vs passage search vs generation), see [`Decision Models for Enterprise Agentic Architecture.md`](Decision%20Models%20for%20Enterprise%20Agentic%20Architecture.md#what-the-benchmark-showed-developer-takeaways).

### Headline findings

| Question | Winner | Key numbers |
|---|---|---|
| **Best Choice router (Block A)** | `anyjev-l0-lux` | S1 nDCG@5 **0.8625** (+0.021 vs Lux 0.8413); Top-1 recall 95.1%; OFR 9.0% |
| **Best passage scorer (Block B)** | `lux-e5` | S2 nDCG@5 **0.2825** scored-only (+0.061 vs Lux); pipeline-averaged **0.157** |
| **Routing / yield** | Lux Choice | Empty-Top-1 **40.5%**; pipeline yield **59.5%**. Many empties are **correct Top-1 + empty pool** (67/200), not only wrong type — see Routing accounting in the analysis. |

**Block A order (S1 nDCG@5):** AnyJev 0.862 → Lux 0.841 → Kai 0.783 → AR 0.777 → Laya 0.751.

**Block B order (scored-only S2 nDCG@5):** E5 0.282 → BM25 0.265 → Lux Score 0.221 → CLM 0.103. Win/tie/loss vs Lux (nDCG@5, ε=0.01): E5 51/26/34; BM25 51/23/37.

**Multi-seed core (seeds 42 / 7 / 123, four pairs):** AnyJev beats Lux S1 on all three seeds. Across-seed mean S2: E5 ≈ 0.265, BM25 ≈ 0.246, Lux ≈ 0.209 — Block B **order is not seed-stable** (BM25 ≈ E5 on seed 7; BM25 collapses on seed 123). Cite mean + min–max from the Multi-seed summary in the analysis.

**Optional baselines** (`paper-n200-optional`, same N/seed; local artifacts): BM25→CLM shortlist S2 **0.1475** (beats zero-shot CLM 0.103, still behind Lux/E5/BM25); one-shot AR S2 **0.2737** (~E5) as a **collapsed** baseline (~3% AR parse fail).

**Synthesis reuse** (`paper-n200-full-synth`): Gemini attached to saved rankings for anyjev / lux / e5 / bm25 (no Choice/Score re-run). Attempted 119–128 / pair, 0 Gemini fails. **Answer EM/F1 are N/A** — the harness dump has `answer_label: null` on all examples (`skipped_no_label`).

Rebuild analysis (no engines):  
`uv run python scripts/run_benchmark.py --analysis-from paper-n200-full --multi-seed-from paper-n200-s7-core,paper-n200-s123-core`

### Detailed artifacts

| Artifact | Path |
|---|---|
| **Analysis (read this first)** | [`artifacts/benchmarks/paper-n200-full.analysis.md`](artifacts/benchmarks/paper-n200-full.analysis.md) |
| Analysis JSON | [`artifacts/benchmarks/paper-n200-full.analysis.json`](artifacts/benchmarks/paper-n200-full.analysis.json) |
| Matrix tables | [`artifacts/benchmarks/paper-n200-full.json`](artifacts/benchmarks/paper-n200-full.json) · [`.csv`](artifacts/benchmarks/paper-n200-full.csv) · [`.md`](artifacts/benchmarks/paper-n200-full.md) |
| Matrix state | [`artifacts/matrix_runs/paper-n200-full.json`](artifacts/matrix_runs/paper-n200-full.json) |
| Compact inspect (GitHub) | [`artifacts/benchmarks/paper-n200-full.inspect.md`](artifacts/benchmarks/paper-n200-full.inspect.md) · [per-pair pages](artifacts/benchmarks/paper-n200-full.inspect/) |
| Full inspect HTML (download) | [`paper-n200-full.inspect.html`](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) — large; open locally |
| Optional / synth analyses (local) | `paper-n200-optional.analysis.md`, `paper-n200-full-synth.analysis.md` under `artifacts/benchmarks/` |

### P0 evidence commands (re-run / extend)

```bash
# Rebuild published analysis + multi-seed rollup (no GPU)
uv run python scripts/run_benchmark.py --analysis-from paper-n200-full \
  --multi-seed-from paper-n200-s7-core,paper-n200-s123-core

# Optional baselines (ranking-only)
uv run python scripts/run_benchmark.py --real --include-optional \
  --pairs lux-clm-shortlist,one-shot-ar \
  --records 200 --seed 42 --run-id paper-n200-optional

# Synthesis reuse (Gemini only; needs GOOGLE_API_KEY)
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --synthesis-from-rankings paper-n200-full \
  --pairs anyjev-l0-lux,lux-lux,lux-e5,lux-bm25 \
  --run-id paper-n200-full-synth
```

Spec: [`specs/004-paper-p0-evidence/`](specs/004-paper-p0-evidence/). Trained CLM-ft remains deferred [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1).

---

## Results: paper-p1-ceilings-n200 (N=200, seed=42)

P1 Stage-2 approach ceilings on the **same example IDs** as `paper-n200-full` (ranking-only). Matrix state merges the four P1 pairs with published baselines so Champion / P1 Δ columns and bootstrap CIs are filled. Spec: [`005-s2-approach-ceilings`](specs/005-s2-approach-ceilings/).

### Headline findings

| Question | Winner | Key numbers |
|---|---|---|
| **Best Stage-2 scorer (incl. P1)** | `lux-lux-shortlist` | S2 nDCG@5 **0.3517** scored (+0.131 vs lux-lux; bootstrap 95% CI excludes 0); S2\|Top-1 0.3735 |
| **Champion compound (S8)** | `anyjev-l0-e5` | S2 **0.2868** (+0.057 vs anyjev-l0-lux; +0.004 vs lux-e5). `anyjev-l0-bm25` 0.2740 |
| **Pretrained CE “ceiling” (S7)** | does **not** beat E5 | `lux-e5-ce` S2 **0.2496** (−0.033 vs lux-e5; +0.028 vs lux-lux) |

**Takeaway:** BM25 shortlist → Lux Score is the Stage-2 win on this sample. Best Choice × classical IR helps vs Lux Score alone, but barely moves the needle vs Lux Choice × the same IR head. Off-the-shelf CrossEncoder is a useful baseline, not an IR ceiling here.

Rebuild (no engines; baselines already merged into matrix state):

```bash
uv run python scripts/run_benchmark.py --analysis-from paper-p1-ceilings-n200 \
  --multi-seed-from paper-n200-s7-core,paper-n200-s123-core
```

| Artifact | Path |
|---|---|
| **Analysis** | [`artifacts/benchmarks/paper-p1-ceilings-n200.analysis.md`](artifacts/benchmarks/paper-p1-ceilings-n200.analysis.md) |
| Analysis JSON | [`artifacts/benchmarks/paper-p1-ceilings-n200.analysis.json`](artifacts/benchmarks/paper-p1-ceilings-n200.analysis.json) |
| Matrix tables | [`artifacts/benchmarks/paper-p1-ceilings-n200.json`](artifacts/benchmarks/paper-p1-ceilings-n200.json) · [`.csv`](artifacts/benchmarks/paper-p1-ceilings-n200.csv) · [`.md`](artifacts/benchmarks/paper-p1-ceilings-n200.md) |
| Matrix state | [`artifacts/matrix_runs/paper-p1-ceilings-n200.json`](artifacts/matrix_runs/paper-p1-ceilings-n200.json) |
| Compact inspect (GitHub) | [`artifacts/benchmarks/paper-p1-ceilings-n200.inspect.md`](artifacts/benchmarks/paper-p1-ceilings-n200.inspect.md) · [per-pair pages](artifacts/benchmarks/paper-p1-ceilings-n200.inspect/) |
| Full inspect HTML (download) | [`paper-p1-ceilings-n200.inspect.html`](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) — large; open locally |

Full re-run:

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs anyjev-l0-e5,anyjev-l0-bm25,lux-lux-shortlist,lux-e5-ce \
  --records 200 --seed 42 --run-id paper-p1-ceilings-n200
```

---

## Results: unsloth-score-paper-n200 (N=200, seed=42)

Parallel **006** eval on the **same paper holdout ids** as `paper-n200-full` (ranking-only). Stage-1 Lux Choice is **frozen** from the published run; Stage-2 is BM25 top-32 → fully trained Unsloth Score (`score-qwen38-r16`). Paper `paper-n200-full*` / `paper-p1-ceilings-n200*` files are left untouched.

### Headline findings

| Comparator | S2 nDCG@5 (scored) | Notes |
|---|---:|---|
| **`lux-unsloth-score` (tuned)** | **0.606** | MRR 0.794; S2\|Top-1 0.643; pipeline-averaged 0.355 |
| Untuned Lux Score (`lux-lux`) | 0.221 | Pre-tune decision Score baseline |
| Best required Block B (`lux-e5`) | 0.283 | Best zero-shot scorer in `paper-n200-full` |
| Best shortlist peer (`lux-lux-shortlist`) | 0.352 | Same BM25→Score *shape*, untuned Lux head (P1) |

**Takeaway:** specializing Stage-2 Score under a fixed Choice + shortlist contract clearly beats both classical IR and untuned Lux Score on this holdout. Empty-Top-1 remains ~**37–40%** — yield is still an architecture/corpus issue, not fixed by Score FT alone. Latency (~29 s p50 for the 27B QLoRA path) is a product trade vs BM25/E5.

### Yield recovery (007 / [#10](https://github.com/caldeirav/finagent-mesh-mcp/issues/10)) — measured

Opt-in **first-non-empty** Stage-2 type fallback when Choice Top-1 has no chunks. Does **not** overwrite `paper-n200-full*` or `unsloth-score-paper-n200*`. Same N=200 / seed 42 holdout as the paper matrix.

| System | Empty (orig → post) | Yield | Fallbacks | S2 nDCG scored | S2 nDCG pipeline |
|---|---:|---:|---:|---:|---:|
| paper `lux-lux` | 40.5% → 40.5% | ~59.5% | — | 0.221 | — |
| **`lux-lux-yield`** | **40.5% → 2.0%** | **94%** | 77 | 0.227 | 0.214 |
| `lux-unsloth-score` (006) | 37.5% → 37.5% | 58.5% | — | 0.606 | 0.354 |
| **`lux-unsloth-score-yield`** | **37.5% → 2.0%** | **94%** | 71 | 0.614 | **0.577** |

**Takeaway:** yield recovery collapses empty Top-1 from ~**38–40%** to **2%** and lifts Unsloth **pipeline** S2 nDCG by **+0.22**; scored-only quality barely moves (+0.008). Score FT (006) and yield fallback (007) fix different gaps. Caveat: first-non-empty may pick a non-gold filing type.

| Artifact | Path |
|---|---|
| **Plain-language comparison** | [`artifacts/benchmarks/yield-recovery-n200-comparison.md`](artifacts/benchmarks/yield-recovery-n200-comparison.md) |
| Lux twin analysis | [`yield-paper-n200-lux.analysis.md`](artifacts/benchmarks/yield-paper-n200-lux.analysis.md) · [matrix](artifacts/matrix_runs/yield-paper-n200-lux.json) |
| Unsloth twin analysis | [`yield-unsloth-score-paper-n200.analysis.md`](artifacts/benchmarks/yield-unsloth-score-paper-n200.analysis.md) · [matrix](artifacts/matrix_runs/yield-unsloth-score-paper-n200.json) |
| Spec / quickstart | [`specs/007-stage2-yield/`](specs/007-stage2-yield/) · [`quickstart.md`](specs/007-stage2-yield/quickstart.md) |

```bash
# Lux twin
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-lux-yield --records 200 --seed 42 --run-id yield-paper-n200-lux

# Unsloth twin
uv run --extra unsloth python scripts/run_unsloth_eval.py --real --skip-synthesis \
  --pairs lux-unsloth-score-yield --yield-recovery \
  --frozen-stage1-from paper-n200-full \
  --checkpoint artifacts/unsloth/checkpoints/score-qwen38-r16 \
  --records 200 --seed 42 --run-id yield-unsloth-score-paper-n200

# Baseline checksum regression (must be unchanged after yield runs)
sha256sum artifacts/benchmarks/paper-n200-full.json \
          artifacts/benchmarks/unsloth-score-paper-n200.json
```

| Artifact (006 Unsloth Score) | Path |
|---|---|
| **Plain-language comparison** | [`artifacts/benchmarks/unsloth-score-paper-n200-comparison.md`](artifacts/benchmarks/unsloth-score-paper-n200-comparison.md) |
| Harness analysis | [`artifacts/benchmarks/unsloth-score-paper-n200.analysis.md`](artifacts/benchmarks/unsloth-score-paper-n200.analysis.md) |
| Matrix tables | [`artifacts/benchmarks/unsloth-score-paper-n200.json`](artifacts/benchmarks/unsloth-score-paper-n200.json) · [`.csv`](artifacts/benchmarks/unsloth-score-paper-n200.csv) · [`.md`](artifacts/benchmarks/unsloth-score-paper-n200.md) |
| Matrix state | [`artifacts/matrix_runs/unsloth-score-paper-n200.json`](artifacts/matrix_runs/unsloth-score-paper-n200.json) |
| Compact inspect | [`artifacts/benchmarks/unsloth-score-paper-n200.inspect.md`](artifacts/benchmarks/unsloth-score-paper-n200.inspect.md) · [per-pair](artifacts/benchmarks/unsloth-score-paper-n200.inspect/) |
| Architect write-up | [`Tuning Decision Models for Enterprise Agents.md`](Tuning%20Decision%20Models%20for%20Enterprise%20Agents.md) |
| Spec / quickstart | [`specs/006-unsloth-decision-track/`](specs/006-unsloth-decision-track/) · [`quickstart.md`](specs/006-unsloth-decision-track/quickstart.md) |

Full paper-slice eval (after train; resume-safe ledger):

```bash
uv run --extra unsloth python scripts/run_unsloth_eval.py --real --skip-synthesis \
  --pairs lux-unsloth-score \
  --frozen-stage1-from paper-n200-full \
  --checkpoint artifacts/unsloth/checkpoints/score-qwen38-r16 \
  --records 200 --seed 42 \
  --run-id unsloth-score-paper-n200
```

---

## Technical stack

| Layer | Technology | Role |
|---|---|---|
| Orchestration | **LangGraph** (+ LangChain Core) | Per-example agent graph |
| System-1 | Local `/v1/systemone` sidecars | Choice / Score / Action Cache / BM25 / E5 / AR |
| System-2 | **Gemini Flash** via `langchain-google-genai` | Fail-closed synthesis (no extractive fallback) |
| Tools | **MCP** (`mcp-sec-edgar`, `mcp-financial-calculator`) | Optional enrichment |
| Observability | **MLflow 3** nested Runs + GenAI Traces | Metrics + span tree |
| Eval ledger | SQLite | Crash-resume, leases, ranking vs synthesis phases |
| Packaging | **uv** + Python 3.12, Typer, Pydantic, httpx | `scripts/run_benchmark.py` |

Optional `--extra real`: torch, transformers, sentence-transformers, rank-bm25, huggingface-hub.

### Agent flow

```mermaid
flowchart TD
  Q[Query + SEC chunks] --> S1
  S1["stage1 · Choice<br/>rank filing types"] --> S2
  S2["stage2 · Score / Action Cache<br/>rank passages in Top-1 type"] --> M
  M["metrics · nDCG@5 MAP@5 MRR@5"] --> R{skip_synthesis?}
  R -->|yes · ranking-only| END1[End · ranking_complete]
  R -->|no| G["synthesize · Gemini Flash<br/>top-K chunks"]
  G --> A["answer_score · EM + token F1"]
  A --> END2[End · completed]
```

### MLflow

Tracking defaults to **SQLite** (`MLFLOW_TRACKING_URI=sqlite:///mlflow.db`):

```bash
./scripts/mlflow_ui.sh
# http://127.0.0.1:5000 → experiment finagent-mesh → Runs | Traces
```

| Surface | Contents |
|---|---|
| **Runs** (nested per example) | `stage1_*`, `stage2_*`, `empty_top1_chunks`, `gemini_*` |
| **Traces** | `finagent_example` → LangGraph nodes → `systemone_choice` / `systemone_score` → optional `gemini_synthesize` |

Set `MLFLOW_DISABLE_AUTOLOG=1` to disable LangGraph autolog. Migrate old FileStore: `uv run mlflow migrate-filestore --source ./mlruns --target sqlite:///mlflow.db`.

---

## Quick start: smoke test

Use a **new `--run-id`** every smoke so the SQLite ledger does not resume an old run.

### 0. One-time setup

```bash
cp .env.example .env
# Required for --real:
#   SYSTEMONE_MOCK=0
#   SYSTEMONE_BACKEND=real
#   HF_TOKEN=…                 # Hub rate limits
#   GOOGLE_API_KEY=…           # only if --with-synthesis
#   KAGGLE_USERNAME / KAGGLE_KEY  # first FinAgentBench download only
#   MLFLOW_TRACKING_URI=sqlite:///mlflow.db

uv sync --extra real --group dev
./scripts/prepare_real_stack.sh
# Optional weight prefetch:
./scripts/prepare_real_stack.sh --prefetch
```

Create a Hugging Face **read** token at [HF settings/tokens](https://huggingface.co/settings/tokens). For Gemini, set `GOOGLE_API_KEY`. Accept Kaggle competition rules if data is not already under `data/finagentbench/`.

### 1. MLflow UI (separate terminal)

```bash
./scripts/mlflow_ui.sh
```

### 2. Minimal technical smoke (S1 + S2 + Gemini + MLflow)

```bash
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --pairs lux-lux \
  --records 5 --seed 42 \
  --run-id paper-smoke-mlflow-gemini-5
```

**Pass criteria:** CLI exit 0; ranking in inspect HTML; non-empty Gemini synthesis; nested MLflow Runs + Trace with `systemone_*` and `gemini_synthesize`.

Ranking-only smoke:

```bash
uv run python scripts/run_benchmark.py --real \
  --pairs lux-lux --records 5 --seed 42 \
  --run-id paper-smoke-rank-5
```

---

## Full paper run

```bash
uv run python scripts/run_benchmark.py --real --seed 42 --run-id paper-n200
```

With Gemini synthesis on the same sample:

```bash
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --seed 42 --run-id paper-n200-synth
```

**What `--real` does**

1. Resolves required Block A/B pairs from `configs/engines.yaml`.
2. Starts engines with `SYSTEMONE_BACKEND=real` (refuses `SYSTEMONE_MOCK=1`).
3. Force-restarts sidecars on ports 8000/8001/8002 unless `--keep-servers`.
4. Keeps Lux Score warm on **:8001** across Block A while Choice swaps on **:8000**.
5. Auto-fetches FinAgentBench from Kaggle if missing (`--no-fetch-data` to disable).
6. Writes `artifacts/benchmarks/<run-id>.{json,csv,md,analysis.md,analysis.json,inspect.html,inspect.json}`.

GPU policy: sequential exclusive heavies; keep Lux warm across Block A (shared Score) and Block B (shared Choice). Rebuild reports without engines: `--analysis-from <run-id>` / `--inspect-from <run-id>`.

---

## Selective runs

```bash
uv run python scripts/run_benchmark.py --list-pairs
uv run python scripts/run_benchmark.py --list-engines

# Highest-value subset
uv run python scripts/run_benchmark.py --real \
  --pairs lux-lux,lux-bm25,kai-lux \
  --records 20 --seed 42 --run-id paper-core

# Optional Block B rows
uv run python scripts/run_benchmark.py --real --include-optional --run-id paper-opt

# Reuse warm sidecars
uv run python scripts/run_benchmark.py --real --keep-servers \
  --pairs lux-lux --records 5 --seed 42 --run-id warm-reuse

# External server management
uv run python scripts/run_benchmark.py --real --no-manage-servers \
  --pairs lux-lux --records 5 --run-id external-servers

# Rebuild published analysis/inspect from saved matrix state
uv run python scripts/run_benchmark.py --analysis-from paper-n200-full
uv run python scripts/run_benchmark.py --inspect-from paper-n200-full
```

Stop leftovers: `bash scripts/serve_engine.sh stop-all`.

---

## `run_benchmark.py` CLI reference

| Flag | Default | Meaning |
|---|---|---|
| `--real` | off | Real HF models, refuse mock, ranking-only unless `--with-synthesis`, default N=`min(200, dataset)`, force-restart sidecars unless `--keep-servers` |
| `--records` / `-n` | `--real` → 200 (capped); else all | Seeded sample size |
| `--seed` / `-s` | `42` | RNG seed |
| `--run-id` | `bench-YYYYMMDD-HHMMSS` | Matrix run id (ledger + artifact stem) |
| `--pairs` / `-p` | all required Block A/B | Comma-separated `pair_id`s |
| `--engines` / `-e` | — | Legacy ablation; mutually exclusive with `--pairs` |
| `--include-optional` | off | Add `lux-clm-shortlist`, `one-shot-ar` |
| `--with-synthesis` | off | Gemini Flash + answer scoring |
| `--skip-synthesis` | implied by `--real` | Explicit ranking-only |
| `--gemini-model` | `GEMINI_MODEL` / `gemini-2.5-flash` | System-2 model id |
| `--dataset-path` | `FINAGENTBENCH_PATH` | Dataset directory or JSONL |
| `--out-dir` | `artifacts/benchmarks` | Report output directory |
| `--min-examples` | `100` | With `--real`, minimum labeled examples |
| `--fetch-data` / `--no-fetch-data` | fetch on | Kaggle download if missing |
| `--force-restart` | on with `--real` | Kill ports 8000–8002 before the run |
| `--keep-servers` | off | Reuse running sidecars |
| `--no-manage-servers` | off | Do not start/stop engines |
| `--allow-mock` | off | Debug only; illegal with `--real` |
| `--list-pairs` / `--list-engines` | — | Catalog and exit |
| `--analysis-from` / `--inspect-from` | — | Rebuild reports from a saved matrix; no engines |

---

## Layout

- `scripts/run_benchmark.py` — paper Block A/B matrix + reports (`--real`)
- `scripts/mlflow_ui.sh` — MLflow UI (`sqlite:///mlflow.db`)
- `configs/engines.yaml` — engines, HF ids, **`matrix_pairs`**
- `scripts/download_finagentbench_kaggle.py` — fetch + convert ICAIF’25 dump
- `scripts/prepare_real_stack.sh` — torch/transformers; optional HF prefetch
- `scripts/serve_engine.sh` — start/stop/restart/health/`stop-all`
- `src/finagent_mesh/agent/graph.py` — LangGraph pipeline
- `src/finagent_mesh/runtime/harness.py` / `tracing.py` — ledger + MLflow
- `src/finagent_mesh/matrix/` — report, analysis, inspect, merge
- `src/finagent_mesh/clients/engines/real_infer.py` — Decision-2.0 / embed / AR / CLM
- `artifacts/benchmarks/paper-n200-full.*` — published N=200 analysis; compact `.inspect.md` + per-pair pages for GitHub; full `.inspect.html` for download
- `artifacts/benchmarks/paper-p1-ceilings-n200.*` — same pattern for P1 ceilings
- `artifacts/benchmarks/unsloth-score-paper-n200.*` — trained Score track (006); plus [`unsloth-score-paper-n200-comparison.md`](artifacts/benchmarks/unsloth-score-paper-n200-comparison.md)
- `artifacts/benchmarks/yield-*-n200*` / [`yield-recovery-n200-comparison.md`](artifacts/benchmarks/yield-recovery-n200-comparison.md) — Stage-2 yield recovery (007)
- `scripts/export_unsloth_dataset.py` / `train_unsloth_score.py` / `run_unsloth_eval.py` — 006 parallel train/eval CLIs
- Architecture (short): [`Decision Models for Enterprise Agentic Architecture.md`](Decision%20Models%20for%20Enterprise%20Agentic%20Architecture.md) · [`Tuning Decision Models for Enterprise Agents.md`](Tuning%20Decision%20Models%20for%20Enterprise%20Agents.md)
- Survey (long): [`Architectural Foundations for Open Decision Models.md`](Architectural%20Foundations%20for%20Open%20Decision%20Models.md)
- Specs: [`specs/007-stage2-yield/`](specs/007-stage2-yield/) · [`specs/006-unsloth-decision-track/`](specs/006-unsloth-decision-track/) · [`specs/005-s2-approach-ceilings/`](specs/005-s2-approach-ceilings/) · [`specs/003-choice-score-paper/`](specs/003-choice-score-paper/) · [`specs/004-paper-p0-evidence/`](specs/004-paper-p0-evidence/) · [`specs/002-decision-model-bench/`](specs/002-decision-model-bench/) · [`specs/001-finagentbench-harness/`](specs/001-finagentbench-harness/)
