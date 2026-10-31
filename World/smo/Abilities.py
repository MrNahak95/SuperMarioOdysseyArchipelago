"""Ability Lock items — full Manual AP / smorando action_rando list.

Placement (Project): Dark Side moons / Starbits (not Moon Kingdom).
"""

# Full action list from empathy-mp3 Manual AP (category Action).
ability_items = [
    "Long Jump",
    "Roll",
    "Ground Pound",
    "Dive",
    "Ground Pound Jump",
    "Upward Throw",
    "Downward Throw",
    "Spin Throw",
    "Cap Jump",
    "Homing Cap Throw",
    "Backward Somersault",
    "Side Somersault",
    "Triple Jump",
    "Wall Jump",
    "Hold/Throw",
    "Swim",
    "Quick Swim",
    "Spin",
    "Dash (2D)",
    "Jaxi",
    "Motor scooter",
]

# Auto-started when ability_lock is on so Cap→Moon stays playable before Dark Side.
ability_lock_starts = [
    "Long Jump",
    "Roll",
    "Ground Pound",
    "Dive",
    "Cap Jump",
    "Backward Somersault",
    "Side Somersault",
    "Triple Jump",
    "Wall Jump",
    "Hold/Throw",
    "Swim",
]

# Item IDs 3800+
ability_item_table = {name: 3800 + i for i, name in enumerate(ability_items)}
