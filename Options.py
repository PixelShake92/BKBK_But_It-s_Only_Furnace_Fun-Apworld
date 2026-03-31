from dataclasses import dataclass

from Options import DeathLink, PerGameCommonOptions, StartInventoryPool


@dataclass
class FFOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    death_link: DeathLink
