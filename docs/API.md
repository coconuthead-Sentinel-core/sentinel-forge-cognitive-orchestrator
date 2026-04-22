# API Contract Template

## Status
- Project: Sentinel Forge Cognitive AI Orchestration Platform
- Document state: blank template
- Owner: [Project owner]
- Review date: [YYYY-MM-DD]

## Scope
Use this file to capture the human-readable HTTP and WebSocket contract for the current project version.

## HTTP Endpoints
| Method | Path | Purpose | Request Schema | Response Schema | Auth | Notes |
|---|---|---|---|---|---|---|
| [GET/POST/etc.] | [/api/example] | [Describe endpoint] | [Link or summary] | [Link or summary] | [Required/Optional/None] | [Notes] |

## WebSocket Endpoints
| Path | Purpose | Event Types | Auth | Notes |
|---|---|---|---|---|
| [/ws/example] | [Describe endpoint] | [List events] | [Required/Optional/None] | [Notes] |

## Validation Rules
- Error model: [Describe error format]
- Authentication model: [Describe header, query, or session rules]
- Versioning rule: [Describe contract versioning approach]

## Completion Notes
- Keep this document aligned with the executable routes in `backend/`.
- Add example payloads to `docs/API_EXAMPLES.md`.
