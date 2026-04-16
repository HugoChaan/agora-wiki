---
title: Agora RTC
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [product-rtc, media, events, channels, platform-web, sdk, architecture, gotcha]
sources: [raw/skills/rtc-readme.md]
---

# Agora RTC

Agora RTC is the real-time media foundation for voice and video communication. Users join channels, publish local tracks, and subscribe to remote tracks.

## Critical rules
1. Register event handlers before joining, or you may miss users who are already present.
2. `user-published` fires separately for audio and video; treat them as separate events.
3. Clean up local tracks with `stop()` and then `close()` before dropping references.
4. Web SDK usage requires HTTPS except on localhost.
5. Production deployments need token renewal handling, and the UID used to join must match the UID encoded in the token.
6. Use audience/subscriber roles for non-publishing users in production to reduce unauthorized publishing risk.

## Channel profiles
- `rtc` — communication mode for calls and conferences.
- `live` — host/audience mode for streaming scenarios.

## Cross-platform notes
- Web, iOS, and Android differ in UID types, media defaults, and orientation behavior.
- RTM uses string identities, so a common convention is `String(rtcUid)` when pairing RTC and RTM.
- Codec and dual-stream configuration should be aligned across platforms when building multi-client experiences.

## What belongs here vs live docs
This page should capture stable rules and integration guidance. Exact encoder settings, error codes, release notes, and niche platform details belong to [[agora-live-doc-fetch-policy]].

## Related pages
- [[agora-product-landscape]]
- [[agora-rtm]]
- [[agora-authentication-and-token-model]]
- [[rtc-plus-rtm-integration]]
- [[agora-common-integration-gotchas]]
