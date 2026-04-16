---
title: Agora Token Renewal Testing
created: 2026-04-16
updated: 2026-04-16
type: concept
status: draft
tags: [testing, auth, tokens, rtm, rtc, mobile]
sources: [raw/skills/agora-testing-guidance.md]
---

# Agora Token Renewal Testing

Token renewal is a required production behavior across RTC and RTM flows.

## Coverage expectations
- RTC Web: token-privilege-will-expire should trigger renewal
- RTC iOS / Android: privilege-expiry callbacks should trigger renewal
- RTM Web / native: expired-token states should trigger re-login or token refresh flow

## Common assertions
- fresh token is fetched before expiry
- renew/login methods are called with the new token
- app state remains consistent during renewal
- no partial disconnect path is silently ignored
