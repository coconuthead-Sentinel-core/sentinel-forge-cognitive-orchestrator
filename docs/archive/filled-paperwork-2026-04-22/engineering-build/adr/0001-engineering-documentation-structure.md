# ADR 0001: Establish A Named Engineering Documentation Structure

## Status
Accepted

## Date
2026-04-22

## Context
The repository had working code, SDLC notes, legal paperwork, and compliance documents, but no single engineering-build index showing where architecture, API, message flow, threat modeling, and AI governance artifacts lived. The Codex project-development paperwork package requires named homes for those artifacts.

## Decision
Create `docs/engineering-build/` as the routing layer for:
- arc42
- ADR/MADR
- C4
- OpenAPI
- AsyncAPI
- threat modeling
- AI governance
- NIST AI RMF

The existing validated repo documents remain authoritative. The engineering-build suite points to them and adds missing connective paperwork.

## Consequences
- The repo now has a deterministic paperwork entry point.
- Future contributors can find the architecture and compliance stack without guessing.
- Documentation claims can be reviewed against a stable index before release.
