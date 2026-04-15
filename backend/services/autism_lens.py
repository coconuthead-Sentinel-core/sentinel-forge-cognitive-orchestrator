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
    
    # Odooe Lattice Integration
    ODOOE_LATTICE_ENABLED = True
    MIRROR_ID = "M3"  # Deconstruction

    def __init__(self):
        """Initialize Autism lens with default settings."""
        self.category_index = 0
        logger.info("🧠 Autism Precision Lens initialized (Odooe Lattice Active)")

    def transform_context(self, context: str) -> str:
        """
        Transform context into an Autism-friendly format with explicit structure.
        This fulfills Task 5.2.

        Args:
            context: Original context string.

        Returns:
            Transformed context with headings, numbered lists, and definitions.
        """
        if not context or not context.strip():
            return context

        # 1. Identify the main point or summary
        sentences = re.split(r'(?<=[.!?])\s+', context.strip())
        main_point = sentences[0] if sentences else ""
        
        # 2. Extract key details or steps
        # Simple heuristic: find bullet points, numbered lists, or just split the rest
        details = []
        if '- ' in context or '* ' in context:
            details = [line.strip() for line in context.split('\n') if line.strip().startswith(('- ', '* '))]
        elif len(sentences) > 1:
            details = sentences[1:]

        # 3. Look for potential definitions (e.g., "X is Y", "X means Y")
        definitions = re.findall(r'\b([A-Z][a-zA-Z0-9_]+)\s+(is|means)\s+([^.]+)\.', context)

        # 4. Assemble the structured output
        transformed_parts = []
        transformed_parts.append("### 🎯 Main Point")
        transformed_parts.append(main_point)
        transformed_parts.append("\n---")

        if details:
            transformed_parts.append("### 🔢 Key Details")
            for i, detail in enumerate(details, 1):
                transformed_parts.append(f"{i}. {detail}")
            transformed_parts.append("\n---")

        if definitions:
            transformed_parts.append("### 📚 Definitions")
            for term, _, definition in definitions:
                transformed_parts.append(f"- **{term.strip()}**: {definition.strip()}.")
            transformed_parts.append("\n---")

        conclusion = f"### 🏁 Conclusion\nThe text covers the main point about '{main_point[:30]}...' with {len(details)} supporting detail(s) and {len(definitions)} definition(s)."
        transformed_parts.append(conclusion)

        logger.debug(f"🧠 Autism lens transformed text into {len(transformed_parts)} structured parts.")
        return "\n\n".join(transformed_parts)

    def _enhance_structure(self, text: str) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return text

    def _add_categorization(self, text: str) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return text

    def _emphasize_relationships(self, text: str) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return text

    def _add_structure_summary(self, text: str) -> str:
        """DEPRECATED: This logic has been replaced by the new transform_context method."""
        return text


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