#pragma once

#include "Packet.h"

struct PACKED SlotData : Packet {
    SlotData() : Packet() {
        this->mType = PacketType::SLOTDATA;
        mPacketSize = sizeof(SlotData) - sizeof(Packet);
    };
    ushort cascade = 0;
    ushort sand = 0;
    ushort wooded = 0;
    ushort lake = 0;
    ushort lost = 0;
    ushort metro = 0;
    ushort seaside = 0;
    ushort snow = 0;
    ushort luncheon = 0;
    ushort ruined = 0;
    ushort bowser = 0;
    ushort dark = 0;
    ushort darker = 0;
    bool regionals = false;
    bool captures = false;
    // Phase B flags (appended — keep order stable)
    bool abilityLock = false;
    bool paintingUnlock = false;
    u8 entranceMode = 0; // 0=off, 1=standard, 2=chains, 3=limited, 4=decoupled
};
