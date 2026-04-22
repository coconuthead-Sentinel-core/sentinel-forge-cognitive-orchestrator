# API Examples

## POST /api/chat
Request:
```json
{
  "messages": [
    {
      "role": "system",
      "content": "Answer concisely."
    },
    {
      "role": "user",
      "content": "Explain how glyph routing works."
    }
  ],
  "temperature": 0.2
}
```

Response shape:
```json
{
  "id": "chat-123",
  "created": 1710000000,
  "model": "mock-or-adapter-model",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Glyph routing matches seed terms to symbolic topics and applies lens-aware response formatting."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 20,
    "total_tokens": 32
  }
}
```

## GET /api/cognitive/status
Response shape:
```json
{
  "status": "active",
  "default_lens": "neurotypical",
  "available_lenses": [
    "neurotypical",
    "adhd",
    "autism",
    "dyslexia"
  ],
  "event_listener_running": false,
  "orchestrator_metrics": {
    "total_processed": 1,
    "zone_distribution": {},
    "default_lens": "neurotypical"
  },
  "memory_manager": {
    "active_count": 0,
    "pattern_count": 0,
    "crystal_count": 0,
    "avg_entropy": 0.0,
    "last_transition": null
  }
}
```

## POST /api/task/orchestrate/start
Response shape:
```json
{
  "status": "initiated",
  "protocol": "Neurodivergent Task Orchestration",
  "listener_running": true,
  "lenses": [
    "neurotypical",
    "adhd",
    "autism",
    "dyslexia"
  ]
}
```

## GET /api/dashboard/metrics
Response shape:
```json
{
  "timestamp": 1710000000.0,
  "health_status": "green",
  "core": {
    "status": "active",
    "pools": 2,
    "processors": 10,
    "executions": 100
  },
  "performance": {
    "avg_latency_ms": 12.5,
    "p95_latency_ms": 18.9,
    "heap_mib": 0.0,
    "heap_stale_ratio": 0.0
  },
  "cognition": {
    "enabled": true,
    "memory_entries": 0,
    "symbolic_rules": 0,
    "embedding_active": false,
    "evaluation_scores": {
      "relevance": 0.0,
      "coherence": 0.0,
      "groundedness": 0.0
    }
  },
  "platform": "Windows"
}
```

## WebSocket /ws/cognitive
Initial event:
```json
{
  "type": "cognitive.state",
  "data": {
    "zone_metrics": {},
    "active_lens": "neurotypical",
    "timestamp": 1710000000.0
  }
}
```

Follow-on event:
```json
{
  "type": "zone.classified",
  "data": {
    "zone": "active",
    "entropy": 0.8
  }
}
```
