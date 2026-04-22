"""
Lightweight smoke tests for the FastAPI app.

Runs in-process using FastAPI's TestClient, so it doesn't require the server
to be started or any external services.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient

from backend.main import app


def _configure_stdout() -> None:
    """Best-effort UTF-8 console output for Windows terminals."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


def run_smoke_test() -> bool:
    _configure_stdout()
    print("🚀 INITIATING SMOKE TEST SEQUENCE...")
    print("=" * 40)

    with TestClient(app) as client:

        # 1. Check API Connectivity
        print("[1/5] Pinging System Core...", end=" ")
        try:
            resp = client.get("/api/status")
            if resp.status_code == 200:
                status = resp.json()
                version = status.get("version") or status.get("system_id") or "ok"
                print(f"✅ ONLINE ({version})")
            else:
                print(f"❌ FAILED: {resp.status_code} - {resp.text}")
                return False
        except Exception as exc:
            print(f"❌ ERROR: {exc}")
            return False

        # 2. Trigger a supported activation sequence
        print("[2/5] Triggering activation sequence...", end=" ")
        try:
            resp = client.post("/api/activate/standard")
            if resp.status_code == 200:
                data = resp.json()
                print(f"✅ INITIATED ({data.get('preset', 'standard')})")
            else:
                print(f"❌ FAILED: {resp.status_code} - {resp.text}")
                return False
        except Exception as exc:
            print(f"❌ ERROR: {exc}")
            return False

        # 3. Check AI Readiness
        print("[3/5] Probing AI runtime...", end=" ")
        try:
            resp = client.get("/api/runtime/ai-readiness")
            if resp.status_code == 200:
                readiness = resp.json()
                ai = readiness.get("ai", {})
                provider = ai.get("selected_provider", "unknown")
                verified = ai.get("verified_live_access", False)
                print(f"✅ {provider} (verified_live_access={verified})")
                if readiness.get("blockers"):
                    print(f"      Blockers: {', '.join(readiness['blockers'])}")
            else:
                print(f"❌ FAILED: {resp.status_code} - {resp.text}")
                return False
        except Exception as exc:
            print(f"❌ ERROR: {exc}")
            return False

        # 4. Check AI Response (Mock or Real)
        print("[4/5] Testing Cognitive Engine...", end=" ")
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
                    provider = reply.get("provider", "unknown")
                    live_response = reply.get("live_response", False)
                    print(f"✅ RESPONSIVE ({provider}, live_response={live_response})")
                    print(f"      Received: {str(reply)[:120]}...")
                else:
                    print("⚠️  NO RESPONSE (Check logs)")
            else:
                print(f"❌ FAILED: {resp.status_code} - {resp.text}")
                return False
        except Exception as exc:
            print(f"❌ FAILED: {exc}")
            return False

        # 5. Check Database Write
        print("[5/5] Testing Memory Lattice...", end=" ")
        try:
            payload = {"text": "Smoke Test Entry", "tag": "diagnostics"}
            resp = client.post("/api/notes/upsert", json=payload)
            if resp.status_code == 200:
                note = resp.json()
                if note and note.get("id"):
                    print("✅ WRITE CONFIRMED")
                else:
                    print("❌ WRITE FAILED")
                    return False
            else:
                print(f"❌ FAILED: {resp.status_code} - {resp.text}")
                return False
        except Exception as exc:
            print(f"❌ FAILED: {exc}")
            return False

    print("=" * 40)
    print("🏁 SMOKE TEST COMPLETE")
    return True


if __name__ == "__main__":
    raise SystemExit(0 if run_smoke_test() else 1)
