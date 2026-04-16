---
title: Agora Cloud Recording
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [product-cloud-recording, rest-api, auth, platform-server, architecture, gotcha]
sources: [raw/skills/cloud-recording-readme.md]
---

# Agora Cloud Recording

[[agora-product-landscape]] | [[agora-authentication-and-token-model]] | [[agora-live-doc-fetch-policy]]

## Summary
Agora Cloud Recording is a server-side REST product for recording active RTC channels. It depends on an existing RTC session and uses Agora REST authentication rather than client SDK tokens.

## Lifecycle
```text
acquire -> start -> [query] -> stop
```

The critical operational rule is that `resourceId` expires 5 minutes after `acquire`, so `start` must happen quickly.

## Core rules
- Cloud Recording must be enabled in Agora Console before use.
- The target RTC channel must already have active participants.
- Always call `stop` to avoid unnecessary billing and dangling sessions.
- Auth uses HTTP Basic Auth with `AGORA_CUSTOMER_KEY` and `AGORA_CUSTOMER_SECRET`.
- Full field-level storage and layout details should be fetched live from official docs.

## Modes
- `individual` — one file per user stream; useful for post-processing and transcription.
- `mix` — one mixed output file; useful for playback and archival.
- `web` — records rendered web content for browser-based workflows.

## Common failures
- `403` often means the feature is not enabled in Console.
- `404` often means `resourceId` expired or `sid` is wrong.
- `432` means a recording session is already active.
- `435` means no one is currently in the RTC channel.
- Storage failures usually come from wrong bucket settings or credentials.

## Live-doc boundary
Keep lifecycle and auth guidance in the wiki. Fetch live docs for exact request/response schemas, storage vendor fields, composite layout parameters, and current error listings.
