# C4 Container Model

## System Scope
Sentinel Forge is a FastAPI-based cognitive orchestration system with a browser-facing dashboard and optional Azure-backed AI and persistence integrations.

```mermaid
flowchart LR
    User["User / Browser / Voice Input"]
    API["FastAPI App\nbackend/main.py + backend/api.py"]
    WS["WebSocket Layer\nbackend/ws_api.py"]
    Orchestrator["Cognitive Orchestrator\nbackend/services/cognitive_orchestrator.py"]
    Lenses["Lens Services\nADHD / Autism / Dyslexia"]
    Symbols["Glyph Processing\nbackend/services/glyph_processor.py"]
    Memory["Three-Zone Memory\nbackend/services/memory_zones.py"]
    EventBus["EventBus\nbackend/eventbus.py"]
    AI["AI Adapter\nMock or Azure OpenAI"]
    Store["Persistence\nCosmos repo with mock fallback"]
    Dashboard["Dashboard / Static UI"]

    User --> API
    User --> WS
    API --> Orchestrator
    WS --> EventBus
    Orchestrator --> Lenses
    Orchestrator --> Symbols
    Orchestrator --> Memory
    Orchestrator --> AI
    Orchestrator --> Store
    Orchestrator --> EventBus
    EventBus --> WS
    WS --> Dashboard
```

## Container Notes
- The primary runtime container is the FastAPI application.
- Event streaming is internal to the repo through the EventBus and WebSocket routes.
- AI and persistence both support local fallback paths for development and validation.
