---
title: RTC Platform Implementation Patterns
created: 2026-04-16
updated: 2026-04-16
type: pattern
status: draft
tags: [rtc, web, ios, android, platform-patterns, tokens]
sources: [raw/skills/rtc-web.md, raw/skills/rtc-ios.md, raw/skills/rtc-android.md]
---

# RTC Platform Implementation Patterns

## Shared pattern
Across Web, iOS, and Android, RTC implementations follow the same lifecycle:
- initialize engine/client,
- wire event/delegate handlers,
- join channel,
- publish local media,
- subscribe to remote media,
- renew tokens before expiry,
- clean up local media and engine resources.

## Platform differences
### Web
- event listeners must be registered before join;
- tracks must be stopped and closed explicitly;
- user-published is media-type specific.

### iOS
- shared engine + delegate pattern;
- Info.plist camera/mic permissions are required;
- remote setup is commonly performed in delegate callbacks.

### Android
- runtime permission gate comes first;
- `RtcEngine.destroy()` matters for full teardown;
- Bluetooth-related permissions can affect audio accessories.

## Design implication
The wiki should hold the shared lifecycle and major platform distinctions, while live docs should answer exact SDK method signatures and newest feature matrices.
