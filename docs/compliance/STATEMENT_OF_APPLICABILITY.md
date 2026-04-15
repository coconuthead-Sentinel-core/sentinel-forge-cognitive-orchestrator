# Statement of Applicability (SoA)
## Sovereign Forge v4.0

**Template source:** ICT Institute — ISO 27001:2022 Annex A (CC Attribution License)
**Prepared by:** Shannon Bryan Kelly | **Date:** April 2026

---

## Key Controls — Sovereign Forge Specific

| Control | Title | Status | Notes |
|---------|-------|--------|-------|
| 5.1 | Information security policies | ✅ | INFORMATION_SECURITY_POLICY.md |
| 5.8 | Security in project management | ✅ | SDLC suite; security in Definition of Done |
| 5.9 | Asset inventory | ✅ | ASSET_RISK_REGISTER.md |
| 5.12 | Classification of information | ✅ | IS Policy §3 |
| 5.14 | Information transfer | ✅ | Azure DPA; no third-party voice storage |
| 5.17 | Authentication information | ✅ | API keys in `.env`; excluded from GitHub |
| 5.19 | Supplier security | ✅ | Azure, GitHub ISO 27001 certified |
| 5.23 | Cloud service security | ✅ | Azure OpenAI — Microsoft certified |
| 5.24 | Incident management | ✅ | INCIDENT_LOG.md |
| 5.29 | Business continuity | ✅ | Mock mode fallback |
| 5.31 | Legal and regulatory compliance | ✅ | GDPR (DPIA); AI Act (FRIA) |
| 5.34 | Privacy and data protection | ✅ | No persistent user data by default |
| 8.1 | User endpoint devices | ✅ | Owner's laptop — standard security |
| 8.5 | Secure authentication | ✅ | GitHub MFA; Azure MFA |
| 8.7 | Malware protection | ✅ | Windows Defender |
| 8.10 | Information deletion | ✅ | Session-only; voice not recorded |
| 8.12 | Data leakage prevention | ✅ | `.gitignore` covers all credentials |
| 8.13 | Backup | ✅ | GitHub code backup |
| 8.14 | Redundancy | ✅ | Mock mode for Azure outages |
| 8.24 | Cryptography | ✅ | HTTPS to Azure; TLS in transit |
| 8.25 | Secure development lifecycle | ✅ | Full SDLC documentation |
| 8.28 | Secure coding | ✅ | No hardcoded secrets |
| 8.29 | Security testing | ✅ | Unit tests; 1000 Strikes protocol |
| 8.32 | Change management | ✅ | Git commits; version history |

### Voice Interface — Additional Controls

| Control | Requirement | Status |
|---------|-------------|--------|
| Audio data minimization | No audio files saved | ✅ STT in-browser only |
| User notification | Recording indicator in UI | ⚠️ Planned |
| Consent for voice | Required before any recording storage | ✅ Not stored |

---

*Template adapted from ICT Institute Statement of Applicability ISO 27001-2022 under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
