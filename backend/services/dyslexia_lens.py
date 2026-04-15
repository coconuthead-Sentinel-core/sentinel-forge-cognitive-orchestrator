"""Dyslexia Spatial Lens - Multi-dimensional Processing for Cognitive Enhancement.

Implements Dyslexia-friendly processing mode with:
- Visual anchors and spatial organization
- Symbol-rich representations
- Chunking with color-coded sections
- Alternative pathways for information flow

Architecture:
    DyslexiaLens → CognitiveOrchestrator → AI Adapter
"""

import logging
import re
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class DyslexiaLens:
    """
    Dyslexia Spatial Lens for multi-dimensional, visually-anchored processing.

    Transforms content into Dyslexia-friendly formats:
    - Adds visual anchors and spatial markers
    - Uses symbols and colors for organization
    - Breaks information into manageable chunks
    - Provides alternative navigation paths
    """

    # Configuration
    SPATIAL_ANCHORS = ["🌟", "🔮", "🎨", "🌈", "🎭", "🎪", "🎨", "🌟"]
    CHUNK_MARKERS = ["📦", "🎁", "🗂️", "📚", "🎯", "🧭"]
    NAVIGATION_SYMBOLS = ["⬆️", "⬇️", "⬅️", "➡️", "🔄", "🔀"]
    COLOR_INDICATORS = ["🟡", "🟠", "🟣", "🟢", "🔵", "🟤"]
    
    # Odooe Lattice Integration
    ODOOE_LATTICE_ENABLED = True
    MIRROR_ID = "M5"  # Spatial Mapping

    def __init__(self):
        """Initialize Dyslexia lens with default settings."""
        self.anchor_index = 0
        self.chunk_index = 0
        self.color_index = 0
        logger.info("🧠 Dyslexia Spatial Lens initialized (Odooe Lattice Active)")

    def transform_context(self, context: str) -> str:
        """
        Transform context into a Dyslexia-friendly format using spatial layout and symbols.
        This fulfills Task 5.3.

        Args:
            context: Original context string.

        Returns:
            Transformed context with a mind-map-like structure.
        """
        if not context or not context.strip():
            return context

        sentences = re.split(r'(?<=[.!?])\s+', context.strip())
        if not sentences:
            return ""

        # 1. Identify the central idea (first sentence)
        central_idea = sentences[0]
        
        # 2. Identify key concepts (nouns and verbs from the rest of the text)
        other_text = " ".join(sentences[1:])
        words = re.findall(r'\b\w{4,}\b', other_text.lower()) # Find words with 4+ letters
        # A simple way to get "key concepts" is to find unique words.
        # A more advanced method would use NLP part-of-speech tagging.
        key_concepts = sorted(list(set(words)))[:5] # Limit to 5 key concepts

        # 3. Create a symbol map for concepts
        symbol_map = {concept: symbol for concept, symbol in zip(key_concepts, ["💡", "⚙️", "🔗", "🎯", "📊"])}

        # 4. Assemble the spatial/symbolic output
        transformed_parts = []
        transformed_parts.append("--- Spatial Map ---")
        transformed_parts.append(f"      [ 🧠 Central Idea ]")
        transformed_parts.append(f"              |")
        transformed_parts.append(f"      \" {central_idea} \"")
        transformed_parts.append("              |")
        transformed_parts.append("     /        |        \\")
        transformed_parts.append("    /         |         \\")

        # Branch out with key concepts
        if key_concepts:
            concept_lines = []
            for concept in key_concepts:
                symbol = symbol_map.get(concept, "🔹")
                concept_lines.append(f"{symbol} {concept.capitalize()}")
            
            # Arrange concepts in a branching structure
            if len(concept_lines) > 0:
                transformed_parts.append(f"  {concept_lines[0]:<15}")
            if len(concept_lines) > 1:
                transformed_parts[-1] += f"--- [ {concept_lines[1]} ]"
            if len(concept_lines) > 2:
                 transformed_parts.append(f"    /         |         \\")
                 transformed_parts.append(f"  [ {concept_lines[2]} ]")
            if len(concept_lines) > 3:
                 transformed_parts[-1] += f" --- {concept_lines[3]} 🔹"
            if len(concept_lines) > 4:
                 transformed_parts.append(f"              |")
                 transformed_parts.append(f"        🔹 {concept_lines[4]}")


        transformed_parts.append("\n--- End Map ---")

        logger.debug(f"🧠 Dyslexia lens transformed text into a spatial map with {len(key_concepts)} concepts.")
        return "\n".join(transformed_parts)

    def _identify_chunks(self, text: str) -> List[str]:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return text.split('\n\n')

    def _add_spatial_anchors(self, chunk: str, position: int) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return chunk

    def _add_visual_chunking(self, chunk: str, position: int) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return chunk

    def _add_navigation_paths(self, chunk: str, position: int, total: int) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return chunk

    def _create_spatial_layout(self, chunks: List[str]) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return "\n".join(chunks)

    def _add_overview_map(self, text: str, num_chunks: int) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return text


    def get_transformation_stats(self) -> Dict[str, Any]:
        """Get statistics about transformations applied."""
        return {
            "lens_type": "dyslexia_spatial",
            "anchors_used": self.anchor_index,
            "chunks_processed": self.chunk_index,
            "colors_used": self.color_index,
            "spatial_anchors": self.SPATIAL_ANCHORS,
            "navigation_symbols": self.NAVIGATION_SYMBOLS,
        }


# --- Convenience Functions ---

def create_dyslexia_lens() -> DyslexiaLens:
    """Create and return a configured Dyslexia lens instance."""
    return DyslexiaLens()


def transform_with_dyslexia_lens(text: str) -> str:
    """Convenience function to transform text with Dyslexia lens."""
    lens = DyslexiaLens()
    return lens.transform_context(text)