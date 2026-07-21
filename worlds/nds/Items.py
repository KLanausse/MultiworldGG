from __future__ import annotations

import random
from typing import Dict, TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .Types import ItemData, NaturalDisasterSurvivalItem, base_id, nds_disasters, nds_maps

if TYPE_CHECKING:
    from .World import NaturalDisasterSurvivalWorld

id_offset = base_id + 1
disasters: Dict[str, ItemData] = {}
maps: Dict[str, ItemData] = {}

for nds_disaster in nds_disasters:
    disasters[nds_disaster] = ItemData(id_offset, ItemClassification.progression)
    id_offset+=1

for nds_map in nds_maps:
    maps[nds_map] = ItemData(id_offset, ItemClassification.progression)
    id_offset+=1

gears: Dict[str, ItemData] = {
    "Green Balloon": ItemData(id_offset + 1, ItemClassification.filler)
}

traps: Dict[str, ItemData] = {
    "Trip Everyone":        ItemData(id_offset+2, ItemClassification.trap),
    "Slow Down":            ItemData(id_offset+3, ItemClassification.trap),
}

filler_items: Dict[str, ItemData] = {
    **traps,
    "+10 Health":           ItemData(id_offset+4, ItemClassification.filler),
    "Speed Up":             ItemData(id_offset+5, ItemClassification.filler),
    "Time Change":          ItemData(id_offset+6, ItemClassification.filler),
}

ALL_ITEMS: Dict[str, ItemData] = {
    **disasters,
    **maps,
    **gears,
    **filler_items,
}

ITEM_TABLE = {name: data.id for name, data in ALL_ITEMS.items()}

def get_random_filler_item_name(world: NaturalDisasterSurvivalWorld):
    return random.choice([name for name in filler_items]) # Temp

def create_item_with_correct_classification(world: NaturalDisasterSurvivalWorld, name: str) -> NaturalDisasterSurvivalItem:
    return NaturalDisasterSurvivalItem(name, ALL_ITEMS[name].classification, ALL_ITEMS[name].id, world.player)

def create_all_items(world: NaturalDisasterSurvivalWorld) -> None:
    itempool: list[Item] = [world.create_item(name) for name, data in gears.items()]
    disaster_pool: list[Item] = [world.create_item(name) for name, data in disasters.items()]
    map_pool: list[Item] = [world.create_item(name) for name, data in maps.items()]

    # Start with 1 Map & 1 Disaster. Remove them from their pool
    starting_map: Item = random.choice(map_pool)
    world.push_precollected(starting_map)
    map_pool.remove(starting_map)
    itempool += map_pool

    starting_disaster: Item = random.choice(disaster_pool)
    world.push_precollected(starting_disaster)
    disaster_pool.remove(starting_disaster)
    itempool += disaster_pool

    # Based off of APQuest Code
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool