# Emulator build & install (Project fork)

**Target:** Super Mario Odyssey **1.0.0** on Ryujinx / Yuzu-family only (no Switch CFW path for this Project).  
**Fork:** https://github.com/MrNahak95/SuperMarioOdysseyArchipelago  
**Upstream:** https://github.com/Kgamer77/SuperMarioOdysseyArchipelago

Cloud agents **never** hold SMO ROMs or title keys. Everything below that needs a dump is **local on Jérôme’s machine**.

---

## A0 — local smoke checklist

### Prerequisites (local)

| Piece | Notes |
| --- | --- |
| Game | SMO **1.0.0** only (not 1.1.0 / 1.3.0) |
| Emulator | Ryujinx (or fork) **or** Yuzu-family with mod support |
| Archipelago | Recent install with Launcher (SMO Client component) |
| Network | Emulator and Client on the same PC/LAN; port **1027** free |

### 1. Build / grab Emu mod

**Option A — use a release zip** (when this fork publishes one):

- `SMO_Archipelago_*_Emu.zip` → extract → folder `SMOAP`

**Option B — rebuild from this repo** (`Mod/`):

```bash
cd Mod
./docker-build.sh 1          # ISEMU=1
# or: make SMOVER=100 ISEMU=1
```

Pack Atmosphere layout under `starlight_patch_100/atmosphere/contents/0100000000010000/` into an emulator mod folder named `SMOAP` (exefs `subsdk1` + `romfs` + exefs_patches as upstream does).

### 2. Install mod on emulator

**Ryujinx / forks:** right-click SMO → Open Mods Directory → place `SMOAP` there.  
**Yuzu-family:** Right-click game → Open Mod Data Location → place `SMOAP`.

Enable the mod; boot once to confirm the game still loads with the NSO patched.

### 3. Package `smo.apworld`

From repo root (or CI later):

```bash
# Example: zip World/smo contents as Archipelago expects for an apworld
cd World && zip -r smo.apworld smo
```

Copy `smo.apworld` into Archipelago’s `custom_worlds`  
(default Windows: `C:\ProgramData\Archipelago\custom_worlds`).

Restart Archipelago / regenerate YAML templates so SMO options appear (`capture_lock`, `ability_lock`, `painting_unlock`, `entrance_mode`, `goal`, …).

### 4. Generate a seed

Minimal YAML knobs for A0 (moon check only):

```yaml
Super Mario Odyssey:
  goal: moon
  capture_lock: false
  ability_lock: false
  painting_unlock: false
  entrance_mode: off
```

Full keys + variants: [`sample-player.yaml`](sample-player.yaml).

Generate → open the room / start hosting.

### 5. Connect Client (:1027)

1. Archipelago Launcher → **Super Mario Odyssey Client** (or run the world connector).
2. Connect the client to the AP server (room / host / port / slot / password as usual).
3. Confirm the proxy is listening on **TCP 1027** (default; do not change unless you know why).

### 6. Connect in-game

When the mod prompts for connection:

- **IP:** your PC’s LAN IPv4 (`ipconfig` / `ip a`) — use `127.0.0.1` if emulator networking is host-local and that works for your setup
- **Port:** `1027`

### 7. Verify the check

1. Collect any reachable Power Moon.
2. Archipelago client / tracker shows the location checked and an item received (or sent).
3. Optional: receive a Capture / Ability item with locks on and confirm gating (later A0+).

**A0 pass:** moon collect → AP location check / item round-trip on `:1027`.

### If it fails

| Symptom | Check |
| --- | --- |
| No connect prompt / can’t join | Mod not loaded; wrong SMO version; wrong title ID folder |
| Client connects, game doesn’t | Firewall blocking 1027; wrong IP; Client not running |
| Game connects, no checks | Wrong slot / seed; `smo.apworld` not the fork build; client not joined to room |
| Softlock / missing progression | Leave locks off for first A0; enable `capture_lock` / `ability_lock` only after baseline works |

---

## Rebuild mod (Emu) — quick ref

```bash
cd Mod
./docker-build.sh 1          # ISEMU=1
# or
make SMOVER=100 ISEMU=1
```

## Client / apworld paths

- World package: `World/smo/`
- Connector proxy: `World/smo/Connector/` → **:1027**
- Feature notes: [`PHASE_FEATURES.md`](PHASE_FEATURES.md)

## Goal (YAML)

`Goal` remains a player YAML option (`sand` / `lake` / `metro` / `luncheon` / `moon` / `dark` / `darker`). No Project-fixed goal.

## What only Jérôme can do locally

- Provide / dump SMO 1.0.0 ROM (never commit or upload to cloud agents)
- Run emulator + confirm A0 pass
- Publish Emu zip / `smo.apworld` release assets from a green local build if desired
