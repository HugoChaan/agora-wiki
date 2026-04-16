---
title: Agora RTM Android SDK
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [rtm, android, kotlin, signaling, presence]
sources: [raw/skills/rtm-android.md]
---

# Agora RTM Android SDK

## Core flow
1. Create `RtmClient` from config with event listener.
2. Login with server-generated token.
3. Subscribe to channels with message/presence options.
4. Publish channel or user-channel messages.
5. Handle presence and message callbacks in listener.
6. Unsubscribe, logout, and release in cleanup.

## Important rules
- Login completion must happen before subscribe.
- Presence and messaging are opt-in features on subscription.
- RTM user IDs are strings even if RTC UIDs elsewhere are numeric.
- Cleanup should release client even on logout failure.

## Common mistakes
- not sequencing login before subscribe;
- confusing `publish` channel types;
- incomplete cleanup paths;
- assuming presence events exist without enabling them.
