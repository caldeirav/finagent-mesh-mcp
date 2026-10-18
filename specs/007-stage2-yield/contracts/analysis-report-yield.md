# Contract: Analysis report — Yield recovery section

## Placement

For matrix/eval runs that include any `role=yield_recovery` pair (or `yield_recovery` flag), analysis markdown/JSON MUST include a **Yield recovery** section (alongside existing Block A/B / trained track as applicable).

## Required content

1. **Run facts**: N, seed, recovery enabled, pair ids, run id  
2. **Dual empty table**: original Top-1 empty rate vs post-recovery empty rate vs published Lux Choice empty (~40.5% on `paper-n200-full`)  
3. **Pipeline vs scored**: post-recovery pipeline S2 nDCG/MRR and scored-only S2  
4. **Fallback counts**: `n_yield_fallback`, rate, still-empty after exhaust  
5. **Δ vs read-only baselines** (do not edit baseline files):
   - vs `lux-lux` (for Lux twin)
   - vs `unsloth-score-paper-n200` / `lux-unsloth-score` (for Unsloth twin)
6. **Conditional dual series** with clear column headers  
7. **Limitations**: first-non-empty may select non-gold types; corpus-limited empties remain  

## Forbidden

- Overwriting `paper-n200-full*`, `paper-p1-ceilings-n200*`, `unsloth-score-paper-n200*`  
- Presenting effective-type conditional as if it were published Top-1 conditional  
