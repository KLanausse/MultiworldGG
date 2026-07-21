from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink, OptionGroup

class ServerPercentage(Range):
    """
    What percent of the server needs to survive for the check to count.
    """

    display_name = "Server Percentage"

    range_start = 10
    range_end = 100
    default = 60

class IntermissionDuration(Range):
    """
    How long intermissions last for.
    """

    display_name = "Intermission Duration"

    range_start = 10
    range_end = 90
    default = 40

class DisasterDuration(Range):
    """
    How long disasters last for. Doesn't affect Flash Flood
    """

    display_name = "Disaster Duration"

    range_start = 30
    range_end = 180
    default = 90

@dataclass
class NaturalDisasterSurvivalOptions(PerGameCommonOptions):
    death_link: DeathLink
    server_percentage: ServerPercentage
    disaster_duration: DisasterDuration
    intermission_duration: IntermissionDuration

OPTION_GROUPS = [
    OptionGroup("Game Options", [ServerPercentage, IntermissionDuration,DisasterDuration]),
    OptionGroup("Death Link", [DeathLink]),
]

option_presets = {
    "Default": {
        "death_link": True,
        "server_percentage": 60,
        "disaster_duration": 90,
        "intermission": 40
    }
}