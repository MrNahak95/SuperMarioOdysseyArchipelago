"""B3 — Painting unlock via Cloud moons + destination shuffle."""

# Warp paintings keyed by a stable id; destinations are kingdom stage names.
# Vanilla-ish set of major kingdom paintings (odyssey warp art).
painting_ids = [
    "Painting Cap",
    "Painting Cascade",
    "Painting Sand",
    "Painting Lake",
    "Painting Wooded",
    "Painting Lost",
    "Painting Metro",
    "Painting Snow",
    "Painting Seaside",
    "Painting Luncheon",
    "Painting Ruined",
    "Painting Bowser",
    "Painting Moon",
    "Painting Mushroom",
    "Painting Cloud",
]

# Default destination stage per painting (identity mapping before shuffle).
painting_default_destinations = {
    "Painting Cap": "CapWorldHomeStage",
    "Painting Cascade": "WaterfallWorldHomeStage",
    "Painting Sand": "SandWorldHomeStage",
    "Painting Lake": "LakeWorldHomeStage",
    "Painting Wooded": "ForestWorldHomeStage",
    "Painting Lost": "ClashWorldHomeStage",
    "Painting Metro": "CityWorldHomeStage",
    "Painting Snow": "SnowWorldHomeStage",
    "Painting Seaside": "SeaWorldHomeStage",
    "Painting Luncheon": "LavaWorldHomeStage",
    "Painting Ruined": "BossRaidWorldHomeStage",
    "Painting Bowser": "SkyWorldHomeStage",
    "Painting Moon": "MoonWorldHomeStage",
    "Painting Mushroom": "PeachWorldHomeStage",
    "Painting Cloud": "CloudWorldHomeStage",
}

# Item IDs 3900+
painting_item_table = {name: 3900 + i for i, name in enumerate(painting_ids)}
