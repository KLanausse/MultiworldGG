from enum import Enum
from typing import NamedTuple, Optional

from BaseClasses import Location, Item, ItemClassification

base_id = 189707

nds_disasters = [
    "Meteor Shower",
    "Flash Flood",
    "Thunder Storm",
    "Fire",
    "Tornado",
    "Tsunami",
    "Blizzard",
    "Sandstorm",
    "Volcanic Eruption",
    "Earthquake",
    "Acid Rain",
]

nds_maps = [
    "Arch Park",
    "Costal Quickstop",
    "Fort Indestructable",
    "Glass Office",
    "Happy Home",
    "Rakish Refinery",
    "Raving Raceway",
    "Sky Tower",
    "Sunny Ranch",
    "Surf Central",
    "Trailer Park",
]


class NaturalDisasterSurvivalLocation(Location):
    game = "Natural Disaster Survival"


class NaturalDisasterSurvivalItem(Item):
    game = "Natural Disaster Survival"


class ItemData(NamedTuple):
    id: Optional[int]
    classification: Optional[ItemClassification]
