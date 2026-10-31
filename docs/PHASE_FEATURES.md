# Phase B feature notes (Project)

Order: **B1 → B4**. Hardware: emulator. Goal: YAML option.

| Jalon | Option(s) | Placement / behavior |
| --- | --- | --- |
| **B1 Capture Lock** | `capture_lock` | Capture items gated in-game. Placement on **Mushroom** moons (1→1; multi-moon → 3 slots). Story-critical captures auto-started so Cap→Moon stays beatable before post-game Mushroom. |
| **B2 Ability Lock** | `ability_lock` | Full Manual AP `action_rando` list. Placement on **Dark Side** moons/Starbits (not Moon Kingdom). Safe starter subset auto-started; remainder on Dark Side. |
| **B3 Paintings** | `painting_unlock` | Cloud moons grant painting unlocks; painting **destinations shuffled**; mapping in `slot_data`. |
| **B4 Entrances** | `entrance_mode` | v1 **`standard`** kingdom loading-zone shuffle; `off` default. `chains` / `limited` / `decoupled` reserved in YAML for later. Spoiler + `slot_data["entrances"]`. |

Legacy `capture_sanity` still accepted and enables the same gating flag sent to the mod (`captures` in SlotData).
