# Contract: Matrix pairs / engines (Unsloth track)

## Engines (`configs/engines.yaml`)

| config_id | Role | Notes |
|-----------|------|-------|
| `unsloth-decision-score` | Stage-2 Score | New family/backend; checkpoint via env; fail-closed if missing |
| `bm25-unsloth-score-shortlist-32` | Stage-2 hybrid | BM25 top-32 then Unsloth Score (in-process orchestrator) |

Sidecar deps: hybrid may require no Lux sidecar if Choice is frozen and injected; Unsloth Score may be in-process or local URL — document in CLI contract.

## Pair (v1 required for acceptance)

| pair_id | stage1 | stage2 | role | optional |
|---------|--------|--------|------|----------|
| `lux-unsloth-score` | `noop-frozen-lux` **or** synthetic frozen Choice | `bm25-unsloth-score-shortlist-32` | `trained_decision` | true |

**Behavior**:
- Stage-1 MUST NOT call live Lux by default; Top-1 comes from frozen `paper-n200-full` Lux Choice records.
- Stage-2 shortlist **k=32** (env override allowed, recorded in metadata).
- MUST NOT appear in default required Block A/B set for `run_benchmark.py --real`.

## Deferred (not v1)

- `unsloth-choice-lux`, `anyjev-l0-unsloth-score`

## Resolver rules

- Selecting `lux-unsloth-score` without checkpoint → skip/error with reason (no fallback to Lux Score / E5).
- Default `run_benchmark.py --real` without `--pairs` MUST unchanged vs pre-006.
