# Tuned Score vs paper baselines — plain-language comparison

**Run:** `unsloth-score-paper-n200`  
**Companion technical analysis:** [`unsloth-score-paper-n200.analysis.md`](unsloth-score-paper-n200.analysis.md)  
**Paper baselines (unchanged):** [`paper-n200-full.analysis.md`](paper-n200-full.analysis.md), [`paper-p1-ceilings-n200.analysis.md`](paper-p1-ceilings-n200.analysis.md)

This note is **additional** to the harness analysis. It explains what we measured and how the **fully tuned** Score model compares to scores you already published on the **same 200 questions**.

---

## What we tested (one sentence)

On the same FinAgentBench sample as the paper matrix (N=200, seed 42), we kept Lux’s **filing-type Choice** frozen, then ranked passages with **BM25 top-32 → our QLoRA-tuned Score head**, and compared that to zero-shot Lux Score, E5, BM25, and the best shortlist ceiling from the earlier P1 run.

---

## Numbers at a glance

Primary metric: **Stage-2 nDCG@5 (scored)** — how well the agent ranks the right passages when it has a non-empty candidate list. Higher is better (0–1).

| System | Role in the story | S2 nDCG (scored) | S2 MRR (scored) | S2 nDCG when Top-1 type correct | Pipeline S2 nDCG\* | Empty Top-1 rate |
|--------|-------------------|-----------------:|----------------:|--------------------------------:|-------------------:|-----------------:|
| **lux-unsloth-score** (this run) | **After full tuning** — BM25 k=32 → trained Score | **0.606** | **0.794** | **0.643** | **0.355** | 37.5% |
| lux-lux | **Before tuning** — zero-shot Decision-2.0 Lux Score (full pool) | 0.221 | 0.405 | 0.233 | 0.123 | 40.5% |
| lux-e5 | Best **required** Block B scorer in `paper-n200-full` | 0.283 | 0.496 | 0.313 | 0.157 | 40.5% |
| lux-bm25 | Strong cheap IR baseline | 0.265 | 0.438 | 0.283 | 0.147 | 40.5% |
| lux-lux-shortlist | Best **shortlist** ceiling in `paper-p1-ceilings-n200` (BM25 k=32 → **untuned** Lux Score) | 0.352 | 0.582 | 0.374 | 0.195 | 40.5% |
| lux-clm | Weak zero-shot stress baseline | 0.103 | 0.182 | 0.107 | 0.057 | 40.5% |

\*Pipeline S2 nDCG averages over **all** 200 questions and treats empty Stage-2 pools as 0.

**Deltas for the tuned model (scored S2 nDCG):**

| Compared to | Δ nDCG | In plain words |
|-------------|-------:|----------------|
| Untuned Lux Score (`lux-lux`) | **+0.385** | Roughly **2.7×** the passage-ranking quality of the pre-tune decision Score head on questions that had candidates |
| Best required Block B (`lux-e5`) | **+0.323** | Beats the previous paper “best scorer” by a large margin |
| Best shortlist peer (`lux-lux-shortlist`) | **+0.254** | Same BM25→Score *pattern*, but the **trained** head beats **untuned** Lux Score after the same shortlist |

---

## How to read “before tuning”

- **Before tuning** here means the published zero-shot **Decision-2.0 Lux Score** path (`lux-lux`): same family of decision engine, **no** FinAgentBench fine-tune.
- The fairest *architectural* peer is **`lux-lux-shortlist`**: also BM25 top-32 then a Score head—but the head is still **untuned Lux**. Our trained run uses the same shortlist idea with a new head.
- We did **not** re-train Lux weights; we trained a **parallel** Score track (`unsloth-decision-score` / Qwen3.8-27B QLoRA) and plugged it into the same agent harness.

Smoke N=20 (`unsloth-score-smoke20`) used a small train subset and is **not** the production claim. For the record only: smoke scored S2 nDCG ≈ **0.40** on 20 ids; full train + full N=200 reached **0.61**.

---

## What stayed the same (important)

- **Same 200 test questions** as `paper-n200-full` (holdout ids; train/val had **zero** overlap with that set).
- **Same Stage-1 Choice freeze** from published Lux rankings — we did **not** re-run Lux Choice GPU inference for this eval.
- **Paper artifact files were not overwritten** (`paper-n200-full*`, `paper-p1-ceilings-n200*`). New outputs live only under `unsloth-score-paper-n200*`.
- **Empty Top-1 rate (~37–40%)** is still mostly a **routing / corpus yield** story: many questions never get a passage list. Tuning Score **cannot** fix “no chunks of that type.” Pipeline metrics (~0.35) are lower than scored metrics (~0.61) for that reason.

---

## Training snapshot (for context)

| Item | Value |
|------|--------|
| Base model | `unsloth/Qwen3.8-27B-unsloth-bnb-4bit` |
| Method | Supervised QLoRA + Unsloth `FastDecisionModel` / `DecisionTrainer` (Score grades 0/1/2) — **not** RL/GRPO in this run |
| Checkpoint | `artifacts/unsloth/checkpoints/score-qwen38-r16` |
| Train steps / loss | 2000 steps, train_loss ≈ 0.158 |
| Calibration (holdout) | accuracy ≈ 0.95, ECE ≈ 0.05 |
| Eval path | frozen Lux Choice → BM25 k=32 → trained Score |
| Wall time (final resume segment) | ~19 min ranking after load for remaining examples; full pair ~1128 s logged for completed pass |

---

## Bottom line

On the published N=200 paper slice, the **fully tuned Score track** clearly beats:

1. the **pre-tune** Lux Score baseline,  
2. the **best required** Block B scorer (E5), and  
3. the **best shortlist** untuned Lux Score ceiling from P1,

while keeping Stage-1 Choice and the test set fixed. The remaining large gap between **scored** (~0.61) and **pipeline** (~0.35) quality is still empty pools after type routing—an agent-architecture problem, not a missing Score epoch.

For a developer/architect narrative of *why* we tuned and what to do next, see [`Tuning Decision Models for Enterprise Agents.md`](../../Tuning%20Decision%20Models%20for%20Enterprise%20Agents.md).
