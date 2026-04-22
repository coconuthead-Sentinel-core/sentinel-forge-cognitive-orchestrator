# C4 Container Model

## System Context
- System of interest: Sentinel Forge Cognitive AI Orchestration Platform
- Primary users:
  - Technical reviewer: validate the codebase, docs, and tests
  - Project owner: maintain a portfolio-grade AI orchestration repository
  - Future contributor: extend orchestration, glyph, or dashboard behavior
- External systems:
  - Optional Azure OpenAI: model inference
  - Optional Azure Cosmos DB: external persistence
  - Local filesystem: JSON state, docs, generated OpenAPI schema

## Container View
| Container | Responsibility | Technology |
|---|---|---|
| FastAPI app | exposes REST and WebSocket endpoints | FastAPI, Python |
| QNF service layer | manages pools, jobs, events, profile, and status | Python service object |
| Cognitive orchestrator | applies lenses, symbolic routing, and memory zoning | Python orchestration service |
| Event transport | internal publish/subscribe for live updates | in-process EventBus |
| Dashboard templates | renders HTML dashboards and JSON-backed views | Jinja2 templates |
| Persistence layer | stores local state and optional cloud notes | JSONStore, optional Cosmos DB |

## Component View
### FastAPI app
- `backend/api.py`: REST routes
- `backend/ws_api.py`: WebSocket routes
- `backend/main.py`: bootstrap and middleware wiring

### Cognitive orchestrator
- `chat_service.py`: adapter-facing chat behavior
- `cognitive_orchestrator.py`: lens, glyph, entropy, and event coordination
- `memory_zones.py`: entropy classification
- `glyph_processor.py` and `glyph_parser.py`: symbolic matching and parsing

### QNF service layer
- `backend/service.py`: platform runtime wrapper
- `backend/storage.py`: JSON persistence
- `sentinel_profile.py` and `sentinel_sync.py`: profile and sync support

## Dynamic View
### Chat path
1. Client posts to `/api/chat`.
2. FastAPI route sends the message to `_orchestrator`.
3. The orchestrator applies symbolic and lens-aware processing.
4. The adapter path or fallback returns a response.
5. Memory and event metadata are updated.

### Dashboard metrics path
1. Client requests `/api/dashboard/metrics`.
2. The route aggregates service metrics, status, and cognition state.
3. The dashboard renders structured health, performance, and cognition blocks.
