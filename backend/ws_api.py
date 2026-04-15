import asyncio
import json
import logging
from typing import Any, List, Annotated

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends

from .eventbus import bus
from .security import websocket_require_api_key
from .core.config import Settings
from .core.dependencies import get_settings
from .services.memory_zones import ThreeZoneMemory

logger = logging.getLogger(__name__)

router = APIRouter(tags=["WebSockets"])


class ConnectionManager:
    """Manages active WebSocket connections."""
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        """Broadcast a message to all connected clients."""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except RuntimeError:
                # Handle case where connection is closed during broadcast
                pass

# Singleton instance of the connection manager
manager = ConnectionManager()


async def event_broadcaster():
    """
    Subscribes to the event bus and broadcasts messages to all connected clients.
    This runs as a background task.
    """
    loop = asyncio.get_running_loop()
    # Subscribe to all relevant topics
    queue = bus.subscribe(loop, maxsize=1000, policy="latest", topic="*")
    logger.info("Event broadcaster started, subscribed to all topics.")
    while True:
        try:
            event = await queue.get()
            await manager.broadcast(event)
        except Exception as e:
            logger.error(f"Error in event broadcaster: {e}", exc_info=True)
            # Avoid tight loop on continuous errors
            await asyncio.sleep(1)


@router.on_event("startup")
async def startup_event():
    """Start the event broadcaster as a background task."""
    asyncio.create_task(event_broadcaster())


@router.websocket("/ws/events")
async def ws_events(
    websocket: WebSocket,
    api_key: None = Depends(websocket_require_api_key)
):
    """
    Master WebSocket endpoint for all real-time events.
    Authenticates the connection and then keeps it open to receive
    broadcasted events from the `event_broadcaster`.
    """
    await manager.connect(websocket)
    logger.info(f"New WebSocket connection established: /ws/events")
    try:
        while True:
            # Keep the connection alive, listening for client messages (if any)
            # or disconnects. The broadcaster handles sending data.
            await websocket.receive_text()
    except WebSocketDisconnect:
        logger.info("WebSocket connection closed.")
    finally:
        manager.disconnect(websocket)


@router.websocket("/ws/cognitive")
async def ws_cognitive(
    websocket: WebSocket,
    settings: Annotated[Settings, Depends(get_settings)],
    api_key: None = Depends(websocket_require_api_key)
):
    """
    [DEPRECATED] WebSocket endpoint for cognitive events.
    Use /ws/events instead.
    """
    await websocket.accept()
    await websocket.send_json({
        "type": "deprecation_warning",
        "message": "This endpoint is deprecated. Please use /ws/events for all real-time updates."
    })
    await websocket.close()


@router.websocket("/ws/sync")
async def ws_sync(
    websocket: WebSocket,
    api_key: None = Depends(websocket_require_api_key)
):
    """
    [DEPRECATED] WebSocket endpoint for sync events.
    Use /ws/events instead.
    """
    await websocket.accept()
    await websocket.send_json({
        "type": "deprecation_warning",
        "message": "This endpoint is deprecated. Please use /ws/events for all real-time updates."
    })
    await websocket.close()


@router.websocket("/ws/metrics")
async def ws_metrics(
    websocket: WebSocket,
    api_key: None = Depends(websocket_require_api_key)
):
    """
    [DEPRECATED] WebSocket endpoint for metrics.
    Use /ws/events instead.
    """
    await websocket.accept()
    await websocket.send_json({
        "type": "deprecation_warning",
        "message": "This endpoint is deprecated. Please use /ws/events for all real-time updates."
    })
    await websocket.close()
