"""Glyph Processor for Symbolic Pattern Recognition.

Loads and processes glyph patterns from JSON configuration for symbolic
processing in the Cognitive Orchestrator. Provides fuzzy matching against
text to identify symbolic patterns and generate metadata.

Architecture:
    GlyphProcessor → glyphs_pack.json → SymbolicMetadata → CognitiveOrchestrator
"""

import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass

logger = logging.getLogger(__name__)

# Import from domain models to avoid circular imports
from backend.domain.models import GlyphMatch, SymbolicMetadata


class GlyphProcessor:
    """
    Processes text against glyph patterns for symbolic recognition.

    Responsibilities:
    1. Load glyph definitions from JSON
    2. Perform fuzzy pattern matching against text
    3. Generate symbolic metadata with confidence scores
    4. Apply transformation rules based on matches
    """

    def __init__(self, glyphs_path: Optional[str] = None):
        """
        Initialize GlyphProcessor.

        Args:
            glyphs_path: Path to glyphs JSON file. Defaults to data/glyphs_pack.json
        """
        self.glyphs_path = glyphs_path or self._default_glyphs_path()
        self.glyphs: Dict[str, Dict[str, Any]] = {}
        self._load_glyphs()
        logger.info(f"🜂 GlyphProcessor initialized with {len(self.glyphs)} shapes")

    def _default_glyphs_path(self) -> str:
        """Get default path to glyphs file."""
        # Assume we're in backend/services/, go up two levels to project root
        backend_dir = Path(__file__).parent.parent.parent
        return str(backend_dir / "data" / "glyphs_pack.json")

    def _load_glyphs(self) -> None:
        """Load glyph definitions from JSON file."""
        try:
            with open(self.glyphs_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.glyphs = data.get('shapes', {})
                logger.info(f"📖 Loaded {len(self.glyphs)} glyph shapes")
        except FileNotFoundError:
            logger.warning(f"⚠️ Glyphs file not found: {self.glyphs_path}")
            # Create sample glyphs if file doesn't exist
            self._create_sample_glyphs()
        except json.JSONDecodeError as e:
            logger.error(f"🔴 Invalid JSON in glyphs file: {e}")
            raise

    def _create_sample_glyphs(self) -> None:
        """Create sample glyphs for development."""
        logger.info("🜂 Creating sample glyphs for development")
        self.glyphs = {
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

    def process_text(self, text: str) -> SymbolicMetadata:
        """
        Process text for symbolic patterns.

        Args:
            text: Input text to analyze

        Returns:
            SymbolicMetadata with matches and derived information
        """
        if not text or not text.strip():
            return SymbolicMetadata([], None, set(), 0.0)

        # Find all glyph matches
        matches = []
        for shape_name, shape_data in self.glyphs.items():
            match = self._match_glyph(text, shape_name, shape_data)
            if match:
                matches.append(match)

        # Sort by confidence
        matches.sort(key=lambda m: m.confidence, reverse=True)

        # Derive metadata
        dominant_topic = matches[0].topic if matches else None
        
        return SymbolicMetadata(
            matched_glyphs=matches,
            dominant_topic=dominant_topic,
        )

    def _match_glyph(self, text: str, shape_name: str, shape_data: Dict[str, Any]) -> Optional[GlyphMatch]:
        """
        Match a single glyph against text.

        Uses fuzzy matching with:
        - Exact word matches (highest confidence)
        - Partial substring matches (medium confidence)
        - Stem/root similarity (lower confidence)
        """
        text_lower = text.lower()
        seeds = shape_data.get('seeds', [])
        rules = shape_data.get('rules', {})
        topic = shape_data.get('topic', 'unknown')

        matched_seeds = []
        applied_rules = {}
        total_score = 0.0
        match_count = 0

        for seed in seeds:
            seed_lower = seed.lower()

            # Exact word match (highest confidence)
            if re.search(r'\b' + re.escape(seed_lower) + r'\b', text_lower):
                matched_seeds.append(seed)
                total_score += 1.0
                match_count += 1

                # Apply rules if seed matches
                if seed in rules:
                    applied_rules[seed] = rules[seed]

            # Partial substring match (medium confidence)
            elif seed_lower in text_lower:
                matched_seeds.append(seed)
                total_score += 0.7
                match_count += 1

                # Apply rules for partial matches too
                if seed in rules:
                    applied_rules[seed] = rules[seed]

        if match_count == 0:
            return None

        # Calculate average confidence
        confidence = total_score / match_count

        return GlyphMatch(
            shape=shape_name,
            topic=topic,
            confidence=min(confidence, 1.0),  # Cap at 1.0
            matched_seeds=matched_seeds,
            applied_rules=applied_rules
        )

    def get_available_shapes(self) -> List[str]:
        """Get list of available glyph shapes."""
        return list(self.glyphs.keys())

    def get_shape_info(self, shape: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific glyph shape."""
        return self.glyphs.get(shape)

    def reload_glyphs(self) -> None:
        """Reload glyphs from file."""
        self._load_glyphs()


# --- Singleton Instance (Optional convenience) ---

_glyph_processor: Optional[GlyphProcessor] = None


def get_glyph_processor() -> GlyphProcessor:
    """
    Get the default GlyphProcessor instance (lazy singleton).

    Returns:
        GlyphProcessor instance
    """
    global _glyph_processor
    if _glyph_processor is None:
        _glyph_processor = GlyphProcessor()
    return _glyph_processor