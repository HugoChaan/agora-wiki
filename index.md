# Agora Wiki Index

> Structured knowledge base for Agora integrations.
> Last updated: 2026-04-16 | Total pages: 63 markdown files in repo

## Entities
- [[agora-product-landscape]] — Overview of the Agora product ecosystem and how RTC, RTM, ConvoAI, Cloud Recording, token services, and Server Gateway relate.
- [[agora-rtc]] — Real-time audio/video foundation product, critical rules, channel profiles, and platform guidance.
- [[agora-rtm]] — Signaling and messaging layer, channel types, presence model, and RTC coordination guidance.
- [[agora-conversational-ai]] — REST-driven voice agent platform, lifecycle, auth defaults, and implementation guidance.
- [[agora-cloud-recording]] — Cloud recording lifecycle, auth model, recording modes, and operational traps.
- [[agora-server-gateway]] — Self-hosted server-side media bridge, lifecycle, media constraints, and deployment rules.

## Concepts
- [[agora-authentication-and-token-model]] — Token requirements, App Certificate boundaries, and auth choices across RTC, RTM, and ConvoAI.
- [[agora-live-doc-fetch-policy]] — What belongs in stable wiki pages versus what must be fetched from live docs.

## Patterns
- [[rtc-plus-rtm-integration]] — Recommended way to combine RTC media with RTM signaling and presence.
- [[rtc-platform-implementation-patterns]] — Shared RTC lifecycle with key Web/iOS/Android distinctions.
- [[rtm-platform-implementation-patterns]] — Shared RTM login/subscription lifecycle with platform differences.

## Gotchas
- [[agora-common-integration-gotchas]] — Cross-product failure modes and subtle integration traps worth checking early.
- [[agora-platform-identity-and-lifecycle-gotchas]] — UID/userId mismatches, cleanup misses, and token complacency.

## Testing Concepts
- [[agora-testing-completeness-gate]]
- [[agora-token-renewal-testing]]
- [[agora-rtc-web-testing]]
- [[agora-convoai-rest-testing]]

## Validation Docs
- `docs/tests/acceptance-test-matrix.md`
- `docs/tests/execution-template.md`
- `docs/tests/final-acceptance-plan.md`

## Platform Entities
- [[agora-rtc-web-sdk]]
- [[agora-rtc-ios-sdk]]
- [[agora-rtc-android-sdk]]
- [[agora-rtm-web-sdk]]
- [[agora-rtm-ios-sdk]]
- [[agora-rtm-android-sdk]]
