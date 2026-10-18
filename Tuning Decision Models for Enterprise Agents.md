# Tuning Decision Models for Enterprise Agents

*A short continuation of [`Decision Models for Enterprise Agentic Architecture.md`](Decision%20Models%20for%20Enterprise%20Agentic%20Architecture.md) for developers and architects. Plain-language numbers: [`artifacts/benchmarks/unsloth-score-paper-n200-comparison.md`](artifacts/benchmarks/unsloth-score-paper-n200-comparison.md). Technical matrix: `unsloth-score-paper-n200.analysis.md`.*

---

## 1. Why tune—and what we set out to improve

The earlier note argued that enterprise agents need a **control plane**: typed **Choice** (pick a filing type / tool) and **Score** (rank passages / candidates), with generation only after evidence is selected. On FinAgentBench we already saw that pattern work for **routing**—open decision Choice beat “ask an LLM for JSON”—but **passage scoring** lagged.

On the published N=200 sample (`paper-n200-full`):

- Zero-shot **Lux Score** sat at Stage-2 nDCG@5 ≈ **0.22**.
- Classical **E5** and **BM25** beat it (~0.28 / ~0.26).
- A **BM25 top-32 → Lux Score** shortlist path (`paper-p1-ceilings-n200`) lifted Lux Score to ≈ **0.35**—architecture helped more than swapping routers alone.

So the problem we chose was not “reinvent Choice.” It was: **can we specialize a Score head to FinAgentBench relevance labels, keep the same agent contract (frozen Choice + shortlist + Score), and beat both the untuned decision Score and the best IR baselines on the same holdout—without contaminating published paper artifacts?**

That is a product question as much as a model question. If Score can be trained as a **swap-in engine** behind the same `/v1/systemone` path, architects keep MCP gating, ledgers, and traces, while quality moves with checkpoints instead of prompt rewrites.

---

## 2. How we did it (dataset, training method, and stack)

### Dataset and leakage

We exported FinAgentBench into a decision-training pack (`fab-paper-test-v1`):

- **Test** = exactly the paper matrix’s 200 `selected_example_ids`.
- **Train / val** = remaining labeled examples only.
- Automated **leakage report**: zero overlap between train/val and the paper test ids.

Stage-2 training rows use **gold filing-type** passage pools with relevance grades **0 / 1 / 2** (Score criteria), so the model learns “how relevant is this chunk?” under the type that *should* be correct—not under a noisy live router.

At **eval** time we deliberately use a harder, production-shaped path: **frozen Lux Choice Top-1** from the published run (so Stage-1 matches the paper accounting), then **BM25 shortlist k=32**, then the trained Score head. Training on gold type and evaluating under frozen router Top-1 is intentional: it measures whether the Score head generalizes when the agent’s actual type pick is imperfect—the case you ship.

### Training method (supervised decision FT—not RL yet)

We used Unsloth’s **`FastDecisionModel` + `DecisionTrainer`** path: **supervised QLoRA** on a 4-bit **Qwen3.8-27B** base (`unsloth/Qwen3.8-27B-unsloth-bnb-4bit`), LoRA r=16, producing adapter + joint Score head under `artifacts/unsloth/checkpoints/score-qwen38-r16`.

Important naming clarity for architects:

- This is **not** RL / GRPO / PPO in v1. It is **labeled Score fine-tuning** with a decision (ordinal) head.
- We tried a **smoke** train (1k rows) first, then a **full** train (~2k steps, ~5+ hours on a single GB10-class GPU, calibrate accuracy ≈ 0.95).
- Dependencies live in `uv` (`--extra unsloth`); paper benchmark extras stay separate so zero-shot matrix work does not inherit training stack churn.

### Eval contract

Dedicated CLI `scripts/run_unsloth_eval.py` writes only `unsloth-*` artifacts. Same harness metrics as the paper matrix (Stage-1 / Stage-2 nDCG@5, MRR, empty-Top-1, pipeline yield). Paper files stay read-only baselines for Δ tables.

---

## 3. Results—from a developer / architect point of view

Full N=200 eval after full training (`lux-unsloth-score`):

| Comparator | S2 nDCG (scored) | What it means for a shippable agent |
|------------|-----------------:|-------------------------------------|
| **Tuned Score (this work)** | **0.61** | When the agent has passages to rank, evidence quality jumps hard |
| Untuned Lux Score (`lux-lux`) | 0.22 | Same Choice freeze, **before** Score specialization |
| Best required Block B (`lux-e5`) | 0.28 | Previous “best scorer” on the paper matrix |
| Best shortlist untuned Lux (`lux-lux-shortlist`) | 0.35 | Same BM25→Score *shape*, untuned Lux head |
| Pipeline average (empties = 0) | **0.35** | End-to-end yield after type routing still caps the story |

**Interpretation for people designing agents:**

1. **Score was the right knob.** Holding Choice fixed and specializing Score moved us past both classical IR and the best untuned shortlist Lux path on this holdout. That validates “train the hop that lost,” not “fine-tune the whole chat agent.”

2. **Shortlist remains part of the architecture.** We did not dump millions of chunks into the Score head at eval. BM25 k=32 is still the gate in front of the expensive model—same pattern that already helped Lux in P1, now with a stronger head behind it.

3. **Yield still dominates UX.** Empty Top-1 stayed ~**37–40%**. Tuned Score cannot invent chunks the corpus does not have. Dashboards that only show “ranking quality on scored examples” will look triumphant while users still hit “no evidence” ~4 times in 10. Log **yield** next to nDCG.

4. **Latency is a product trade.** Median Stage-2 for the tuned head is ~**29 s** on this box (large 27B QLoRA path), vs milliseconds for BM25 and sub-second for E5. For interactive agents you may want: BM25/E5 first, escalate to tuned Score when confidence or policy demands it—or distill / shorter shortlists later.

5. **Smoke ≠ ship.** The N=20 smoke on a 1k-row train looked encouraging (~0.40 nDCG) but was not the claim. Full train + full holdout is what you put in a design review.

6. **Parallel track, not silent overwrite.** Architects can keep `paper-n200-full` as the compliance / paper baseline and treat `unsloth-score-paper-n200` as an **optional trained engine**—same ledger and MLflow story, different checkpoint env var.

---

## 4. Key takeaways and where to explore next

### Takeaways

- **Specialize the weak hop.** On FinAgentBench, Choice was already strong open-weight; Score was the bottleneck—and supervised decision fine-tuning moved it past published IR and untuned decision baselines on the same sample.
- **Keep the agent contract.** Frozen Choice + shortlist + Score preserved auditability and MCP-friendly stages; training did not force a one-shot generative ranker.
- **Hold out the paper slice.** Zero leakage vs the published 200 ids is what makes the comparison fair.
- **Measure two numbers:** scored quality (is the scorer good?) and pipeline yield (does the route deliver candidates?). Improving only the first leaves empty-pool pain untouched.
- **SFT before RL.** Labeled Score grades were enough for a large lift; RL is optional complexity until the reward and online loop are clear.

### Future exploration

1. **Trained Choice (and compounds).** Deferred pairs (`unsloth-choice-lux`, AnyJev × trained Score) test whether router FT + Score FT compound—or whether AnyJev + tuned Score is enough.
2. **Yield engineering.** Better type→chunk coverage, fallback types, or “empty pool” recovery policies matter as much as another LoRA epoch.
3. **Latency path.** Distillation, smaller bases, adaptive shortlist K, or “IR first / Score escalate” routing policies for interactive SLAs.
4. **RL / preference later.** Only after a stable offline Score and a clear preference signal (human or judge) that maps to Stage-2 ranks—not as a substitute for leakage-safe SFT.
5. **Answer-level eval.** Reuse rankings with synthesis + human or LLM-as-judge when free-form gold exists; routing/Score wins are necessary but not sufficient for user-facing quality.
6. **Multi-seed / full dump.** Confirm the N=200 seed-42 story on additional draws and larger slices before calling it a general finance Score ceiling.

---

## Pointers

| Artifact | Purpose |
|----------|---------|
| [`Decision Models for Enterprise Agentic Architecture.md`](Decision%20Models%20for%20Enterprise%20Agentic%20Architecture.md) | Prior note: why decision models + MCP |
| [`artifacts/benchmarks/unsloth-score-paper-n200-comparison.md`](artifacts/benchmarks/unsloth-score-paper-n200-comparison.md) | Non-specialist comparison tables |
| `artifacts/benchmarks/unsloth-score-paper-n200.analysis.md` | Harness analysis for the tuned run |
| `artifacts/benchmarks/paper-n200-full.analysis.md` | Untuned matrix / Block B baselines |
| `artifacts/benchmarks/paper-p1-ceilings-n200.analysis.md` | Shortlist / CE ceilings |
| `specs/006-unsloth-decision-track/` | Spec, quickstart, contracts for the training track |
