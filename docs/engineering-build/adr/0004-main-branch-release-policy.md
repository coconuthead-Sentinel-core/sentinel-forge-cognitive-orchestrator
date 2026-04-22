# ADR 0004: Use Main As The Sole Review-Release Branch

## Context And Problem Statement
- The repository accumulated multiple local and remote child branches, which made it harder to tell which branch defined the actual review candidate.
- The user requested a single authoritative branch by the end of this completion pass.

## Decision Drivers
- Simplify HR and technical review.
- Make the repository state easy to mirror between laptop and GitHub.
- Reduce branch drift and stale side branches.

## Considered Options
1. Keep multiple long-lived child branches.
2. Use a release branch separate from `main`.
3. Collapse the review release onto `main` and delete child branches once changes are merged.

## Decision Outcome
Chosen option: 3. Collapse the review release onto `main` and delete child branches once changes are merged.

### Positive Consequences
- Reviewers only need to inspect `main`.
- Local and remote branch state become simpler to reason about.
- Documentation can refer to one canonical branch.

### Negative Consequences
- Experimental branch history is no longer kept as active working branches.
- Future parallel work will need fresh branches when needed.

## Links
- Related docs:
  - `../../../README.md`
  - `../../../docs/sdlc/QA_RELEASE_READINESS.md`
  - `../../../docs/HR_REVIEW_PACKET.md`
