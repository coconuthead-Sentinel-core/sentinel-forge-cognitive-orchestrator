# Sovereign Forge 🌌

**Real-Time Self-Optimizing Cognitive AI Platform**

![CI](https://github.com/coconuthead-Sentinel-core/sentinel-forge-cognitive-orchestrator/workflows/Python%20application/badge.svg)

**Architect:** Shannon Bryan Kelly | **Version:** 4.0 | **Updated:** April 2026

---

## 🎯 What It Is

Sovereign Forge is a real-time, self-optimizing cognitive AI operating system. Unlike standard chatbots or agent platforms, Sovereign Forge monitors and adjusts its own performance continuously — achieving the "Stillwater State" (perfect cognitive flow) through its CNO-AX Metacognition Engine.

Built on FastAPI with live WebSocket streaming, a 14-Mirror Cognitive Array, voice interface, and a 7-Layer Neural Framework — this is the most architecturally advanced platform in the Forge trilogy.

---

## 🧠 What Makes It Different

| Sovereign Forge | Standard AI Platforms |
|----------------|----------------------|
| Self-optimizing metacognition | Static response pipeline |
| Real-time WebSocket event streaming | Request/response only |
| 14-Mirror Cognitive Array | Single processing path |
| Voice-enabled (TTS/STT) | Text only |
| Sentinel Profile — persistent user state | Stateless sessions |
| C++ performance bridge layer | Pure Python only |
| 7-Layer Neural Framework | 1-2 layer architecture |
| "1000 Strikes" load optimization (11.90ms) | No performance protocol |

---

## 🏗️ Core Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Sovereign Forge v4.0                  │
├─────────────────┬──────────────────┬────────────────────┤
│  FastAPI        │  CNO-AX          │  Sigma Network     │
│  REST + WS      │  Metacognition   │  Engine            │
│  Endpoints      │  Engine          │  (Profile-Driven)  │
├─────────────────┴──────────────────┴────────────────────┤
│              14-Mirror Cognitive Array                   │
│  GREEN: M1,M2,M4,M6 | YELLOW: M3,M5,M7,M8 | RED: M9-14 │
├─────────────────────────────────────────────────────────┤
│           Three-Zone Memory System                       │
│    🟢 Active (>0.7)  🟡 Pattern (0.3-0.7)  🔴 Crystal (<0.3) │
├─────────────────────────────────────────────────────────┤
│  Neurodivergent Lenses: ADHD | Autism | Dyslexia | NT   │
├─────────────────────────────────────────────────────────┤
│     Azure OpenAI (GPT-4o-mini) + Mock Fallback          │
└─────────────────────────────────────────────────────────┘
```

---

## ⚡ Key Systems

### CNO-AX Metacognition Engine
The self-optimizing core. Runs the "1000 Strikes" Protocol — a recursive simulation targeting the Stillwater State (perfect flow). Achieved **11.90ms average latency** with **3.41ms jitter** in verified testing.

### 14-Mirror Cognitive Array
Visual-symbolic processing unit mapped to Platonic geometry symmetry points. Each mirror zone corresponds directly to the A1 Filing System zones:
- **GREEN Mirrors (M1,M2,M4,M6):** Real-time glyph synthesis and active thought reflection
- **YELLOW Mirrors (M3,M5,M7,M8):** Pattern recognition and semi-stable memory integration
- **RED Mirrors (M9-M14):** Deep archival storage, ethical boundaries, core truths

### Sigma Network Engine
Feature-flagged cognitive decision engine driven by the Sentinel Profile. Adapts behavior dynamically based on persisted user state. Includes MOUSE Cache Manager for write-through persistence.

### Voice Interface
Full TTS/STT "Karaoke" system. Spoken user input routed to `/api/chat`. AI responses fed back through the speech engine with real-time visual highlighting.

### Sentinel Profile System
Persistent profile drives all feature flags and runtime behavior. Profile state stored via JSONStore and loaded on startup.

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/coconuthead-Sentinel-core/sentinel-forge-cognitive-orchestrator.git
cd sentinel-forge-cognitive-orchestrator

# Install
pip install -r requirements.txt

# Configure
cp .env.example .env
# Add your Azure OpenAI credentials to .env

# Run (mock mode — no Azure needed)
MOCK_AI=true uvicorn backend.main:app --reload --port 8000

# Run (live mode)
uvicorn backend.main:app --reload --port 8000
```

---

## 📡 API Reference

### REST Endpoints
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/status` | Health check + system state |
| POST | `/api/chat` | Cognitive processing with lens |
| GET | `/api/metrics` | Full zone + mirror + performance metrics |
| POST | `/api/glyph/process` | Symbol/emoji interpretation |

### WebSocket Endpoints
| Endpoint | Events | Interval |
|----------|--------|---------|
| `/ws/cognitive` | Zone transitions, cognitive events, metrics | Real-time |
| `/ws/metrics` | Performance dashboard data | 2 seconds |
| `/ws/events` | System notifications | Event-driven |

---

## 📁 Project Structure

```
sovereign-forge/
├── backend/                          # FastAPI application
│   ├── api.py                        # REST endpoints
│   ├── ws_api.py                     # WebSocket real-time sync
│   ├── services/
│   │   ├── cognitive_orchestrator.py # Main processing engine
│   │   ├── glyph_processor.py        # 14-Mirror symbol processing
│   │   ├── memory_zones.py           # Three-zone memory system
│   │   ├── adhd_lens.py              # ADHD burst processing
│   │   ├── autism_lens.py            # Precision pattern lens
│   │   └── dyslexia_lens.py          # Spatial symbol lens
│   ├── infrastructure/
│   │   └── cosmos_repo.py            # Azure Cosmos DB persistence
│   └── adapters/
│       ├── azure_openai.py           # Azure OpenAI integration
│       └── mock_adapter.py           # Development fallback
├── sigma_network_engine.py           # Sigma cognitive decision engine
├── l7_singularity_kernel.py          # Layer 7 processing kernel
├── sentinel_cognition.py             # Cognition base layer
├── sentinel_profile.py               # Persistent profile system
├── evaluation/                       # Testing & validation
├── frontend/                         # Web dashboard + voice UI
│   └── recursive_nexus_sigil_dashboard_unified.html
├── docs/
│   ├── sdlc/                         # Full SDLC documentation
│   └── compliance/                   # GDPR, AI Act, ISO 27001
├── tests/                            # Unit test suite
├── ARCHITECTURE.md                   # Full architecture reference
└── docker-compose.yml                # Container deployment
```

---

## 📊 Performance

| Metric | Result | Protocol |
|--------|--------|---------|
| Average Latency | **11.90ms** | 1000 Strikes |
| Jitter (Stdev) | **3.41ms** | 1000 Strikes |
| Persona State | **Crystalline Navigator** | Stillwater Verified |
| Evaluation Score | **3.94–3.99 / 5.0** | 80-prompt pipeline |

---

## 🔧 Configuration

```bash
# .env
MOCK_AI=true                          # false for live Azure
AOAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AOAI_CHAT_DEPLOYMENT=gpt-4o-mini      # Azure deployment name
API_KEY=your-guard-key
COSMOS_ENDPOINT=https://your-db.documents.azure.com/
COSMOS_KEY=your-cosmos-key
COSMOS_DATABASE_NAME=SovereignForgeDB
```

---

## 🧪 Testing

```bash
# Unit tests
pytest tests/

# 1000 Strikes performance protocol
python launch_1000_strikes.py

# Evaluation pipeline
python evaluation/run_evaluation.py

# Smoke test
python scripts/smoke_test.py
```

---

## 📄 Documentation

| Suite | Location |
|-------|---------|
| SDLC (PRD, Design, API, Backlog, Tests) | `docs/sdlc/` |
| Compliance (GDPR, AI Act, ISO 27001) | `docs/compliance/` |
| Architecture reference | `ARCHITECTURE.md` |

---

## 👤 Author

**Shannon Bryan Kelly** (Coconut Head)
*AI Architect — Sovereign Forge Trilogy*

Built in collaboration with Claude AI (Anthropic)

---

## 📄 License

MIT License

---

*Part of the Sovereign Forge Trilogy: Quantum Nexus Forge · Sentinel-of-sentinel-s-Forge · Sovereign Forge* 🌌
