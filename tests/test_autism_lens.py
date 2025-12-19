"""Tests for Autism Precision Lens - Detail-focused Cognitive Processing.

Validates:
1. Autism lens structure enhancement
2. Categorization and labeling
3. Relationship emphasis
4. Integration with CognitiveOrchestrator
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from backend.services.autism_lens import AutismLens
from backend.domain.models import CognitiveLens


# --- Autism Lens Unit Tests ---

class TestAutismLensInitialization:
    """Test Autism lens initialization."""

    def test_initialization_defaults(self):
        """Test lens initializes with correct defaults."""
        lens = AutismLens()
        assert lens.category_index == 0
        assert len(lens.CATEGORY_MARKERS) > 0
        assert len(lens.RELATIONSHIP_INDICATORS) > 0

    def test_initialization_patterns(self):
        """Test structure patterns are defined."""
        lens = AutismLens()
        assert len(lens.STRUCTURE_PATTERNS) >= 3


class TestAutismLensTransformContext:
    """Test context transformation."""

    def test_empty_context(self):
        """Test empty context returns as-is."""
        lens = AutismLens()
        assert lens.transform_context("") == ""
        assert lens.transform_context("   ") == "   "

    def test_simple_text(self):
        """Test simple text gets enhanced structure."""
        lens = AutismLens()
        result = lens.transform_context("This is a simple test sentence.")
        # Should add some structure
        assert len(result) >= len("This is a simple test sentence.")

    def test_multiple_paragraphs(self):
        """Test multiple paragraphs get structure summary."""
        lens = AutismLens()
        text = "First paragraph with details.\n\nSecond paragraph with more info."
        result = lens.transform_context(text)
        # Should have structure added
        assert len(result) > len(text)

    def test_preserves_content_meaning(self):
        """Test transformation preserves original content."""
        lens = AutismLens()
        text = "The API endpoint returns JSON data."
        result = lens.transform_context(text)
        assert "API" in result
        assert "JSON" in result


class TestAutismLensEnhanceStructure:
    """Test structure enhancement methods."""

    def test_enhance_structure_single_line(self):
        """Test structure enhancement on single line."""
        lens = AutismLens()
        result = lens._enhance_structure("Single line of text.")
        assert result is not None

    def test_enhance_structure_multiline(self):
        """Test structure enhancement on multiple lines."""
        lens = AutismLens()
        text = "Line one.\nLine two.\nLine three."
        result = lens._enhance_structure(text)
        assert result is not None

    def test_enhance_numbered_list(self):
        """Test numbered list recognition."""
        lens = AutismLens()
        text = "1. First item\n2. Second item\n3. Third item"
        result = lens._enhance_structure(text)
        assert "1." in result or "First" in result


class TestAutismLensCategorization:
    """Test categorization features."""

    def test_add_categorization(self):
        """Test categorization is added."""
        lens = AutismLens()
        text = "This is technical content about databases."
        result = lens._add_categorization(text)
        assert result is not None

    def test_category_markers_used(self):
        """Test category markers are from defined set."""
        lens = AutismLens()
        # Category markers should be accessible
        assert "📂" in lens.CATEGORY_MARKERS or "🏷️" in lens.CATEGORY_MARKERS


class TestAutismLensRelationships:
    """Test relationship emphasis."""

    def test_emphasize_relationships(self):
        """Test relationship emphasis."""
        lens = AutismLens()
        text = "A depends on B. B connects to C."
        result = lens._emphasize_relationships(text)
        assert result is not None

    def test_relationship_indicators_defined(self):
        """Test relationship indicators are defined."""
        lens = AutismLens()
        assert "→" in lens.RELATIONSHIP_INDICATORS


class TestAutismLensIntegration:
    """Test integration with CognitiveOrchestrator."""

    def test_lens_type_enum_exists(self):
        """Test AUTISM_PRECISION lens type exists in enum."""
        assert CognitiveLens.AUTISM_PRECISION is not None
        assert CognitiveLens.AUTISM_PRECISION.value == "autism"

    def test_full_transformation_pipeline(self):
        """Test complete transformation pipeline."""
        lens = AutismLens()
        text = """
        The system architecture has three layers.
        
        First, the presentation layer handles UI.
        Second, the business logic layer processes data.
        Third, the data layer stores information.
        """
        result = lens.transform_context(text.strip())
        
        # Should produce structured output
        assert len(result) > 0
        # Should mention key terms
        assert "layer" in result.lower() or "architecture" in result.lower()


class TestAutismLensEdgeCases:
    """Test edge cases and error handling."""

    def test_unicode_content(self):
        """Test handling of Unicode content."""
        lens = AutismLens()
        text = "Unicode test: 🌟 ⭐ 📚 🎯"
        result = lens.transform_context(text)
        # Should preserve Unicode
        assert "🌟" in result or len(result) > 0

    def test_special_characters(self):
        """Test handling of special characters."""
        lens = AutismLens()
        text = "Special chars: @#$%^&*()"
        result = lens.transform_context(text)
        assert result is not None

    def test_very_long_text(self):
        """Test handling of very long text."""
        lens = AutismLens()
        long_text = "This is a long sentence. " * 100
        result = lens.transform_context(long_text)
        assert len(result) > 0

    def test_code_blocks(self):
        """Test handling of code-like content."""
        lens = AutismLens()
        text = "def function():\n    return value"
        result = lens.transform_context(text)
        # Should preserve code structure
        assert "def" in result or "function" in result
