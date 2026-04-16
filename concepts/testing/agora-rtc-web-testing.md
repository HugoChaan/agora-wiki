---
title: Agora RTC Web Testing
created: 2026-04-16
updated: 2026-04-16
type: concept
status: draft
tags: [testing, rtc, web, jest, events]
sources: [raw/skills/agora-testing-guidance.md]
---

# Agora RTC Web Testing

Mock `agora-rtc-sdk-ng` at the module boundary.

## Required mocked boundaries
- `createClient()`
- microphone/camera track factories
- `client.on()` event registration

## Core assertions
- joins the correct channel and UID
- publishes expected tracks
- subscribes after `user-published`
- renews token before expiry
- stops and closes tracks before leave
