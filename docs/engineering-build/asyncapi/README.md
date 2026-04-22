# AsyncAPI-Style Channel Catalog

## Applicability
- Async interface present: yes
- Current async transport: internal EventBus plus WebSocket delivery
- External broker present: no

## Channels
| Channel | Producer | Consumer | Payload | Notes |
|---|---|---|---|---|
| `raw_events` | runtime services and instrumentation hooks | cognitive orchestrator listener | arbitrary event payload | used by task orchestration listener |
| `cognitive` | orchestrator and cognition services | `/ws/cognitive`, `/ws/metrics` | cognition and zone events | metrics stream filters this channel |
| `symbolic` | glyph and symbolic services | `/ws/cognitive` | symbolic match events | event details vary by producer |
| `glyph` | glyph parsing and bridge services | `/ws/cognitive` | parsed glyph events | used for symbolic UI and test flows |

## Event Types In Current Tests
- `cognitive.state`
- `metrics.initial_state`
- `zone.classified`
- `zone.transition`
- application-specific pass-through events on `/ws/sync`

## Delivery Rules
- Ordering: best effort within a single in-process queue, not globally ordered across topics
- Retry behavior: none beyond subscriber reconnection and fresh subscription
- Failure handling: bounded queues, unsubscribe on disconnect, listener cancellation on shutdown

## Transport Notes
- The active async contract is internal and review-release scoped.
- If an external broker is adopted later, this document and ADR 0003 should be updated together.
