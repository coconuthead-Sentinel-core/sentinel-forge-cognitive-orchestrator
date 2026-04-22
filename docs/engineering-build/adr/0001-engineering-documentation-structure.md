# ADR 0001: Keep Active Paperwork In-Repo And Archive Prior Filled Packets

## Context And Problem Statement
- The repository accumulated multiple generations of paperwork, including previously filled narrative packets and new clean template surfaces.
- Reviewers need a single active documentation path that matches `main`, while earlier filled artifacts still need to remain available as proof of past work.

## Decision Drivers
- Reduce ambiguity for technical reviewers.
- Preserve historical evidence without letting it define the active release.
- Keep documentation maintenance inside the repository.

## Considered Options
1. Keep all filled and active paperwork mixed together.
2. Delete all older paperwork and keep only the newest files.
3. Archive prior filled packets inside the repo and keep the active packet at canonical paths.

## Decision Outcome
Chosen option: 3. Archive prior filled packets inside the repo and keep the active packet at canonical paths.

### Positive Consequences
- Reviewers can follow one documentation path through `docs/README.md`.
- Historical artifacts are still available under `docs/archive/`.
- Active paperwork can be updated without copying claims from older packets.

### Negative Consequences
- The repository contains more documentation files overall.
- Maintainers must keep archive and active sections clearly separated.

## Pros And Cons Of The Options
### Keep all paperwork mixed together
- Pros:
  - No file movement required.
- Cons:
  - Review confusion remains high.
  - Contradictory statements are harder to detect.

### Delete older paperwork
- Pros:
  - Repository appears simpler.
- Cons:
  - Historical evidence is lost.
  - Prior work cannot be audited later.

### Archive prior filled packets inside the repo
- Pros:
  - Clean active path with preserved evidence.
  - Supports HR and technical review simultaneously.
- Cons:
  - Requires archive maintenance discipline.

## Links
- Related docs:
  - `../../README.md`
  - `../../../docs/archive/filled-paperwork-2026-04-22/README.md`
  - `../../../docs/README.md`
