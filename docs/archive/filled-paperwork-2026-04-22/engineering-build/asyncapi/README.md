# AsyncAPI Home

## Scope
The repo does not currently use an external broker such as Kafka, RabbitMQ, or Service Bus. Its asynchronous interface is the internal EventBus plus WebSocket delivery.

## Channels
- `cognitive`
- `symbolic`
- `glyph`
- `raw_events`

## Consumers
- `/ws/cognitive`
- `/ws/metrics`
- `/ws/sync`

## Event Types
- `zone.classified`
- `symbolic.matched`
- `glyph.parsed`
- compatibility pass-through events on `/ws/sync`

## Contract Source
- publisher code: `../../../backend/services/cognitive_orchestrator.py`
- event bus: `../../../backend/eventbus.py`
- websocket transport: `../../../backend/ws_api.py`

## Current Decision
A lightweight AsyncAPI-style channel catalog is sufficient for the repo because no external broker contract has to be versioned yet.
