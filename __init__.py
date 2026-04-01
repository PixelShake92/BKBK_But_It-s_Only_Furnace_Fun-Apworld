from typing import List, Dict

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .Constants import *
from .Items import FFItem, FFItemData, item_data_table, item_table, BRENTILDA_ITEMS
from .Locations import FFLocation, FFLocationData, location_data_table, location_table, locked_locations
from .Options import FFOptions
from .Regions import region_data_table
from .Rules import get_location_rules


class FFWebWorld(WebWorld):
    setup_en = Tutorial(
        "Furnace Fun Only Setup Guide",
        "A guide to setting up the BK Furnace Fun Only randomizer",
        "English",
        "setup_en.md",
        "setup/en",
        ["PixelShake92"],
    )
    tutorials = [setup_en]


class FFWorld(World):
    """
    Banjo-Kazooie, but it's ONLY Furnace Fun.

    The entire game is the Furnace Fun board. Every tile is a check.
    Receive FF Board Access items to unlock further groups of 7 tiles.
    Collect Brentilda's Secrets to get quiz hints on Grunty questions.
    Complete all 77 tiles to roll the credits.

    This is a joke. Happy April Fools.
    """

    game = "BK - Furnace Fun Only"
    web = FFWebWorld()
    options_dataclass = FFOptions
    options: FFOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def generate_early(self) -> None:
        self.options.accessibility.value = self.options.accessibility.option_minimal

    def create_item(self, name: str) -> FFItem:
        return FFItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def place(self, location, item):
        self.multiworld.get_location(location, self.player).place_locked_item(self.create_item(item))

    def create_items(self) -> None:
        mw = self.multiworld
        player = self.player

        item_pool: List[FFItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            item_pool_count[name] = 0
            if item.code and item.can_create(self.options):
                while item_pool_count[name] < item.num_exist:
                    item_pool.append(self.create_item(name))
                    item_pool_count[name] += 1

        mw.itempool += item_pool

        total_unfilled = sum(1 for loc in mw.get_locations(player) if not loc.item)
        total_items = sum(1 for item in mw.itempool if item.player == player)

        filler_needed = total_unfilled - total_items
        if filler_needed > 0:
            self.create_and_add_filler_items(filler_needed)

    def create_regions(self) -> None:
        player = self.player
        mw = self.multiworld

        for region_name in region_data_table.keys():
            region = Region(region_name, player, mw)
            mw.regions.append(region)

        for region_name, region_data in region_data_table.items():
            region = mw.get_region(region_name, player)
            region.add_locations({
                location_name: location_data.address
                for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.options)
            }, FFLocation)
            region.add_exits(region_data.connecting_regions)

        for location_name, location_data in locked_locations.items():
            if not location_data.can_create(self.options):
                continue
            self.place(location_name, location_data.locked_item)

    def set_rules(self) -> None:
        player = self.player
        mw = self.multiworld

        mw.completion_condition[player] = lambda state: state.has(ITEM_VICTORY, player)

        location_rules = get_location_rules(player)

        for location in mw.get_locations(player):
            name = location.name
            if name in location_rules and location_data_table[name].can_create(self.options):
                location.access_rule = location_rules[name]

    def create_and_add_filler_items(self, count: int = 1):
        for _ in range(count):
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))

    def get_filler_item_name(self) -> str:
        return self.random.choice([ITEM_EGG_REFILL, ITEM_REDFEATHER_REFILL, ITEM_GOLDFEATHER_REFILL])

    def fill_slot_data(self):
        return {
            "furnace_fun_only": 1,
            "furnace_fun_sanity": 1,
        }