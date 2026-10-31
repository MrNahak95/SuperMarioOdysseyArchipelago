"""Helpers for Capture / Ability Lock placement (1 moon → 1 item, multi → 3 slots)."""

from typing import Iterable, List, Sequence

from .Items import capture_items, multi_moons
from .Locations import loc_Cloud, loc_Cloud_Postgame, loc_Dark, loc_Mushroom, loc_Mushroom_Post_Luncheon
from .Abilities import ability_items, ability_lock_starts
from .Paintings import painting_ids


# Extra AP location IDs for multi-moon unlock slots (base location keeps slot 1).
CAPTURE_SLOT_ID_BASE = 4000
ABILITY_SLOT_ID_BASE = 4100
PAINTING_SLOT_ID_BASE = 4200


def mushroom_moon_names() -> List[str]:
    return list({**loc_Mushroom, **loc_Mushroom_Post_Luncheon}.keys())


def dark_side_moon_names() -> List[str]:
    return list(loc_Dark.keys())


def cloud_moon_names() -> List[str]:
    return list({**loc_Cloud, **loc_Cloud_Postgame}.keys())


def expand_multi_slots(moon_names: Sequence[str], kingdom: str, label: str, id_base: int) -> dict:
    """For each multi-moon in kingdom, add Unlock Slot 2/3 locations.

    Returns dict name -> id for the *extra* slots only.
    """
    extras = {}
    multis = set(multi_moons.get(kingdom, []))
    n = 0
    for name in moon_names:
        if name in multis:
            for slot in (2, 3):
                extra_name = f"{name} — {label} Slot {slot}"
                extras[extra_name] = id_base + n
                n += 1
    return extras


def capture_lock_slot_locations() -> dict:
    return expand_multi_slots(mushroom_moon_names(), "Mushroom", "Capture", CAPTURE_SLOT_ID_BASE)


def ability_lock_slot_locations() -> dict:
    return expand_multi_slots(dark_side_moon_names(), "Dark", "Ability", ABILITY_SLOT_ID_BASE)


def painting_lock_slot_locations() -> dict:
    # Cloud multi-moons: none in multi_moons table; keep helper for symmetry / future.
    return expand_multi_slots(cloud_moon_names(), "Cloud", "Painting", PAINTING_SLOT_ID_BASE)


def placement_targets(base_moons: Sequence[str], extras: dict) -> List[str]:
    """Ordered list of locations that can receive lock items (base + multi extras)."""
    targets = list(base_moons)
    targets.extend(extras.keys())
    return targets


def capture_lock_starts_for_goal(goal_value: int, goal_moon: int = 13) -> List[str]:
    """Captures required to reach post-game Mushroom for typical story path.

    These are removed from locked Mushroom placement and granted at start so
    Cap→Sand→…→Moon stays beatable before Mushroom opens.
    """
    # Minimal set mirrored from existing Capture Sanity story rules + traversal.
    starts = [
        "Frog",
        "Spark Pylon",
        "Chain Chomp",
        "Big Chain Chomp",
        "Broode's Chain Chomp",
        "T-Rex",
        "Bullet Bill",
        "Knucklotec's Fist",
        "Goomba",
        "Uproot",
        "Sherm",
        "Manhole",
        "Gushen",
        "Shiverian Racer",
        "Lava Bubble",
        "Hammer Bro",
        "Meat",
        "Pokio",
        "Bowser",
        "Paragoomba",
    ]
    # Dedupe preserve order; only known capture names
    known = set(capture_items)
    out = []
    for name in starts:
        if name in known and name not in out:
            out.append(name)
    return out


def ability_items_to_place() -> List[str]:
    """Abilities that still need Dark Side placement (not auto-started)."""
    started = set(ability_lock_starts)
    return [a for a in ability_items if a not in started]


def shuffle_place_locked(world, player, location_names: List[str], item_names: List[str], random) -> List[str]:
    """Place item_names onto a random subset of location_names as locked items.

    Returns location names that received an item.
    """
    locs = location_names[:]
    random.shuffle(locs)
    items = item_names[:]
    random.shuffle(items)
    placed_locs = []
    for item_name, loc_name in zip(items, locs):
        world.get_location(loc_name).place_locked_item(world.create_item(item_name))
        placed_locs.append(loc_name)
    return placed_locs
