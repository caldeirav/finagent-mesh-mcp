# Research: Paper-Ready Choice/Score Matrix

**Feature**: `003-choice-score-paper` | **Date**: 2026-10-05

## 1. Matrix shape: Block A / Block B vs CLM cross-product

**Decision**: Replace default `*-clm` cross-product with Block A (Choice varies, Lux Score fixed) and Block B (Score varies, Lux Choice fixed). Physical `lux-lux` runs once and appears in both block tables.

**Rationale**: Smoke runs showed Stage-2 nDCG differences across `*-clm` rows were subset artifacts, not scorer differences. Reviewers need single-factor ablations.

**Alternatives considered**: Keep CLM as universal Stage-2 (rejected: confounds paper); full factorial Choice×Score (rejected: GPU cost, weak narrative).

## 2. Required pair catalog

**Decision**: Stable pair ids:

| pair_id | Block | Stage 1 | Stage 2 | Default |
|---------|-------|---------|---------|---------|
| `lux-lux` | A+B | decision20-lux | decision20-lux | required |
| `anyjev-l0-lux` | A | anyjev-l0 | decision20-lux | required |
| `kai-lux` | A | decision20-kai | decision20-lux | required |
| `laya-lux` | A | laya-modernbert | decision20-lux | required |
| `ar-lux` | A | ar-qwen3-8b-instruct | decision20-lux | required (baseline role; include with Block A) |
| `lux-clm` | B | decision20-lux | clm-8b | required |
| `lux-bm25` | B | decision20-lux | bm25-stage2 | required |
| `lux-e5` | B | decision20-lux | e5-base | required |
| `lux-clm-shortlist` | opt B | decision20-lux | clm-shortlist-32 | optional |
| `one-shot-ar` | opt B | — collapsed — | ar one-shot rank | optional |

**Rationale**: Matches clarified FR-001–003. `ar-lux` is required for Block A generative Choice story (parse failures); `one-shot-ar` is optional Stage-collapse baseline.

**Alternatives considered**: Keep AR optional via `--include-baseline` only (rejected for Block A completeness—AR Choice must appear in the Choice table); make shortlist required (rejected: cost).

## 3. Dense bi-encoder Hub id

**Decision**: `intfloat/e5-base-v2` via `sentence-transformers`, with mandatory prefixes `query: ` / `passage: `. Env override `E5_WEIGHTS`. Score = cosine similarity of mean-pooled embeddings; rank descending.

**Rationale**: Clarification picked E5/GTE-class; e5-base-v2 is the standard English IR baseline, lighter on Nano than large/GTE-Qwen variants, well documented.

**Alternatives considered**: `Alibaba-NLP/gte-base-en-v1.5` (equivalent class; pick one frozen id); `e5-large-v2` (heavier); Qwen3 pooled without CLM heads (rejected: not a classical IR comparator).

## 4. Lexical Stage-2

**Decision**: In-process BM25 (`rank_bm25.BM25Okapi`) over whitespace-tokenized chunk texts for the Top-1 type shortlist after Stage-1. Engine id `bm25-stage2`. No GPU sidecar.

**Rationale**: Classical lexical floor; CPU-only; fits Score primitive without mock System-1.

**Alternatives considered**: Elasticsearch (ops heavy); sidecar lexical from smoke backend (rejected: must not look like SYSTEMONE_MOCK).

## 5. Shortlist + CLM

**Decision**: Optional engine `clm-shortlist-32`: BM25 top-32 on Top-1-type chunks, then existing CLM Score on that shortlist (default k=32, env `CLM_SHORTLIST_K`).

**Rationale**: Clarified in-scope optional; plays to Action Cache list length vs 2k truncation on 100+ chunks.

**Alternatives considered**: E5 shortlist then CLM (deferred to plan tweak if BM25 too weak); k=16/64 (default 32 per spec assumption).

## 6. One-shot generative baseline

**Decision**: Pair `one-shot-ar` uses AR JSON to emit an ordered list of chunk ids over **all** chunks (or a length-capped subset with explicit truncation flag). No Stage-1 type Choice. Labeled `role: baseline_collapsed`. Opt-in via `--include-optional`.

**Rationale**: Motivates two-stage contract; Principle VII exception must be explicit.

**Alternatives considered**: Force AR through Stage-1 then rank all chunks (weaker stuffing contrast).

## 7. Default synthesis policy

**Decision**: `--real` paper path defaults to **ranking-only** (`skip_synthesis=True`). Opt in with `--with-synthesis` (or explicit negation of skip). Analysis report shows answer EM/F1 as “not run” when disabled.

**Rationale**: Clarification FR-014; IR paper tables do not need Gemini cost on every example.

**Alternatives considered**: Keep 002 full-pipeline default (rejected by clarify).

## 8. Reviewer metrics

**Decision**: Compute and persist per pair:

- Stage-1/2 nDCG@5, MAP@5, MRR@5 (existing)
- Stage-1 Top-1 and Top-5 type recall
- Pre-filter / `empty_top1_chunks` rate
- Stage-2 nDCG/MAP/MRR **conditional on Top-1 type correct**
- Latency p50/p95 per stage (from traces)
- GPU memory high-water when available (best-effort `torch.cuda.max_memory_allocated`)
- Option-flip rate (OFR) for AnyJev L0: fraction of examples where argmax type changes under a reversed option order (one extra Choice call or cached dual order)
- Parse-failure rate for AR rows
- Answer EM/F1 only if synthesis ran

**Rationale**: FR-010; separates routing from scoring for paper claims.

**Alternatives considered**: Only overall S2 nDCG (rejected: confounds routing).

## 9. Analysis report

**Decision**: New artifact `artifacts/benchmarks/<run-id>.analysis.md` (and `.analysis.json` machine index) generated after every matrix run and via `--analysis-from <run-id>`. Sections: research questions, Block A table, Block B table, routing-vs-scoring, latency, findings (template rules: never attribute Block A S2 diffs to different scorers), limitations (incl. deferred #1/#2), artifact index with links into `*.inspect.html#pair-<id>-ex-<example_id>`.

**Rationale**: FR-011–013; inspect HTML already exists—analysis is the paper-facing layer.

**Alternatives considered**: Expand interpret.md only (rejected: not structured for Block A/B); separate static site (overkill).

## 10. Deferred work

**Decision**: Do not implement trained CLM heads or cross-encoder rows. Analysis report lists them as deferred with links to GitHub issues [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) and [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2).

**Rationale**: Clarification 2026-10-05.

## 11. Publishable N

**Decision**: `--real` without `--records` defaults to `min(200, dataset_size)` seeded sample (seed default 42 unless overridden). Explicit `--records` overrides (smoke). Report prints N, seed, dataset path/revision.

**Rationale**: SC-003 / FR-014.

**Alternatives considered**: Full 6k default (too slow for iteration); keep requiring explicit `--records` (easy to publish N=10 by mistake).
