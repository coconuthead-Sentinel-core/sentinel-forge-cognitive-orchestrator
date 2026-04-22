# ADR 0003: Use Internal EventBus And WebSockets Instead Of An External Broker

## Context And Problem Statement
- Sentinel Forge has asynchronous behavior, but the current release is a local-first review artifact rather than a broker-backed production platform.
- The documentation still needs an async contract even without Kafka, RabbitMQ, or Service Bus.

## Decision Drivers
- Keep the runtime simple for local verification.
- Expose real-time updates for dashboards and tests.
- Avoid introducing external infrastructure that is not required for the current release.

## Considered Options
1. Add an external message broker now.
2. Remove async behavior entirely.
3. Keep an internal EventBus and document the WebSocket-delivered contract as the active async surface.

## Decision Outcome
Chosen option: 3. Keep an internal EventBus and document the WebSocket-delivered contract as the active async surface.

### Positive Consequences
- The async story matches the current runtime.
- Tests can verify event delivery in-process.
- The project remains easy to run locally.

### Negative Consequences
- The async contract is internal rather than enterprise-broker oriented.
- Future broker adoption would require a new ADR and contract update.

## Links
- Related docs:
  - `../../../backend/eventbus.py`
  - `../../../backend/ws_api.py`
  - `../asyncapi/README.md`
