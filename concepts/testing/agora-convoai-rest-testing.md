---
title: Agora ConvoAI REST Testing
created: 2026-04-16
updated: 2026-04-16
type: concept
status: draft
tags: [testing, convoai, rest-api, auth, payloads]
sources: [raw/skills/agora-testing-guidance.md]
---

# Agora ConvoAI REST Testing

Mock at the HTTP client layer, not the Agora SDK layer.

## Required assertions
- `Authorization` header is present
- `agent_rtc_uid` is a string
- `remote_rtc_uids` is an array of strings
- auth is sourced from environment/server configuration
- `/update` sends a full `params` object
- error responses surface `detail` / `reason`
