# Contract: Paper Analysis Report

Artifacts (under `artifacts/benchmarks/`):

| File | Purpose |
|------|---------|
| `<run-id>.analysis.md` | Human-readable paper-facing report |
| `<run-id>.analysis.json` | Machine index of sections + artifact links |
| `<run-id>.inspect.html` | Existing per-example investigation UI (linked) |
| `<run-id>.inspect.json` | Existing inspect payload |

## Generation

```bash
# After a matrix run (automatic)
# Or rebuild without engines:
uv run python scripts/run_benchmark.py --analysis-from <run-id>
```

**Behavior**:
1. Load matrix JSON + ledger + inspect JSON for `run-id`.
2. Refuse to invent I/O when an example trace is missing; emit `trace_missing` in the index.
3. Do not start System-1 sidecars or call Gemini.
4. Wall time target: under 5 minutes for N≤200 × ≤12 pairs (SC-006).

## Required Markdown sections (order)

1. **Title + run facts** — run id, N, seed, dataset path, `synthesis_enabled`, timestamp
2. **Research questions** — fixed template:
   - Which Choice head routes filing types (Block A)?
   - How should agents score long passages after type routing (Block B)?
   - Does typed Choice→Score beat one-shot stuffing (optional baseline)?
3. **Block A table** — pairs with block A; columns include S1 nDCG/MAP/MRR, Top-1/Top-5 recall, OFR (if applicable), parse-fail (if applicable), S1 latency p50/p95, **shared S2 engine id** (must be identical across rows)
4. **Block B table** — pairs with block B; columns include S2 nDCG/MAP/MRR overall **and** `*_given_top1`, empty-top1 rate, S2 latency, S1 engine id (must be identical except `one-shot-ar`)
5. **Routing vs scoring** — overall vs conditional S2; pre-filter rates; narrative that wrong Top-1 caps Stage 2
6. **Latency / resources** — p50/p95 per stage; GPU high-water if present
7. **Findings** — bullet list generated from metrics with **guardrails**:
   - MUST NOT claim Block A Stage-2 model differences when S2 partner is fixed
   - MUST label `one-shot-ar` as collapsed-stage baseline
   - MUST state answer EM/F1 as “not run” when synthesis disabled
8. **Limitations / threats to validity** — sample N, zero-shot CLM, E5 not finance-tuned, deferred [#1](https://github.com/caldeirav/finagent-mesh-mcp/issues/1) / [#2](https://github.com/caldeirav/finagent-mesh-mcp/issues/2)
9. **Skipped / deferred pairs** — SkipRecord list with reasons and issue URLs
10. **Artifact index** — for every pair × example: link to inspect anchor

## Inspect link contract

Anchors in inspect HTML MUST be stable:

```text
#pair-<pair_id>-ex-<example_id>
```

Analysis index entries:

```json
{
  "pair_id": "lux-lux",
  "example_id": "…",
  "status": "completed|failed|empty_top1|trace_missing",
  "href": "smoke-10-rank.inspect.html#pair-lux-lux-ex-…"
}
```

Relative hrefs from the analysis file directory.

## Findings guardrail checks (automated)

Before write completes, assert:

- All Block A completed pairs share the same `stage2_engine` string.
- All Block B completed pairs (excluding `one-shot-ar`) share the same `stage1_engine` string.
- If any Block A S2 overall nDCG differs across rows, findings MUST mention subset/routing noise and MUST NOT name different S2 models.
