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

    def __init__(self):
        """Initialize Dyslexia lens with default settings."""
        self.anchor_index = 0
        self.chunk_index = 0
        self.color_index = 0
        logger.info("🧠 Dyslexia Spatial Lens initialized")

    def transform_context(self, context: str) -> str:
        """
        Transform context into Dyslexia-friendly format.

        Args:
            context: Original context string

        Returns:
            Transformed context with spatial anchors and visual organization
        """
        if not context.strip():
            return context

        # Split into logical chunks
        chunks = self._identify_chunks(context)

        # Transform each chunk
        transformed_chunks = []
        for i, chunk in enumerate(chunks):
            transformed = self._add_spatial_anchors(chunk, i)
            transformed = self._add_visual_chunking(transformed, i)
            transformed = self._add_navigation_paths(transformed, i, len(chunks))
            transformed_chunks.append(transformed)

        # Combine with spatial layout
        result = self._create_spatial_layout(transformed_chunks)

        # Add overview map
        result = self._add_overview_map(result, len(chunks))

        return result

    def _identify_chunks(self, text: str) -> List[str]:
        """Identify logical chunks in the text."""
        # Split by paragraphs first
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

        chunks = []
        for para in paragraphs:
            # Further split long paragraphs into sentences
            if len(para) > 200:
                sentences = re.split(r'(?<=[.!?])\s+', para)
                # Group sentences into chunks of 2-3
                for i in range(0, len(sentences), 2):
                    chunk = ' '.join(sentences[i:i+2])
                    if chunk.strip():
                        chunks.append(chunk.strip())
            else:
                chunks.append(para)

        return chunks

    def _add_spatial_anchors(self, chunk: str, position: int) -> str:
        """Add spatial anchor to chunk."""
        anchor = self.SPATIAL_ANCHORS[self.anchor_index % len(self.SPATIAL_ANCHORS)]
        self.anchor_index += 1

        # Add anchor at the beginning
        return f"{anchor} {chunk}"

    def _add_visual_chunking(self, chunk: str, position: int) -> str:
        """Add visual chunking markers."""
        marker = self.CHUNK_MARKERS[self.chunk_index % len(self.CHUNK_MARKERS)]
        color = self.COLOR_INDICATORS[self.color_index % len(self.COLOR_INDICATORS)]

        self.chunk_index += 1
        self.color_index += 1

        # Wrap chunk in visual container
        return f"{marker}{color} {chunk} {color}{marker}"

    def _add_navigation_paths(self, chunk: str, position: int, total: int) -> str:
        """Add navigation path indicators."""
        nav_symbols = []

        # Add flow indicators
        if position > 0:
            nav_symbols.append("⬆️")  # Previous
        if position < total - 1:
            nav_symbols.append("⬇️")  # Next

        # Add connection indicators
        if total > 1:
            nav_symbols.append("🔀")  # Connections

        nav_string = ' '.join(nav_symbols)
        if nav_string:
            chunk = f"{chunk} [{nav_string}]"

        return chunk

    def _create_spatial_layout(self, chunks: List[str]) -> str:
        """Create a spatial layout for the chunks."""
        if len(chunks) <= 3:
            # Simple vertical layout
            return '\n\n'.join(chunks)
        else:
            # Create a grid-like layout with visual separation
            layout_lines = []
            for i, chunk in enumerate(chunks):
                if i % 2 == 0:
                    layout_lines.append(chunk)
                else:
                    # Indent alternating chunks for spatial variety
                    layout_lines.append(f"   ↳ {chunk}")

            return '\n\n'.join(layout_lines)

    def _add_overview_map(self, text: str, num_chunks: int) -> str:
        """Add an overview map of the content structure."""
        if num_chunks <= 1:
            return text

        # Create a simple map
        map_symbols = []
        for i in range(min(num_chunks, 5)):  # Limit to 5 for readability
            map_symbols.append(self.SPATIAL_ANCHORS[i % len(self.SPATIAL_ANCHORS)])

        if num_chunks > 5:
            map_symbols.append("...")

        map_str = ' → '.join(map_symbols)
        overview = f"🗺️ **Content Map:** {map_str}\n\n{text}"

        return overview

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