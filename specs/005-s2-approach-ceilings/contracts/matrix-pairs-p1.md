# Contract: P1 matrix pairs and engines

## Engines to add (`configs/engines.yaml`)

```yaml
- config_id: lux-score-shortlist-32
  family: hybrid-ir
  primitives: [score]
  primary_stages: [stage2]
  backend: lux_shortlist
  shortlist_k: 32
  shortlist_method: bm25
  scorer: decision20-lux
  is_heavy_gpu: false
  is_light_edge: false

- config_id: e5-ce-shortlist-32
  family: hybrid-ir
  primitives: [score]
  primary_stages: [stage2]
  backend: e5_ce_shortlist
  shortlist_k: 32
  shortlist_method: e5
  reranker: cross-encoder
  weights_ref: ${CE_WEIGHTS:-cross-encoder/ms-marco-MiniLM-L6-v2}
  is_heavy_gpu: false
  is_light_edge: false
```

## Pairs to add

| pair_id | stage1 | stage2 | optional | role |
|---------|--------|--------|----------|------|
| anyjev-l0-e5 | anyjev-l0 | e5-base | true | champion |
| anyjev-l0-bm25 | anyjev-l0 | bm25-stage2 | true | champion |
| lux-lux-shortlist | decision20-lux | lux-score-shortlist-32 | true | optional |
| lux-e5-ce | decision20-lux | e5-ce-shortlist-32 | true | ir_ceiling |

## Deferred

- Keep `lux-clm-ft` → https://github.com/caldeirav/finagent-mesh-mcp/issues/1
- **Remove** `lux-e5-ce` from `deferred_pairs` (now runnable)

## Resolver rules

- Default `--real`: required Spec 003 pairs only (unchanged).
- `--include-optional`: may include existing optionals **and** P1 pairs if marked `optional: true`, **or** document that P1 pairs require explicit `--pairs` only—**plan default**: P1 pairs are `optional: true` and included when `--include-optional` is set; operators may also pass `--pairs anyjev-l0-e5,...` without other optionals.
- Never auto-select `deferred: true`.
