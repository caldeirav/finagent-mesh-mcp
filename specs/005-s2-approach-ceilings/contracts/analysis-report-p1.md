# Contract: Analysis report P1 ceilings extensions

Extends Spec 003/004 analysis artifacts (`*.analysis.md`, `*.analysis.json`).

## New / updated sections

### Champion / compound (S8)

When any of `anyjev-l0-e5`, `anyjev-l0-bm25` are measured:

| Column | Required |
|--------|----------|
| pair_id | yes |
| S1 nDCG@5, Top-1 recall, empty rate, yield | yes |
| S2 nDCG@5 / MRR@5 (scored) | yes |
| S2 nDCG\|Top-1 | yes |
| S2 nDCG (pipeline) | yes (P0) |
| Δ S2 vs `lux-e5` or `lux-bm25` (same scorer, Lux Choice) | when reference present |
| Δ S2 vs `anyjev-l0-lux` (same Choice, Lux Score) | when reference present |

Narrative MUST state these are **compound** cells, not orthogonal Block A/B.

### P1 ceilings (S2b + S7)

When `lux-lux-shortlist` and/or `lux-e5-ce` measured:

| Column | Required |
|--------|----------|
| pair_id | yes |
| shortlist_k / methods | yes |
| CE model id (for `lux-e5-ce`) | yes |
| S2 nDCG@5 / MRR@5 (scored + conditional Top-1) | yes |
| S2 p50/p95 latency ms | yes when available |
| Compare to `lux-lux`, `lux-e5` | when present in run or linked reference run id |

Label `lux-e5-ce` as **IR ceiling / baseline**.

### Limitations

- MUST link [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) as still deferred (`lux-clm-ft`).
- MUST NOT list [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2) as unimplemented once `lux-e5-ce` is measured; MAY note CE is pretrained zero-shot ceiling.
- MUST NOT claim Lux Score SOTA from champion or CE results alone.

### JSON index

`analysis.json` SHOULD include:

```json
{
  "champion_pairs": ["anyjev-l0-e5", "anyjev-l0-bm25"],
  "p1_ceiling_pairs": ["lux-lux-shortlist", "lux-e5-ce"],
  "deferred": [{"pair_id": "lux-clm-ft", "issue": "https://github.com/caldeirav/finagent-mesh-mcp/issues/1"}]
}
```
