# The __init__.py file of the test directory should be empty.
# (Before you say it: Comments are fine, smart*ss ;D)

# You'll want to start with reading bases.py.

# If you want to read more about tests, there is also the "Tests" section of the World API document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#tests
from test.bases import WorldTestBase
from worlds.nds import NaturalDisasterSurvivalWorld


class MyGameTestBase(WorldTestBase):
    game = "Natural Disaster Survival"
    world: NaturalDisasterSurvivalWorld