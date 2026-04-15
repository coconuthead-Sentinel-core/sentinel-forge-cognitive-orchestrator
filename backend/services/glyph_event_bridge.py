"""Glyph Event Bridge - Phase 4 Symbolic Processing.

Bridges GlyphProcessor output to EventBus with Quantum Nexus lattice coordinates.
Each glyph shape maps to a cell in the lattice, enabling symbolic event routing.

Architecture:
    GlyphProcessor → GlyphEventBridge → EventBus[topic=glyph.*] → WebSocket/Dashboard
    
Lattice Mapping:
    APEX  → A1 (Node 1: Technical Arsenal) - Initiation/Query start
    CORE  → H1 (Node 2: Core Frameworks)   - Processing/Logic
    EMIT  → O1 (Node 3: Skill Forge)       - Action/Output
    ROOT  → V1 (Node 4: Meta Research)     - Ethics/Memory binding
    CUBE  → Z1 (Node 5: Career)            - Stability/Grounding
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from backend.eventbus import bus
from backend.domain.models import SymbolicMetadata
from backend.core.config import Settings

logger = logging.getLogger(__name__)

@dataclass
class GlyphEvent:
    """Event payload for glyph processing results."""
    
    glyph: str
    cell: str
    node: int
    topic: str
    confidence: float
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    matched_seeds: List[str] = field(default_factory=list)
    applied_rules: Dict[str, str] = field(default_factory=dict)
    source_text_hash: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "glyph": self.glyph,
            "cell": self.cell,
            "node": self.node,
            "topic": self.topic,
            "confidence": self.confidence,
            "timestamp": self.timestamp,
            "matched_seeds": self.matched_seeds,
            "applied_rules": self.applied_rules,
            "source_text_hash": self.source_text_hash,
        }


class GlyphEventBridge:
    """
    Bridges glyph processing results to EventBus with lattice coordinates.
    """

    def __init__(self, settings: Settings):
        """Initialize the bridge with application settings."""
        self.settings = settings
        self.processed_hashes: Set[str] = set()
        logger.info("Glyph Event Bridge initialized.")

    async def publish_glyph_event(self, glyph_metadata: SymbolicMetadata):
        """
        Publish a glyph event to the EventBus based on lattice mapping.
        """
        glyph_name = glyph_metadata.glyph
        lattice_info = self.settings.GLYPH_LATTICE_MAP.get(glyph_name)

        if not lattice_info:
            logger.warning(f"No lattice mapping found for glyph: {glyph_name}")
            return

        # Avoid duplicate events for the same text processing result
        if glyph_metadata.source_text_hash and glyph_metadata.source_text_hash in self.processed_hashes:
            logger.debug(f"Skipping duplicate glyph event for hash: {glyph_metadata.source_text_hash}")
            return
        
        if glyph_metadata.source_text_hash:
            self.processed_hashes.add(glyph_metadata.source_text_hash)

        event = GlyphEvent(
            glyph=glyph_name,
            cell=lattice_info["cell"],
            node=lattice_info["node"],
            topic=lattice_info["topic"],
            confidence=glyph_metadata.confidence,
            matched_seeds=glyph_metadata.matched_seeds,
            applied_rules=glyph_metadata.applied_rules,
            source_text_hash=glyph_metadata.source_text_hash,
        )

        try:
            await bus.publish(event.topic, event.to_dict())
            logger.info(f"Published glyph event to topic '{event.topic}': {event.glyph} -> {event.cell}")
        except Exception as e:
            logger.error(f"Failed to publish glyph event: {e}")
