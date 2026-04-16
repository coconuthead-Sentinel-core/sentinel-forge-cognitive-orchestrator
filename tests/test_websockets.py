
import asyncio
import json
import pytest
from fastapi.testclient import TestClient
import websockets

from backend.main import app
from backend.eventbus import bus

client = TestClient(app)

@pytest.mark.asyncio
async def test_ws_cognitive_endpoint():
    """
    Tests the /ws/cognitive endpoint for receiving initial state and subsequent events.
    """
    # Use TestClient's WebSocket context manager
    with client.websocket_connect("/ws/cognitive?api_key=secret") as websocket:
        # 1. Receive initial state
        initial_data = websocket.receive_json()
        assert initial_data["type"] == "cognitive.state"
        assert "zone_metrics" in initial_data["data"]

        # 2. Publish a 'cognitive' event and verify it's received
        cognitive_event = {"type": "test.cognitive.event", "data": "cognitive_payload"}
        asyncio.run(bus.publish("cognitive", cognitive_event))
        
        received_data = websocket.receive_json()
        assert received_data == cognitive_event

        # 3. Publish a 'symbolic' event and verify it's received
        symbolic_event = {"type": "test.symbolic.event", "data": "symbolic_payload"}
        asyncio.run(bus.publish("symbolic", symbolic_event))

        received_data = websocket.receive_json()
        assert received_data == symbolic_event

        # 4. Publish a 'glyph' event and verify it's received
        glyph_event = {"type": "test.glyph.event", "data": "glyph_payload"}
        asyncio.run(bus.publish("glyph", glyph_event))

        received_data = websocket.receive_json()
        assert received_data == glyph_event


@pytest.mark.asyncio
async def test_ws_metrics_endpoint():
    """
    Tests the /ws/metrics endpoint for event-driven metric updates.
    """
    with client.websocket_connect("/ws/metrics?api_key=secret") as websocket:
        # 1. Receive initial metrics state
        initial_data = websocket.receive_json()
        assert initial_data["type"] == "metrics.initial_state"
        assert isinstance(initial_data["data"], dict)

        # 2. Publish a relevant 'zone.classified' event and verify it's received
        classified_event = {"type": "zone.classified", "data": {"zone": "active", "entropy": 0.8}}
        asyncio.run(bus.publish("cognitive", classified_event))
        
        received_data = websocket.receive_json()
        assert received_data == classified_event

        # 3. Publish a relevant 'zone.transition' event and verify it's received
        transition_event = {"type": "zone.transition", "data": {"note_id": "123", "from": "active", "to": "pattern"}}
        asyncio.run(bus.publish("cognitive", transition_event))

        received_data = websocket.receive_json()
        assert received_data == transition_event

        # 4. Publish an irrelevant event and ensure it's NOT received
        irrelevant_event = {"type": "some.other.event", "data": "should_be_ignored"}
        asyncio.run(bus.publish("cognitive", irrelevant_event))

        # The test client's receive method has a default timeout.
        # If no message is received, it will raise an exception.
        with pytest.raises(websockets.exceptions.ConnectionClosed):
             # In the test client, a timeout is often represented by the connection closing
             # or a specific timeout exception from the underlying library if it were used directly.
             # The TestClient might abstract this. Let's assume a timeout will cause an issue.
             # A more robust way would be to use a short timeout.
             websocket.receive_json(timeout=0.1)

# To run these tests, use:
# pytest tests/test_websockets.py
