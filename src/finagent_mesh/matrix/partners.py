"""Stage partners, architecture-true matrix pairs, and legacy one-variable binding."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from finagent_mesh.clients.engines.registry import EngineConfiguration, EngineRegistry


INPROCESS_BACKENDS = frozenset(
    {"bm25_inprocess", "e5_inprocess", "noop_inprocess", "clm_shortlist"}
)


@dataclass(frozen=True)
class FixedStagePartners:
    stage1_partner_id: str = "anyjev-l0"
    stage2_partner_id: str = "clm-8b"

    @classmethod
    def from_registry(cls, registry: EngineRegistry) -> FixedStagePartners:
        return cls(
            stage1_partner_id=registry.partners.get("stage1_partner_id", "anyjev-l0"),
            stage2_partner_id=registry.partners.get("stage2_partner_id", "clm-8b"),
        )


@dataclass(frozen=True)
class StageBinding:
    stage1_config_id: str
    stage2_config_id: str
    variable_config_id: str


@dataclass(frozen=True)
class MatrixPair:
    """One end-to-end FinAgentBench row: Stage-1 Choice × Stage-2 Score."""

    pair_id: str
    stage1_config_id: str
    stage2_config_id: str
    role: str = "production"
    optional: bool = False
    requires_calibration: bool = False
    rationale: str = ""
    blocks: tuple[str, ...] = ()
    collapsed_stages: bool = False
    deferred: bool = False
    deferred_issue: str | None = None

    def as_binding(self) -> StageBinding:
        return StageBinding(
            stage1_config_id=self.stage1_config_id,
            stage2_config_id=self.stage2_config_id,
            variable_config_id=self.pair_id,
        )

    def unique_engines(self) -> list[str]:
        ids: list[str] = []
        for eid in (self.stage1_config_id, self.stage2_config_id):
            if eid and eid not in ids:
                ids.append(eid)
        # Shortlist adapter needs the CLM sidecar, not a separate shortlist process
        if self.stage2_config_id == "clm-shortlist-32" and "clm-8b" not in ids:
            ids.append("clm-8b")
        return ids


@dataclass(frozen=True)
class SkipRecord:
    pair_id: str
    reason: str
    issue_url: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "pair_id": self.pair_id,
            "reason": self.reason,
            "issue_url": self.issue_url,
        }


def bind_matrix_row(
    variable: EngineConfiguration,
    partners: FixedStagePartners,
) -> StageBinding:
    """Legacy ablation: vary one engine; fill the other stage from fixed partners."""
    stages = set(variable.primary_stages)
    vid = variable.config_id
    if "stage1" in stages and "stage2" not in stages:
        return StageBinding(
            stage1_config_id=vid,
            stage2_config_id=partners.stage2_partner_id,
            variable_config_id=vid,
        )
    if "stage2" in stages and "stage1" not in stages:
        return StageBinding(
            stage1_config_id=partners.stage1_partner_id,
            stage2_config_id=vid,
            variable_config_id=vid,
        )
    return StageBinding(
        stage1_config_id=vid,
        stage2_config_id=vid,
        variable_config_id=vid,
    )


def _parse_pair(raw: dict[str, Any], registry: EngineRegistry) -> MatrixPair:
    s1_raw = raw.get("stage1")
    s2_raw = raw.get("stage2")
    s1 = "noop-choice" if s1_raw in (None, "", "null") else str(s1_raw)
    s2 = str(s2_raw)
    registry.get(s1)
    registry.get(s2)
    blocks_raw = raw.get("blocks") or []
    blocks = tuple(str(b) for b in blocks_raw)
    return MatrixPair(
        pair_id=str(raw["pair_id"]),
        stage1_config_id=s1,
        stage2_config_id=s2,
        role=str(raw.get("role") or "production"),
        optional=bool(raw.get("optional", False)),
        requires_calibration=bool(raw.get("requires_calibration", False)),
        rationale=str(raw.get("rationale") or ""),
        blocks=blocks,
        collapsed_stages=bool(raw.get("collapsed_stages", False)),
        deferred=bool(raw.get("deferred", False)),
        deferred_issue=str(raw["deferred_issue"]) if raw.get("deferred_issue") else None,
    )


def pairs_from_registry(registry: EngineRegistry) -> list[MatrixPair]:
    return [_parse_pair(raw, registry) for raw in registry.matrix_pairs]


def deferred_skip_records(registry: EngineRegistry) -> list[SkipRecord]:
    out: list[SkipRecord] = []
    for raw in registry.deferred_pairs:
        out.append(
            SkipRecord(
                pair_id=str(raw["pair_id"]),
                reason="deferred_issue",
                issue_url=str(raw.get("issue") or "") or None,
            )
        )
    return out


def _calibration_ready(cfg: EngineConfiguration, repo_root: Path) -> bool:
    if not cfg.calibration_ref:
        return True
    path = Path(cfg.calibration_ref)
    if not path.is_absolute():
        path = repo_root / path
    if not path.exists():
        return False
    import json

    try:
        ids = json.loads(path.read_text(encoding="utf-8")).get("example_ids") or []
    except (OSError, ValueError):
        return False
    return len(ids) == 200


def is_inprocess_engine(registry: EngineRegistry, config_id: str) -> bool:
    if not config_id:
        return True
    cfg = registry.get(config_id)
    # clm_shortlist is hybrid: decide() is in-process orchestration but needs CLM sidecar
    if cfg.backend == "clm_shortlist" or cfg.family == "hybrid-ir":
        return True
    return cfg.backend in INPROCESS_BACKENDS or cfg.family in {
        "lexical-ir",
        "dense-ir",
        "noop",
    }


def resolve_matrix_pairs(
    registry: EngineRegistry,
    *,
    pair_ids: list[str] | None = None,
    engines: list[str] | None = None,
    include_baseline: bool = False,
    include_optional: bool = False,
    repo_root: Path | None = None,
) -> list[MatrixPair]:
    """Select architecture-true pairs, or fall back to one-variable partner binding.

    Default: required (`optional=false`) pairs. Optional rows need ``include_optional``.
    Deferred catalog entries are never selected. ``lux-lux`` appears once even if in A+B.
    """
    root = repo_root or Path.cwd()
    partners = FixedStagePartners.from_registry(registry)
    catalog = pairs_from_registry(registry)

    if engines:
        out: list[MatrixPair] = []
        for eid in engines:
            cfg = registry.get(eid)
            binding = bind_matrix_row(cfg, partners)
            out.append(
                MatrixPair(
                    pair_id=eid,
                    stage1_config_id=binding.stage1_config_id,
                    stage2_config_id=binding.stage2_config_id,
                    role="ablation",
                    rationale="Legacy one-variable row with fixed stage partner.",
                    blocks=(),
                )
            )
        return out

    if not catalog:
        return resolve_matrix_pairs(
            registry,
            engines=list(registry.all_ids()),
            repo_root=root,
        )

    by_id = {p.pair_id: p for p in catalog}
    if pair_ids:
        missing = [p for p in pair_ids if p not in by_id]
        if missing:
            raise KeyError(f"Unknown matrix pair_id(s): {missing}")
        selected = [by_id[p] for p in pair_ids]
        for pair in selected:
            if pair.deferred:
                raise RuntimeError(
                    f"Pair {pair.pair_id} is deferred"
                    + (f" ({pair.deferred_issue})" if pair.deferred_issue else "")
                )
            if pair.requires_calibration:
                cfg = registry.get(pair.stage1_config_id)
                if not _calibration_ready(cfg, root):
                    raise RuntimeError(
                        f"Pair {pair.pair_id} needs a 200-id calibration file "
                        f"at {cfg.calibration_ref}"
                    )
        return selected

    selected: list[MatrixPair] = []
    for pair in catalog:
        if pair.deferred:
            continue
        if pair.optional and not include_optional:
            # Legacy: include_baseline used to unlock AR baseline rows
            if include_baseline and pair.role in {"baseline", "baseline_collapsed"}:
                pass
            else:
                continue
        if pair.requires_calibration:
            cfg = registry.get(pair.stage1_config_id)
            if not _calibration_ready(cfg, root):
                continue
        selected.append(pair)
    return selected
