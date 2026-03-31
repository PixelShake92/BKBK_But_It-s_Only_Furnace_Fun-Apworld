from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location

from .Constants import *


class FFLocation(Location):
    game = "BK - Furnace Fun Only"


class FFLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, FFLocationData] = {
    LOC_FF_1_BANJO:     FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C000191),
    LOC_FF_2_PICTURE:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C000192),
    LOC_FF_3_SKULL:     FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C000194),
    LOC_FF_4_JOKER:     FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C000195),
    LOC_FF_5_MUSIC:     FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C000197),
    LOC_FF_6_BANJO:     FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C000198),
    LOC_FF_7_GRUNTY:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C00019A),
    LOC_FF_8_PICTURE:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C00019B),
    LOC_FF_9_BANJO:     FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C00019C),
    LOC_FF_10_JOKER:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C00019D),
    LOC_FF_11_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C00019E),
    LOC_FF_12_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A0),
    LOC_FF_13_JOKER:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A1),
    LOC_FF_14_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A2),
    LOC_FF_15_MINIGAME: FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A3),
    LOC_FF_16_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A5),
    LOC_FF_17_MINIGAME: FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A6),
    LOC_FF_18_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A7),
    LOC_FF_19_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A8),
    LOC_FF_20_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001A9),
    LOC_FF_21_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001AA),
    LOC_FF_22_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001AB),
    LOC_FF_23_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001AE),
    LOC_FF_24_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001AF),
    LOC_FF_25_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B0),
    LOC_FF_26_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B1),
    LOC_FF_27_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B2),
    LOC_FF_28_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B3),
    LOC_FF_29_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B6),
    LOC_FF_30_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B7),
    LOC_FF_31_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001B9),
    LOC_FF_32_MINIGAME: FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001BA),
    LOC_FF_33_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001BB),
    LOC_FF_34_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001BC),
    LOC_FF_35_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001BD),
    LOC_FF_36_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001BE),
    LOC_FF_37_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001BF),
    LOC_FF_38_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C0),
    LOC_FF_39_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C1),
    LOC_FF_40_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C2),
    LOC_FF_41_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C3),
    LOC_FF_42_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C5),
    LOC_FF_43_MINIGAME: FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C6),
    LOC_FF_44_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C7),
    LOC_FF_45_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C8),
    LOC_FF_46_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001C9),
    LOC_FF_47_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001CA),
    LOC_FF_48_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001CB),
    LOC_FF_49_JOKER:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001CC),
    LOC_FF_50_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001CD),
    LOC_FF_51_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001CF),
    LOC_FF_52_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D0),
    LOC_FF_53_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D1),
    LOC_FF_54_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D2),
    LOC_FF_55_MINIGAME: FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D3),
    LOC_FF_56_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D4),
    LOC_FF_57_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D6),
    LOC_FF_58_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D7),
    LOC_FF_59_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D8),
    LOC_FF_60_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001D9),
    LOC_FF_61_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001DA),
    LOC_FF_62_MUSIC:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001DC),
    LOC_FF_63_MINIGAME: FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001DD),
    LOC_FF_64_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001DE),
    LOC_FF_65_JOKER:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001DF),
    LOC_FF_66_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E0),
    LOC_FF_67_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E1),
    LOC_FF_68_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E2),
    LOC_FF_69_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E3),
    LOC_FF_70_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E4),
    LOC_FF_71_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E6),
    LOC_FF_72_GRUNTY:   FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E7),
    LOC_FF_73_BANJO:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001E8),
    LOC_FF_74_PICTURE:  FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001EA),
    LOC_FF_75_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001EC),
    LOC_FF_76_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001ED),
    LOC_FF_77_SKULL:    FFLocationData(region=RGN_FURNACE_FUN_BOARD, address=0x1C0001EF),

    LOC_FF_BOARD_COMPLETE: FFLocationData(
        region=RGN_FURNACE_FUN_BOARD,
        address=None,
        locked_item=ITEM_VICTORY,
    ),
}

location_table = {
    name: data.address
    for name, data in location_data_table.items()
    if data.address is not None
}

locked_locations = {
    name: data
    for name, data in location_data_table.items()
    if data.locked_item is not None
}
