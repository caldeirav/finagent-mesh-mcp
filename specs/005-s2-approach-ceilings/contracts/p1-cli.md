# Contract: P1 ceilings CLI

Extends `scripts/run_benchmark.py` / matrix runner. No new top-level script required.

## Examples

Smoke (S8):

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs anyjev-l0-e5,anyjev-l0-bm25 \
  --records 5 --seed 42 --run-id paper-p1-champ-smoke5
```

Smoke (S2b):

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-lux-shortlist \
  --records 5 --seed 42 --run-id paper-p1-luxshort-smoke5
```

Smoke (S7):

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs lux-e5-ce \
  --records 5 --seed 42 --run-id paper-p1-ce-smoke5
```

Full N=200 (per story or combined):

```bash
uv run python scripts/run_benchmark.py --real --skip-synthesis \
  --pairs anyjev-l0-e5,anyjev-l0-bm25,lux-lux-shortlist,lux-e5-ce \
  --records 200 --seed 42 --run-id paper-p1-ceilings-n200
```

Analysis rebuild:

```bash
uv run python scripts/run_benchmark.py --analysis-from paper-p1-ceilings-n200
```

## Env

| Variable | Default | Meaning |
|----------|---------|---------|
| `LUX_SHORTLIST_K` | `32` | BM25 shortlist size before Lux Score |
| `CE_SHORTLIST_K` | `32` | E5 shortlist size before CE |
| `CE_WEIGHTS` | `cross-encoder/ms-marco-MiniLM-L6-v2` | CrossEncoder model id/path |
| `E5_WEIGHTS` | `intfloat/e5-base-v2` | Unchanged |

## List pairs

`--list-pairs` MUST show new P1 ids; deferred list MUST NOT include `lux-e5-ce` after this feature.
