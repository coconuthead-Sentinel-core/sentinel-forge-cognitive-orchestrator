# MASVS Control Mapping

## Scope Decision
OWASP MASVS is not applicable to the current release because this repository does not ship a mobile application binary.

## Control Family Disposition
| MASVS Area | Applicability | Rationale |
|---|---|---|
| Architecture and design | Not applicable | No mobile client target exists |
| Data storage and privacy | Not applicable | No on-device mobile storage path exists |
| Cryptography | Not applicable | No mobile app runtime exists |
| Authentication and session management | Not applicable | No mobile app authentication surface exists |
| Network communication | Not applicable | No mobile app network stack exists |
| Platform interaction | Not applicable | No iOS entitlements, permissions, or bundle metadata exist |
| Code quality and build settings | Not applicable | No Xcode or Apple build pipeline exists |
| Resilience | Not applicable | No mobile app binary exists to harden |

## Review Rule
This `not applicable` mapping is considered complete for the current release. If a mobile client is introduced later, replace this file with an active MASVS mapping by feature and control.
