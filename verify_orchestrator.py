import sys
import os
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from backend.services.cognitive_orchestrator import CognitiveOrchestrator
from backend.mock_adapter import MockOpenAIAdapter

try:
    adapter = MockOpenAIAdapter()
    orch = CognitiveOrchestrator(adapter)
    print("SUCCESS: CognitiveOrchestrator instantiated.")
except Exception as e:
    print(f"FAILURE: {e}")
