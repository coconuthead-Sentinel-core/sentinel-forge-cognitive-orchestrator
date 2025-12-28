# PRIME DIRECTIVE - Sentinel Forge Cognitive Orchestrator

## Mission Statement

Sentinel Forge is a **Cognitive AI Orchestration Platform** designed to support neurodivergent-aware AI processing. The system provides adaptive processing modes for ADHD, Autism, Dyslexia, and Neurotypical cognitive patterns, with a three-zone memory system for optimal information management.

## Core Principles

### 1. Neurodivergent-First Design
- **ADHD Lens**: Burst processing with rapid context switching
- **Autism Lens**: Precision-focused with deep pattern analysis  
- **Dyslexia Lens**: Spatial and visual processing emphasis
- **Neurotypical Lens**: Baseline balanced processing

### 2. Three-Zone Memory Architecture
- **🟢 Active Zone** (>0.7 entropy): High-entropy, actively processed information
- **🟡 Pattern Zone** (0.3-0.7 entropy): Mid-level patterns and connections
- **🔴 Crystal Zone** (<0.3 entropy): Low-entropy, crystallized knowledge

### 3. Domain-Driven Design
- Pure domain models with no infrastructure concerns
- Repository pattern for data persistence abstraction
- Clean separation between API, domain, and infrastructure layers

## Development Workflow

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Create local configuration
cp .env.example .env

# Run in mock mode (zero external dependencies)
uvicorn backend.main:app --reload --port 8000
```

### Environment Modes

#### Mock Mode (Development)
- Set `MOCK_AI=true` in .env
- Leave `COSMOS_KEY` empty
- Zero external dependencies
- Instant startup

#### Production Mode
- Set `MOCK_AI=false`
- Configure Azure OpenAI credentials
- Configure Cosmos DB credentials
- Full cloud integration

## Automated Pull Request Protocol

### Pre-Commit Checklist
1. ✅ All backend dependencies in requirements.txt
2. ✅ Backend starts without errors in mock mode
3. ✅ API endpoints return valid responses
4. ✅ Evaluation pipeline runs successfully
5. ✅ Documentation updated as needed

### CI/CD Pipeline
The repository uses GitHub Actions for continuous integration:

1. **Backend Stability**: Server must start without errors
2. **Dependency Check**: All Python dependencies must be installable
3. **HTTP Testing**: Evaluation uses real HTTP requests (not TestClient)
4. **Automated Lifecycle**: run_full_eval.py manages server start/stop

### Pull Request Standards

#### Title Format
```
[Type]: Brief description

Types: Fix, Feat, Refactor, Docs, Test, Chore
```

#### Description Template
```markdown
## Summary
Brief description of changes

## Changes Made
- [ ] Backend stability fixes
- [ ] Evaluation pipeline updates
- [ ] Documentation updates
- [ ] Configuration improvements

## Testing
- [ ] Backend starts without errors
- [ ] Full evaluation pipeline passes
- [ ] CI/CD passes

## Breaking Changes
None / List any breaking changes
```

### Automated Server Lifecycle

The evaluation pipeline (`scripts/run_full_eval.py`) follows this workflow:

1. **Start Server**: Spawn backend server process
2. **Wait for Ready**: Poll port 8000 until server responds
3. **Run Collection**: HTTP requests to collect AI responses
4. **Run Evaluation**: Score responses using evaluation metrics
5. **Cleanup**: Terminate server process gracefully

**Key Change from Previous Version**: Uses `requests` library with real HTTP instead of FastAPI's `TestClient` for true integration testing.

## Architecture Overview

```
backend/
├── domain/          # Pure business logic (no DB fields)
├── infrastructure/  # Cosmos DB, repositories
├── services/        # Cognitive orchestration, lenses
├── adapters/        # AI provider adapters (Azure, Mock)
├── api.py          # FastAPI routes
└── main.py         # Application entry point

evaluation/
├── test_queries.json      # Test cases
├── collect_responses.py   # HTTP-based collection
└── run_evaluation.py      # Scoring engine

scripts/
└── run_full_eval.py       # Full pipeline orchestration
```

## Configuration Management

All environment variables defined in `backend/core/config.py` using Pydantic Settings:
- Single source of truth
- Type validation
- .env file support
- Graceful defaults

Example `.env` file provided in `.env.example` with comprehensive documentation.

## Error Handling Philosophy

### Graceful Degradation
- Mock DB mode if Cosmos DB unavailable
- Mock AI mode if Azure OpenAI unavailable
- Continue operation with reduced functionality

### Explicit Logging
- Clear warning messages for degraded mode
- Info messages for successful initialization
- Error messages with context

### Zero External Dependencies (Development)
- Local development requires NO cloud services
- Full mock mode for offline development
- CI/CD can run without Azure credentials

## Testing Strategy

### Integration Testing
- Real HTTP requests via `requests` library
- Automated server lifecycle management
- End-to-end pipeline validation

### Evaluation Metrics
- Relevance scoring
- Coherence analysis  
- Groundedness verification
- Mock mode for pipeline testing

## Security Considerations

1. **API Key Protection**: Never commit real keys
2. **Environment Variables**: Use .env (gitignored)
3. **Mock Mode Defaults**: Safe for public repositories
4. **Azure AAD**: Token-based authentication when enabled

## Contribution Guidelines

1. Fork the repository
2. Create feature branch
3. Make minimal, focused changes
4. Run full evaluation pipeline locally
5. Create PR following template
6. Wait for CI/CD validation
7. Address review feedback

## Resources

- **Architecture**: See ARCHITECTURE.md
- **Quick Start**: See README.md  
- **API Docs**: http://localhost:8000/docs (when running)
- **Troubleshooting**: See TROUBLESHOOTING.md

---

**Last Updated**: 2025-12-28  
**Version**: 2.0.0  
**Status**: Active Development
