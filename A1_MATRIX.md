# A1 Matrix: Cognitive Zone Partitioning

This document partitions the Sentinel Forge project files into three cognitive zones, as defined by the **A1 Filing System**. This matrix provides a spatial guide to the codebase, helping to manage cognitive load and prevent architectural drift by categorizing files based on their stability and rate of change.

---

## 🔴 RED ZONE (Crystallized)

**Description:** Foundational, stable, and rarely changing files. This is the bedrock of the application, representing crystallized knowledge and established architecture. Changes here require careful consideration.

| File / Directory | Purpose | Justification |
| :--- | :--- | :--- |
| **`backend/domain/models.py`** | Data Contracts | Defines the core entities and data structures (Note, Glyph, etc.). The foundation of all services. |
| **`backend/core/config.py`** | Environment Config | Single source of truth for all environment variables and settings. Changes are architectural. |
| **`backend/main.py`** | Application Entry | Wires together routers, middleware, and lifespan events. Structurally stable. |
| **`.github/copilot-instructions.md`** | Agent Instructions | The master instructions guiding the AI coding agent's behavior and architecture. |
| **`A1.Ω.Master_Optimization.json`** | Master Manifest | The definitive control document defining the SQA v8.1 Capstone status. Immutable. |
| **`Dockerfile` / `docker-compose.yml`** | Containerization | Defines the production and development environments. Stable unless dependencies change. |
| **`ARCHITECTURE.md`** | System Blueprint | High-level architectural overview of the entire system. |
| **`README.md`** | Project Overview | The main entry point for understanding the project's purpose and setup. |

---

## 🟡 YELLOW ZONE (Transitional)

**Description:** Semi-stable components and services. This zone represents emerging patterns and established logic that may still be refined or extended as the system evolves.

| File / Directory | Purpose | Justification |
| :--- | :--- | :--- |
| **`backend/infrastructure/`** | Data Persistence | The repository layer. The interface is stable, but implementations may be optimized. |
| **`backend/services/memory_zones.py`** | Memory Logic | Core logic for the three-zone memory system. Mostly stable but could be tuned. |
| **`backend/services/glyph_processor.py`** | Symbolic Logic | The engine for processing glyphs. The core is stable, but new glyph rules may be added. |
| **`backend/services/*_lens.py`** | Cognitive Lenses | The individual cognitive lenses (ADHD, Autism, Dyslexia). Core logic is set, but transformations can be refined. |
| **`backend/eventbus.py`** | Event System | The central event bus. The pattern is stable, but new topics or policies may be added. |
| **`backend/security.py`** | Auth & Guards | Security implementations. Stable, but may evolve with new security requirements. |

---

## 🟢 GREEN ZONE (Active)

**Description:** Highly dynamic files that are under active development, frequently changed, or serve as the primary interaction points for new logic and features. This is the "workbench" zone.

| File / Directory | Purpose | Justification |
| :--- | :--- | :--- |
| **`backend/services/cognitive_orchestrator.py`** | Core Orchestration | The central nervous system of the application, where all other services are integrated. Under constant refinement. |
| **`backend/api.py`** | REST Endpoints | The primary interface for HTTP requests. New endpoints are added and existing ones are modified frequently. |
| **`backend/ws_api.py`** | WebSocket Endpoints | The interface for real-time communication. Actively being developed and tested. |
| **`tests/`** | Validation Suite | All test files. Must be continuously updated to reflect new features and refactoring in the codebase. |
| **`evaluation/`** | Performance Scripts | Scripts for evaluating model and system performance. Actively used and modified to test new hypotheses. |
| **`scripts/`** | Utility & Ops | Helper scripts for database initialization, testing, and other operational tasks. Frequently created and modified. |
| **`invoke_sentinel.py`** | CLI Tool | The interactive command-line tool. Likely to be enhanced with new commands and features. |
