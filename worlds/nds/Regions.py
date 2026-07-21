from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .Types import nds_maps

if TYPE_CHECKING:
    from .World import NaturalDisasterSurvivalWorld

region_names = [
    "Spawn",
]
region_names += nds_maps


def create_and_connect_regions(world: NaturalDisasterSurvivalWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: NaturalDisasterSurvivalWorld) -> None:
    regions = [Region(name, world.player, world.multiworld) for name in region_names]
    world.multiworld.regions += regions


def connect_regions(world: NaturalDisasterSurvivalWorld) -> None:
    spawn = world.get_region("Spawn")
    for nds_map_name in nds_maps:
        region = world.get_region(nds_map_name)
        spawn.connect(region, f"Spawn To {nds_map_name}")