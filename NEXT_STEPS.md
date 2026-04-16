# Agora Wiki-Backed Skills Completion Plan

**Date:** 2026-04-16
**Repository:** `agora-wiki`

## Goal
Finish the migration from the current bundled-reference Agora skills to a wiki-first skill system that is testable, routable, and safe around live-doc boundaries.

---

## Phase 1 — Complete content migration

### Objective
Move the remaining high-value stable knowledge into wiki pages and reduce duplication in the skill layer.

### Work items
1. RTC platform pages
   - react
   - nextjs
   - react-native
   - flutter
   - cross-platform coordination
2. RTM platform pages
   - advanced channel/topic behavior
   - pairing guidance with RTC on mobile/web
3. Conversational AI pages
   - quickstarts
   - auth-flow
   - python-sdk
   - go-sdk
   - agent-toolkit
   - agent-client-toolkit-react
   - agent-ui-kit
   - server-custom-llm
   - server-mcp
   - server-sdks
4. Server pages
   - tokens
   - production auth patterns
5. Testing pages
   - rtc-react
   - rtc-ios
   - rtc-android
   - mobile/rtm/renewal
   - broader convoai and server validation

### Exit criteria
- Every current reference file has either a migrated wiki page or an explicit live-doc-only note.

---

## Phase 2 — Strengthen skill layer

### Objective
Turn the current skeleton into a usable skill package.

### Work items
1. Expand `skills/SKILL.md` with clearer routing rules and examples.
2. Expand `skills/intake/SKILL.md` with product-combination decision trees.
3. Expand each `skills/products/*.md` file with:
   - exact wiki pages to read;
   - when to escalate to live docs;
   - common anti-patterns.
4. Keep `skills/shared/live-doc-policy.md` current.
5. Keep `skills/shared/repo-strategy.md` current.

### Exit criteria
- The skill layer can be read independently and still route correctly.

---

## Phase 3 — Real acceptance testing

### Objective
Test behavior, not just file existence.

### Work items
1. Create prompt-based acceptance cases across all major products.
2. Create routing expectation matrix.
3. Create live-doc escalation cases.
4. Create implementation-task testing-guidance cases.
5. Run the cases manually or via harness and capture outputs.

### Exit criteria
- 10–15 core prompt scenarios pass with expected routing and policy behavior.

---

## Phase 4 — Release prep

### Objective
Make the repository consumable.

### Work items
1. Commit and push all new work.
2. Add a concise install/use guide for the new skills.
3. Document migration notes from the old Agora skill structure.
4. Optionally add packaging/export instructions if you want to install this elsewhere.

### Exit criteria
- Repo is pushed, documented, and ready for downstream use.

---

## My recommendation
Do **not** claim full completion yet. The right next milestone is:

> Run prompt-based acceptance tests against the real runtime, then finish remaining migration gaps.

That is where this stops being a promising prototype and starts being a trustworthy skill system.
