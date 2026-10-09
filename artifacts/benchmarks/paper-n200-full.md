# FinAgentBench Decision-Model Benchmark Report

**Generated**: 2026-10-09T13:20:14.914917+00:00  
**Matrix run ID**: `paper-n200-full`  
**Dataset**: `data/finagentbench`  
**Sample size**: 200  
**Sample seed**: 42  
**Examples processed**: 200  
**Gemini model**: `gemini-2.5-flash`  
**Synthesis enabled**: False  
**System-1 mock**: False  
**Overall status**: `completed`  

## What this run did

This benchmark evaluates **open System-1 decision engines** on FinAgentBench using the FinAgent Mesh agentic pipeline:

1. **Stage 1 (Choice)** — rank document types for each query.
2. **Stage 2 (Score / Action Cache)** — rank passage chunks from the Top-1 Stage-1 type.
3. **System-2 (optional)** — Gemini synthesizes a final answer from top Stage-2 chunks (fail-closed; no extractive fallback).

Each matrix row is an **architecture-true pair**: Stage 1 is a small-K **Choice** (five filing types) and Stage 2 is **Score** over long enumerated chunks. Default partners remain available for `--engines` ablation (Stage-1 partner=`anyjev-l0`, Stage-2 partner=`clm-8b`; binding=`architecture-pairs`). Stage-1 metrics are attributed to the Stage-1 producer; Stage-2 metrics to the Stage-2 producer.

## Metric definitions

| Metric | Meaning |
|--------|---------|
| **nDCG@5** | Normalized discounted cumulative gain at 5 — ranking quality with position discount |
| **MAP@5** | Mean average precision at 5 — precision across relevant ranks |
| **MRR@5** | Mean reciprocal rank at 5 — how early the first relevant item appears |
| **Answer EM / token-F1** | Exact-match and token overlap vs labeled answers (when synthesis ran) |
| **Parse failure rate** | Share of AR baseline JSON parses that failed |
| **Latency p50/p95** | Decision latency percentiles (when recorded by adapters) |

Higher nDCG / MAP / MRR / answer scores are better. Lower parse-failure and latency are better.

## Results by pair (Stage 1 × Stage 2)

| Pair | Status | Stage-1 producer | Stage-2 producer | S1 nDCG@5 | S1 MAP@5 | S1 MRR@5 | S2 nDCG@5 | S2 MAP@5 | S2 MRR@5 | Ans EM | Ans F1 | Parse fail | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `lux-lux` | completed | `decision20-lux` | `decision20-lux` | 0.8413 | 0.9069 | 0.9683 | 0.2212 | 0.2139 | 0.4053 | — | — | 0.0000 | 200 |
| `anyjev-l0-lux` | completed | `anyjev-l0` | `decision20-lux` | 0.8625 | 0.9114 | 0.9711 | 0.2300 | 0.2151 | 0.4274 | — | — | 0.0000 | 200 |
| `kai-lux` | completed | `decision20-kai` | `decision20-lux` | 0.7830 | 0.8602 | 0.9121 | 0.1975 | 0.1810 | 0.3973 | — | — | 0.0000 | 200 |
| `laya-lux` | completed | `laya-modernbert` | `decision20-lux` | 0.7509 | 0.8548 | 0.9029 | 0.2145 | 0.2160 | 0.4089 | — | — | 0.0000 | 200 |
| `ar-lux` | completed | `ar-qwen3-8b-instruct` | `decision20-lux` | 0.7772 | 0.8609 | 0.8821 | 0.2142 | 0.2067 | 0.4177 | — | — | 0.0000 | 200 |
| `lux-clm` | completed | `decision20-lux` | `clm-8b` | 0.8413 | 0.9069 | 0.9683 | 0.1026 | 0.0794 | 0.1818 | — | — | 0.0000 | 200 |
| `lux-bm25` | completed | `decision20-lux` | `bm25-stage2` | 0.8413 | 0.9069 | 0.9683 | 0.2648 | 0.2347 | 0.4375 | — | — | 0.0000 | 200 |
| `lux-e5` | completed | `decision20-lux` | `e5-base` | 0.8413 | 0.9069 | 0.9683 | 0.2825 | 0.2643 | 0.4959 | — | — | 0.0000 | 200 |

## Leaderboard (this sample)

- **Best Stage-1 ranking (nDCG@5)**: anyjev-l0-lux (0.8625)
- **Best Stage-2 ranking (nDCG@5)**: lux-e5 (0.2825)
- **Best answer quality (token-F1)**: n/a (synthesis disabled)

**Paper note (Block A):** When Stage-2 is held fixed (e.g. all `*-lux` Score), do **not** treat Stage-2 nDCG differences across Choice ablations as a scorer bake-off — prefer Stage-1 metrics and Top-1 recall for those rows. See `*.analysis.md` for Block A/B tables.

### Stage-1 ranking order

1. `anyjev-l0-lux` — nDCG@5=0.8625
2. `lux-bm25` — nDCG@5=0.8413
3. `lux-clm` — nDCG@5=0.8413
4. `lux-e5` — nDCG@5=0.8413
5. `lux-lux` — nDCG@5=0.8413
6. `kai-lux` — nDCG@5=0.7830
7. `ar-lux` — nDCG@5=0.7772
8. `laya-lux` — nDCG@5=0.7509

### Stage-2 ranking order

1. `lux-e5` — nDCG@5=0.2825
2. `lux-bm25` — nDCG@5=0.2648
3. `anyjev-l0-lux` — nDCG@5=0.2300
4. `lux-lux` — nDCG@5=0.2212
5. `laya-lux` — nDCG@5=0.2145
6. `ar-lux` — nDCG@5=0.2142
7. `kai-lux` — nDCG@5=0.1975
8. `lux-clm` — nDCG@5=0.1026

## Interpretation

8 / 8 engine row(s) completed successfully.

### Reading the scores

- Sample size N=200 (seed=42). Re-run with the same seed to reproduce the example slice.
- Compare **pairs**, not isolated engines. Stage-1 nDCG judges the Choice model; Stage-2 nDCG judges the chunk scorer (and is bounded by Stage-1 recall).
- Paper matrix: **Block A** (`*-lux`) varies Stage-1 Choice with Lux Score fixed; **Block B** (`lux-*`) varies Stage-2 scorers with Lux Choice fixed. `lux-lux` is the shared long-context control; `lux-bm25` / `lux-e5` / `lux-clm` are Score ablations; `kai-lux` / `laya-lux` are latency/edge Choice routers.
- **Synthesis was disabled** (paper default / ranking-only). Answer EM/F1 are empty. Pass `--with-synthesis` (and set `GOOGLE_API_KEY`) for Gemini answer scoring.

### Comparative takeaway

On Stage-1 nDCG@5, `anyjev-l0-lux` leads `lux-bm25` by 0.0212. If the gap is small on a tiny sample, re-run with a larger `--records` before drawing product conclusions.

## Selected example IDs

```
dev:chunk-only:q299865e6e67e, dev:q9a5cfe35fecd, dev:q9c255237096a, dev:q8e053e02a010, dev:q4acd5677c3da, dev:qd08d64c0654c, dev:q238a8429d152, dev:qe2edf9d38872, dev:chunk-only:q504aef305d62, dev:q31f6fd1f392c, dev:q4d8ac905167b, dev:q95535bca90c9, dev:q0d51e9ef12aa, dev:q2fe5769567d7, dev:qeccd6f3b9d06, dev:q09b8cfa51b60, dev:q27a01443f529, dev:qff56bedc2f87, dev:q8cc1033cf552, dev:q811679c2d742, dev:qd483c94f1ec6, dev:q2d8eb319367a, dev:qb35a5efa65ce, eval:chunk-only:chunk_q29280e, dev:chunk-only:qb7d1dfae8271, eval:doc_qa9fda3, dev:q3ef7ce37ae77, dev:q05bfc5cb3e17, dev:q99ec5f1aeea5, dev:qb590e4e6d1ec, dev:q1ab49a3f086f, dev:q430300b97e2f, dev:q7eb4e8a11956, dev:q1ff3eed25e64, eval:doc_q0617ad, dev:qfbef9973c7fb, dev:q0e5327ae1aff, dev:qf8cbcec9fec6, dev:q5d75c4f1ac86, dev:q7b42f1295dc1, dev:qf9c15fa46d48, dev:q8b55a229e784, dev:q0b8d55d58be2, dev:q7c284aabbba4, dev:qf5b4bbe60015, dev:qa057a3d428a2, dev:q636b07dd9c11, dev:q4e3318b7d0e9, dev:qf13afdfcadcf, dev:qd5c685de4d7a ...
```

## How to reproduce

```bash
uv run python scripts/run_benchmark.py \
  --run-id paper-n200-full \
  --pairs lux-lux,anyjev-l0-lux,kai-lux,laya-lux,ar-lux,lux-clm,lux-bm25,lux-e5 \
  --records 200 \
  --seed 42 \
  --skip-synthesis \
  --gemini-model gemini-2.5-flash
```

## Artifacts

- Paper analysis (Block A/B tables, findings, record index): `artifacts/benchmarks/paper-n200-full.analysis.md`
- Analysis JSON: `artifacts/benchmarks/paper-n200-full.analysis.json`
- Interactive inspect (pair → example labels vs S1/S2 I/O): `artifacts/benchmarks/paper-n200-full.inspect.html`
- Inspect JSON: `artifacts/benchmarks/paper-n200-full.inspect.json`
- Matrix JSON / CSV: `artifacts/benchmarks/paper-n200-full.json`, `artifacts/benchmarks/paper-n200-full.csv`
- This report: `artifacts/benchmarks/paper-n200-full.md`

---
*Generated by `scripts/run_benchmark.py`*
