"""B4 — Entrance rando (v1 Standard). Chains/Limited/Decoupled reserved."""

from typing import Dict, List, Tuple

# Ordered kingdom hubs used for Standard couple shuffle (bidirectional pairs).
# Edges follow the vanilla story spine used by Regions.create_regions.
VANILLA_ENTRANCES: List[Tuple[str, str]] = [
    ("Cascade", "Sand"),
    ("Sand", "Lake"),
    ("Lake", "Wooded"),
    ("Wooded", "Cloud"),  # Post Cloud / Bowser-in-Cloud path abstracted as Cloud hub
    ("Cloud", "Lost"),
    ("Lost", "Metro"),
    ("Metro", "Snow"),
    ("Snow", "Seaside"),
    ("Seaside", "Luncheon"),
    ("Luncheon", "Ruined"),
    ("Ruined", "Bowser"),
    ("Bowser", "Moon"),
]


def shuffle_entrances_standard(random) -> Dict[str, str]:
    """Standard mode: couple destinations among story hub exits (derangement-friendly shuffle).

    Returns mapping source_kingdom -> destination_kingdom for each vanilla exit.
    """
    sources = [a for a, _ in VANILLA_ENTRANCES]
    destinations = [b for _, b in VANILLA_ENTRANCES]
    # Shuffle destinations; retry if any fixed point-heavy self-loop on first edge only
    for _ in range(50):
        shuffled = destinations[:]
        random.shuffle(shuffled)
        mapping = {sources[i]: shuffled[i] for i in range(len(sources))}
        # Ensure Cascade still leads somewhere other than Cascade
        if mapping.get("Cascade") != "Cascade":
            return mapping
    return {a: b for a, b in VANILLA_ENTRANCES}
