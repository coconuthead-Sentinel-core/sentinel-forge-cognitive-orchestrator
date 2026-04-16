# LLM Middleware Layer for VR App
# Provides structured conversation management between user input and LLM responses
# Implements mode classification, state management, and response contracts for coherent interactions

import json
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum

class ConversationMode(Enum):
    EXPLORE = "explore"
    DECIDE = "decide"
    EXECUTE = "execute"
    DEBUG = "debug"
    EXPLAIN = "explain"

@dataclass
class ConversationState:
    goal: Optional[str] = None
    constraints: List[str] = None
    open_threads: List[str] = None
    decision_log: List[Dict[str, Any]] = None

    def __post_init__(self):
        if self.constraints is None:
            self.constraints = []
        if self.open_threads is None:
            self.open_threads = []
        if self.decision_log is None:
            self.decision_log = []

@dataclass
class ModeClassification:
    mode: ConversationMode
    confidence: float
    rationale: str
    extracted_goal: Optional[str] = None
    extracted_constraints: List[str] = None
    extracted_threads: List[str] = None

@dataclass
class ResponseGeneration:
    assistant_response: str
    state_updates: Dict[str, Any]
    decisions_made: List[Dict[str, str]]

class LLMMiddleware:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.state = ConversationState()

    def process_user_input(self, user_message: str) -> str:
        """Main pipeline: classify -> update state -> generate -> enforce contract"""
        # Step 1: Classify mode
        classification = self.classify_mode(user_message)

        # Step 2: Update state with extractions
        self.update_state(classification)

        # Step 3: Generate response
        response = self.generate_response(user_message, classification.mode)

        # Step 4: Enforce response contract
        final_response = self.enforce_contract(response, classification.mode)

        return final_response

    def classify_mode(self, user_message: str) -> ModeClassification:
        """Classify user input into conversation mode using heuristics + LLM"""
        # Heuristic rules first
        message_lower = user_message.lower()

        if any(word in message_lower for word in ['what if', 'explore', 'possibilities', 'options']):
            mode = ConversationMode.EXPLORE
            confidence = 0.8
            extracted_goal = None
            extracted_constraints = []
            extracted_threads = []
        elif any(word in message_lower for word in ['choose', 'decide', 'which', 'select']):
            mode = ConversationMode.DECIDE
            confidence = 0.8
            extracted_goal = None
            extracted_constraints = []
            extracted_threads = []
        elif any(word in message_lower for word in ['do it', 'execute', 'run', 'implement']):
            mode = ConversationMode.EXECUTE
            confidence = 0.8
            extracted_goal = None
            extracted_constraints = []
            extracted_threads = []
        elif any(word in message_lower for word in ['error', 'bug', 'fix', 'debug', 'problem']):
            mode = ConversationMode.DEBUG
            confidence = 0.8
            extracted_goal = None
            extracted_constraints = []
            extracted_threads = []
        elif any(word in message_lower for word in ['explain', 'how', 'why', 'what is']):
            mode = ConversationMode.EXPLAIN
            confidence = 0.8
            extracted_goal = None
            extracted_constraints = []
            extracted_threads = []
        else:
            # Fallback to LLM classification
            prompt = f"""
Analyze this user message and classify it into one of these modes:
- EXPLORE: Investigating possibilities, brainstorming, or gathering information
- DECIDE: Making choices between options or committing to a path
- EXECUTE: Taking action, implementing decisions, or performing tasks
- DEBUG: Identifying and fixing problems or errors
- EXPLAIN: Clarifying concepts, providing understanding, or answering questions

User message: "{user_message}"
Current state: {json.dumps(asdict(self.state), indent=2)}

Return JSON with:
{{
  "mode": "explore|decide|execute|debug|explain",
  "confidence": 0.0-1.0,
  "rationale": "brief explanation",
  "extracted_goal": "goal if mentioned, else null",
  "extracted_constraints": ["constraint1", "constraint2"],
  "extracted_threads": ["thread1", "thread2"]
}}
"""
            llm_response = self.llm_client.generate(prompt)
            result = json.loads(llm_response)
            mode = ConversationMode(result['mode'])
            confidence = result['confidence']
            extracted_goal = result.get('extracted_goal')
            extracted_constraints = result.get('extracted_constraints', [])
            extracted_threads = result.get('extracted_threads', [])

        return ModeClassification(
            mode=mode,
            confidence=confidence,
            rationale="Heuristic classification" if confidence >= 0.8 else "LLM classification",
            extracted_goal=extracted_goal,
            extracted_constraints=extracted_constraints,
            extracted_threads=extracted_threads
        )

    def update_state(self, classification: ModeClassification):
        """Update conversation state with extracted information"""
        if classification.extracted_goal:
            self.state.goal = classification.extracted_goal

        if classification.extracted_constraints:
            self.state.constraints.extend(classification.extracted_constraints)

        if classification.extracted_threads:
            self.state.open_threads.extend(classification.extracted_threads)

    def generate_response(self, user_message: str, mode: ConversationMode) -> ResponseGeneration:
        """Generate assistant response based on mode and state"""
        mode_templates = {
            ConversationMode.EXPLORE: "Let's explore this together. Here are some possibilities and considerations:",
            ConversationMode.DECIDE: "Based on the current situation, I recommend this approach:",
            ConversationMode.EXECUTE: "I'll help you execute this step by step:",
            ConversationMode.DEBUG: "Let me analyze this issue and provide a solution:",
            ConversationMode.EXPLAIN: "Here's a clear explanation of what's happening:"
        }

        prompt = f"""
Generate a response for this user message in {mode.value} mode.

Mode guidelines:
- EXPLORE: Be open-ended, suggest multiple options, ask clarifying questions
- DECIDE: Be decisive, weigh pros/cons, recommend specific choices
- EXECUTE: Be action-oriented, provide step-by-step instructions
- DEBUG: Be analytical, identify root causes, suggest fixes
- EXPLAIN: Be educational, break down complex concepts simply

User message: "{user_message}"
Current state: {json.dumps(asdict(self.state), indent=2)}

Response should start with: "{mode_templates[mode]}"

Return JSON with:
{{
  "assistant_response": "full response text",
  "state_updates": {{"field": "value"}},
  "decisions_made": [{{"decision": "what was decided", "reason": "why"}}]
}}
"""
        llm_response = self.llm_client.generate(prompt)
        result = json.loads(llm_response)

        return ResponseGeneration(
            assistant_response=result['assistant_response'],
            state_updates=result.get('state_updates', {}),
            decisions_made=result.get('decisions_made', [])
        )

    def enforce_contract(self, response: ResponseGeneration, mode: ConversationMode) -> str:
        """Ensure response follows mode-specific contract and remove contradictions"""
        contract_rules = {
            ConversationMode.EXPLORE: ["suggests options", "asks questions", "open-ended"],
            ConversationMode.DECIDE: ["makes recommendation", "weighs pros/cons", "decisive"],
            ConversationMode.EXECUTE: ["step-by-step", "actionable", "progress-focused"],
            ConversationMode.DEBUG: ["identifies problem", "provides solution", "analytical"],
            ConversationMode.EXPLAIN: ["educational", "clear", "comprehensive"]
        }

        prompt = f"""
Review this response and ensure it follows the {mode.value} mode contract.
Contract requirements: {', '.join(contract_rules[mode])}

Remove any contradictory statements and ensure consistency with current state.

Response to check: "{response.assistant_response}"
Current state: {json.dumps(asdict(self.state), indent=2)}

Return the cleaned response as plain text.
"""
        cleaned_response = self.llm_client.generate(prompt)

        # Apply state updates
        for key, value in response.state_updates.items():
            if hasattr(self.state, key):
                setattr(self.state, key, value)

        # Log decisions
        for decision in response.decisions_made:
            self.state.decision_log.append({
                **decision,
                'timestamp': time.time()
            })

        return cleaned_response.strip()

# Mock LLM client for testing
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        # Simple mock responses based on prompt content
        if 'classify' in prompt.lower():
            if 'VR app' in prompt:
                return '{"mode": "explore", "confidence": 0.9, "rationale": "User wants to build VR app", "extracted_goal": "build VR app", "extracted_constraints": ["budget constraints"], "extracted_threads": ["VR development"]}'
            elif 'decide' in prompt.lower():
                return '{"mode": "decide", "confidence": 0.9, "rationale": "User wants to make a decision", "extracted_goal": null, "extracted_constraints": [], "extracted_threads": []}'
            return '{"mode": "explore", "confidence": 0.9, "rationale": "User is asking about possibilities", "extracted_goal": "explore VR options", "extracted_constraints": ["budget limit"], "extracted_threads": ["VR hardware research"]}'
        elif 'response' in prompt.lower():
            if 'decide' in prompt.lower():
                return '{"assistant_response": "Based on the current situation, I recommend Unity for its ease of use and strong VR support.", "state_updates": {}, "decisions_made": [{"decision": "Choose Unity over Unreal", "reason": "Better for beginners and VR development"}]}'
            return '{"assistant_response": "Let\'s explore this together. Here are some possibilities and considerations: 1) Option A, 2) Option B", "state_updates": {}, "decisions_made": []}'
        else:
            return "This is a cleaned and validated response that follows the contract."

# Unit Tests
def test_mode_classification():
    """Test mode classification edge cases"""
    middleware = LLMMiddleware(MockLLMClient())

    # Test heuristic classification
    result = middleware.classify_mode("What if we explore different options?")
    assert result.mode == ConversationMode.EXPLORE
    assert result.confidence >= 0.8

    # Test fallback to LLM
    result = middleware.classify_mode("This is an ambiguous message")
    assert isinstance(result.mode, ConversationMode)

def test_state_persistence():
    """Test state persistence across turns"""
    middleware = LLMMiddleware(MockLLMClient())

    # First turn
    middleware.process_user_input("I want to build a VR app with budget constraints")
    assert middleware.state.goal == "build VR app"
    assert "budget constraints" in middleware.state.constraints

    # Second turn
    middleware.process_user_input("Let's decide on Unity vs Unreal")
    assert len(middleware.state.decision_log) > 0

def test_contract_enforcement():
    """Test contract enforcement formatting"""
    middleware = LLMMiddleware(MockLLMClient())

    response = ResponseGeneration(
        assistant_response="This response might have issues",
        state_updates={},
        decisions_made=[]
    )

    cleaned = middleware.enforce_contract(response, ConversationMode.EXPLORE)
    assert isinstance(cleaned, str)
    assert len(cleaned) > 0

if __name__ == "__main__":
    # Example usage
    client = MockLLMClient()
    middleware = LLMMiddleware(client)

    # Process a user message
    response = middleware.process_user_input("What VR platforms should I consider?")
    print("Response:", response)
    print("Current state:", asdict(middleware.state))