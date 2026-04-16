---
title: Agora Authentication and Token Model
created: 2026-04-16
updated: 2026-04-16
type: concept
status: draft
tags: [auth, security, product-token-service, product-rtc, product-rtm, product-convoai, platform-server]
sources: [raw/skills/server-readme.md, raw/skills/conversational-ai-readme.md]
---

# Agora Authentication and Token Model

Authentication is one of the few concerns that spans almost every Agora product.

## Core rules
- Production systems should always use tokens.
- Token generation must happen server-side.
- App Certificate must never be exposed to client code.
- If a project has no App Certificate enabled, the user should be warned explicitly before any tokenless development shortcut is suggested.

## Token types
- **RTC Token** — grants access to a specific RTC channel and UID.
- **RTM Token** — grants access to RTM services for a specific user identity.
- **AccessToken2** — current token format that can bundle privileges across services.

## ConvoAI auth guidance
For direct REST access to Conversational AI, token auth is preferred over Basic Auth for new systems because it limits blast radius and aligns better with app-level access control.

## Design implications
Auth is not a side topic. It affects:
- join flows,
- identity mapping,
- renewal behavior,
- backend architecture,
- production readiness.

That is why auth should live both in the wiki and in skill-level guardrails.

## Related pages
- [[agora-rtc]]
- [[agora-rtm]]
- [[agora-conversational-ai]]
- [[agora-product-landscape]]
- [[agora-common-integration-gotchas]]
