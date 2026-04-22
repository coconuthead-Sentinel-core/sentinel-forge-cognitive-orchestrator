# Threat Model

## Scope
- System in scope: Sentinel Forge Cognitive AI Orchestration Platform
- Review date: 2026-04-22
- Reviewer: Codex-prepared, owner-approved release pending

## Assets
- source code and generated review paperwork
- chat inputs and model outputs
- symbolic rules, seeds, and cognition thread state
- optional Azure credentials and optional Cosmos-backed data
- local JSON persistence artifacts

## Trust Boundaries
- browser or API client to FastAPI
- WebSocket client to EventBus-backed streams
- application to optional Azure services
- application to local filesystem persistence

## Entry Points
- HTTP endpoints under `/api`
- WebSocket endpoints under `/ws`
- local scripts under `scripts/`
- dashboard HTML routes

## Threats
| ID | Threat | Affected Asset | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|---|
| TD-001 | Unauthenticated use of routes in permissive local mode | API surface and state | Medium | Medium | document current auth posture clearly and keep WebSocket key support available | Controlled |
| TD-002 | Credential leakage through docs or logs | cloud credentials | Low | High | keep mock-mode workflow primary for review, maintain `SECURITY.md`, avoid hardcoded secrets | Controlled |
| TD-003 | Stale paperwork causes unsafe operator assumptions | reviewers and operators | Medium | Medium | active docs routed through `docs/README.md`, older packets archived, CNO validation before push | Controlled |
| TD-004 | Event listener leaks or orphan subscriptions | runtime stability | Low | Medium | shared orchestrator now unsubscribes its raw-event queue on stop | Controlled |
| TD-005 | Malformed symbolic input causes misleading behavior | symbolic outputs and reviewer trust | Medium | Low | glyph parsing and validation routes plus lens/firewall tests | Controlled |

## Residual Risk
- HTTP route authentication is not yet uniformly enforced across all endpoints.
- Cloud deployment controls are not part of the current review-release scope.

## Verification
- `python -m pytest -q`
- `python scripts/smoke_test.py`
- route/documentation coherence review in this completion pass
