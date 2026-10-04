<!--
Sync Impact Report
- Version change: (unset template) → 1.0.0
- Modified principles:
  - [PRINCIPLE_1_NAME] → I. Deterministic Finance Math
  - [PRINCIPLE_2_NAME] → II. Local System-1 First Guardrails
  - [PRINCIPLE_3_NAME] → III. Local ARM64 Container Native
  - [PRINCIPLE_4_NAME] → IV. MCP Protocol Isolation
  - [PRINCIPLE_5_NAME] → V. State Persistence & Auto-Resume
  - (added) VI. Trace Completeness
- Added sections:
  - Technology Stack Constraints
  - Evaluation & Runtime Workflow
  - Governance (concrete rules)
- Removed sections: none (template placeholders replaced)
- Follow-up TODOs: none
-->

# FinAgent Mesh Constitution

## Core Principles

### I. Deterministic Finance Math
No financial math or ratio calculations MAY be performed via direct
model token generation. All numeric evaluations MUST be dispatched to
deterministic MCP Python tool servers.

Rationale: Financial correctness requires reproducible arithmetic;
language-model numerics are non-deterministic and unsuitable as a source
of truth for ratios, valuations, or benchmark scoring.

### II. Local System-1 First Guardrails
Incoming routing, policy checks, and tool choices MUST be evaluated by
open decision models (System 1) running locally inside containerized
engines on local ZGX Nano (DGX Spark) hardware before triggering
frontier models (System 2).

Rationale: Local System-1 gatekeeping reduces unsafe or wasteful
frontier calls, keeps policy enforcement on-premises, and preserves a
clear control plane before expensive System-2 reasoning.

### III. Local ARM64 Container Native
Container builds MUST target native Grace Blackwell ARM64 architecture
using Podman with `nvidia-container-toolkit`.

Rationale: The deployment target is ZGX Nano / DGX Spark; non-native
or Docker-only paths introduce emulation risk and diverge from the
supported GPU container stack.

### IV. MCP Protocol Isolation
All tool calls MUST adhere strictly to Model Context Protocol (MCP)
schemas and pass through AgentGateway for access control and rate
limiting.

Rationale: MCP schemas and AgentGateway form the sole trusted tool
boundary; bypassing them breaks auditability, authorization, and
rate-limit guarantees.

### V. State Persistence & Auto-Resume
The evaluation runner MUST maintain an atomic persistence ledger. If an
execution run crashes or breaks, re-launching the harness MUST
automatically resume from the last uncompleted benchmark task without
duplicating completed work.

Rationale: Long FinAgentBench runs must survive process failure without
lost progress or double-counted results.

### VI. Trace Completeness
Every state transition in LangGraph, decision probability distribution,
and tool execution MUST be recorded in MLflow traces.

Rationale: Agentic evaluation is only trustworthy when every routing
decision and tool side effect is reconstructible from traces.

## Technology Stack Constraints

- Orchestration MUST use LangGraph for agent state machines.
- System-1 inference MUST run on local open models (e.g. CLM-8B,
  AnyJev, vLLM-sr) inside ARM64 containers on ZGX Nano.
- System-2 reasoning MAY use frontier models (e.g. Gemini) only after
  System-1 guardrails approve the escalation.
- Tooling MUST be exposed exclusively as MCP servers; clients MUST
  reach tools only via AgentGateway.
- Observability MUST use MLflow agentic tracing for runs and decisions.
- Python packaging and environments MUST use `uv` (not pip/poetry/
  conda/pyenv as project tooling).
- Container runtime MUST be Podman with `nvidia-container-toolkit` on
  Grace Blackwell ARM64.

## Evaluation & Runtime Workflow

1. Persist benchmark task state atomically before and after each task
   transition in the evaluation ledger.
2. Route each request through local System-1 policy and tool-choice
   models; escalate to System-2 only when System-1 authorizes it.
3. Dispatch all financial numerics to MCP Python tool servers; never
   accept model-generated numbers as evaluation results.
4. Emit MLflow traces for LangGraph transitions, System-1 probability
   distributions, and every MCP tool invocation.
5. On harness restart, resume from the first incomplete ledger entry and
   skip tasks already marked complete.

## Governance

This constitution supersedes conflicting project conventions, prompts,
and ad-hoc implementation choices. Amendments MUST:

1. Update `.specify/memory/constitution.md` with a Sync Impact Report
   for human review (remove the report before committing the amend).
2. Bump `CONSTITUTION_VERSION` using semantic versioning:
   - MAJOR: remove or redefine a principle incompatibly
   - MINOR: add a principle/section or materially expand guidance
   - PATCH: clarifications, wording, or non-semantic refinements
3. Set **Last Amended** to the amendment date (ISO `YYYY-MM-DD`).
4. Document migration impact for any change that invalidates existing
   runners, containers, gateway policies, or trace schemas.

Compliance review expectations:

- Every PR and Spec Kit plan/implement cycle MUST verify alignment with
  all six Core Principles and the Technology Stack Constraints.
- Exceptions MUST be recorded in the relevant spec with explicit
  rationale and an expiration or removal condition.
- Complexity that bypasses MCP, AgentGateway, local System-1, or MLflow
  tracing is forbidden unless this constitution is first amended.

**Version**: 1.0.0 | **Ratified**: 2026-10-04 | **Last Amended**: 2026-10-04
