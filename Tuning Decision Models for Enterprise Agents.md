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

### A concrete example: same question, better evidence after tuning

Aggregate tables can feel abstract. Here is **one held-out question** from the N=200 paper slice (`dev:q76caada13eca`) where Stage 1 stayed the same and Stage 2 clearly improved after Score tuning. You can open the same case in the inspect reports under `unsloth-score-paper-n200` and `paper-n200-full`.

**The user question**

> What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?

In plain terms: the agent must find filing passages that explain why cash flow and reported earnings can diverge for a timber company—not a housing-outlook chat snippet, and not a call “Operator” line.

**Stage 1 — which document class? (unchanged by tuning)**

The Choice engine (the same frozen Lux decision used in the paper matrix) ranked filing types and picked **10-K** first, with confidence about **48%**, ahead of Earnings (~28%) and 10-Q (~19%). That Top-1 type is among the labels FinAgentBench marks as acceptable for this question, so routing did its job: the agent is looking in the right *kind* of document pool.

Tuning did **not** redo this step. Before and after Score training, Stage 1 is the same freeze—so any quality jump below is from passage ranking, not from a luckier type pick.

**Stage 2 — which passages? (what improved)**

After type filtering, every system ranked the same style of candidate list. What they put at the top differed:

| System | What landed at #1 (paraphrased) | Passage ranking quality on this question\* |
|--------|----------------------------------|-------------------------------------------:|
| **Tuned Score** (BM25 shortlist → trained head) | Management discussing **cash from operations** (~$288M in the quarter, >$1.4B for the year) as they walk financial items | **~0.98** (gold evidence at rank 1) |
| Untuned Lux Score | Literally the call line **“Operator”** | **0.00** (no gold evidence in the top ranks) |
| Dense search (E5) | An analyst Q&A about **housing outlook and ramping production** | **~0.28** (the cash-flow gold chunk only appears around rank 5) |
| Shortlist → untuned Lux | Discussion of **lumber production flexibility** for 2024 | **~0.12** |

\*Stage-2 nDCG@5 on this single example (1.0 = gold evidence ranked ideally; 0 = missed in the top of the list).

So the story for architects is concrete: **same question, same type route, same agent stages**—only the Score engine changed. The tuned head promoted the cash-from-operations discussion that matches the question; the untuned decision Score and the general search baselines preferred boilerplate or adjacent topics.

**System 2 — the generative LLM**

For this comparison run we stayed **ranking-only**: no Gemini (or other) answer synthesis was attached. That is deliberate. We wanted to see whether the agent selected the *right evidence*, not whether a frontier model could write a fluent paragraph. In a full product path you would next feed the top-ranked passages into System 2 to draft an answer—and fail closed if no evidence list exists. Here, System 2 did **nothing**, because we did not turn it on; the win is entirely in the control-plane ranking step.

**Why this example matters**

If you only watched the final chat reply, you might blame “the LLM.” In this case the failure mode of the untuned stack is earlier: Stage 1 was fine, Stage 2 handed the wrong passages (or noise) to whatever would come next. Tuning Score is how we improved that handoff without rewriting MCP tools or the whole agent graph.

---

## 4. Key takeaways and where to explore next

### Takeaways

**Specialize the hop that is actually weak.** In our FinAgentBench agent, open decision models were already good at Stage 1 (picking a filing type). The weaker link was Stage 2 (ranking passages after that pick). We spent training budget on Score, not on rewriting the whole agent or fine-tuning a chat model to “do everything.” After that focused work, the tuned Score path beat both classical search (BM25 / E5) and the untuned Lux Score baseline on the same held-out questions. For architects, the lesson is practical: profile which stage fails users, then improve that stage behind a stable interface.

**Keep a clear agent contract when you train.** We did not collapse the design into one giant generative ranker. Stage 1 still returns a typed Choice, Stage 2 still ranks an explicit candidate list, and tools still sit behind MCP. Training only changed *which Score engine* sits in that slot. That matters for audit trails, fail-closed behavior, and swapping engines later: you can change a checkpoint without redesigning the control plane.

**Protect the evaluation set the way you protect a production regression suite.** The 200 paper questions never appeared in train or validation. Without that holdout, a “big win” on the same ids you trained on is not comparable to the published matrix. Treat the paper slice like a locked golden test pack: train elsewhere, measure here, and refuse silent leakage.

**Track two different health metrics.** *Scored quality* asks: when we have passages to rank, how well do we order them? *Pipeline yield* asks: how often does the agent even get a passage list after routing? Our tuned Score looked strong on the first (~0.61 nDCG) while empty pools still blocked roughly four questions in ten. If product dashboards only show ranking quality, you will over-celebrate models that cannot help empty-pool cases. Log both numbers the way you would log success rate and “dependency unavailable.”

**Prefer labeled supervised training before reinforcement learning.** We used human-style relevance grades (0 / 1 / 2) and ordinary supervised fine-tuning of a decision Score head. That was enough for a large lift. Reinforcement learning (trial-and-error from a reward signal) adds moving parts: what counts as reward, how you sample online, how you stop the model from gaming the metric. Start with clean labels and a fair holdout; add RL only when those basics are stable and you know what “better” means in production.

**Treat smoke runs as engineering checks, not product claims.** A tiny train and a 20-question eval can prove that the pipeline boots. They should not set expectations for stakeholders. Put full-train + full-holdout numbers in design reviews, and keep smoke artifacts clearly labeled.

**Ship trained engines as an optional parallel track.** Published zero-shot baselines (`paper-n200-full`) stayed untouched. The tuned run lives under its own run id and artifact prefix. That is the same discipline you use for canary services: keep the known-good baseline, attach the new engine behind a flag or config, and compare side by side.

### Future exploration

**Train Choice as well—and test combinations carefully.** We only specialized Score. Next experiments can fine-tune a Choice head the same way, then try compounds such as “best open router × tuned Score” or “tuned Choice × tuned Score.” The question for architects is not “train everything,” but whether a second trained hop still pays for itself once Score is strong, versus simply pairing today’s best router with the new Score engine.

**Invest in yield, not only model quality.** Empty Stage-2 pools often mean “we routed to a type that has no chunks in the index,” not “the ranker is dumb.” Fixes look like better corpus coverage, fallback types when the top type is empty, clearer operator alerts, or a second-chance route. Those are product and data-engineering problems. Another training epoch will not invent missing documents.

**Design a latency ladder for interactive agents.** The tuned 27B Score path is much slower than BM25 or E5 on our hardware. A sensible production shape is a ladder: cheap search first, escalate to the tuned Score when policy or low confidence requires it; or train a smaller / distilled Score for the hot path. Architects should set latency budgets explicitly so quality wins do not silently break SLAs.

**Consider reinforcement learning or preference tuning only after the offline story is solid.** Once Score is stable offline, you can explore preference data (humans or a trusted judge picking which ranking is better) or RL-style loops. Do that as an *upgrade path*, not as a replacement for a leakage-safe labeled train set. Without a clear reward tied to Stage-2 ranking quality, RL is easy to mis-aim.

**Add answer-level evaluation when you care about user-facing prose.** Our N=200 claim is about routing and passage ranking. Users still experience the final answer. When you have gold answers or a review process, reuse the saved rankings, run synthesis, and score answers separately. Strong Score is necessary for grounded answers; it is not proof that the paragraph the user reads is correct.

**Confirm the result beyond one 200-question draw.** Seed 42 / N=200 is a solid, comparable paper slice—not the entire FinAgentBench universe. Re-running on other seeds and larger slices reduces the risk that we overfit a lucky sample. Treat broader confirmation the way you would treat load tests on more than one environment before calling a pattern “the standard.”

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
