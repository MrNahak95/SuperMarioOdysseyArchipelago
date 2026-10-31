#include "server/RuntimeMaps.hpp"
#include "al/util.hpp"
#include <cstring>

struct AnimGate {
    const char* anim;
    int ability;
};

// Substring / exact anim names → ability. Checked with isPartOf-style contains or equal.
static const AnimGate sAnimGates[] = {
    {"LongJump", ABI_LongJump},
    {"ContinuousLongJump", ABI_LongJump},
    {"Rolling", ABI_Roll},
    {"HipDrop", ABI_GroundPound},
    {"SwimHipDrop", ABI_GroundPound},
    {"JumpHipDrop", ABI_GroundPoundJump},
    {"SwimJumpHipDrop", ABI_GroundPoundJump},
    {"Dive", ABI_Dive},
    {"DiveInWater", ABI_Dive},
    {"SwimDive", ABI_Dive},
    {"CatchCapJump", ABI_CapJump},
    {"SpinCapJump", ABI_CapJump},
    {"SpinCap", ABI_Spin},
    {"SpinSeparate", ABI_Spin},
    {"BackFlip", ABI_BackwardSomersault},
    {"SideFlip", ABI_SideSomersault},
    {"TripleJump", ABI_TripleJump},
    {"WallJump", ABI_WallJump},
    {"WallKeep", ABI_WallJump},
    {"WallCatch", ABI_WallJump},
    {"SwimHeadSliding", ABI_QuickSwim},
    {"SwimSurface", ABI_Swim},
    {"Swim", ABI_Swim},
    {"Squat", ABI_HoldThrow}, // carry/hold often starts from squat; imperfect but blocks hold path
};

int abilityIndexForAnim(const char* animName) {
    if (!animName || !animName[0])
        return -1;
    for (unsigned i = 0; i < sizeof(sAnimGates) / sizeof(sAnimGates[0]); i++) {
        // Prefer prefix / contained match for variants (HipDropStart, RollingEnd, …)
        if (strstr(animName, sAnimGates[i].anim) != nullptr)
            return sAnimGates[i].ability;
    }
    return -1;
}

static const char* sKingdomStages[ENT_COUNT] = {
    "WaterfallWorldHomeStage", // Cascade
    "SandWorldHomeStage",
    "LakeWorldHomeStage",
    "ForestWorldHomeStage",
    "CloudWorldHomeStage",
    "ClashWorldHomeStage",
    "CityWorldHomeStage",
    "SnowWorldHomeStage",
    "SeaWorldHomeStage",
    "LavaWorldHomeStage",
    "BossRaidWorldHomeStage",
    "SkyWorldHomeStage",
};

static const char* sKingdomNames[ENT_COUNT] = {
    "Cascade", "Sand", "Lake", "Wooded", "Cloud", "Lost",
    "Metro", "Snow", "Seaside", "Luncheon", "Ruined", "Bowser",
};

int kingdomIndexForStage(const char* stageName) {
    if (!stageName)
        return -1;
    for (int i = 0; i < ENT_COUNT; i++) {
        if (al::isEqualString(stageName, sKingdomStages[i]))
            return i;
    }
    // Also accept Moon as non-entrance-table stage for painting lookups
    return -1;
}

const char* stageForKingdomIndex(int kingdomIndex) {
    if (kingdomIndex < 0 || kingdomIndex >= ENT_COUNT)
        return nullptr;
    return sKingdomStages[kingdomIndex];
}

const char* kingdomNameForIndex(int kingdomIndex) {
    if (kingdomIndex < 0 || kingdomIndex >= ENT_COUNT)
        return nullptr;
    return sKingdomNames[kingdomIndex];
}

int kingdomIndexForName(const char* kingdomName) {
    if (!kingdomName)
        return -1;
    for (int i = 0; i < ENT_COUNT; i++) {
        if (al::isEqualString(kingdomName, sKingdomNames[i]))
            return i;
    }
    return -1;
}
