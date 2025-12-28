"""Glyph Parser for Symbolic Sequence Processing.

Parses symbolic glyph sequences and converts them to structured metadata
for the Cognitive Orchestrator. Provides mapping from visual symbols to
cognitive concepts and actions.

Architecture:
    glyph_parser.py → CognitiveOrchestrator → EventBus
"""

import logging
from typing import Dict, Any, Optional

from backend.core.config import Settings

logger = logging.getLogger(__name__)


def parse_glyph_sequence(sequence: str, settings: Settings) -> Dict[str, Any]:
    """
    Parse a sequence of glyphs into structured metadata.

    Args:
        sequence: String containing glyph symbols
        settings: The application settings object

    Returns:
        Dict with parsed glyph information
    """
    if not sequence or not sequence.strip():
        return {"parsed": False, "glyphs": [], "concepts": []}

    parsed_glyphs = []
    concepts = []

    for char in sequence:
        if char in settings.GLYPH_MAP:
            concept = settings.GLYPH_MAP[char]
            parsed_glyphs.append({"symbol": char, "concept": concept})
            concepts.append(concept)
            logger.debug(f"🜂 Parsed glyph: {char} → {concept}")

    return {
        "parsed": len(parsed_glyphs) > 0,
        "glyphs": parsed_glyphs,
        "concepts": concepts,
        "sequence_length": len(sequence),
        "parsed_count": len(parsed_glyphs)
    }


def get_available_glyphs(settings: Settings) -> Dict[str, str]:
    """Get the complete glyph symbol map."""
    return settings.GLYPH_MAP.copy()


def add_glyph_mapping(symbol: str, concept: str, settings: Settings) -> None:
    """
    Add a new glyph mapping dynamically.

    Args:
        symbol: The glyph symbol (emoji/character)
        concept: The cognitive concept it represents
        settings: The application settings object
    """
    settings.GLYPH_MAP[symbol] = concept
    logger.info(f"🜂 Added glyph mapping: {symbol} → {concept}")


def get_concept_for_glyph(symbol: str, settings: Settings) -> Optional[str]:
    """Get the concept for a specific glyph symbol."""
    return settings.GLYPH_MAP.get(symbol)