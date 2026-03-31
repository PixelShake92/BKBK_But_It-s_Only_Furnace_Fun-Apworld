from typing import Dict, NamedTuple, List

from .Constants import RGN_MENU, RGN_FURNACE_FUN_BOARD


class FFRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, FFRegionData] = {
    # AP requires a "Menu" region as the root of every world.
    RGN_MENU: FFRegionData(
        connecting_regions=[RGN_FURNACE_FUN_BOARD]
    ),
    RGN_FURNACE_FUN_BOARD: FFRegionData(),
}
