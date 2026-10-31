#pragma once

#include "types.h"

// Ability indices must match World/smo/Abilities.py ability_items order (3800+).
enum AbilityIndex : int {
    ABI_LongJump = 0,
    ABI_Roll = 1,
    ABI_GroundPound = 2,
    ABI_Dive = 3,
    ABI_GroundPoundJump = 4,
    ABI_UpwardThrow = 5,
    ABI_DownwardThrow = 6,
    ABI_SpinThrow = 7,
    ABI_CapJump = 8,
    ABI_HomingCapThrow = 9,
    ABI_BackwardSomersault = 10,
    ABI_SideSomersault = 11,
    ABI_TripleJump = 12,
    ABI_WallJump = 13,
    ABI_HoldThrow = 14,
    ABI_Swim = 15,
    ABI_QuickSwim = 16,
    ABI_Spin = 17,
    ABI_Dash2D = 18,
    ABI_Jaxi = 19,
    ABI_MotorScooter = 20,
    ABI_COUNT = 21
};

// Kingdom indices for entrance map (Entrances.VANILLA_ENTRANCES sources).
enum EntranceKingdom : int {
    ENT_Cascade = 0,
    ENT_Sand = 1,
    ENT_Lake = 2,
    ENT_Wooded = 3,
    ENT_Cloud = 4,
    ENT_Lost = 5,
    ENT_Metro = 6,
    ENT_Snow = 7,
    ENT_Seaside = 8,
    ENT_Luncheon = 9,
    ENT_Ruined = 10,
    ENT_Bowser = 11,
    ENT_COUNT = 12
};

constexpr int PAINTING_COUNT = 15;
constexpr int ENTRANCE_COUNT = ENT_COUNT;

// Returns ability index for a player anim name, or -1 if not gated.
int abilityIndexForAnim(const char* animName);

// Stage helpers for entrance / painting remaps.
int kingdomIndexForStage(const char* stageName);
const char* stageForKingdomIndex(int kingdomIndex);
const char* kingdomNameForIndex(int kingdomIndex);
int kingdomIndexForName(const char* kingdomName);
