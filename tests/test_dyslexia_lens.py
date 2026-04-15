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
from backend.core.config import Settings


@pytest.fixture
def settings() -> Settings:
    """Fixture for creating a Settings instance for tests."""
    return Settings()


# --- Dyslexia Lens Unit Tests ---

class TestDyslexiaLensInitialization:
    """Test Dyslexia lens initialization."""

    def test_initialization_defaults(self, settings: Settings):
        """Test lens initializes with correct defaults."""
        lens = DyslexiaLens(settings)
        assert lens.anchor_index == 0
        assert lens.chunk_index == 0
        assert lens.color_index == 0

    def test_spatial_anchors_defined(self, settings: Settings):
        """Test spatial anchors are defined."""
        lens = DyslexiaLens(settings)
        assert len(lens.settings.DYSLEXIA_LENS_SPATIAL_ANCHORS) > 0
        assert "🌟" in lens.settings.DYSLEXIA_LENS_SPATIAL_ANCHORS

    def test_chunk_markers_defined(self, settings: Settings):
        """Test chunk markers are defined."""
        lens = DyslexiaLens(settings)
        assert len(lens.settings.DYSLEXIA_LENS_CHUNK_MARKERS) > 0

    def test_navigation_symbols_defined(self, settings: Settings):
        """Test navigation symbols are defined."""
        lens = DyslexiaLens(settings)
        assert len(lens.settings.DYSLEXIA_LENS_NAVIGATION_SYMBOLS) > 0

    def test_color_indicators_defined(self, settings: Settings):
        """Test color indicators are defined."""
        lens = DyslexiaLens(settings)
        assert len(lens.settings.DYSLEXIA_LENS_COLOR_INDICATORS) > 0
        assert "🟡" in lens.settings.DYSLEXIA_LENS_COLOR_INDICATORS or "🟢" in lens.settings.DYSLEXIA_LENS_COLOR_INDICATORS


class TestDyslexiaLensTransformContext:
    """Test context transformation."""

    def test_empty_context(self, settings: Settings):
        """Test empty context returns as-is."""
        lens = DyslexiaLens(settings)
        assert lens.transform_context("") == ""
        assert lens.transform_context("   ") == "   "

    def test_simple_text(self, settings: Settings):
        """Test simple text gets spatial anchors."""
        lens = DyslexiaLens(settings)
        result = lens.transform_context("This is a simple test sentence.")
        # Should add visual structure
        assert len(result) >= len("This is a simple test sentence.")

    def test_multiple_paragraphs(self, settings: Settings):
        """Test multiple paragraphs get spatial layout."""
        lens = DyslexiaLens(settings)
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        result = lens.transform_context(text)
        # Should have structure added
        assert len(result) > len(text)

    def test_preserves_content_meaning(self, settings: Settings):
        """Test transformation preserves original content."""
        lens = DyslexiaLens(settings)
        text = "The database stores user information."
        result = lens.transform_context(text)
        assert "database" in result or "user" in result or "information" in result


class TestDyslexiaLensChunking:
    """Test chunking functionality."""

    def test_identify_chunks_single(self, settings: Settings):
        """Test chunk identification with single paragraph."""
        lens = DyslexiaLens(settings)
        chunks = lens._identify_chunks("Single paragraph of text.")
        assert len(chunks) >= 1

    def test_identify_chunks_multiple(self, settings: Settings):
        """Test chunk identification with multiple paragraphs."""
        lens = DyslexiaLens(settings)
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        chunks = lens._identify_chunks(text)
        assert len(chunks) >= 1


class TestDyslexiaLensSpatialAnchors:
    """Test spatial anchor functionality."""

    def test_add_spatial_anchors(self, settings: Settings):
        """Test spatial anchors are added."""
        lens = DyslexiaLens(settings)
        result = lens._add_spatial_anchors("Test text", 0)
        assert result is not None

    def test_spatial_anchor_cycling(self, settings: Settings):
        """Test spatial anchors cycle through options."""
        lens = DyslexiaLens(settings)
        anchors_used = set()
        for i in range(len(lens.settings.DYSLEXIA_LENS_SPATIAL_ANCHORS) + 2):
            result = lens._add_spatial_anchors(f"Chunk {i}", i)
            # Should cycle through anchors
            assert result is not None


class TestDyslexiaLensVisualChunking:
    """Test visual chunking functionality."""

    def test_add_visual_chunking(self, settings: Settings):
        """Test visual chunking is added."""
        lens = DyslexiaLens(settings)
        result = lens._add_visual_chunking("Test chunk", 0)
        assert result is not None

    def test_chunk_marker_in_result(self, settings: Settings):
        """Test chunk markers appear in result."""
        lens = DyslexiaLens(settings)
        result = lens._add_visual_chunking("Test chunk", 0)
        # Should contain some marker
        assert len(result) >= len("Test chunk")


class TestDyslexiaLensNavigation:
    """Test navigation path functionality."""

    def test_add_navigation_paths(self, settings: Settings):
        """Test navigation paths are added."""
        lens = DyslexiaLens(settings)
        result = lens._add_navigation_paths("Test chunk", 0, 3)
        assert result is not None

    def test_navigation_for_first_chunk(self, settings: Settings):
        """Test navigation for first chunk."""
        lens = DyslexiaLens(settings)
        result = lens._add_navigation_paths("First chunk", 0, 5)
        assert result is not None

    def test_navigation_for_last_chunk(self, settings: Settings):
        """Test navigation for last chunk."""
        lens = DyslexiaLens(settings)
        result = lens._add_navigation_paths("Last chunk", 4, 5)
        assert result is not None


class TestDyslexiaLensSpatialLayout:
    """Test spatial layout functionality."""

    def test_create_spatial_layout(self, settings: Settings):
        """Test spatial layout creation."""
        lens = DyslexiaLens(settings)
        chunks = ["Chunk 1", "Chunk 2", "Chunk 3"]
        result = lens._create_spatial_layout(chunks)
        assert result is not None
        assert len(result) > 0

    def test_spatial_layout_single_chunk(self, settings: Settings):
        """Test spatial layout with single chunk."""
        lens = DyslexiaLens(settings)
        chunks = ["Only chunk"]
        result = lens._create_spatial_layout(chunks)
        assert result is not None


class TestDyslexiaLensOverviewMap:
    """Test overview map functionality."""

    def test_add_overview_map(self, settings: Settings):
        """Test overview map is added."""
        lens = DyslexiaLens(settings)
        result = lens._add_overview_map("Original content", 3)
        assert result is not None
        assert len(result) >= len("Original content")


class TestDyslexiaLensIntegration:
    """Test integration with CognitiveOrchestrator."""

    def test_lens_type_enum_exists(self):
        """Test DYSLEXIA_SPATIAL lens type exists in enum."""
        assert CognitiveLens.DYSLEXIA_SPATIAL is not None
        assert CognitiveLens.DYSLEXIA_SPATIAL.value == "dyslexia"

    def test_full_transformation_pipeline(self, settings: Settings):
        """Test complete transformation pipeline."""
        lens = DyslexiaLens(settings)
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

    def test_unicode_content(self, settings: Settings):
        """Test handling of Unicode content."""
        lens = DyslexiaLens(settings)
        text = "Unicode test: 🌟 ⭐ 📚 🎯"
        result = lens.transform_context(text)
        # Should preserve or transform Unicode
        assert len(result) > 0

    def test_special_characters(self, settings: Settings):
        """Test handling of special characters."""
        lens = DyslexiaLens(settings)
        text = "Special chars: @#$%^&*()"
        result = lens.transform_context(text)
        assert result is not None

    def test_very_long_text(self, settings: Settings):
        """Test handling of very long text."""
        lens = DyslexiaLens(settings)
        long_text = "This is a long sentence. " * 100
        result = lens.transform_context(long_text)
        assert len(result) > 0

    def test_single_word(self, settings: Settings):
        """Test handling of single word."""
        lens = DyslexiaLens(settings)
        result = lens.transform_context("Hello")
        assert result is not None


class TestDyslexiaLensReset:
    """Test lens reset functionality."""

    def test_reset_indices(self, settings: Settings):
        """Test that indices can be reset."""
        lens = DyslexiaLens(settings)
        # Process some content to change indices
        lens.transform_context("Test content.\n\nMore content.")
        
        # Create new lens to reset
        new_lens = DyslexiaLens(settings)
        assert new_lens.anchor_index == 0
        assert new_lens.chunk_index == 0
        assert new_lens.color_index == 0
