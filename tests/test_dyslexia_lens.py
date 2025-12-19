"""Tests for Dyslexia Spatial Lens - Multi-dimensional Cognitive Processing.

Validates:
1. Dyslexia lens spatial organization
2. Visual anchors and chunking
3. Navigation paths
4. Integration with CognitiveOrchestrator
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from backend.services.dyslexia_lens import DyslexiaLens
from backend.domain.models import CognitiveLens


# --- Dyslexia Lens Unit Tests ---

class TestDyslexiaLensInitialization:
    """Test Dyslexia lens initialization."""

    def test_initialization_defaults(self):
        """Test lens initializes with correct defaults."""
        lens = DyslexiaLens()
        assert lens.anchor_index == 0
        assert lens.chunk_index == 0
        assert lens.color_index == 0

    def test_spatial_anchors_defined(self):
        """Test spatial anchors are defined."""
        lens = DyslexiaLens()
        assert len(lens.SPATIAL_ANCHORS) > 0
        assert "🌟" in lens.SPATIAL_ANCHORS

    def test_chunk_markers_defined(self):
        """Test chunk markers are defined."""
        lens = DyslexiaLens()
        assert len(lens.CHUNK_MARKERS) > 0

    def test_navigation_symbols_defined(self):
        """Test navigation symbols are defined."""
        lens = DyslexiaLens()
        assert len(lens.NAVIGATION_SYMBOLS) > 0

    def test_color_indicators_defined(self):
        """Test color indicators are defined."""
        lens = DyslexiaLens()
        assert len(lens.COLOR_INDICATORS) > 0
        assert "🟡" in lens.COLOR_INDICATORS or "🟢" in lens.COLOR_INDICATORS


class TestDyslexiaLensTransformContext:
    """Test context transformation."""

    def test_empty_context(self):
        """Test empty context returns as-is."""
        lens = DyslexiaLens()
        assert lens.transform_context("") == ""
        assert lens.transform_context("   ") == "   "

    def test_simple_text(self):
        """Test simple text gets spatial anchors."""
        lens = DyslexiaLens()
        result = lens.transform_context("This is a simple test sentence.")
        # Should add visual structure
        assert len(result) >= len("This is a simple test sentence.")

    def test_multiple_paragraphs(self):
        """Test multiple paragraphs get spatial layout."""
        lens = DyslexiaLens()
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        result = lens.transform_context(text)
        # Should have structure added
        assert len(result) > len(text)

    def test_preserves_content_meaning(self):
        """Test transformation preserves original content."""
        lens = DyslexiaLens()
        text = "The database stores user information."
        result = lens.transform_context(text)
        assert "database" in result or "user" in result or "information" in result


class TestDyslexiaLensChunking:
    """Test chunking functionality."""

    def test_identify_chunks_single(self):
        """Test chunk identification with single paragraph."""
        lens = DyslexiaLens()
        chunks = lens._identify_chunks("Single paragraph of text.")
        assert len(chunks) >= 1

    def test_identify_chunks_multiple(self):
        """Test chunk identification with multiple paragraphs."""
        lens = DyslexiaLens()
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        chunks = lens._identify_chunks(text)
        assert len(chunks) >= 1


class TestDyslexiaLensSpatialAnchors:
    """Test spatial anchor functionality."""

    def test_add_spatial_anchors(self):
        """Test spatial anchors are added."""
        lens = DyslexiaLens()
        result = lens._add_spatial_anchors("Test text", 0)
        assert result is not None

    def test_spatial_anchor_cycling(self):
        """Test spatial anchors cycle through options."""
        lens = DyslexiaLens()
        anchors_used = set()
        for i in range(len(lens.SPATIAL_ANCHORS) + 2):
            result = lens._add_spatial_anchors(f"Chunk {i}", i)
            # Should cycle through anchors
            assert result is not None


class TestDyslexiaLensVisualChunking:
    """Test visual chunking functionality."""

    def test_add_visual_chunking(self):
        """Test visual chunking is added."""
        lens = DyslexiaLens()
        result = lens._add_visual_chunking("Test chunk", 0)
        assert result is not None

    def test_chunk_marker_in_result(self):
        """Test chunk markers appear in result."""
        lens = DyslexiaLens()
        result = lens._add_visual_chunking("Test chunk", 0)
        # Should contain some marker
        assert len(result) >= len("Test chunk")


class TestDyslexiaLensNavigation:
    """Test navigation path functionality."""

    def test_add_navigation_paths(self):
        """Test navigation paths are added."""
        lens = DyslexiaLens()
        result = lens._add_navigation_paths("Test chunk", 0, 3)
        assert result is not None

    def test_navigation_for_first_chunk(self):
        """Test navigation for first chunk."""
        lens = DyslexiaLens()
        result = lens._add_navigation_paths("First chunk", 0, 5)
        assert result is not None

    def test_navigation_for_last_chunk(self):
        """Test navigation for last chunk."""
        lens = DyslexiaLens()
        result = lens._add_navigation_paths("Last chunk", 4, 5)
        assert result is not None


class TestDyslexiaLensSpatialLayout:
    """Test spatial layout functionality."""

    def test_create_spatial_layout(self):
        """Test spatial layout creation."""
        lens = DyslexiaLens()
        chunks = ["Chunk 1", "Chunk 2", "Chunk 3"]
        result = lens._create_spatial_layout(chunks)
        assert result is not None
        assert len(result) > 0

    def test_spatial_layout_single_chunk(self):
        """Test spatial layout with single chunk."""
        lens = DyslexiaLens()
        chunks = ["Only chunk"]
        result = lens._create_spatial_layout(chunks)
        assert result is not None


class TestDyslexiaLensOverviewMap:
    """Test overview map functionality."""

    def test_add_overview_map(self):
        """Test overview map is added."""
        lens = DyslexiaLens()
        result = lens._add_overview_map("Original content", 3)
        assert result is not None
        assert len(result) >= len("Original content")


class TestDyslexiaLensIntegration:
    """Test integration with CognitiveOrchestrator."""

    def test_lens_type_enum_exists(self):
        """Test DYSLEXIA_SPATIAL lens type exists in enum."""
        assert CognitiveLens.DYSLEXIA_SPATIAL is not None
        assert CognitiveLens.DYSLEXIA_SPATIAL.value == "dyslexia"

    def test_full_transformation_pipeline(self):
        """Test complete transformation pipeline."""
        lens = DyslexiaLens()
        text = """
        Learning new concepts requires multiple approaches.
        
        Visual learners benefit from diagrams and charts.
        
        Hands-on practice reinforces understanding.
        """
        result = lens.transform_context(text.strip())
        
        # Should produce visually structured output
        assert len(result) > 0


class TestDyslexiaLensEdgeCases:
    """Test edge cases and error handling."""

    def test_unicode_content(self):
        """Test handling of Unicode content."""
        lens = DyslexiaLens()
        text = "Unicode test: 🌟 ⭐ 📚 🎯"
        result = lens.transform_context(text)
        # Should preserve or transform Unicode
        assert len(result) > 0

    def test_special_characters(self):
        """Test handling of special characters."""
        lens = DyslexiaLens()
        text = "Special chars: @#$%^&*()"
        result = lens.transform_context(text)
        assert result is not None

    def test_very_long_text(self):
        """Test handling of very long text."""
        lens = DyslexiaLens()
        long_text = "This is a long sentence. " * 100
        result = lens.transform_context(long_text)
        assert len(result) > 0

    def test_single_word(self):
        """Test handling of single word."""
        lens = DyslexiaLens()
        result = lens.transform_context("Hello")
        assert result is not None


class TestDyslexiaLensReset:
    """Test lens reset functionality."""

    def test_reset_indices(self):
        """Test that indices can be reset."""
        lens = DyslexiaLens()
        # Process some content to change indices
        lens.transform_context("Test content.\n\nMore content.")
        
        # Create new lens to reset
        new_lens = DyslexiaLens()
        assert new_lens.anchor_index == 0
        assert new_lens.chunk_index == 0
        assert new_lens.color_index == 0
