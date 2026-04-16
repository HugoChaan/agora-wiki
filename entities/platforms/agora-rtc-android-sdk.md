---
title: Agora RTC Android SDK
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [rtc, android, kotlin, sdk, permissions, tokens]
sources: [raw/skills/rtc-android.md]
---

# Agora RTC Android SDK

## Core flow
1. Request runtime permissions first.
2. Create `RtcEngine` with config and handler.
3. Enable video/audio and configure encoder options.
4. Setup local preview surface.
5. Join channel with `ChannelMediaOptions`.
6. Handle remote callbacks and token renewal.
7. Stop preview, leave, then destroy engine.

## Important rules
- Runtime camera/audio permission checks are mandatory.
- Handle `onTokenPrivilegeWillExpire` for renewal.
- Separate cleanup for leave vs full destroy.
- Android Bluetooth permissions matter for headset audio on newer versions.

## Common mistakes
- initializing before runtime permissions are granted;
- skipping `RtcEngine.destroy()`;
- ignoring renewal path in production;
- treating preview teardown as optional.
