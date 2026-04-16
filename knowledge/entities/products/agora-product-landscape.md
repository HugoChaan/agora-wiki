---
title: Agora Product Landscape
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [architecture, routing, product-rtc, product-rtm, product-convoai, product-cloud-recording, product-token-service, product-server-gateway]
sources: [raw/skills/agora-intake.md]
---

# Agora Product Landscape

Agora's integration surface is not a single product. It is a product ecosystem with a few recurring combinations.

## Core products
- **RTC SDK** — real-time audio/video between users. This is the foundation for voice and video experiences.
- **RTM / Signaling** — messaging, signaling, presence, and metadata exchange.
- **Conversational AI** — server-driven AI voice agents that join RTC channels.
- **Cloud Recording** — server-side recording of RTC sessions.
- **Server / Tokens** — token generation and auth infrastructure.
- **Server Gateway SDK** — server-side media streaming on Linux.

## Product relationships
- [[agora-rtc]] is the foundation layer for human audio/video sessions.
- [[agora-conversational-ai]] depends on RTC because the AI agent joins an RTC channel.
- Cloud Recording depends on RTC because it records activity inside RTC channels.
- [[agora-rtm]] is independent, but often paired with RTC or ConvoAI for chat, presence, signaling, and transcript delivery.
- [[agora-authentication-and-token-model]] cuts across the whole stack.

## Common product combinations
- RTC only — basic voice/video calling.
- RTC + RTM — media plus chat, signaling, or presence.
- ConvoAI + RTC — AI voice agent with client-side media.
- ConvoAI + RTC + RTM — AI voice agent plus transcripts, state events, or messaging.
- RTC + Cloud Recording — media with session recording.
- ConvoAI + RTC + Cloud Recording — AI interactions with archival or QA capture.

## Why this matters for agent behavior
A good assistant should not jump directly into a single product guide when the user's request is vague. It should first identify:
1. the primary product,
2. supporting products,
3. optional products.

That routing behavior is why the skill layer still matters even if the stable knowledge moves into this wiki.

## Related pages
- [[agora-rtc]]
- [[agora-rtm]]
- [[agora-conversational-ai]]
- [[agora-authentication-and-token-model]]
- [[rtc-plus-rtm-integration]]
