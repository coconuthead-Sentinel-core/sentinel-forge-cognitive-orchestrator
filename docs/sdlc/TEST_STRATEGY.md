# Test Strategy

## Testing Philosophy
Validate the repository at the level required for a finished review release: public behavior must be testable, documentation must match the implementation, and the local mock-mode workflow must remain healthy.

## Test Levels
### Unit And Component Tests
| Test ID | What It Covers | Pass Criteria |
|---|---|---|
| UT-001 | cognitive lens behavior | formatting and transformation expectations hold |
| UT-002 | glyph and symbolic processing | glyph matches and symbolic metadata behave as expected |
| UT-003 | EventBus and firewall helpers | event delivery and guard constraints behave correctly |

### Integration And API Tests
| Test ID | Scenario | Steps | Pass Criteria |
|---|---|---|---|
| IT-001 | runtime API regression | run `pytest -q` | full automated suite passes |
| IT-002 | orchestrator route coherence | run `pytest -q tests/test_api_completion.py` | dashboard and orchestrator routes pass |
| IT-003 | smoke validation | run `scripts/smoke_test.py` | core runtime sequence completes without failure |

### Manual Validation
- inspect README, architecture, API docs, engineering-build docs, and SDLC packet for contradictions
- verify the iOS packet reflects a `not applicable` outcome rather than a copied mobile release narrative

## Environments
| Environment | Purpose | Notes |
|---|---|---|
| Local mock mode | primary validation path | does not require Azure credentials |
| Optional Azure-backed mode | future extension path | not required for this review release |

## Known Gaps
| Gap | Risk | Mitigation |
|---|---|---|
| No live Azure deployment validation in this cycle | reviewers may assume cloud readiness | document Azure as a separate excluded workstream |
| No Apple client target | mobile paperwork could be misread | complete the iOS packet as an applicability assessment |

## Definition Of Done
- focused API regression passes
- smoke test passes
- full suite passes
- documentation and generated contract artifacts are refreshed
