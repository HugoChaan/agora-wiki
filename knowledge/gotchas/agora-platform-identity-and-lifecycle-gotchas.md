---
title: Agora Platform Identity and Lifecycle Gotchas
created: 2026-04-16
updated: 2026-04-16
type: gotcha
status: draft
tags: [gotcha, rtc, rtm, identity, lifecycle, cleanup]
sources: [raw/skills/rtc-web.md, raw/skills/rtc-ios.md, raw/skills/rtc-android.md, raw/skills/rtm-web.md, raw/skills/rtm-ios.md, raw/skills/rtm-android.md]
---

# Agora Platform Identity and Lifecycle Gotchas

## Identity mismatch
RTC commonly uses numeric UIDs while RTM uses string identities. Any mixed RTC + RTM flow must make that mapping explicit.

## Login / subscribe ordering
RTM login completion must happen before subscribe or publish. Treating subscribe as if it can race login is a classic bug.

## Cleanup incompleteness
- RTC Web: forgetting `close()` keeps devices locked.
- RTC native: forgetting engine destroy/release leaves resources hanging.
- RTM native: skipping destroy/release can leak client state.

## Token complacency
Tokenless examples may work for testing, but production flows must renew tokens before expiry and handle failure paths.
