# AI Governance Summary

## Scope
This file captures project-specific AI governance notes for the current repository release.

## Intended AI Use
- Capability: advisory chat and symbolic orchestration with adaptive presentation lenses
- User-facing purpose: demonstrate cognitive-formatting and symbolic-routing concepts through a testable FastAPI platform
- Human oversight model: all outputs are reviewer-facing and owner-controlled; the system does not make autonomous business decisions

## Guardrails
- Prompt controls: system context is passed through the chat contract and can be constrained by route callers
- Output handling rules: orchestrator responses pass through the L6 firewall constraints before final return
- Escalation rules: security and incident escalation route through `SECURITY.md` and `docs/compliance/INCIDENT_LOG.md`

## Operational Controls
- Logging and audit: metrics, status endpoints, event history, and generated documentation provide audit surfaces for review
- Change control: `main` is the sole review-release branch, and route or doc changes are meant to ship together
- Incident path: use `docs/compliance/INCIDENT_LOG.md` for incidents and `SECURITY.md` for sensitive disclosures

## Linked Documents
- RMF workspace: `../nist-ai-rmf/README.md`
- Compliance packet: `../../compliance/`
- AI policy: `../../compliance/AI_POLICY.md`
