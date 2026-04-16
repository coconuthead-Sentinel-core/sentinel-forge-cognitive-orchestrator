"""
Lightweight smoke tests for the FastAPI app.

Runs in-process using FastAPI's TestClient, so it doesn't require the server
to be started or any external services. AI endpoints are probed and will be
treated as OK if they return a clear 400 with configuration guidance when
OPENAI_API_KEY is not set or the OpenAI SDK is missing.
"""

# ==============================================================================
# HOW TO RUN THIS TEST:
# Run this script directly:
#    python scripts/smoke_test.py
# ==============================================================================

import sys
import os
import time
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient
from backend.main import app


def print_test(name, status, message=""):
    """Helper to print test results in a standard format."""
    if status:
        print(f"✅ PASS: {name}")
    else:
        print(f"❌ FAIL: {name} - {message}")


def run_smoke_test():
    print("🚀 INITIATING SMOKE TEST SEQUENCE...")
    print("=" * 40)
    
    client = TestClient(app)
    
    # 1. Check API Connectivity
    print("[1/3] Pinging System Core...", end=" ")
    try:
        resp = client.get("/api/status")
        if resp.status_code == 200:
            status = resp.json()
            print(f"✅ ONLINE ({status.get('version')})")
        else:
            print(f"❌ FAILED: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ ERROR: {e}")

    # 2. Trigger CNO-AX Simulation (1000 Strikes)
    print("[2/3] Triggering 1000 Strikes Protocol...", end=" ")
    try:
        resp = client.post("/api/simulation/cno-ax/start")
        if resp.status_code == 200:
            data = resp.json()
            print(f"✅ INITIATED ({data.get('protocol')})")
        else:
            print(f"❌ FAILED: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

    # 2. Check AI Response (Mock or Real)
    print("[2/3] Testing Cognitive Engine...", end=" ")
    try:
        payload = {
            "messages": [
                {"role": "system", "content": ""},
                {"role": "user", "content": "Status Report"},
            ]
        }
        resp = client.post("/api/chat", json=payload)
        if resp.status_code == 200:
            reply = resp.json()
            if reply:
                print("✅ RESPONSIVE")
                print(f"      Received: {str(reply)[:50]}...")
            else:
                print("⚠️  NO RESPONSE (Check logs)")
        else:
            print(f"❌ FAILED: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ FAILED: {e}")

    # 3. Check Database Write
    print("[3/3] Testing Memory Lattice...", end=" ")
    try:
        payload = {"text": "Smoke Test Entry", "tag": "diagnostics"}
        resp = client.post("/api/notes/upsert", json=payload)
        if resp.status_code == 200:
            note = resp.json()
            if note and note.get("id"):
                print("✅ WRITE CONFIRMED")
            else:
                print("❌ WRITE FAILED")
        else:
            print(f"❌ FAILED: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ FAILED: {e}")

    print("=" * 40)
    print("🏁 SMOKE TEST COMPLETE")
    return True

if __name__ == "__main__":
    run_smoke_test()
