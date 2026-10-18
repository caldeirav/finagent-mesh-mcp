# FinAgentBench Decision-Model Benchmark Report

**Generated**: 2026-10-18T10:02:14.312145+00:00  
**Matrix run ID**: `yield-paper-n200-lux`  
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
| `lux-lux-yield` | completed | `decision20-lux` | `decision20-lux` | 0.8413 | 0.9069 | 0.9683 | 0.2272 | 0.2028 | 0.4057 | — | — | 0.0000 | 200 |

## Leaderboard (this sample)

- **Best Stage-1 ranking (nDCG@5)**: lux-lux-yield (0.8413)
- **Best Stage-2 ranking (nDCG@5)**: lux-lux-yield (0.2272)
- **Best answer quality (token-F1)**: n/a (synthesis disabled)

**Paper note (Block A):** When Stage-2 is held fixed (e.g. all `*-lux` Score), do **not** treat Stage-2 nDCG differences across Choice ablations as a scorer bake-off — prefer Stage-1 metrics and Top-1 recall for those rows. See `*.analysis.md` for Block A/B tables.

### Stage-1 ranking order

1. `lux-lux-yield` — nDCG@5=0.8413

### Stage-2 ranking order

1. `lux-lux-yield` — nDCG@5=0.2272

## Interpretation

1 / 1 engine row(s) completed successfully.

### Reading the scores

- Sample size N=200 (seed=42). Re-run with the same seed to reproduce the example slice.
- Compare **pairs**, not isolated engines. Stage-1 nDCG judges the Choice model; Stage-2 nDCG judges the chunk scorer (and is bounded by Stage-1 recall).
- Paper matrix: **Block A** (`*-lux`) varies Stage-1 Choice with Lux Score fixed; **Block B** (`lux-*`) varies Stage-2 scorers with Lux Choice fixed. `lux-lux` is the shared long-context control; `lux-bm25` / `lux-e5` / `lux-clm` are Score ablations; `kai-lux` / `laya-lux` are latency/edge Choice routers.
- **Champion / compound** pairs (`anyjev-l0-e5`, `anyjev-l0-bm25`) combine AnyJev Choice with E5/BM25 Score — not an orthogonal Block A Score bake-off. Optional P1 ceilings: `lux-lux-shortlist` (BM25→Lux), `lux-e5-ce` (E5→CrossEncoder IR ceiling).
- **Synthesis was disabled** (paper default / ranking-only). Answer EM/F1 are empty. Pass `--with-synthesis` (and set `GOOGLE_API_KEY`) for Gemini answer scoring.

## Selected example IDs

```
dev:chunk-only:q299865e6e67e, dev:q9a5cfe35fecd, dev:q9c255237096a, dev:q8e053e02a010, dev:q4acd5677c3da, dev:qd08d64c0654c, dev:q238a8429d152, dev:qe2edf9d38872, dev:chunk-only:q504aef305d62, dev:q31f6fd1f392c, dev:q4d8ac905167b, dev:q95535bca90c9, dev:q0d51e9ef12aa, dev:q2fe5769567d7, dev:qeccd6f3b9d06, dev:q09b8cfa51b60, dev:q27a01443f529, dev:qff56bedc2f87, dev:q8cc1033cf552, dev:q811679c2d742, dev:qd483c94f1ec6, dev:q2d8eb319367a, dev:qb35a5efa65ce, eval:chunk-only:chunk_q29280e, dev:chunk-only:qb7d1dfae8271, eval:doc_qa9fda3, dev:q3ef7ce37ae77, dev:q05bfc5cb3e17, dev:q99ec5f1aeea5, dev:qb590e4e6d1ec, dev:q1ab49a3f086f, dev:q430300b97e2f, dev:q7eb4e8a11956, dev:q1ff3eed25e64, eval:doc_q0617ad, dev:qfbef9973c7fb, dev:q0e5327ae1aff, dev:qf8cbcec9fec6, dev:q5d75c4f1ac86, dev:q7b42f1295dc1, dev:qf9c15fa46d48, dev:q8b55a229e784, dev:q0b8d55d58be2, dev:q7c284aabbba4, dev:qf5b4bbe60015, dev:qa057a3d428a2, dev:q636b07dd9c11, dev:q4e3318b7d0e9, dev:qf13afdfcadcf, dev:qd5c685de4d7a ...
```

## How to reproduce

```bash
uv run python scripts/run_benchmark.py \
  --run-id yield-paper-n200-lux \
  --pairs lux-lux-yield \
  --records 200 \
  --seed 42 \
  --skip-synthesis \
  --gemini-model gemini-2.5-flash
```

## Artifacts

- Paper analysis (Block A/B tables, findings, record index): `artifacts/benchmarks/yield-paper-n200-lux.analysis.md`
- Analysis JSON: `artifacts/benchmarks/yield-paper-n200-lux.analysis.json`
- Interactive inspect (pair → example labels vs S1/S2 I/O): `artifacts/benchmarks/yield-paper-n200-lux.inspect.html`
- Inspect JSON: `artifacts/benchmarks/yield-paper-n200-lux.inspect.json`
- Matrix JSON / CSV: `artifacts/benchmarks/yield-paper-n200-lux.json`, `artifacts/benchmarks/yield-paper-n200-lux.csv`
- This report: `artifacts/benchmarks/yield-paper-n200-lux.md`

---
*Generated by `scripts/run_benchmark.py`*
