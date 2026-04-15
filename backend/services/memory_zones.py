"""Three-Zone Memory Manager for Sentinel Forge.

Manages entropy-based routing of notes between cognitive zones:
- 🟢 ACTIVE: High entropy (>0.7) - Real-time processing
- 🟡 PATTERN: Mid entropy (0.3-0.7) - Pattern emergence  
- 🔴 CRYSTALLIZED: Low entropy (<0.3) - Stable storage

Architecture:
    CognitiveOrchestrator → ThreeZoneMemory → ZonedNote → cosmos_repo
"""

from __future__ import annotations

import logging
from typing import Dict, Any, List, Optional
from collections import defaultdict

from backend.domain.models import (
    Note,
    ZonedNote,
    MemoryZone,
    ZoneMetrics,
    CognitiveLens,
)
from backend.core.config import settings, Settings

logger = logging.getLogger(__name__)


# --- Entropy Calculation ---

def calculate_entropy(text: str) -> float:
    """
    Calculate information entropy of text.
    
    Higher entropy = more diverse/novel content.
    Lower entropy = more repetitive/stable content.
    
    Algorithm: Unique token ratio (simple but effective).
    Future: Shannon entropy with character/n-gram distribution.
    
    Args:
        text: Input text to analyze
        
    Returns:
        float between 0.0 and 1.0
    """
    if not text or not text.strip():
        return 0.0
    
    # Token frequency analysis
    tokens = text.lower().split()
    if not tokens:
        return 0.0
    
    # Unique ratio: more unique = higher entropy
    unique_ratio = len(set(tokens)) / len(tokens)
    
    # Clamp to valid range
    return max(0.0, min(1.0, unique_ratio))


def classify_zone(entropy: float, active_threshold: float, pattern_threshold: float) -> MemoryZone:
    """
    Route content to appropriate memory zone based on entropy.
    
    Thresholds are passed in to make the function pure.
    
    Args:
        entropy: Entropy score (0.0-1.0)
        active_threshold: The threshold for the active zone.
        pattern_threshold: The threshold for the pattern zone.
        
    Returns:
        MemoryZone enum value
    """
    if entropy > active_threshold:
        return MemoryZone.ACTIVE
    elif entropy > pattern_threshold:
        return MemoryZone.PATTERN
    else:
        return MemoryZone.CRYSTALLIZED


# --- Three-Zone Memory Manager ---

class ThreeZoneMemory:
    """
    Manages the three-zone memory system for cognitive processing.
    
    Responsibilities:
    1. Calculate entropy for incoming content
    2. Classify content into appropriate zone
    3. Track zone transitions and metrics
    4. Provide zone-aware querying (future)
    
    Thread-safe: Uses simple counters (future: add locks if needed).
    """
    
    def __init__(self, settings: Settings) -> None:
        """Initialize ThreeZoneMemory with empty zone counters."""
        self._zone_counts: Dict[MemoryZone, int] = defaultdict(int)
        self.settings = settings
        logger.info(f"🧠 ThreeZoneMemory initialized with thresholds: "
                    f"Active > {self.settings.ZONE_ACTIVE_THRESHOLD}, "
                    f"Pattern > {self.settings.ZONE_PATTERN_THRESHOLD}")

    def process_note(self, note: Note) -> ZonedNote:
        """
        Process a note, calculate its entropy, and assign it to a zone.
        
        Args:
            note: The note to process
            
        Returns:
            A ZonedNote with entropy and zone information
        """
        entropy = calculate_entropy(note.text)
        zone = classify_zone(
            entropy,
            self.settings.ZONE_ACTIVE_THRESHOLD,
            self.settings.ZONE_PATTERN_THRESHOLD
        )
        
        self._zone_counts[zone] += 1
        
        zoned_note = ZonedNote(
            **note.model_dump(),
            entropy=entropy,
            zone=zone
        )
        
        logger.debug(f"📝 Processed note '{note.id or ''[:8]}...': "
                     f"Entropy={entropy:.2f} -> Zone={zone.value}")
        
        return zoned_note
    
    def create_zoned_note(
        self,
        text: str,
        tag: str,
        lens: Optional[CognitiveLens] = None,
        vector: Optional[List[float]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> ZonedNote:
        """
        Create a ZonedNote with automatic zone classification.
        
        Args:
            text: Note content
            tag: Categorization tag
            lens: Cognitive lens applied during creation
            vector: Optional embedding vector
            metadata: Optional additional metadata
            
        Returns:
            ZonedNote with zone and entropy populated
        """
        zone, entropy = self.route_to_zone(text)
        
        note = ZonedNote(
            text=text,
            tag=tag,
            zone=zone,
            entropy=entropy,
            lens_applied=lens,
            vector=vector,
            metadata=metadata or {},
        )
        
        return note
    
    def record_transition(self, from_zone: MemoryZone, to_zone: MemoryZone) -> None:
        """
        Record a zone transition event.
        
        Args:
            from_zone: Original zone
            to_zone: New zone after transition
        """
        self._last_transition = f"{from_zone.value}→{to_zone.value}"
        logger.info(f"🔄 Zone transition: {self._last_transition}")
    
    def get_metrics(self) -> ZoneMetrics:
        """
        Get current zone distribution metrics.
        
        Returns:
            ZoneMetrics with counts and averages
        """
        avg_entropy = (
            self._total_entropy / self._total_items 
            if self._total_items > 0 
            else 0.0
        )
        
        return ZoneMetrics(
            active_count=self._zone_counts[MemoryZone.ACTIVE],
            pattern_count=self._zone_counts[MemoryZone.PATTERN],
            crystal_count=self._zone_counts[MemoryZone.CRYSTALLIZED],
            avg_entropy=round(avg_entropy, 3),
            last_transition=self._last_transition,
        )
    
    def get_zone_distribution(self) -> Dict[str, float]:
        """
        Get percentage distribution across zones.
        
        Returns:
            Dict with zone names and percentages
        """
        total = sum(self._zone_counts.values()) or 1
        
        return {
            zone.value: round(count / total * 100, 1)
            for zone, count in self._zone_counts.items()
        }
    
    def reset_metrics(self) -> None:
        """Reset all zone counters and metrics."""
        self._zone_counts.clear()
        self._total_entropy = 0.0
        self._total_items = 0
        self._last_transition = None
        logger.info("🔄 ThreeZoneMemory metrics reset")


# --- Singleton Instance (Optional convenience) ---

_memory_manager: Optional[ThreeZoneMemory] = None


def get_memory_manager(settings: Settings) -> ThreeZoneMemory:
    """
    Get the default ThreeZoneMemory instance (lazy singleton).
    
    Args:
        settings: The application settings object.

    Returns:
        ThreeZoneMemory instance
    """
    global _memory_manager
    if _memory_manager is None:
        _memory_manager = ThreeZoneMemory(settings)
    return _memory_manager
