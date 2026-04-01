# Setup Guide

Welcome to the setup guide. This should take less than 5 minutes. 

## What you need

- [Banjo-Kazooie Recompiled](https://github.com/BanjoRecomp/BanjoRecomp/releases/tag/v1.0.1) — the recompilation. The game itself.
- [Archipelago](https://archipelago.gg) — the multiworld framework holding this entire disaster together.
- The `bkbk_only_ff.nrm` mod file — from the releases page of this repo.
- The `APCpp-Glue` native library — also in the release. Don't lose it.

## Installing the mod

1. Grab the latest release.
2. Drag the BKBKFF.zip over the top of your Banjo Recompiled launch screen (or the mods screen)
3. Launch the game, go to the mod menu, enable it.
4. Contemplate your choices.

## Generating a game

1. Drop `bk_furnace_fun_only.apworld` into your Archipelago `custom_worlds/` folder.
2. use the template yaml or generate your own template yaml using the options creator or generate template buttons in the archipelago launcher.


3. Generate via the Archipelago website or your local install.
4. Host it. Tell your friends. Watch them suffer alongside you.

## Connecting

1. Launch Banjo-Kazooie Recompiled with the mod enabled.
2. Enter your server, slot name, and password.
3. Hit connect. Select the first save file and then have fun.

## Troubleshooting

**The board isn't loading** — Make sure both the `.nrm` and the native library are in the `mods/` folder. The mod needs both.

**I'm not getting any items** — Check your connection. If the AP client says connected, try walking onto a tile.

**I keep dying on skull tiles** — Yes. That's correct. That's how the game works. You're doing great.

**The barriers aren't opening** — You need more FF Board Access items. That means waiting for your multiworld to deliver. Patience. Or beg your co-players.

**Something is genuinely broken** — Open an issue. Include what happened, what you expected, and a screenshot if you have one. This was made in a single weekend so there will probably be bugs. 
