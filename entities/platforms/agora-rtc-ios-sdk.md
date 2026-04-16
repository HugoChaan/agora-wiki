---
title: Agora RTC iOS SDK
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [rtc, ios, swift, sdk, tokens, delegates]
sources: [raw/skills/rtc-ios.md]
---

# Agora RTC iOS SDK

## Core flow
1. Configure `AgoraRtcEngineConfig` with app ID and channel profile.
2. Create shared engine with delegate.
3. Enable video/audio as needed.
4. Prepare local preview canvas.
5. Join channel with media options.
6. Handle delegate callbacks for remote users and token renewal.
7. Stop preview, leave, and destroy on full cleanup.

## Important rules
- Add camera and microphone usage descriptions to Info.plist.
- Renew tokens in `tokenPrivilegeWillExpire`.
- Setup remote video in `didJoinedOfUid`.
- Pair RTC numeric UIDs carefully with RTM string identities.

## Common mistakes
- missing Info.plist permissions;
- not destroying the engine on teardown;
- assuming tokenless flows are acceptable in production;
- mixing RTC UID semantics with RTM userId semantics.
