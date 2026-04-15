# Asset Inventory and Risk Register
## Sovereign Forge v4.0

**Template source:** ICT Institute — ISO 27001:2022 (CC Attribution License)
**Prepared by:** Shannon Bryan Kelly | **Date:** April 2026

---

## Asset Inventory

| ID | Asset | Type | Classification |
|----|-------|------|---------------|
| A-001 | Azure OpenAI API Key | Credential | 🔴 Confidential |
| A-002 | Azure Endpoint URL | Credential | 🔴 Confidential |
| A-003 | `.env` file | Credential | 🔴 Confidential |
| A-004 | `backend/` FastAPI application | Source code | 🟡 Internal |
| A-005 | `sigma_network_engine.py` | Source code | 🟡 Internal |
| A-006 | `sentinel_profile.py` + JSONStore | Source code + Data | 🟡 Internal |
| A-007 | `l7_singularity_kernel.py` | Source code | 🟡 Internal |
| A-008 | `recursive_nexus_sigil_dashboard_unified.html` | Frontend | 🟢 Public |
| A-009 | GitHub repository | Platform | 🟢 Public |
| A-010 | Azure OpenAI resource | Platform | 🔴 Confidential |
| A-011 | SDLC + compliance documentation | Documentation | 🟢 Public |
| A-012 | Developer laptop | Hardware | 🟡 Internal |
| A-013 | `results_1000_strikes.txt` | Performance data | 🟡 Internal |

---

## Risk Register

| ID | Risk | Likelihood | Severity | Level | Controls | Residual |
|----|------|-----------|---------|-------|---------|---------|
| R-001 | API key committed to GitHub | 2 | 5 | 🟡 HIGH | `.gitignore`; secret scanning | 🟢 LOW |
| R-002 | Azure account compromised | 2 | 5 | 🟡 HIGH | MFA; limited access | 🟢 LOW |
| R-003 | Voice data inadvertently recorded | 2 | 4 | 🟡 MEDIUM | No audio files; STT in-browser | 🟢 LOW |
| R-004 | User speaks PII into voice interface | 3 | 3 | 🟡 MEDIUM | No storage; user guidance | 🟢 LOW |
| R-005 | Sentinel Profile contains identifiable data | 1 | 3 | 🟢 LOW | Preferences only; not identity | 🟢 LOW |
| R-006 | Azure outage | 3 | 2 | 🟡 MEDIUM | Mock mode fallback | 🟢 LOW |
| R-007 | Laptop lost or stolen with Sentinel Profile | 2 | 3 | 🟡 MEDIUM | Disk encryption; preferences only | 🟡 MEDIUM |
| R-008 | WebSocket connection exposes unencrypted data | 2 | 3 | 🟡 MEDIUM | Localhost only; no external exposure | 🟢 LOW |
| R-009 | Malicious dependency | 2 | 3 | 🟡 MEDIUM | Dependabot; pinned versions | 🟡 MEDIUM |

---

## Treatment Plan

| Risk | Action | Owner | Date |
|------|--------|-------|------|
| R-001 | Maintain `.gitignore`; pre-commit review | Shannon Bryan Kelly | Ongoing |
| R-002 | Enable Azure MFA | Shannon Bryan Kelly | April 2026 |
| R-003 | Add voice recording indicator to UI | Shannon Bryan Kelly | Next sprint |
| R-007 | Enable full disk encryption | Shannon Bryan Kelly | April 2026 |

---

*Template adapted from ICT Institute Assets-and-risks-ISO-27001 under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
