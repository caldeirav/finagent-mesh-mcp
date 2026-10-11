# Quickstart: P1 Stage-2 ceilings (005)

Operator path on ZGX Nano / DGX Spark. Prerequisites: same as paper matrix (`SYSTEMONE_MOCK=0`, Podman GPU, `uv sync --extra real` for E5/CE).

## 1. Catalog check

```bash
uv run python scripts/run_benchmark.py --list-pairs
```

Expect: `anyjev-l0-e5`, `anyjev-l0-bm25`, `lux-lux-shortlist`, `lux-e5-ce` listed; `lux-e5-ce` **not** only under deferred.

## 2. Smokes (order: S8 → S2b → S7)

```bash
# S8 champions (AnyJev + in-process IR)
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs anyjev-l0-e5,anyjev-l0-bm25 \
  --records 5 --seed 42 --run-id paper-p1-champ-smoke5

# S2b shortlist Lux (needs Lux Choice + Lux Score sidecars)
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-lux-shortlist \
  --records 5 --seed 42 --run-id paper-p1-luxshort-smoke5

# S7 CE ceiling (Lux Choice + in-process E5/CE)
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-e5-ce \
  --records 5 --seed 42 --run-id paper-p1-ce-smoke5
```

## 3. Full sample

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs anyjev-l0-e5,anyjev-l0-bm25,lux-lux-shortlist,lux-e5-ce \
  --records 200 --seed 42 --run-id paper-p1-ceilings-n200
```

Compare against published `paper-n200-full` references for `anyjev-l0-lux`, `lux-e5`, `lux-bm25`, `lux-lux` (same seed/N).

## 4. Analysis

```bash
uv run python scripts/run_benchmark.py --analysis-from paper-p1-ceilings-n200
```

Check Champion + P1 ceilings sections; limitations show #1 deferred, #2 delivered.

## Env knobs

- `LUX_SHORTLIST_K=32`, `CE_SHORTLIST_K=32`
- `CE_WEIGHTS=cross-encoder/ms-marco-MiniLM-L6-v2`
