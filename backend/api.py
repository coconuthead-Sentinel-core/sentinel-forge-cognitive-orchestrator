import json
import logging
import time
from typing import Annotated, Any

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Request,
    Response,
    status,
)
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from starlette.concurrency import run_in_threadpool

from .core.config import Settings
from .core.dependencies import get_adapter, get_settings, get_orchestrator
from .services.cognitive_orchestrator import CognitiveOrchestrator
from .infrastructure.cosmos_repo import cosmos_repo
from .domain.models import Note
from .schemas import (
    BootStep,
    GlyphValidateRequest,
    GlyphValidateResponse,
    JobStatusResponse,
    JobSubmitResponse,
    MemorySnapshot,
    PoolCreateRequest,
    PrimeMetrics,
    ProcessRequest,
    ChatRequest,
    ProcessResponse,
    ChatResponse,
    RebuildRequest,
    SetRulesRequest,
    StatusResponse,
    StressRequest,
    StressResult,
    Suggestions,
    SymbolicRules,
    SyncSnapshot,
    SyncUpdateRequest,
    EmbeddingsResponse,
    EmbeddingsRequest,
)
from .core.security import api_key_guard

router = APIRouter()
ai_router = APIRouter(dependencies=[Depends(api_key_guard)])

# Initialize Jinja2 templates for Phase 2 dashboard
templates = Jinja2Templates(directory="templates")

# --- AI Routes (Protected by API Key) ---

@ai_router.post("/chat", response_model=ChatResponse)
async def chat(
    req: ChatRequest,
    orchestrator: Annotated[CognitiveOrchestrator, Depends(get_orchestrator)],
):
    """
    Process a chat request through the Cognitive Pipeline.
    """
    try:
        response = await orchestrator.process_message(
            user_message=req.messages[-1].content if req.messages else "",
            context=req.messages[0].content if len(req.messages) > 1 and req.messages[0].role == "system" else "",
        )
        return ChatResponse(**response)
    except Exception as e:
        logging.error(f"Error in chat endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error processing chat request.")


@ai_router.post("/embeddings", response_model=EmbeddingsResponse)
async def embeddings(
    req: EmbeddingsRequest,
    adapter: Annotated[Any, Depends(get_adapter)],
    settings: Annotated[Settings, Depends(get_settings)],
):
    """
    Embedding generation via Azure OpenAI (AAD).
    """
    try:
        raw = await adapter.embeddings(
            deployment=settings.AOAI_EMBED_DEPLOYMENT,
            inputs=req.input,
            dimensions=req.dimensions,
        )
        return raw
    except Exception as exc:
        logging.error(f"Error in embeddings endpoint: {exc}", exc_info=True)
        raise HTTPException(status_code=502, detail=f"Error communicating with AI service: {exc}")


# --- Nexus Notes (Refactored to use Repository) ---

@router.get("/notes", tags=["Notes"])
async def notes_list() -> Any:
    """Lists all notes from Cosmos DB via Repository."""
    return await cosmos_repo.get_all_notes()

@router.post("/notes/upsert", tags=["Notes"])
async def notes_upsert(payload: dict = Body(...)) -> Any:
    """Creates or updates a note via Repository."""
    import uuid
    # Create Domain Model
    note_id = payload.get("id") or str(uuid.uuid4())
    try:
        note = Note(
            text=payload.get("text"),
            tag=payload.get("tag"),
            vector=payload.get("vec"),
            metadata=payload.get("metadata", {})
        )
        note.id = note_id
        result = await cosmos_repo.upsert_note(note)
        return result
    except Exception as e:
        # Graceful fallback - return mock success so system stays functional
        logging.warning(f"DB unavailable, returning mock: {e}")
        return {"id": note_id, "status": "mock_saved", "text": payload.get("text")}

@router.get("/test", tags=["Testing"])
def test_endpoint():
    return {"ok": True}

# --- Health and Status ---
@router.get("/healthz", tags=["Health"])
async def healthz() -> Response:
    """Kubernetes-style liveness probe."""
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/readyz", tags=["Health"])
async def readyz(settings: Annotated[Settings, Depends(get_settings)]) -> Response:
    """
    Kubernetes-style readiness probe. Checks DB and AI service connectivity.
    """
    db_ready = await cosmos_repo.ping()
    
    ai_ready = False
    if settings.MOCK_AI:
        ai_ready = True
    else:
        try:
            adapter = get_adapter(settings)
            ai_ready = await adapter.ping()
        except Exception:
            ai_ready = False

    if db_ready and ai_ready:
        return Response(content='{"status": "ready"}', media_type="application/json", status_code=status.HTTP_200_OK)
    
    details = {
        "status": "not_ready",
        "checks": {
            "database": "ok" if db_ready else "error",
            "ai_service": "ok" if ai_ready else "error",
        }
    }
    return Response(content=json.dumps(details), media_type="application/json", status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


@router.get("/status", response_model=StatusResponse, tags=["Status"])
async def get_status(settings: Annotated[Settings, Depends(get_settings)]) -> Any:
    """Get the current status of the application."""
    # This is a simplified status endpoint. The legacy one was tied to the old service.
    return {
        "project_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "mock_ai_enabled": settings.MOCK_AI,
        "timestamp": time.time(),
    }

# --- Dashboard Endpoints ---

@router.get("/dashboard", response_class=HTMLResponse, tags=["Dashboard"])
async def dashboard_view(request: Request) -> Any:
    """Serves the main interactive dashboard view."""
    return templates.TemplateResponse("dashboard.html", {"request": request})