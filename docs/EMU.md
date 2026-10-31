# Emulator build & install (Project fork)

**Target:** Super Mario Odyssey **1.0.0** on Ryujinx / Yuzu-family only (no Switch CFW path for this Project).  
**Fork:** https://github.com/MrNahak95/SuperMarioOdysseyArchipelago  
**Upstream:** https://github.com/Kgamer77/SuperMarioOdysseyArchipelago

## A0 — local smoke (ROM stays on your machine)

Cloud agents never hold SMO ROMs. A0 is done on Jérôme’s PC:

1. Install Archipelago; drop this fork’s `smo.apworld` into `custom_worlds`.
2. Generate a YAML seed (`goal` free — Moon / Metro / …).
3. Install the **Emu** mod zip (`SMO_Archipelago_*_Emu.zip` → `SMOAP` under the title’s mods dir).
4. Launch the **Super Mario Odyssey Client**; proxy listens on **TCP :1027**.
5. In-game, connect to your LAN IPv4, port `1027`.
6. Collect a moon → Archipelago shows the check / item.

**A0 pass:** moon check ↔ AP item round-trip works.

## Rebuild mod (Emu)

From `Mod/`:

```bash
# Docker (preferred)
./docker-build.sh 1          # ISEMU=1

# Or make
make SMOVER=100 ISEMU=1
```

Layout after build: Atmosphere-style tree under `starlight_patch_100/`. For emulator zips, ship the same contents as upstream’s `SMOAP` folder (exefs + romfs for title `0100000000010000`).

## Client / apworld

- World package: `World/smo/`
- Connector proxy: `World/smo/Connector/` → **:1027**
- Package as `smo.apworld` for Archipelago `custom_worlds`

## Goal (YAML)

`Goal` remains a player YAML option (`sand` / `lake` / `metro` / `luncheon` / `moon` / `dark` / `darker`). No Project-fixed goal.
