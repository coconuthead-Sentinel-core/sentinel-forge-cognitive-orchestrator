# API Contract Governance

## Purpose
This document governs how the Sentinel Forge API contract is maintained for the current repository release.

## Contract Sources
- Human-readable API document: `../API.md`
- Example payloads: `../API_EXAMPLES.md`
- Executable routes: `../../backend/api.py`
- Executable WebSocket routes: `../../backend/ws_api.py`
- Typed schemas: `../../backend/schemas.py`
- Generated OpenAPI schema: `../engineering-build/openapi/openapi.generated.json`

## Contract Rules
- A route change requires the code, docs, and generated schema to be refreshed together.
- Placeholder endpoints are not allowed in active release docs.
- Compatibility routes may exist, but the canonical path must be identified explicitly in `docs/API.md`.
- Public behavior changes should be backed by tests.

## Current Release Decisions
- `/api/dashboard/metrics` is the canonical aggregated dashboard metrics route.
- `/api/dashboard/nexus-metrics` is retained as a narrower compatibility or legacy metrics surface.
- `/api/task/orchestrate/start` and `/api/task/orchestrate/stop` operate on the shared orchestrator instance.

## Sign-Off
- Owner review: Approved for current repository release
- Engineering review: Approved after validation refresh
