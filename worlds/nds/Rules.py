from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, Rule, And, True_
from .Types import nds_maps, nds_disasters

if TYPE_CHECKING:
    from .World import NaturalDisasterSurvivalWorld


def set_all_rules(world: NaturalDisasterSurvivalWorld) -> None:
    completion_rule = True_()
    for nds_map in nds_maps:
        completion_rule = And(completion_rule, Has(nds_map))
    for nds_disaster in nds_disasters:
        completion_rule = And(completion_rule, Has(nds_disaster))
    world.set_completion_rule(completion_rule)