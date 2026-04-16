---
title: Agora RTM iOS SDK
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [rtm, ios, swift, signaling, presence]
sources: [raw/skills/rtm-ios.md]
---

# Agora RTM iOS SDK

## Core flow
1. Create `AgoraRtmClientKit` with config and delegate.
2. Login with a server-generated RTM token.
3. Subscribe to channels with message/presence features.
4. Publish typed messages or peer/user-channel messages.
5. Handle message and presence delegate callbacks.
6. Unsubscribe, logout, and destroy during cleanup.

## Important rules
- Constructor can throw; use `do/catch`.
- RTM user IDs are strings.
- Wait for login completion before subscribe/publish.
- When pairing with RTC, convert numeric RTC UID to string as needed.

## Common mistakes
- skipping error handling around constructor or login;
- mixing RTC numeric IDs with RTM string IDs;
- publishing before login completion;
- forgetting destroy on teardown.
