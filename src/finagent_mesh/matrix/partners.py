"""Fixed Stage partners and matrix row binding rules."""

from __future__ import annotations

from dataclasses import dataclass

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


def bind_matrix_row(
    variable: EngineConfiguration,
    partners: FixedStagePartners,
) -> StageBinding:
    """Bind stages for a variable matrix engine per data-model rules."""
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
    # Dual-capable: bind both stages to the variable engine
    return StageBinding(
        stage1_config_id=vid,
        stage2_config_id=vid,
        variable_config_id=vid,
    )
