# Threat Model Home

## Scope
This is the current lightweight threat model for the repository-aligned local deployment and development workflow.

## Assets
- source code and documentation
- user prompts and model outputs
- optional Azure credentials
- optional Cosmos persistence data
- local profile and state artifacts

## Trust Boundaries
- browser or caller to FastAPI API boundary
- WebSocket clients to EventBus-delivered events
- application to Azure OpenAI
- application to Cosmos persistence
- local filesystem for saved state and documentation

## Primary Threats
- unauthorized use of API or WebSocket surfaces
- stale documentation leading to unsafe operator assumptions
- accidental disclosure through logs or public issue reports
- insecure handling of optional cloud credentials
- prompt or symbolic input causing misleading system behavior

## Current Mitigations
- API key guard support in `backend/security.py`
- mock-mode development path for offline validation
- explicit release and handoff paperwork in `docs/sdlc/`
- security disclosure path in `../../../SECURITY.md`

## Residual Risks
- cloud-backed production deployment posture is not fully documented here
- the repo still contains multiple legacy top-level artifacts that require operator discipline
