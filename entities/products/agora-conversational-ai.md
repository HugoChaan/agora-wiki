---
title: Agora Conversational AI
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [product-convoai, rest-api, auth, architecture, sdk, platform-nodejs, platform-python, platform-go, gotcha, live-docs]
sources: [raw/skills/conversational-ai-readme.md]
---

# Agora Conversational AI

Agora Conversational AI is a REST-driven voice agent platform. Your server starts and controls agents, and the agents join RTC channels to speak with users.

## Default guidance
- For new projects, start from an official or curated quickstart rather than building from scratch.
- If the user's backend language has an SDK, prefer the SDK over direct REST calls.
- Use direct REST mainly for languages without an SDK or for deliberately lower-level integrations.

## Architecture
1. Your server sends a `/join` request with agent configuration.
2. Agora creates an agent session.
3. The agent joins an RTC channel.
4. Users interact with the agent through RTC media, while transcripts or state updates can flow through RTC data channels or RTM.

## Important operational rules
- `agent_rtc_uid` is a string, not an integer.
- `remote_rtc_uids` must be an array of strings.
- Agent names must be unique per project.
- Success from `POST /join` means the agent is starting, not that it has already appeared in the RTC channel.
- `/update` overwrites nested `params` objects, so partial updates can accidentally erase fields.
- Token auth should be the default for new direct REST integrations.

## What should stay out of the wiki
This page should not try to freeze full request/response schemas, vendor-specific model parameters, or release-note-level details. Those belong to [[agora-live-doc-fetch-policy]] and should be fetched live.

## Related pages
- [[agora-product-landscape]]
- [[agora-authentication-and-token-model]]
- [[agora-rtm]]
- [[agora-live-doc-fetch-policy]]
- [[agora-common-integration-gotchas]]
