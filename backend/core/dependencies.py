"""Core application dependencies, managed by FastAPI's dependency injection system.

This module centralizes the creation and lifecycle of shared resources like
the AI adapter, cognitive orchestrator, and application settings. Using
dependency injection makes the application more modular, testable, and easier
to manage.

- `get_settings()`: Provides the global application settings.
- `get_adapter()`: Provides a singleton instance of the AI adapter (either mock or real).
- `get_orchestrator()`: Provides a singleton instance of the CognitiveOrchestrator.
"""

from functools import lru_cache
from typing import Annotated, Any

from fastapi import Depends, Request

from ..adapters.azure_openai import (
    AIO_TIMEOUT,
    AzureCognitiveTokenProvider,
    AzureOpenAIAdapter,
)
from ..mock_adapter import MockOpenAIAdapter
from ..services.cognitive_orchestrator import CognitiveOrchestrator
from .config import Settings


# The lru_cache is kept here as Settings has no inputs and is truly a singleton.
@lru_cache()
def get_settings() -> Settings:
    """
    Returns a cached instance of the application settings.
    The lru_cache ensures the Settings object is created only once.
    """
    return Settings()


def get_adapter(request: Request) -> Any:
    """
    Provides an adapter instance from the application state.
    The adapter is initialized once in the lifespan manager.
    """
    return request.app.state.adapter


def get_orchestrator(
    settings: Annotated[Settings, Depends(get_settings)],
    adapter: Annotated[Any, Depends(get_adapter)],
) -> CognitiveOrchestrator:
    """
    Provides a singleton instance of the CognitiveOrchestrator,
    initialized with the appropriate AI adapter.
    FastAPI handles caching this dependency within a single request.
    """
    return CognitiveOrchestrator(ai_adapter=adapter, settings=settings)
