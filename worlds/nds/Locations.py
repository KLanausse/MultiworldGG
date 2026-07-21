from __future__ import annotations
from typing import TYPE_CHECKING, Dict

from rule_builder.rules import HasAll

from .Types import NaturalDisasterSurvivalLocation, base_id, nds_disasters, nds_maps

if TYPE_CHECKING:
    from .World import NaturalDisasterSurvivalWorld

id_offset = 1
base_locations_by_region: Dict[str, Dict[str, int]] = {}
for nds_map in nds_maps:
    base_locations_by_region[nds_map] = {}
    for nds_disaster in nds_disasters:
        base_locations_by_region[nds_map][f"{nds_map} - {nds_disaster}"] = base_id + id_offset
        id_offset += 1

misc: Dict[str, int] = {
    "Green Balloon": base_id + id_offset + 1,
}

all_locations: Dict[str, int] = {
    **misc,
}
for map_table in base_locations_by_region:
    all_locations.update(base_locations_by_region[map_table])


LOCATION_TABLE = {location_name: all_locations[location_name] for location_name in all_locations}


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: all_locations[location_name] for location_name in location_names}


def create_all_locations(world: NaturalDisasterSurvivalWorld) -> None:
    spawn = world.get_region("Spawn")
    for nds_map_name in base_locations_by_region:
        region = world.get_region(nds_map_name)
        for location_name in base_locations_by_region[nds_map_name]:
            location = NaturalDisasterSurvivalLocation(
                world.player, location_name, world.location_name_to_id[location_name], spawn
            )
            disaster_name = location_name.split(" - ")[1]
            world.set_rule(location, HasAll(disaster_name, nds_map_name))
            region.locations.append(location)


    misc_locations = get_location_names_with_ids([name for name in misc])
    spawn.add_locations(misc_locations, NaturalDisasterSurvivalLocation)