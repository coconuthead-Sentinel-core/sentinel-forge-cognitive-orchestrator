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

from backend.core.config import Settings


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

    def __init__(self, settings: Settings):
        """Initialize Dyslexia lens with settings."""
        self.settings = settings
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
        anchor = self.settings.DYSLEXIA_LENS_SPATIAL_ANCHORS[self.anchor_index % len(self.settings.DYSLEXIA_LENS_SPATIAL_ANCHORS)]
        self.anchor_index += 1
        return f"{anchor} {chunk}"

    def _add_visual_chunking(self, chunk: str, position: int) -> str:
        """Add visual chunking markers."""
        marker = self.settings.DYSLEXIA_LENS_CHUNK_MARKERS[self.chunk_index % len(self.settings.DYSLEXIA_LENS_CHUNK_MARKERS)]
        color = self.settings.DYSLEXIA_LENS_COLOR_INDICATORS[self.color_index % len(self.settings.DYSLEXIA_LENS_COLOR_INDICATORS)]
        self.chunk_index += 1
        self.color_index += 1
        return f"\n--- {marker} {color} Chunk {position + 1} ---\n{chunk}"

    def _add_navigation_paths(self, chunk: str, position: int, total_chunks: int) -> str:
        """Add navigation symbols for alternative pathways."""
        nav = []
        if position > 0:
            nav.append(f"{self.settings.DYSLEXIA_LENS_NAVIGATION_SYMBOLS[0]} Prev")
        if position < total_chunks - 1:
            nav.append(f"{self.settings.DYSLEXIA_LENS_NAVIGATION_SYMBOLS[1]} Next")

        nav.append(f"{self.settings.DYSLEXIA_LENS_NAVIGATION_SYMBOLS[4]} Re-read")
        nav_str = " | ".join(nav)
        return f"{chunk}\n\n_Navigate: [ {nav_str} ]_"

    def _create_spatial_layout(self, chunks: List[str]) -> str:
        """Create a spatial layout for the chunks."""
        # Simple vertical layout for now
        return "\n".join(chunks)

    def _add_overview_map(self, text: str, total_chunks: int) -> str:
        """Add an overview map to the beginning of the text."""
        map_items = [f"{self.settings.DYSLEXIA_LENS_CHUNK_MARKERS[i % len(self.settings.DYSLEXIA_LENS_CHUNK_MARKERS)]} Chunk {i+1}" for i in range(total_chunks)]
        overview = f"🗺️ Overview Map: {' -> '.join(map_items)}\n\n"
        return overview + text

    def get_transformation_stats(self) -> Dict[str, Any]:
        """Get statistics about transformations applied."""
        return {
            "lens_type": "dyslexia_spatial",
            "anchors_used": self.anchor_index,
            "chunks_processed": self.chunk_index,
            "colors_used": self.color_index,
            "spatial_anchors": self.settings.DYSLEXIA_LENS_SPATIAL_ANCHORS,
            "navigation_symbols": self.settings.DYSLEXIA_LENS_NAVIGATION_SYMBOLS,
        }


# --- Convenience Functions ---

def create_dyslexia_lens(settings: Settings) -> DyslexiaLens:
    """Create and return a configured Dyslexia lens instance."""
    return DyslexiaLens(settings)


def transform_with_dyslexia_lens(text: str, settings: Settings) -> str:
    """Convenience function to transform text with Dyslexia lens."""
    lens = DyslexiaLens(settings)
    return lens.transform_context(text)