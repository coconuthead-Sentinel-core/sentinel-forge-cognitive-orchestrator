# Traceability Matrix

| Requirement | Source | Implementation / Evidence | Validation |
|---|---|---|---|
| Adaptive cognitive response formatting | `PRD.md` section 4.7 | `backend/services/adhd_lens.py`, `autism_lens.py`, `dyslexia_lens.py` | `tests/test_adhd_lens.py`, `tests/test_dyslexia_lens.py`, full `pytest -q` |
| Symbolic glyph processing | `PRD.md` section 4.2 and 4.8 | `backend/services/glyph_processor.py`, `glyph_event_bridge.py` | `tests/test_glyph_processor.py`, `tests/test_glyph_event_bridge.py` |
| Real-time WebSocket streaming | `PRD.md` section 4.3 | `backend/ws_api.py`, `backend/eventbus.py` | `tests/test_websockets.py`, `tests/test_ws_api.py` |
| Three-zone memory orchestration | `SYSTEM_DESIGN.md` | `backend/services/cognitive_orchestrator.py`, `memory_zones.py` | full `pytest -q`, `scripts/smoke_test.py` |
| Release-ready paperwork set | Codex SDLC and project paperwork packages | `docs/engineering-build/`, `docs/sdlc/`, `SECURITY.md`, `GOVERNANCE.md` | documentation review on 2026-04-22 |
| iOS compliance disposition | Codex iOS compliance package | `docs/compliance/ios/` | repository applicability review on 2026-04-22 |
