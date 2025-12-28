"""
Full evaluation pipeline for Sentinel Forge.
Manages the uvicorn server lifecycle automatically, then runs collection and evaluation.
"""
import subprocess
import time
import sys
import os
import socket
import signal
from pathlib import Path

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

def is_port_in_use(port):
    """Check if a port is already in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('127.0.0.1', port))
        return result == 0

def main():
    # Ensure we are in the project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    print("🚀 Starting Sentinel Forge Evaluation Pipeline...")
    print("=" * 60)

    port = 8000
    server_process = None
    
    try:
        # 1. Start the uvicorn server
        print(f"\n[1/4] Starting uvicorn server on port {port}...")
        
        # Check if port is already in use
        if is_port_in_use(port):
            print(f"   ⚠️  Port {port} is already in use. Using existing server.")
            server_was_running = True
        else:
            server_was_running = False
            # Start uvicorn in a subprocess
            server_process = subprocess.Popen(
                [
                    sys.executable, "-m", "uvicorn",
                    "backend.main:app",
                    "--host", "127.0.0.1",
                    "--port", str(port),
                    "--log-level", "warning"
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait for server to be ready
            print(f"   ⏳ Waiting for server to start...")
            if wait_for_port(port, timeout=30):
                print(f"   ✅ Server is running on http://127.0.0.1:{port}")
            else:
                print("   ❌ Server failed to start within timeout")
                if server_process:
                    server_process.terminate()
                return 1
            
            # Give it a moment to fully initialize
            time.sleep(2)

        # 2. Run the Collection Script (uses HTTP requests)
        print("\n[2/4] Collecting Responses via HTTP...")
        collect_result = subprocess.run(
            [sys.executable, "evaluation/collect_responses.py"],
            capture_output=False,
            env={**os.environ, "BASE_URL": f"http://127.0.0.1:{port}"}
        )
        
        if collect_result.returncode != 0:
            print("❌ Collection failed.")
            return 1
        
        # 3. Run the Evaluation Script
        print("\n[3/4] Running Evaluation...")
        eval_result = subprocess.run(
            [sys.executable, "evaluation/run_evaluation.py"],
            capture_output=False
        )
        if eval_result.returncode != 0:
            print("❌ Evaluation failed.")
            return 1
        
        print("\n[4/4] Pipeline Complete ✅")
        print("=" * 60)
        return 0

    except KeyboardInterrupt:
        print("\n⚠️  Pipeline interrupted by user")
        return 1
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
        return 1
    finally:
        # 4. Clean up: Stop the server if we started it
        if server_process and not server_was_running:
            print("\n🛑 Shutting down server...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
                print("   ✅ Server stopped cleanly")
            except subprocess.TimeoutExpired:
                print("   ⚠️  Force killing server...")
                server_process.kill()
                server_process.wait()

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
