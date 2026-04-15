import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router
from .infrastructure.cosmos_repo import CosmosDBRepository
import uvicorn
import asyncio

# Set event loop policy for Windows
if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sentinel-middleware")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize Cosmos DB Repository (will use Mock DB mode if unavailable)
    try:
        await CosmosDBRepository.initialize()
        logger.info("Cosmos DB Repository initialized.")
    except Exception as exc:
        logger.warning("Cosmos DB initialization failed, using Mock DB: %s", exc)

    # Warm up token to fail-fast on bad identity/env.
    # Only attempt if not in MOCK_AI mode
    from .core.config import settings
    if not settings.MOCK_AI:
        try:
            from .adapters.azure_openai import AzureCognitiveTokenProvider
            provider = AzureCognitiveTokenProvider()
            try:
                await provider.get_token()
                logger.info("AAD token warmup successful.")
            except Exception as exc:
                logger.warning("AAD warmup failed (will use mock): %s", exc)
            finally:
                await provider.aclose()
        except ImportError as exc:
            logger.warning("Azure adapters not available: %s", exc)
    else:
        logger.info("MOCK_AI mode enabled, skipping AAD token warmup.")
    
    yield
    
    # Cleanup on shutdown
    try:
        await CosmosDBRepository.close()
    except Exception as exc:
        logger.warning("Cosmos DB close failed: %s", exc)

app = FastAPI(title="Neurodivergent AI Middleware", lifespan=lifespan)

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
# app.include_router(ai_router, prefix="/api")

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
