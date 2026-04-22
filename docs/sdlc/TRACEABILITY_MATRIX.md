# Traceability Matrix

| Requirement ID | Requirement Summary | Design Artifact | Implementation Artifact | Test Artifact | Status |
|---|---|---|---|---|---|
| REQ-001 | provide a local HTTP API for health, chat, cognition, dashboard, and operations | `ARCHITECTURE.md`, `docs/API.md` | `backend/main.py`, `backend/api.py` | smoke test, `pytest -q` | Complete |
| REQ-002 | adapt responses through multiple cognitive lenses | `docs/engineering-build/arc42/README.md` | `backend/services/cognitive_orchestrator.py`, `backend/services/*_lens.py` | `pytest -q` | Complete |
| REQ-003 | support symbolic or glyph-aware interpretation | `docs/engineering-build/asyncapi/README.md` | `backend/services/glyph_processor.py`, `glyph_event_bridge.py`, `glyph_parser.py` | `pytest -q` | Complete |
| REQ-004 | expose event-driven runtime streams | `docs/API.md`, async API summary | `backend/ws_api.py`, `backend/eventbus.py` | `pytest -q` | Complete |
| REQ-005 | keep review paperwork complete and coherent | `docs/README.md`, `docs/HR_REVIEW_PACKET.md` | active docs under `docs/` | repo review and final validation | Complete |
| REQ-006 | remain runnable without Azure credentials | `README.md`, `docs/sdlc/TEST_STRATEGY.md` | mock adapter and mock persistence paths | smoke test, `pytest -q` | Complete |
