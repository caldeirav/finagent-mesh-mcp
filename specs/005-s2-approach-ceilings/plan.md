# Implementation Plan: Stage-2 Approach Ceilings (S8 + S2b + S7)

**Branch**: `005-s2-approach-ceilings` | **Date**: 2026-10-11 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/005-s2-approach-ceilings/spec.md` (S8 champion AnyJev×E5/BM25; S2b shortlist→Lux Score; S7 E5→CE ceiling closing #2).

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Deliver a short-timeline P1 MVP that can raise Stage-2 / end-to-end evidence on ZGX Nano without training: (S8) catalog + run `anyjev-l0-e5` and `anyjev-l0-bm25`; (S2b) hybrid engine + pair `lux-lux-shortlist` (BM25 top-32 → Lux Score); (S7) promote `lux-e5-ce` from deferred to runnable (E5 shortlist → pretrained cross-encoder). Extend analysis with a **Champion / compound** and **P1 ceilings** section. Default required Block A/B unchanged. Keep #1 deferred; close #2 when S7 acceptance is met. Out of scope: S5/S6/S9, LLM judge (#4), Unsloth decision track (#5).

## Technical Context

**Language/Version**: Python 3.12 (uv-managed `finagent-mesh-mcp`)

**Primary Dependencies**: Existing matrix/harness (`typer`, `httpx`, ledger, MLflow); `rank_bm25` + Lux HTTP Score for S2b; `sentence-transformers` CrossEncoder for S7 (same extra as E5); Decision-2.0 Lux + AnyJev sidecars unchanged

**Storage**: Existing SQLite ledger + `artifacts/benchmarks/` / matrix JSON; extended `*.analysis.md` / `*.analysis.json`

**Testing**: `pytest` unit tests for shortlist-Lux adapter, CE hybrid adapter (mocked models), catalog resolver (champions optional, `lux-e5-ce` not deferred), ports/sidecar deps for `lux-score-shortlist`; analysis section smoke

**Target Platform**: HP ZGX Nano / DGX Spark (Grace Blackwell ARM64, ~128GB unified); sequential exclusive GPU sidecars; E5/CE in-process

**Project Type**: Extension of existing evaluation harness + matrix catalog (not a new app)

**Performance Goals**: Smoke N=5 per new pair <30 minutes wall; full N=200 per new pair within sequential GPU budget (~1–2 weeks calendar for all three stories including analysis)

**Constraints**: Constitution v1.1.0; `SYSTEMONE_MOCK=0` for official runs; fail-closed ranking; no silent engine substitution; default `--real` pair set frozen; #1 stays deferred

**Scale/Scope**: Five new/changed catalog entities: pairs `anyjev-l0-e5`, `anyjev-l0-bm25`, `lux-lux-shortlist`, `lux-e5-ce`; engines `lux-score-shortlist-32`, `e5-ce-shortlist-32` (names may vary slightly if registry style dictates)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Plan alignment |
|-----------|------|----------------|
| I. Deterministic Finance Math | PASS | No calculator changes |
| II. Local System-1 First | PASS | All new pairs are local ranking; no Gemini required |
| III. Local ARM64 Container Native | PASS | Lux/AnyJev remain Podman sidecars; E5/CE in-process like today |
| IV. MCP Protocol Isolation | PASS | No new tool bypass |
| V. State Persistence & Auto-Resume | PASS | Existing ledger resume per pair/eval_run_id |
| VI. Trace Completeness | PASS | Distributions/latency/inspect for new pairs |
| VII. Two-Stage Agentic Retrieval | PASS | All P1 pairs keep Choice→Score; CE labeled ceiling/baseline |

**Post-design re-check**: PASS — hybrids mirror `clm_shortlist` pattern; champions are architecture-true two-stage pairs; Complexity Tracking empty.

## Project Structure

### Documentation (this feature)

```text
specs/005-s2-approach-ceilings/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── matrix-pairs-p1.md
│   ├── p1-cli.md
│   └── analysis-report-p1.md
└── tasks.md
```

### Source Code (repository root — extensions)

```text
configs/engines.yaml              # add pairs + engines; remove lux-e5-ce from deferred_pairs
src/finagent_mesh/clients/engines/
├── lux_shortlist.py              # NEW: BM25 → Lux Score (HTTP)
├── e5_ce_shortlist.py            # NEW: E5 → CrossEncoder
└── registry.py                   # register backends; ports sidecar_deps for lux shortlist → decision20-lux
src/finagent_mesh/matrix/
├── ports.py                      # sidecar_dependencies for lux-score-shortlist → decision20-lux
├── partners.py                   # optional/champion roles; deferred list without lux-e5-ce
├── analysis.py / interpret.py    # Champion + P1 ceilings sections; #2 limitations update
└── runner.py                     # unchanged orchestration if catalog-driven
scripts/run_benchmark.py          # help text for P1 pair examples
tests/unit/
├── test_lux_shortlist.py
├── test_e5_ce_shortlist.py
└── test_partners_p1_ceilings.py
```

**Structure Decision**: Extend existing matrix/engine registry; no new top-level package. Hybrid adapters copy `ClmShortlistAdapter` control flow with different second-stage scorers.

## Complexity Tracking

> No constitution violations. Empty.
