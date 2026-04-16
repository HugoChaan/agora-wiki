---
title: Agora RTM Web SDK
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [rtm, web, signaling, presence, topics]
sources: [raw/skills/rtm-web.md]
---

# Agora RTM Web SDK

## What it is
Web RTM v2 uses the `agora-rtm` package for messaging, presence, signaling, and stream-channel topics.

## Core flow
1. Initialize RTM with app ID and string user ID.
2. Login before any subscribe or publish.
3. Subscribe to channels with explicit features.
4. Publish typed messages or structured JSON.
5. Listen for `message`, `presence`, and `status` events.
6. Unsubscribe and logout during cleanup.

## Important rules
- RTC and RTM channels are separate namespaces.
- Login must resolve before subscribe/publish.
- Presence requires `withPresence: true`.
- RTM identities are strings.
- Stream channels and message channels are different models.

## Common mistakes
- assuming RTC join also joins RTM;
- subscribing before login resolves;
- forgetting to request presence features;
- confusing channel messaging with stream-channel topic flows.
