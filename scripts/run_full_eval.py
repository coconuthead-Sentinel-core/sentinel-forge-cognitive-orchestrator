import subprocess
import time
import sys
import os
import socket
from pathlib import Path
from typing import Optional

# --- Unicode Patch for Windows Consoles ---
# Ensures emojis (🚀, ✅, etc.) don't crash the script on legacy terminals.
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Fallback for older Python versions or environments
        pass

def wait_for_port(port, timeout=30):
    """Wait until the port is open."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                return True
        time.sleep(1)
    return False

def main():
    # Ensure we are in the project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    print("🚀 Starting Sentinel Forge Evaluation Pipeline...")
    print("=" * 60)

    server_process: Optional[subprocess.Popen] = None
    try:
        # 1. Start the backend server
        print("\n[1/4] Starting Backend Server...")
        # Ensure MOCK_AI mode for evaluation
        env = os.environ.copy()
        env["MOCK_AI"] = "true"
        
        server_process = subprocess.Popen(
            [sys.executable, "-m", "backend.main"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=project_root,
            env=env
        )
        
        # Wait for server to be ready
        if wait_for_port(8000, timeout=30):
            print("      ✅ Server ready at http://localhost:8000")
        else:
            print("      ❌ Server failed to start within 30 seconds")
            if server_process:
                server_process.terminate()
            return

        # 2. Run the Collection Script (uses requests library for real HTTP)
        print("\n[2/4] Collecting Responses via HTTP...")
        collect_result = subprocess.run(
            [sys.executable, "evaluation/collect_responses.py"],
            capture_output=False 
        )
        
        if collect_result.returncode != 0:
            print("❌ Collection failed.")
            return
        
        # 3. Run the Evaluation Script
        print("\n[3/4] Running Evaluation...")
        eval_result = subprocess.run(
            [sys.executable, "evaluation/run_evaluation.py"],
            capture_output=False
        )
        if eval_result.returncode != 0:
            print("❌ Evaluation failed.")
        else:
            print("\n[4/4] Shutting down server...")
            print("✅ Pipeline Complete.")

    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
    finally:
        # Always clean up the server process
        if server_process:
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()
                server_process.wait()

if __name__ == "__main__":
    main()
