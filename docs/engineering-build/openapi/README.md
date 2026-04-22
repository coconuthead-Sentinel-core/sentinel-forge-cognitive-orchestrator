# OpenAPI Workspace

## Contract Metadata
- API name: Sentinel Forge HTTP API
- Version: main branch review release
- Base path: `/api`
- Authentication:
  - HTTP routes are open by default in the current release
  - WebSocket auth is handled separately and documented in `docs/API.md`

## Current Contract Sources
- Human-readable contract: `../../API.md`
- Example payloads: `../../API_EXAMPLES.md`
- Executable routes: `../../../backend/api.py`
- Generated schema: `openapi.generated.json`
- Export command:
  - `.\.venv\Scripts\python.exe scripts\export_openapi.py`

## Covered Route Families
- health and metrics
- chat and notes
- cognitive status and orchestration control
- cognition pipeline and symbolic rules
- glyph and sync operations
- platform runtime operations
- dashboard views

## Operational Notes
- Validation and schema generation rely on FastAPI and the Pydantic models in `backend/schemas.py`.
- OpenAPI should be regenerated any time public HTTP routes or request/response models change.
