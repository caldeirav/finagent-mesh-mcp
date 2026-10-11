# Contract: P0 Evidence CLI

Extends `scripts/run_benchmark.py` (Spec 003 paper CLI). Exact flag names may alias existing ones; behavior below is normative.

## Rebuild analysis (no engines) — S0 / S3 / S4 bootstrap / strata

```bash
uv run python scripts/run_benchmark.py --analysis-from paper-n200-full
```

**MUST**:
- Load matrix + ledger/inspect
- Emit routing classes, pipeline yield, pipeline-averaged S2, MRR@5 columns, strata, win/loss, bootstrap CIs
- Not start System-1 sidecars or call Gemini
- Finish under ~5 minutes for N=200 × ≤12 pairs (SC-008)

## Multi-seed core subset (ranking-only)

```bash
# Seed 42 may reuse published pairs from paper-n200-full
uv run python scripts/run_benchmark.py --real \
  --pairs lux-lux,anyjev-l0-lux,lux-e5,lux-bm25 \
  --records 200 --seed 7 --run-id paper-n200-s7-core

uv run python scripts/run_benchmark.py --real \
  --pairs lux-lux,anyjev-l0-lux,lux-e5,lux-bm25 \
  --records 200 --seed 123 --run-id paper-n200-s123-core
```

**MUST**: Independent samples per seed; ranking-only default under `--real`.

Rollup into analysis via documented merge/rollup path (implementation choice): either extend `--analysis-from` with multi-run inputs or a small helper invoked from analysis rebuild.

## Optional baselines (S2)

```bash
uv run python scripts/run_benchmark.py --real --include-optional \
  --pairs lux-clm-shortlist,one-shot-ar \
  --records 200 --seed 42 --run-id paper-n200-optional
```

**MUST**: Label one-shot as collapsed baseline in report; print shortlist K; leave #1/#2 deferred.

## Synthesis reuse (S1)

```bash
# Normative behavior: attach Gemini to saved rankings for four pairs
uv run python scripts/run_benchmark.py --real --with-synthesis \
  --synthesis-from-rankings paper-n200-full \
  --pairs anyjev-l0-lux,lux-lux,lux-e5,lux-bm25 \
  --run-id paper-n200-full-synth
```

If a dedicated flag is not yet present, an equivalent documented harness resume path that **does not** re-infer Choice/Score is acceptable for P0, provided quickstart records the exact invocation.

**MUST NOT**: Re-run Stage-1/Stage-2 engines for those examples.  
**MUST**: Skip empty/missing-evidence examples with counters; fail closed on Gemini errors.

## Pair lists (frozen for P0)

| Purpose | Pairs |
|---------|--------|
| Core multi-seed | `lux-lux`, `anyjev-l0-lux`, `lux-e5`, `lux-bm25` |
| Synthesis reuse | same four |
| Optional baselines | `lux-clm-shortlist`, `one-shot-ar` |
| Deferred | `lux-clm-ft` (#1), `lux-e5-ce` (#2) |
