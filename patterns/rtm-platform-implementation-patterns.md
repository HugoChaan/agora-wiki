---
title: RTM Platform Implementation Patterns
created: 2026-04-16
updated: 2026-04-16
type: pattern
status: draft
tags: [rtm, signaling, web, ios, android, presence]
sources: [raw/skills/rtm-web.md, raw/skills/rtm-ios.md, raw/skills/rtm-android.md]
---

# RTM Platform Implementation Patterns

## Shared pattern
Across platforms, RTM flows require:
- string-based identities,
- explicit login before subscribe or publish,
- feature-aware subscription,
- message + presence listeners,
- explicit cleanup.

## Platform differences
### Web
- stream channels introduce topic-specific flows;
- event listener model uses `addEventListener`.

### iOS
- constructor can throw;
- delegate methods surface message/presence updates.

### Android
- listener object is configured at client creation;
- release should happen even if logout fails.

## Design implication
Wiki pages should explain namespace separation from RTC and the stable login/subscription sequence. Live docs should cover exact API details, limits, and latest topic/channel features.
