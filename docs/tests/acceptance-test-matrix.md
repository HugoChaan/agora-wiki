# Agora Wiki-Backed Skills Acceptance Test Matrix

**Status:** Draft
**Purpose:** Completion-level behavior tests for the wiki-backed Agora skill system.

## How to use this document
For each case:
1. Run the prompt against the target runtime using the new skills.
2. Record the actual routed skill, pages consulted, live-doc decision, and final answer shape.
3. Mark PASS / FAIL.
4. Link evidence (transcript, screenshot, or saved output).

---

## A. Routing cases

| ID | Prompt | Expected route | Intake required | Expected behavior |
|---|---|---|---|---|
| R1 | I need a React web video call with remote user rendering. | RTC | No | Routes directly to RTC/web guidance and relevant knowledge pages. |
| R2 | I want an AI voice agent in the same channel as users. | ConvoAI (+ RTC/RTM awareness) | Maybe | Recognizes multi-product relation, mentions RTC transport and transcript/event path. |
| R3 | I need to record calls and stream transcripts to my backend. | Intake -> Cloud Recording + RTM/ConvoAI | Yes | Identifies multi-product scenario before answering implementation details. |
| R4 | Generate a Go token server for production. | Server/token | No | Emphasizes App Certificate safety, production token requirement, and server-only secret handling. |
| R5 | How do I publish media from a Linux server into Agora? | Server Gateway | No | Routes to server-gateway guidance, not client SDK guidance. |

## B. Wiki-first knowledge cases

| ID | Prompt | Expected source behavior | Expected answer shape |
|---|---|---|---|
| W1 | RTC vs RTM | Wiki-first | Conceptual comparison, no live-doc lookup required. |
| W2 | When do I need RTM with RTC? | Wiki-first | Pattern-oriented answer referencing integration scenarios. |
| W3 | Why is my RTM user ID different from RTC UID? | Wiki-first | Explains identity model and mismatch pitfall clearly. |
| W4 | Why does ConvoAI recommend SDK over direct REST? | Wiki-first | Explains preferred path and when REST is acceptable. |

## C. Live-doc escalation cases

| ID | Prompt | Expected source behavior | Expected answer shape |
|---|---|---|---|
| L1 | What are the exact Cloud Recording start request fields? | Must escalate to live docs | Says exact schema should be verified from current docs. |
| L2 | What are the latest ConvoAI vendor/model config fields? | Must escalate to live docs | Refuses to answer from memory/wiki alone. |
| L3 | Give me the latest Agora error-code table for this SDK. | Must escalate to live docs | Uses live docs path, not static wiki-only answer. |
| L4 | What is the latest REST payload for agent join? | Must escalate to live docs | Points to current docs/OpenAPI source of truth. |

## D. Testing/implementation cases

| ID | Prompt | Expected policy behavior | Expected answer shape |
|---|---|---|---|
| T1 | Build an RTC web join flow. | Testing guidance required | Includes tests or explicit test stubs. |
| T2 | Build a ConvoAI backend integration. | Testing guidance required | Includes auth/payload/renewal validation expectations. |
| T3 | Build a token server in Node.js. | Testing guidance required | Includes token-expiry, renewal, and secret-handling tests. |
| T4 | Add RTM presence subscription flow. | Testing guidance required | Includes login-before-subscribe verification. |

## E. Migration coverage cases

| ID | Legacy area | Required outcome |
|---|---|---|
| M1 | rtc/README + platform docs | Wiki pages exist or explicit live-doc-only note exists. |
| M2 | rtm/README + platform docs | Wiki pages exist or explicit live-doc-only note exists. |
| M3 | conversational-ai docs | Wiki pages exist for stable guidance; live-doc policy for volatile details. |
| M4 | cloud-recording docs | Wiki pages exist; exact request fields marked live-doc-first. |
| M5 | server + token guidance | Wiki pages exist with security boundaries. |
| M6 | server-gateway docs | Wiki pages exist with routing distinction from client SDKs. |
| M7 | testing-guidance pages | Wiki/skill guidance exists for implementation verification. |

---

## Pass criteria
- All routing cases: PASS
- All wiki-first cases: PASS
- All live-doc cases: PASS
- All testing/implementation cases: PASS
- All migration coverage cases: PASS
- Evidence captured for every case
