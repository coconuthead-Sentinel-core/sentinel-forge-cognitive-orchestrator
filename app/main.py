# app/main.py
"""
Sentinel Forge Dashboard Application
Adaptive AI processing UI with cognitive metrics visualization

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
    title="Sentinel Forge Dashboard",
    description="Real-time dashboard for AI processing metrics and visualization",
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
        "title": "Sentinel Forge Dashboard",
        "version": "2.0.0",
        "phase": "Dashboard Integration",
        "endpoints": {
            "dashboard": "/dashboard",
            "metrics": "/api/metrics",
            "resolve": "/api/resolve/{ref}",
            "dependency": "/api/dependency/{dep_id}",
            "diagonal_trace": "/api/coordinate/diagonal",
            "lateral_trace": "/api/coordinate/lateral",
        },
        "coordinate_formats": [
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
