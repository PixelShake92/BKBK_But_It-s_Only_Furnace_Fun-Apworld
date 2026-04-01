from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification

from .Constants import *


class FFItem(Item):
    game = "BK - Furnace Fun Only"


class FFItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True


item_data_table: Dict[str, FFItemData] = {
    ITEM_FF_BOARD_ACCESS: FFItemData(
        code=0x1D000001,
        type=ItemClassification.progression,
        num_exist=10,
    ),

    ITEM_BRENTILDA_1:  FFItemData(code=0x20000000, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_2:  FFItemData(code=0x20000001, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_3:  FFItemData(code=0x20000002, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_4:  FFItemData(code=0x20000003, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_5:  FFItemData(code=0x20000004, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_6:  FFItemData(code=0x20000005, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_7:  FFItemData(code=0x20000006, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_8:  FFItemData(code=0x20000007, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_9:  FFItemData(code=0x20000008, type=ItemClassification.useful, num_exist=1),
    ITEM_BRENTILDA_10: FFItemData(code=0x20000009, type=ItemClassification.useful, num_exist=1),

    ITEM_HONEYCOMB:          FFItemData(code=0x0001FBF1, type=ItemClassification.filler),
    ITEM_EXTRA_LIFE:         FFItemData(code=0x0001FBF5, type=ItemClassification.filler),
    ITEM_EGG_REFILL:         FFItemData(code=0x0001FBF2, type=ItemClassification.filler),
    ITEM_REDFEATHER_REFILL:  FFItemData(code=0x0001FBF3, type=ItemClassification.filler),
    ITEM_GOLDFEATHER_REFILL: FFItemData(code=0x0001FBF4, type=ItemClassification.filler),

    ITEM_VICTORY: FFItemData(
        code=None,
        type=ItemClassification.progression,
        can_create=lambda options: False,
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}

BRENTILDA_ITEMS = [
    ITEM_BRENTILDA_1, ITEM_BRENTILDA_2, ITEM_BRENTILDA_3,
    ITEM_BRENTILDA_4, ITEM_BRENTILDA_5, ITEM_BRENTILDA_6,
    ITEM_BRENTILDA_7, ITEM_BRENTILDA_8, ITEM_BRENTILDA_9,
    ITEM_BRENTILDA_10,
]
