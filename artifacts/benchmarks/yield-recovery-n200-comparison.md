# Yield recovery vs baselines — plain-language comparison

**Runs:** `yield-paper-n200-lux`, `yield-unsloth-score-paper-n200`  
**Companion analyses:** [`yield-paper-n200-lux.analysis.md`](yield-paper-n200-lux.analysis.md), [`yield-unsloth-score-paper-n200.analysis.md`](yield-unsloth-score-paper-n200.analysis.md)  
**Baselines (unchanged):** [`paper-n200-full.analysis.md`](paper-n200-full.analysis.md), [`unsloth-score-paper-n200.analysis.md`](unsloth-score-paper-n200.analysis.md)

This note explains what **Stage-2 yield recovery** (007 / [#10](https://github.com/caldeirav/finagent-mesh-mcp/issues/10)) changed on the **same N=200, seed 42** holdout — without rewriting published paper or Unsloth baseline files.

---

## What we tested (one sentence)

When Choice Top-1 filing type has **no chunks**, walk the Choice-ranked type list and Score the **first non-empty** pool (never peek at gold labels); measure original vs post-recovery empty rates and how much pipeline Stage-2 quality improves.

---

## Numbers at a glance

| System | Empty (original → post) | Pipeline yield | Fallbacks used | S2 nDCG (scored) | S2 nDCG (pipeline) |
|--------|------------------------:|---------------:|---------------:|-----------------:|-------------------:|
| paper `lux-lux` | 40.5% → 40.5% | ~59.5%\* | — | 0.221 | ~0.12\* |
| **`lux-lux-yield`** | **40.5% → 2.0%** | **94%** | **77** | 0.227 | **0.214** |
| `lux-unsloth-score` (006) | 37.5% → 37.5% | 58.5% | — | 0.606 | 0.354 |
| **`lux-unsloth-score-yield`** | **37.5% → 2.0%** | **94%** | **71** | 0.614 | **0.577** |

\*Paper `lux-lux` empty / yield from published analysis; pipeline series may be missing on older matrix JSON — scored / empty rates are authoritative.

**Unsloth twin vs its own baseline (`unsloth-score-paper-n200`):**

| Metric | Δ | Plain words |
|--------|--:|-------------|
| Empty Top-1 (post-recovery) | **−35.5 pp** | Almost all former empty pools get a Stage-2 list |
| Pipeline yield | **+35.5 pp** (58.5% → 94%) | Agent actually scores passages on ~19/20 questions |
| Pipeline S2 nDCG | **+0.223** (0.354 → 0.577) | End-to-end passage quality jumps because empties no longer force 0 |
| Scored S2 nDCG | **+0.008** (0.606 → 0.614) | Quality on *already ranked* questions barely moves — as expected |

Still empty after full Choice exhaust: **4/200** on both twins (true corpus-limited miss).

---

## How to read this

- **Original empty** must stay ≈ published Lux / frozen Choice empty (~40.5% / ~37.5%). If it moved, recovery changed Choice — it should not.
- **Post-recovery empty** is the yield story. Dropping to **2%** means first-non-empty almost always finds *some* filing type with chunks.
- **Scored** S2 nDCG staying flat means we did not magically improve the Score head; we **rescued questions that previously contributed 0** to the pipeline mean.
- **S2 nDCG \| Top-1** still conditions on **original** Choice Top-1 ∈ gold. **S2 nDCG \| effective type** uses the type actually scored after fallback — do not mix them with published Top-1-conditional numbers.

---

## What stayed the same (important)

- Same 200 holdout ids / seed 42 as `paper-n200-full`.
- Default pairs without `yield_recovery` are unchanged.
- **`paper-n200-full*`** and **`unsloth-score-paper-n200*`** checksums were not rewritten; new stems only under `yield-*`.
- Fallback never consults gold Stage-1 labels when picking the effective type.

---

## Limitations

- First-non-empty may select a **non-gold** filing type; that can raise yield while diluting passage relevance vs an oracle type.
- The remaining **2%** empty is corpus-limited (no Choice-ranked type has chunks).
- Latency: every recovered example still pays a full Stage-2 Score call on the fallback pool.

---

## Bottom line

Yield recovery turns empty Top-1 from a ~**40%** routing/corpus ceiling into ~**2%** residual miss on this holdout, and lifts Unsloth **pipeline** Stage-2 nDCG by ~**0.22** while leaving scored-only quality essentially unchanged. Score fine-tuning (006) and yield recovery (007) solve **different** gaps: better ranking *when* you have a pool vs *having* a pool at all.

Operator guide: [`specs/007-stage2-yield/quickstart.md`](../../specs/007-stage2-yield/quickstart.md).
