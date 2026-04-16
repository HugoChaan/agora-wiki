---
title: Agora RTM
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [product-rtm, channels, identity, events, sdk, gotcha]
sources: [raw/skills/rtm-readme.md]
---

# Agora RTM

Agora RTM, now positioned as the Signaling SDK, provides text messaging, signaling, presence, and metadata exchange. It can be used independently, but it is often paired with RTC or Conversational AI.

## Default use cases
- Text chat during calls
- Signaling such as invitations and hang-up messages
- Presence and online-state tracking
- Custom data exchange
- Receiving Conversational AI transcripts and state events

## Channel model
RTM has two different channel types:
- **Message channels** — the default choice for most products and apps.
- **Stream channels** — better for topic-based filtering or higher-frequency updates.

## Critical rules
- RTM identities are strings, not RTC-style numeric UIDs.
- RTC and RTM channel namespaces are independent even if they share the same name.
- Login must complete before subscribe, publish, or presence operations.
- Presence events require an active subscription.
- RTM v2 is not compatible with v1 API usage patterns.
- ConvoAI transcript delivery through RTM requires two join flags, not just one.

## Coordination with RTC
The most common pattern is:
1. join RTC,
2. derive an RTM identity from the RTC identity,
3. login to RTM,
4. subscribe to the RTM channel,
5. use RTC for media and RTM for state, messages, and control flow.

This pattern is described in [[rtc-plus-rtm-integration]].

## Related pages
- [[agora-product-landscape]]
- [[agora-rtc]]
- [[rtc-plus-rtm-integration]]
- [[agora-common-integration-gotchas]]
