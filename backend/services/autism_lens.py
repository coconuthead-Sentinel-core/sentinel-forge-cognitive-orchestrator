"""Autism Precision Lens - Detail Focus for Cognitive Processing.

Implements Autism-friendly processing mode with:
- Explicit structure and categorization
- Detail emphasis and pattern recognition
- Logical sequencing and hierarchical organization
- Clear boundaries and explicit relationships

Architecture:
    AutismLens → CognitiveOrchestrator → AI Adapter
"""

import logging
import re
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class AutismLens:
    """
    Autism Precision Lens for detail-focused, structured processing.

    Transforms content into Autism-friendly formats:
    - Adds explicit categorization and labeling
    - Emphasizes logical relationships and hierarchies
    - Provides clear boundaries and structure
    - Highlights patterns and details
    """

    # Configuration
    CATEGORY_MARKERS = ["📂", "🏷️", "🔍", "📊", "🔗"]
    RELATIONSHIP_INDICATORS = ["→", "↔", "⊂", "⊃", "∋"]
    STRUCTURE_PATTERNS = [
        r"^(\d+\.|\-|\•)\s*",  # Numbered/bulleted lists
        r"^(First|Second|Third|Next|Then|Finally)\b",  # Sequential words
        r"^(Because|Therefore|However|Although|Since)\b",  # Logical connectors
    ]

    def __init__(self):
        """Initialize Autism lens with default settings."""
        self.category_index = 0
        logger.info("🧠 Autism Precision Lens initialized")

    def transform_context(self, context: str) -> str:
        """
        Transform context into Autism-friendly format.

        Args:
            context: Original context string

        Returns:
            Transformed context with explicit structure and detail emphasis
        """
        if not context.strip():
            return context

        # Split into paragraphs for processing
        paragraphs = [p.strip() for p in context.split('\n\n') if p.strip()]

        transformed_paragraphs = []
        for para in paragraphs:
            transformed = self._enhance_structure(para)
            transformed = self._add_categorization(transformed)
            transformed = self._emphasize_relationships(transformed)
            transformed_paragraphs.append(transformed)

        result = '\n\n'.join(transformed_paragraphs)

        # Add overall structure summary if multiple paragraphs
        if len(transformed_paragraphs) > 1:
            result = self._add_structure_summary(result)

        return result

    def _enhance_structure(self, text: str) -> str:
        """Enhance structural clarity in text."""
        lines = text.split('\n')
        enhanced_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                enhanced_lines.append("")
                continue

            # Check for existing structure
            has_structure = any(re.match(pattern, line) for pattern in self.STRUCTURE_PATTERNS)

            if not has_structure and len(line) > 50:
                # Add structural markers for long lines
                if any(word in line.lower() for word in ['first', 'then', 'next', 'finally']):
                    line = f"🔗 {line}"
                elif any(word in line.lower() for word in ['because', 'therefore', 'however']):
                    line = f"📊 {line}"
                else:
                    line = f"📝 {line}"

            enhanced_lines.append(line)

        return '\n'.join(enhanced_lines)

    def _add_categorization(self, text: str) -> str:
        """Add explicit categorization labels."""
        # Identify potential categories
        categories = []
        lines = text.split('\n')

        for i, line in enumerate(lines):
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['definition', 'concept', 'category']):
                categories.append((i, "Definition"))
            elif any(keyword in line_lower for keyword in ['example', 'instance', 'case']):
                categories.append((i, "Example"))
            elif any(keyword in line_lower for keyword in ['relationship', 'connection', 'link']):
                categories.append((i, "Relationship"))
            elif any(keyword in line_lower for keyword in ['process', 'method', 'approach']):
                categories.append((i, "Process"))

        # Add category markers
        for line_idx, category in categories:
            marker = self.CATEGORY_MARKERS[self.category_index % len(self.CATEGORY_MARKERS)]
            lines[line_idx] = f"{marker} **{category}:** {lines[line_idx]}"
            self.category_index += 1

        return '\n'.join(lines)

    def _emphasize_relationships(self, text: str) -> str:
        """Emphasize logical relationships and connections."""
        # Add relationship indicators
        text = re.sub(r'\b(because|since|therefore|thus|hence|consequently)\b',
                     r'→ \1', text, flags=re.IGNORECASE)
        text = re.sub(r'\b(if|when|where|while)\b',
                     r'↔ \1', text, flags=re.IGNORECASE)
        text = re.sub(r'\b(contains|includes|has|part of)\b',
                     r'⊂ \1', text, flags=re.IGNORECASE)

        return text

    def _add_structure_summary(self, text: str) -> str:
        """Add a summary of the overall structure."""
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        summary = f"📋 **Structure Overview:** {len(paragraphs)} sections identified\n\n{text}"
        return summary

    def get_transformation_stats(self) -> Dict[str, Any]:
        """Get statistics about transformations applied."""
        return {
            "lens_type": "autism_precision",
            "category_markers_used": self.category_index,
            "structure_patterns": self.STRUCTURE_PATTERNS,
            "relationship_indicators": self.RELATIONSHIP_INDICATORS,
        }


# --- Convenience Functions ---

def create_autism_lens() -> AutismLens:
    """Create and return a configured Autism lens instance."""
    return AutismLens()


def transform_with_autism_lens(text: str) -> str:
    """Convenience function to transform text with Autism lens."""
    lens = AutismLens()
    return lens.transform_context(text)