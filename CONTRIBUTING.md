# Contributing to Sentinel Forge

Thank you for contributing to Sentinel Forge.

## Mission
The project explores AI orchestration patterns that support multiple cognitive presentation styles while remaining testable and reviewable as software.

## Ways To Contribute
- Fix bugs or improve runtime stability
- Improve documentation and review packets
- Add or refine tests
- Propose focused enhancements to lens, glyph, or event-driven behavior

## Development Setup
```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
$env:MOCK_AI = "true"
```

## Required Validation Before Submission
```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe scripts\smoke_test.py
```

Refresh documentation when public behavior changes:
- `README.md`
- `ARCHITECTURE.md`
- `docs/API.md`
- `docs/API_EXAMPLES.md`
- relevant files under `docs/engineering-build/` or `docs/sdlc/`

## Contribution Rules
- Keep changes scoped to the requested problem.
- Do not claim behavior that has not been validated.
- Add tests when public behavior changes.
- Preserve the active paperwork set instead of creating competing versions.

## Branching
- `main` is the canonical release branch.
- Feature branches are acceptable during development, but releases should converge back to `main`.

## Conduct
Follow `CODE_OF_CONDUCT.md`.

## License
By contributing, you agree that contributions are provided under the MIT License.
