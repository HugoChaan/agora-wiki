---
title: RTC Plus RTM Integration
created: 2026-04-16
updated: 2026-04-16
type: pattern
status: draft
tags: [product-rtc, product-rtm, architecture, identity, channels, events]
sources: [raw/skills/rtm-readme.md, raw/skills/rtc-readme.md, raw/skills/agora-intake.md]
---

# RTC Plus RTM Integration

RTC and RTM are separate systems that often work best together.

## Recommended default pattern
1. Join the RTC channel first.
2. Resolve or derive the user's RTC UID.
3. Convert that identity into the RTM identity format, commonly `String(rtcUid)`.
4. Login to RTM.
5. Subscribe to the RTM channel.
6. Use RTC for audio/video and RTM for chat, signaling, transcripts, or state messages.

## Why this pattern works
- Media and signaling have different transport and lifecycle concerns.
- Using a mapped identity makes cross-system debugging simpler.
- Matching channel names across RTC and RTM is a useful convention even though they are still separate namespaces.

## Common uses
- Voice/video calls with text chat
- Presence-aware communication apps
- Conversational AI apps that need transcript or agent-state delivery over RTM

## Failure modes to watch
- Assuming RTC join auto-subscribes RTM
- Forgetting RTM login before subscribe/publish
- Mixing numeric RTC IDs with string RTM IDs
- Missing transcript events because required ConvoAI flags were only partially enabled

## Related pages
- [[agora-rtc]]
- [[agora-rtm]]
- [[agora-product-landscape]]
- [[agora-common-integration-gotchas]]
