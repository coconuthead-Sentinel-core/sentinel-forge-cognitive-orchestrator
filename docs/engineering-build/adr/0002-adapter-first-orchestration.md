# ADR 0002: Use Adapter-First Orchestration With Mock-Safe Fallback

## Context And Problem Statement
- The project needs a stable chat/orchestration surface that works both with optional cloud integrations and without them.
- A review-ready repository cannot require live Azure access to validate its core behavior.

## Decision Drivers
- Keep local validation deterministic.
- Preserve the chat contract exposed by `/api/chat`.
- Avoid breaking the repository when cloud credentials are absent.

## Considered Options
1. Require live Azure-backed inference for all chat processing.
2. Use only an internal synthetic response engine.
3. Prefer the configured adapter path and fall back safely when the adapter fails or is unavailable.

## Decision Outcome
Chosen option: 3. Prefer the configured adapter path and fall back safely when the adapter fails or is unavailable.

### Positive Consequences
- Mock mode remains viable for tests and smoke checks.
- Cloud integrations remain additive rather than mandatory.
- The chat contract stays stable for callers.

### Negative Consequences
- The system has multiple execution paths that must stay aligned.
- Reviewers need documentation to understand which path is active.

## Links
- Related docs:
  - `../../../backend/services/cognitive_orchestrator.py`
  - `../../../README.md`
  - `../openapi/README.md`
