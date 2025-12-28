import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router, ai_router
from .ws_api import router as ws_router
from .core.dependencies import get_settings
from .infrastructure.cosmos_repo import CosmosDBRepository
from .adapters.azure_openai import AzureOpenAIAdapter, AzureCognitiveTokenProvider, AIO_TIMEOUT
from .mock_adapter import MockOpenAIAdapter
import uvicorn
import asyncio
import httpx

# Set event loop policy for Windows
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sentinel-middleware")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle manager."""
    settings = get_settings()
    
    # Initialize Cosmos DB Repository
    await CosmosDBRepository.initialize()
    logger.info("Cosmos DB Repository initialized.")

    # Initialize the AI adapter to warm up connections and auth
    adapter = None
    token_provider = None
    http_client = None

    if settings.MOCK_AI:
        adapter = MockOpenAIAdapter()
        logger.info("AI Adapter running in mock mode. No remote initialization needed.")
    else:
        try:
            token_provider = AzureCognitiveTokenProvider()
            http_client = httpx.AsyncClient(timeout=AIO_TIMEOUT)
            adapter = AzureOpenAIAdapter(http=http_client, token_provider=token_provider)
            logger.info("AI Adapter initialized and AAD token warmup successful.")
        except Exception as exc:
            logger.warning(f"AI Adapter initialization failed: {exc}", exc_info=True)
            # Fallback to mock adapter if real one fails
            adapter = MockOpenAIAdapter()
            logger.info("Fell back to mock AI adapter.")

    app.state.adapter = adapter
    app.state.token_provider = token_provider
    app.state.http_client = http_client

    yield
    
    # Cleanup on shutdown
    logger.info("Closing application resources.")
    if app.state.adapter and not isinstance(app.state.adapter, MockOpenAIAdapter):
        if app.state.token_provider:
            await app.state.token_provider.aclose()
        if app.state.http_client:
            await app.state.http_client.aclose()
    
    await CosmosDBRepository.close()

app = FastAPI(
    title="Sentinel Forge Cognitive Orchestrator",
    description="A neurodivergent-aware AI processing platform.",
    version="2.0.0",
    lifespan=lifespan
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NOTE: Old middleware for request size, rate limiting, and API key are removed.
# New implementation uses dependency injection (`api_key_guard`) and Pydantic settings.

# Include routers
app.include_router(api_router, prefix="/api")
app.include_router(ai_router, prefix="/api/ai")
app.include_router(ws_router)

@app.get("/", tags=["Status"])
async def root():
    """Root endpoint providing a welcome message."""
    return {"message": "Welcome to the Sentinel Forge Cognitive Orchestrator."}

@app.post("/api/testpost")
async def test_post():
    return {"message": "ok"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        timeout_keep_alive=75,
        log_level="info"
    )
