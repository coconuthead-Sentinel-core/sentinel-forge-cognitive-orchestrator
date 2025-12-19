# Sentinel Forge - AI Coding Agent Instructions

## Architecture Overview

Sentinel Forge is a **Cognitive AI Orchestration Platform** for neurodivergent-aware AI processing. Two subsystems:

1. **Backend API** (`backend/`) - FastAPI with Domain-Driven Design (DDD)
2. **Quantum Nexus Forge** (`quantum_nexus_forge_v5_2_enhanced.py`) - Standalone cognitive engine

```
backend/
├── domain/models.py      # Pure entities (Note, Entity) - NO DB fields allowed
├── infrastructure/       # cosmos_repo.py with auto Mock DB fallback
├── services/             # ChatService: Input → AI → Memory pipeline
├── adapters/             # AzureOpenAIAdapter (AAD) ↔ MockOpenAIAdapter
├── core/config.py        # ALL env vars via Pydantic Settings (single source)
├── api.py                # router (public) + ai_router (API key guarded)
└── ws_api.py             # /ws/sync, /ws/metrics, /ws/events
```

**Data Flow:** `api.py` → `ChatService` → `AI Adapter` → `cosmos_repo.upsert_note()`

## Quick Start

```powershell
pip install -r requirements.txt
# Create .env with MOCK_AI=true for offline development
uvicorn backend.main:app --reload --port 8000
curl http://localhost:8000/api/status
```

**Mock Mode:** Set `MOCK_AI=true` + leave `COSMOS_KEY` empty → zero external dependencies.

## Critical Domain Model Pattern

```python
# backend/domain/models.py - ALL entities must have this:
class Note(Entity):
    text: str
    tag: str
    model_config = ConfigDict(extra="ignore")  # REQUIRED
```

**Why:** Repository adds `partitionKey` for Cosmos DB. Domain models silently ignore it.
**Test:** `test_note_strict_config()` in `tests/test_domain.py` enforces this.
**Never:** Pass DB fields (`partitionKey`, `_etag`) to domain constructors.

## Adding API Endpoints

1. **Choose router:**
   - `router` = public endpoints
   - `ai_router` = auto-applies `api_key_guard` dependency (requires `X-API-Key` header)
2. **Pattern:** Routes are thin - delegate to services
3. **Prefix:** All routes get `/api` via `main.py` (e.g., `/api/ai/chat`)

## AI Adapter Contract

Both `AzureOpenAIAdapter` and `MockOpenAIAdapter` implement:
```python
async def chat(deployment, messages, temperature=None, max_tokens=None, ...) -> Dict
async def embeddings(deployment, inputs, dimensions=1536) -> Dict
```

- `AzureOpenAIAdapter`: Uses `DefaultAzureCredential` (AAD tokens, no API key)
- `MockOpenAIAdapter`: Returns `[MOCK]` prefixed responses, random embeddings

## Repository Auto-Fallback

`cosmos_repo.py` enables mock mode on ANY failure:
- Missing credentials → mock mode
- Connection error → mock mode
- Container not found → mock mode

Look for `[MOCK DB]` in logs. Field mapping happens here: `item["partitionKey"] = note.tag`

## Environment Variables

All in `backend/core/config.py` - never scatter `os.getenv()`:
```
MOCK_AI=false              # Toggle MockOpenAIAdapter
COSMOS_ENDPOINT=           # Default: https://localhost:8081/
COSMOS_KEY=                # Empty = auto mock mode
AOAI_ENDPOINT=             # Azure OpenAI endpoint
API_KEY=secret             # For X-API-Key validation
```

## Testing & Evaluation

```powershell
pytest tests/                      # Unit tests
python scripts/smoke_test.py       # Integration (needs running server)
python scripts/run_full_eval.py    # Full pipeline: server → collect → evaluate
```

Evaluation outputs: `evaluation/test_responses.json`, `evaluation/eval_results.json`

## WebSocket Pattern

```python
# ws_api.py pattern:
websocket_require_api_key(websocket)  # Enforce before accept
queue = bus.subscribe(loop, maxsize=1000, policy="latest")
# Send initial snapshot, then stream EventBus updates
```

## Script Import Pattern

Scripts in `scripts/` or `evaluation/` must add repo root:
```python
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
```

## Common Gotchas

1. **Windows emoji handling** - `run_full_eval.py` patches `stdout.reconfigure(encoding='utf-8')`
2. **Adapters must match interface** - New AI adapters need identical signatures
3. **EventBus policies** - Use `"latest"` for real-time UIs (drops old messages when full)
4. **AAD auth** - `AzureOpenAIAdapter` uses `DefaultAzureCredential`, not API keys
