import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # --- Core Application ---
    PROJECT_NAME: str = "Sentinel Forge"
    VERSION: str = "2.0.0"
    ENVIRONMENT: str = "development"  # development, production
    LOG_LEVEL: str = "INFO"
    API_KEY: str = "secret"

    # --- AI Provider ---
    AOAI_ENDPOINT: str = ""
    AOAI_KEY: str = ""  # Mapped from API_KEY in .env if needed, or separate
    AOAI_CHAT_DEPLOYMENT: str = "gpt-4"
    AOAI_EMBED_DEPLOYMENT: str = "text-embedding-ada-002"
    AOAI_API_VERSION: str = "2024-08-01-preview"
    AI_TEMPERATURE: float = 0.7
    MOCK_AI: bool = False

    # --- Infrastructure (Cosmos DB) ---
    COSMOS_ENDPOINT: str = "https://localhost:8081/"
    COSMOS_KEY: str = ""
    COSMOS_DATABASE_NAME: str = "SentinelForgeDB"
    COSMOS_CONTAINER_NAME: str = "Items"

    # --- Data Paths ---
    GLYPHS_PATH: str = str(Path(__file__).parent.parent.parent / "data" / "glyphs_pack.json")
    QUANTUM_NEXUS_BLUEPRINT_PATH: str = str(Path(__file__).parent.parent.parent / "data" / "quantum_nexus_blueprint.yaml")

    # --- Cognitive Zones ---
    ZONE_ACTIVE_THRESHOLD: float = 0.7
    ZONE_PATTERN_THRESHOLD: float = 0.3

    # --- Cognitive Lenses ---
    ADHD_LENS_CHUNK_SIZE: int = 50
    ADHD_LENS_BULLETS: List[str] = ["⚡", "💥", "🚀", "🔥", "💫", "⭐", "🎯"]
    ADHD_LENS_ACTION_WORDS: List[str] = ["start", "begin", "launch", "create", "build", "run", "execute", "activate"]
    AUTISM_LENS_KEYWORDS: List[str] = ["analyze", "clarify", "define", "explain", "specify", "detail", "logic", "system"]
    AUTISM_LENS_DETAIL_DEPTH: int = 3
    DYSLEXIA_LENS_SPATIAL_ANCHORS: List[str] = ["🌟", "🔮", "🎨", "🌈", "🎭", "🎪", "🎨", "🌟"]
    DYSLEXIA_LENS_CHUNK_MARKERS: List[str] = ["📦", "🎁", "🗂️", "📚", "🎯", "🧭"]
    DYSLEXIA_LENS_NAVIGATION_SYMBOLS: List[str] = ["⬆️", "⬇️", "⬅️", "➡️", "🔄", "🔀"]
    DYSLEXIA_LENS_COLOR_INDICATORS: List[str] = ["🟡", "🟠", "🟣", "🟢", "🔵", "🟤"]

    # --- Glyphs ---
    GLYPH_LATTICE_MAP: Dict[str, Dict[str, Any]] = {
        "APEX": {
            "cell": "A1",
            "node": 1,
            "topic": "glyph.initiation",
            "r": 1, "c": 1,
            "label": "Initiation Point (Prime Truth)",
        },
        "CORE": {
            "cell": "H1",
            "node": 2,
            "topic": "glyph.process",
            "r": 2, "c": 2,
            "label": "Processing Core (Diagonal Node 2)",
        },
        "EMIT": {
            "cell": "O1",
            "node": 3,
            "topic": "glyph.action",
            "r": 3, "c": 3,
            "label": "Action Emitter (Diagonal Node 3)",
        },
        "ROOT": {
            "cell": "V1",
            "node": 4,
            "topic": "glyph.ethics",
            "r": 4, "c": 4,
            "label": "Ethics Root (Meta Research focal)",
        },
        "CUBE": {
            "cell": "Z1",
            "node": 5,
            "topic": "glyph.stability",
            "r": 5, "c": 2,
            "label": "Stability Terminus (Career)",
        },
    }
    GLYPH_MAP: Dict[str, str] = {
        # Meta-context symbols
        "🌐": "meta_context",
        "🔭": "observation_mode",
        "🌀": "cognitive_flow",

        # Action pulse symbols
        "🜂": "action_pulse",
        "⚙️": "processing_gear",
        "🔺": "initiation_triangle",

        # Memory zone symbols
        "🟢": "active_zone",
        "🟡": "pattern_zone",
        "🔴": "crystal_zone",

        # Cognitive lens symbols
        "🧠": "neurotypical_mode",
        "⚡": "adhd_burst",
        "🎯": "autism_precision",
        "🌊": "dyslexia_spatial",
    }
    SAMPLE_GLYPHS: Dict[str, Dict[str, Any]] = {
        "APEX": {
            "topic": "initiation",
            "seeds": ["apex", "ignite", "ai_infer", "start", "init", "query"],
            "rules": {"apex": "tag:initiation"}
        },
        "CORE": {
            "topic": "process",
            "seeds": ["core", "resolve", "process", "logic", "reason"],
            "rules": {"process": "tag:process.core"}
        },
        "EMIT": {
            "topic": "action",
            "seeds": ["emit", "launch", "trigger", "output", "send"],
            "rules": {"launch": "tag:action.emit"}
        },
        "ROOT": {
            "topic": "ethics",
            "seeds": ["root", "link", "thread", "memory", "ethics", "bind"],
            "rules": {"ethics": "tag:ethics.guard"}
        },
        "CUBE": {
            "topic": "stability",
            "seeds": ["cube", "resonate", "stabilize", "harmonize", "ground"],
            "rules": {"cube": "tag:stability.struct"}
        }
    }

    # --- Performance ---
    RATE_LIMIT_QPS: float = 10.0

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
