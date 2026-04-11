# Data Protection Impact Assessment (DPIA)
## Sovereign Forge v4.0

**Template source:** ICT Institute — DPIA Template (CC Attribution License)
**Prepared by:** Shannon Bryan Kelly (Data Controller)
**Date:** April 2026

---

## 1. Is a DPIA Required?

| Criterion | Present? |
|-----------|---------|
| Innovative technology (AI + voice) | Yes |
| Audio/voice data processing | Yes |
| Persistent user profile | Yes (preferences only, not identity) |
| Large-scale processing | No |
| Special category data | No (by design) |

**DPIA Decision: Recommended** — Voice interface and Sentinel Profile warrant documented assessment.

---

## 2. Data Flow

```
User speaks / types input
        ↓
FastAPI (in-memory only)
        ↓
Azure OpenAI o4-mini (Microsoft cloud)
        ↓
Response → TTS voice output
        ↓
[Optional] Cosmos DB — NOT active by default
Sentinel Profile → JSONStore (local file, preferences only)
```

---

## 3. Personal Data Inventory

| Data Element | Type | Stored? | Legal Basis |
|-------------|------|---------|-------------|
| User text prompts | Personal (potentially) | No — session only | Legitimate interest |
| Voice/audio input | Personal | No — processed in-session, not recorded | Legitimate interest |
| Sentinel Profile | Preferences (not identity) | Yes — local JSONStore | Legitimate interest |
| IP address | Personal | No — not logged | N/A |
| WebSocket session | Technical | No — session only | Legitimate interest |

---

## 4. Risk Assessment

| Risk | Likelihood | Severity | Level | Mitigation | Residual |
|------|-----------|---------|-------|------------|---------|
| User enters PII in voice/text | Medium | Medium | 🟡 MEDIUM | No storage; user guidance | 🟢 LOW |
| Voice data inadvertently recorded | Low | High | 🟡 MEDIUM | Session-only STT; no audio files saved | 🟢 LOW |
| Sentinel Profile contains identifiable data | Low | Medium | 🟢 LOW | Profile stores preferences only | 🟢 LOW |
| Azure processes personal voice data | High (by design) | Low | 🟢 LOW | Microsoft DPA applies; no training on data | 🟢 LOW |
| Cosmos DB stores personal data when activated | Low (not active) | High | 🟡 MEDIUM | Not active; full DPIA update required before activation | 🟢 LOW |

**Overall: LOW RISK** at current deployment scope.

---

## 5. Data Subject Rights

All rights easily met — no personal data stored by default. Sentinel Profile contains only cognitive preferences and can be deleted by removing the local JSONStore file.

---

## 6. DPIA Conclusion

Processing may proceed. Must update before:
- Activating Cosmos DB persistence
- Multi-user deployment
- Any storage of voice recordings

---

## 7. Sign-Off

| Role | Name | Date |
|------|------|------|
| Data Controller / Architect | Shannon Bryan Kelly | April 2026 |

---

*Template adapted from ICT Institute DPIA Template under Creative Commons Attribution License.*
*Source: https://github.com/swzaken/freetemplates*
