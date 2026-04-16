import json
import time
import sys
import os
import asyncio
from pathlib import Path

# Add root to path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

from backend.services.nexus_bridge import NexusBridge

async def sovereign_handshake():
    print("💠 INITIATING PHASE V: THE SOVEREIGN HANDSHAKE...")
    print("⚙️  Establishing M14 Command Link...")
    
    # 1. Initialize L5 Bridge
    bridge = NexusBridge()
    print("🌉 L5 NexusBridge: CONNECTED")
    
    # 2. Load Sovereign Calibration
    calibration_path = root_dir / "meta_context" / "sovereign_voice_calibration.json"
    try:
        with open(calibration_path, "r", encoding='utf-8') as f:
            calibration = json.load(f)
        print(f"📥 Sovereign Voice: {calibration['persona_id']} LOADED")
    except Exception as e:
        print(f"❌ Calibration Load Failed: {e}")
        return

    # 3. Execute Handshake Protocol
    print("\n🤝 EXECUTING HANDSHAKE PROTOCOL...")
    
    # Simulate M14 Command Injection
    # High coherence vector (all > 0.9) to trigger Crystalline State
    command_vector = [0.99, 0.99, 0.99, 0.99] 
    
    # Ingest Command via Bridge
    bridge.ingest_node({
        "id": "M14-CMD-001",
        "content": "INITIATE_SOVEREIGN_AUTONOMY",
        "entropy": 0.01, # Crystal clear intent
        "vector": command_vector
    })
    
    # Process via C++ Core (Simulated)
    state = await bridge.process_quantum_state(command_vector)
    
    # 4. Verify State
    print(f"🧠 System Entropy: {state.system_entropy:.4f} (Target: < 0.1)")
    print(f"🔄 Active Mode: {state.mode}")
    
    if state.system_entropy < 0.1:
        print("\n✅ HANDSHAKE CONFIRMED. ENTROPY STABILIZED.")
        print("🔴 SYSTEM STATUS: CRYSTALLIZED (RED ZONE)")
        print(f"👑 SOVEREIGN COMMAND: {calibration['interaction_rules']['confirmation']}")
    else:
        print("❌ HANDSHAKE FAILED. ENTROPY TOO HIGH.")

if __name__ == "__main__":
    asyncio.run(sovereign_handshake())
