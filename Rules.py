from .Constants import *


def get_location_rules(player):
    return {
        # Tiles 1-7 (group 0) are free — no entry needed.

        # Group 1 — tiles 8-14
        LOC_FF_8_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,
        LOC_FF_9_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,
        LOC_FF_10_JOKER:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,
        LOC_FF_11_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,
        LOC_FF_12_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,
        LOC_FF_13_JOKER:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,
        LOC_FF_14_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 1,

        # Group 2 — tiles 15-21
        LOC_FF_15_MINIGAME:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,
        LOC_FF_16_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,
        LOC_FF_17_MINIGAME:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,
        LOC_FF_18_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,
        LOC_FF_19_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,
        LOC_FF_20_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,
        LOC_FF_21_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 2,

        # Group 3 — tiles 22-28
        LOC_FF_22_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,
        LOC_FF_23_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,
        LOC_FF_24_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,
        LOC_FF_25_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,
        LOC_FF_26_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,
        LOC_FF_27_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,
        LOC_FF_28_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 3,

        # Group 4 — tiles 29-35
        LOC_FF_29_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,
        LOC_FF_30_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,
        LOC_FF_31_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,
        LOC_FF_32_MINIGAME:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,
        LOC_FF_33_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,
        LOC_FF_34_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,
        LOC_FF_35_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 4,

        # Group 5 — tiles 36-42
        LOC_FF_36_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,
        LOC_FF_37_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,
        LOC_FF_38_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,
        LOC_FF_39_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,
        LOC_FF_40_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,
        LOC_FF_41_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,
        LOC_FF_42_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 5,

        # Group 6 — tiles 43-49
        LOC_FF_43_MINIGAME:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,
        LOC_FF_44_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,
        LOC_FF_45_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,
        LOC_FF_46_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,
        LOC_FF_47_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,
        LOC_FF_48_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,
        LOC_FF_49_JOKER:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 6,

        # Group 7 — tiles 50-56
        LOC_FF_50_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,
        LOC_FF_51_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,
        LOC_FF_52_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,
        LOC_FF_53_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,
        LOC_FF_54_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,
        LOC_FF_55_MINIGAME:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,
        LOC_FF_56_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 7,

        # Group 8 — tiles 57-63
        LOC_FF_57_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,
        LOC_FF_58_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,
        LOC_FF_59_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,
        LOC_FF_60_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,
        LOC_FF_61_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,
        LOC_FF_62_MUSIC:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,
        LOC_FF_63_MINIGAME:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 8,

        # Group 9 — tiles 64-70
        LOC_FF_64_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,
        LOC_FF_65_JOKER:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,
        LOC_FF_66_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,
        LOC_FF_67_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,
        LOC_FF_68_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,
        LOC_FF_69_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,
        LOC_FF_70_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 9,

        # Group 10 — tiles 71-77 (terminal)
        LOC_FF_71_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
        LOC_FF_72_GRUNTY:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
        LOC_FF_73_BANJO:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
        LOC_FF_74_PICTURE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
        LOC_FF_75_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
        LOC_FF_76_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
        LOC_FF_77_SKULL:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,

        # Board Complete requires all 10 access items
        LOC_FF_BOARD_COMPLETE:
            lambda state: state.count(ITEM_FF_BOARD_ACCESS, player) >= 10,
    }
