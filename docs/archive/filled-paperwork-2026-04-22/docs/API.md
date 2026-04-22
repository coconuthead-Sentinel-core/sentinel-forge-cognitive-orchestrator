API Routes (key endpoints)

- GET /api/healthz → 204
- GET /api/readyz → 200 with summary
- GET /api/status → system status (pools, processors, latency)
- GET /api/metrics → compact JSON metrics
- GET /api/metrics/prom → Prometheus text; includes qnf_bus_*, qnf_intent_count, qnf_topic_count, qnf_threads_total, qnf_resonance_*
- POST /api/stress {iterations:int, concurrent:bool, async_mode:bool} → StressResult
- GET /api/jobs/{job_id} → async stress job status

Cognition

- POST /api/cog/process {data:any} → {input, output, processing_time, metadata}
- GET /api/cog/status → orchestrator status
- GET /api/cog/rules | PUT /api/cog/rules {rules: {pattern: tag}}
- GET /api/cog/memory | DELETE /api/cog/memory
- GET /api/cog/prime → prime metrics
- GET /api/cog/suggest?limit=5 → suggested rules

Threads / Seeds / Glyphs

- GET /api/cog/threads[?topic=x] → list threads
- GET /api/cog/threads/{id}[?limit=50] → thread detail
- GET /api/cog/stats → {intents, topics}
- GET /api/cog/seeds → {seeds:[...]}
- POST /api/cog/seeds {items:[...]} → upsert seeds
- GET /api/cog/matrix[?top_k=20] → token matrix per topic
- GET /api/glyphs/aliases → alias map
- POST /api/glyphs/pack {shapes:{...}} → bulk seeds/rules/aliases
- POST /api/glyphs/interpret {sequence:"APEX->CORE->EMIT"} → {tokens, topics, route}

Sync / Glyphic protocol

- POST /api/sync/update {agent, state:{...}} → updates tri-node state
- GET /api/sync/snapshot → session snapshot
- GET /api/sync/trinode → roles/presence
- POST /api/glyphs/validate {sequence:[...]} → validity
- GET /api/glyphs/boot → boot steps

WebSocket

- /ws/sync → NDJSON‑like stream; payloads include {type:"cog.intent"|"sync.update", data:{...}}

Notes

- Include header X-API-Key if QNF_API_KEY is set.

## Universal Input Stream Memory Threading (UISMT)

The **UISMT** protocol (Node 8) automatically threads all input into 7 color-coded categories based on heuristic analysis.

### 7-Color Threading System

| Color | Category | Description |
| :--- | :--- | :--- |
| **GOLDEN** | Framework | Core architecture, rules, and system axioms. |
| **NEURAL** | Processing | Active thought processes and logic chains. |
| **BLUE** | Data | Raw facts, inputs, and unrefined data streams. |
| **RED** | Critical | Errors, alerts, and crystallized truths. |
| **GREEN** | Growth | New ideas, expansion, and novel concepts. |
| **PURPLE** | Creative | Dreams, metaphors, and artistic synthesis. |
| **GREY** | Archive | Old logs, history, and deprecated data. |

### UISMT Endpoints

- **POST** `/api/simulation/cno-ax/start`: Initiates the "1000 Strikes" protocol. Threads input as `GOLDEN` (Command).
- **POST** `/api/simulation/cno-ax/stop`: Halts the simulation.

## WebSocket Event Reference

The `/ws/cognitive` endpoint streams real-time events from the CNO-AX Engine and Cognitive Orchestrator.

### Event Signatures

#### `cno_ax.traffic_update`

Emitted during the "1000 Strikes" optimization loop.

```json
{
  "type": "cno_ax.traffic_update",
  "data": {
    "strike": 42,
    "metrics": {
      "flow_rate": 1250,
      "efficiency": 0.98,
      "congestion_level": 0.05
    }
  }
}
```

#### `cno_ax.complete`

Emitted when the protocol finishes or is halted.

```json
{
  "type": "cno_ax.complete",
  "data": {
    "final_strike": 1000,
    "status": "Stillwater State Achieved"
  }
}
```
