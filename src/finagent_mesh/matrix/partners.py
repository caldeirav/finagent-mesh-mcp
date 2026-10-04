"""Stage partners, architecture-true matrix pairs, and legacy one-variable binding."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from finagent_mesh.clients.engines.registry import EngineConfiguration, EngineRegistry


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

    def as_binding(self) -> StageBinding:
        return StageBinding(
            stage1_config_id=self.stage1_config_id,
            stage2_config_id=self.stage2_config_id,
            variable_config_id=self.pair_id,
        )

    def unique_engines(self) -> list[str]:
        if self.stage1_config_id == self.stage2_config_id:
            return [self.stage1_config_id]
        return [self.stage1_config_id, self.stage2_config_id]


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


def pairs_from_registry(registry: EngineRegistry) -> list[MatrixPair]:
    rows: list[MatrixPair] = []
    for raw in registry.matrix_pairs:
        s1 = str(raw["stage1"])
        s2 = str(raw["stage2"])
        registry.get(s1)
        registry.get(s2)
        rows.append(
            MatrixPair(
                pair_id=str(raw["pair_id"]),
                stage1_config_id=s1,
                stage2_config_id=s2,
                role=str(raw.get("role") or "production"),
                optional=bool(raw.get("optional", False)),
                requires_calibration=bool(raw.get("requires_calibration", False)),
                rationale=str(raw.get("rationale") or ""),
            )
        )
    return rows


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

    Default: required pairs from ``matrix_pairs`` in the registry. Optional L1 is
    included when its 200-id calibration file is present. AR baseline is off
    unless ``include_baseline``. ``--engines`` keeps the legacy ablation matrix.
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
                )
            )
        return out

    if not catalog:
        # Registry without matrix_pairs: previous default engine list
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
            if pair.requires_calibration:
                cfg = registry.get(pair.stage1_config_id)
                if not _calibration_ready(cfg, root):
                    raise RuntimeError(
                        f"Pair {pair.pair_id} needs a 200-id calibration file "
                        f"at {cfg.calibration_ref}"
                    )
        return selected

    selected = []
    for pair in catalog:
        if pair.role == "baseline" and not include_baseline:
            continue
        if (
            pair.optional
            and not include_optional
            and not pair.requires_calibration
            and pair.role != "baseline"
        ):
            continue
        if pair.requires_calibration:
            cfg = registry.get(pair.stage1_config_id)
            if not _calibration_ready(cfg, root):
                continue
        selected.append(pair)
    return selected
