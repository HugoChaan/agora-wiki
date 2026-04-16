# Agora Wiki

Structured markdown wiki for Agora integration knowledge.

## Purpose
This repository captures stable, high-signal integration knowledge from the Agora skills layer and organizes it into an interlinked wiki.

It is not meant to replace official docs for fast-moving API details. Instead:
- the wiki stores stable concepts, relationships, patterns, and gotchas;
- `raw/` stores source snapshots;
- exact schemas and volatile parameters should still be fetched from official live docs.

## Start Here
- Read [[SCHEMA.md]]
- Read [[index.md]]
- Check [[log.md]] for recent updates

## Initial scope
- Agora product landscape
- RTC
- RTM / Signaling
- Conversational AI
- Authentication and token model
- Live-doc fetch policy
- Initial integration patterns and gotchas

## Repository layout

- `entities/`, `concepts/`, `patterns/`, `gotchas/` — stable Agora knowledge
- `skills/` — wiki-backed skill definitions and routing rules
- `raw/` — imported source snapshots and future official-doc captures

## Current direction

This repository now serves both as the knowledge base and as the design home for a new wiki-first Agora skill system. The skills should read from this wiki, preserve routing and live-fetch guardrails, and avoid duplicating large reference bundles.

## Validation assets
- `tests/` contains structural checks for the skill prototype.
- `docs/tests/` contains prompt-based acceptance test planning and execution templates.
