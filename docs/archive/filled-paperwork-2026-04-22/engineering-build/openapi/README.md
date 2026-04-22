# OpenAPI Home

## Current Contract Sources
- Human-readable API reference: `../../API.md`
- Usage examples: `../../API_EXAMPLES.md`
- Implemented routes: `../../../backend/api.py`

## Current Position
This repo uses FastAPI route declarations as the executable contract source. The narrative documentation in `docs/API.md` is the reviewed human-facing surface. A separately checked-in `openapi.json` is not currently required for the local validation path.

## Contract Coverage
- health, status, and metrics routes
- chat processing
- glyph interpretation and validation
- cognitive processing
- sync endpoints
- note upsert flow

## Review Rule
If routes change, update `docs/API.md` and this index in the same change set.
