---
title: Agora Common Integration Gotchas
created: 2026-04-16
updated: 2026-04-16
type: gotcha
status: draft
tags: [gotcha, auth, identity, events, product-rtc, product-rtm, product-convoai]
sources: [raw/skills/rtc-readme.md, raw/skills/rtm-readme.md, raw/skills/conversational-ai-readme.md]
---

# Agora Common Integration Gotchas

This page tracks recurring mistakes that cause wasted debugging time.

## RTC
- Registering event handlers after join and then wondering why existing users were missed.
- Forgetting to stop and close local tracks, which can leak devices and media resources.
- Ignoring token renewal or joining with a UID that does not match the token.

## RTM
- Treating RTM identities as numeric instead of strings.
- Assuming RTC and RTM channels are automatically connected.
- Using v1 API patterns with RTM v2.
- Forgetting that presence requires active subscription.

## ConvoAI
- Sending `agent_rtc_uid` as an integer.
- Treating `/join` success like immediate in-channel presence.
- Sending partial nested `params` to `/update` and wiping previous config.
- Enabling only one of the two flags required for RTM-based transcript and event delivery.

## Cross-product
- Trying to answer schema-level questions from cached prose instead of fetching live docs.
- Treating stable guidance and volatile API truth as the same class of information.

## Related pages
- [[agora-rtc]]
- [[agora-rtm]]
- [[agora-conversational-ai]]
- [[agora-authentication-and-token-model]]
- [[agora-live-doc-fetch-policy]]
