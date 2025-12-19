# app/main.py
"""
Sentinel Forge Phase 2 Dashboard Application
Quantum Nexus lattice-aware cognitive orchestration UI

Run with: uvicorn app.main:app --reload --port 8001
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.dashboard import router as dashboard_router

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
STATIC_DIR = PROJECT_ROOT / "static"

app = FastAPI(
    title="Sentinel Forge • Quantum Nexus Dashboard",
    description="Phase 2 Dashboard with Great Greg coordinate resolver and lattice dependency visualization",
    version="2.0.0",
)

# Include dashboard routes
app.include_router(dashboard_router)

# Mount static files if directory exists
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
async def root():
    """Root endpoint with API overview."""
    return {
        "title": "Sentinel Forge • Quantum Nexus Dashboard",
        "version": "2.0.0",
        "phase": "Phase 2: Dashboard Integration",
        "endpoints": {
            "dashboard": "/dashboard",
            "metrics": "/api/metrics",
            "resolve": "/api/resolve/{ref}",
            "dependency": "/api/dependency/{dep_id}",
            "diagonal_trace": "/api/lattice/diagonal",
            "lateral_trace": "/api/lattice/lateral",
        },
        "great_greg_formats": [
            "P1 (direct cell)",
            "Node_3:P1 (node-prefixed)",
            "Node_3.R3C4 (row/column/node)",
        ],
        "lattice": {
            "origin": "A1 (Prime Truth)",
            "terminus": "Z1 (Dynamic Expansion)",
            "primary_flow": "left_to_right_then_top_to_bottom",
            "rule": "no_bad_input_no_bad_process_no_bad_output",
        }
    }
