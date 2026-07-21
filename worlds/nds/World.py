from collections.abc import Mapping
from typing import Any

from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

from . import Locations, Items, Options, Regions


class NaturalDisasterSurvivalWebWorld(WebWorld):
    game = "Natural Disaster Survival"
    theme = "grassFlowers"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up Natural Disaster Survival for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Lanausse"],
    )

    tutorials = [setup_en]

    # If we have option groups and/or option presets, we need to specify these here as well.
    option_groups = Options.option_groups
    options_presets = Options.option_presets


class NaturalDisasterSurvivalWorld(World):
    """
    Placeholder.
    """
    game = "Natural Disaster Survival"
    web = NaturalDisasterSurvivalWebWorld()

    item_name_to_id = Items.ITEM_TABLE
    location_name_to_id = Locations.LOCATION_TABLE
    options_dataclass = Options.NaturalDisasterSurvivalOptions
    options: Options.NaturalDisasterSurvivalOptions

    origin_region_name = "Spawn"

    def generate_basic(self) -> None:
        pass

    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)

    def create_items(self) -> None:
        Items.create_all_items(self)

    def create_item(self, name: str) -> Items.NaturalDisasterSurvivalItem:
        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "death_link": self.options.death_link.value,
            "server_percentage": self.options.server_percentage.value,
            "disaster_duration": self.options.disaster_duration.value,
            "intermission_duration": self.options.intermission_duration.value,
        }
