---
title: Agora RTC Web SDK
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [rtc, web, sdk, platform-web, events, tokens]
sources: [raw/skills/rtc-web.md]
---

# Agora RTC Web SDK

## What it is
The modern Web SDK is `agora-rtc-sdk-ng` (4.x). Do not use deprecated `agora-rtc-sdk` 3.x for new work.

## Core flow
1. Create client with explicit mode and codec.
2. Register event handlers before join.
3. Join channel.
4. Create local tracks.
5. Publish local tracks.
6. Subscribe on `user-published`.
7. Stop and close tracks before leave.

## Important rules
- Register handlers before `join()`.
- Use server-generated tokens in production.
- Handle both `token-privilege-will-expire` and `token-privilege-did-expire`.
- `user-published` fires separately for audio and video.
- Always `stop()` then `close()` local tracks.

## Common mistakes
- joining before event handlers are wired;
- forgetting to close tracks, leaving camera or microphone locked;
- assuming publish/subscribe is symmetric across live and rtc modes;
- treating volatile codec/version details as static knowledge.
