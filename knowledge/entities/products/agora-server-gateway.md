---
title: Agora Server Gateway
created: 2026-04-16
updated: 2026-04-16
type: entity
status: draft
tags: [product-server-gateway, platform-server, platform-linux, media, architecture, gotcha]
sources: [raw/skills/server-gateway-readme.md]
---

# Agora Server Gateway

[[agora-product-landscape]] | [[agora-rtc]] | [[agora-live-doc-fetch-policy]]

## Summary
Agora Server Gateway is a self-hosted Linux SDK for sending and receiving real-time media between server-side processes and Agora RTC channels.

## Critical rules
- The paired RTC channel must use `LIVE_BROADCASTING`, not `COMMUNICATION`.
- PCM audio must be sent in exact 10 ms frames.
- AAC audio cannot use 44.1 kHz sampling.
- SDK operations are asynchronous; behavior should be driven by callbacks and observers.
- The host must be able to reach `*.agora.io` and `*.agoralab.co`.
- This is an SDK running in your Linux process, not a cloud REST product.

## Architecture
Typical flow:
1. Initialize `IAgoraService` with audio/video enabled.
2. Create one `IRtcConnection` per channel and join.
3. Create senders/receivers via `IMediaNodeFactory`.
4. Publish local tracks or register observers for incoming media.
5. Shutdown in strict order: unpublish -> unregister observers -> disconnect -> release objects.

## Use cases
- server-side voice agents
- AI media processing pipelines
- network testing rigs
- application platform media bridges

## Live-doc boundary
Keep lifecycle and deployment constraints here. Fetch live docs for Java/Go/Python exact APIs, SDK download links, and current platform requirements.
