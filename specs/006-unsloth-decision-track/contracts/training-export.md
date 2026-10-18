# Contract: FinAgentBench → Unsloth Score export

## Score criteria vocabulary (fixed)

Ordinal Score criteria list (legend indices 0..2) MUST be stable across train and eval, e.g.:

```text
["not relevant", "partially relevant", "highly relevant"]
```

mapped from FinAgentBench chunk relevance grades `{0,1,2}`.

## Row JSONL schema (minimum)

```json
{
  "example_id": "dev:q…",
  "query": "…",
  "gold_doc_types": ["10-K"],
  "candidates": [
    {"id": "chunk…", "text": "…", "doc_type": "10-K", "relevance": 2}
  ],
  "decision": {
    "type": "score",
    "instructions": "Rank passages for answering the query.",
    "criteria": ["not relevant", "partially relevant", "highly relevant"]
  }
}
```

Exact Unsloth `build_dataset` field names MAY adapt at implement time; this contract requires semantic equivalence (query + candidates + graded Score).

## Filters

1. Drop examples with empty gold-type candidate pools (count in report).
2. Cap candidate text length / count for `max_seq_length` (document caps in export metadata).
3. Never include `test_ids` in train/val files.

## Leakage checklist artifact

`leakage_report.json` MUST include:

- `paper_test_ids_count`
- `train_overlap_count` (must be 0)
- `val_overlap_count` (must be 0)
- `content_hash`
