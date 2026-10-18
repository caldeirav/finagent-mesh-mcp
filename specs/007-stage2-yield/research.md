# Research: Stage-2 Yield Recovery (007)

## 1. Where to implement type fallback

**Decision**: Implement ordered Choice fallback inside `run_stage2` (`src/finagent_mesh/agent/nodes/stage2.py`), gated by a pair/run flag (e.g. `yield_recovery: true` on matrix pair metadata or harness config), not a separate graph node.

**Rationale**: Empty pools are detected only after type filtering (`chunks = [c for c in … if c.doc_type == top1]`). Stage-1 already returns full `ordered_ids`. Centralizing in Stage-2 keeps Choice engines (live Lux, frozen Lux, AnyJev) unchanged and preserves constitution VII (Choice then Score).

**Alternatives considered**:
- New LangGraph node between Stage-1 and Stage-2 — more plumbing for the same filter loop.
- Re-run Choice after empty — rejected (spec: use existing ranking; frozen S1 must not re-infer).
- Multi-type union pool — rejected (spec clarifications: ordered single-type fallback only).

## 2. Selecting the fallback type

**Decision**: When Top-1 pool is empty and recovery is enabled, iterate `stage1.ordered_ids` (full menu), skip types with zero chunks, take the **first non-empty**. Never consult gold Stage-1 labels. If none non-empty → keep `empty_top1_chunks` / fail closed.

**Rationale**: Matches clarify answers (full exhaust + first-non-empty + no gold peek). Production agents lack gold; bench must not cheat.

**Alternatives considered**: Cap at rank-2/3; prefer gold among non-empty — rejected in clarify.

## 3. Dual empty / yield metrics

**Decision**:
- **Original Top-1 empty**: True iff the Choice Top-1 type alone has zero chunks (computable even when recovery later succeeds). Persist `original_top1_doc_type` + `original_top1_empty` on ranking payloads.
- **Post-recovery empty / pipeline yield**: Based on whether Stage-2 produced `ordered_ids` after optional fallback (`effective_doc_type` may differ).
- SC-001/SC-002 success uses **post-recovery** empty and pipeline figures; reports still show original Top-1 empty for baseline comparison.

**Rationale**: Clarify Option A. Without dual metrics, recovery cannot improve “empty-Top-1 rate” if that rate is defined only on original Top-1.

**Alternatives considered**: Replace primary with post-recovery only; keep only original — both rejected.

## 4. Dual conditional Stage-2 metrics

**Decision**:
- Keep **`stage2_*_given_top1`** meaning = conditioned on **original Choice Top-1 ∈ gold** (published semantics).
- Add **`stage2_*_given_effective_type`** (or similarly named) when `effective_doc_type` is set, conditioned on effective type ∈ gold.
- Analysis labels must not conflate the two series.

**Rationale**: Clarify Option B. Avoid inflating “conditional” by redefining Top-1 after fallback.

**Alternatives considered**: Redefine conditional to effective only; suppress conditional on recovery runs — rejected.

## 5. Routing classes with fallback

**Decision**: Extend routing accounting with an explicit **`fallback_used`** flag (and optional class or sub-count). Keep existing mutually exclusive classes evaluated primarily on **original** Top-1 correctness vs empty/scored **post-recovery** outcome, documented in contracts so “correct_top1_empty” can become scored after recovery while original Top-1 remains correct+empty for the type itself.

**Practical rule for v1**:
- `top1_doc_type` in payloads remains **original Choice Top-1** for recall/OFR compatibility.
- `effective_doc_type` / `yield_recovery` fields describe Stage-2 pool.
- Routing class table adds columns or footnote: `n_fallback_scored`, `n_fallback_still_empty`.

**Rationale**: Spec FR-009; preserve reconciliation with published routing narrative.

**Alternatives considered**: Overwrite `top1_doc_type` with effective type — breaks Top-1 recall vs paper.

## 6. Acceptance pairs and artifact stems

**Decision**:
- Optional pair **`lux-lux-yield`**: live or frozen Lux Choice + Lux Score, `yield_recovery: true` (twin of `lux-lux`).
- Optional pair **`lux-unsloth-score-yield`**: frozen Lux Choice + BM25 k=32 → Unsloth Score, recovery on (twin of `lux-unsloth-score`).
- Run ids / artifact stems MUST use `yield-` prefix or `-yield` suffix (e.g. `yield-paper-n200-lux`, `yield-unsloth-score-paper-n200`); path guards mirror 006 immutability for `paper-*` and `unsloth-score-paper-n200*`.

**Rationale**: Clarify Option C (both paths). Distinct stems prevent accidental overwrite.

**Alternatives considered**: Global CLI flag only without new pairs — harder to keep default matrix clean; still allow a flag that pairs set.

## 7. Enabling recovery without changing defaults

**Decision**: Pair catalog field `yield_recovery: true` (engines.yaml) + harness/MatrixRunner plumbing; default pairs leave it false/absent. `run_unsloth_eval.py` gains `--yield-recovery` that selects or annotates the yield Unsloth pair / run id.

**Rationale**: Spec FR-003 (default off) and FR-007 (new identifiers).

## 8. Frozen Stage-1 ordered lists

**Decision**: Require frozen records to carry full `stage1_ordered_ids` (already loaded in 006). If only Top-1 present, degrade gracefully: recovery cannot walk ranks → behave as no recovery for that example and log a warning count.

**Rationale**: FR-010; frozen path must not re-call Lux GPU.

## 9. Out of scope (confirmed)

- Corpus re-indexing / dump repair
- Multi-type union scoring
- Answer synthesis / LLM-as-judge (#13 / #4)
- Latency ladder (#11)
- Multi-seed (#14)
- Choice FT (#9)
