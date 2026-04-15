import subprocess
import time
import sys
import os
import socket
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

def main():
    # Ensure we are in the project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    print("🚀 Starting Sovereign Forge Evaluation Pipeline...")
    print("=" * 60)

    server_process = None
    try:
        # 1. Start the FastAPI server
        print("\n[1/3] Starting FastAPI server...")
        server_process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "backend.main:app", "--port", "8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        if not wait_for_port(8000):
            print("❌ Server failed to start.")
            stdout, stderr = server_process.communicate()
            print("--- Server STDOUT ---")
            print(stdout)
            print("--- Server STDERR ---")
            print(stderr)
            return
        
        print("      ✅ Server is running on http://127.0.0.1:8000")
        print("      Waiting 2 seconds for application to initialize...")
        time.sleep(2) # Give the app a moment to initialize fully

        # 2. Run the Collection Script
        print("\n[2/3] Collecting Responses via HTTP...")
        collect_result = subprocess.run(
            [sys.executable, "evaluation/collect_responses.py"],
            capture_output=False, # We want to see the output in real-time
            check=True # Raise an exception if it fails
        )
        
        # 3. Run the Evaluation Script
        print("\n[3/3] Running Evaluation...")
        eval_result = subprocess.run(
            [sys.executable, "evaluation/run_evaluation.py"],
            capture_output=False,
            check=True
        )
        
        print("\n✅ Pipeline Complete.")

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ Pipeline script failed: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        if server_process:
            print("\n[+] Shutting down FastAPI server...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
                print("      ✅ Server shut down gracefully.")
            except subprocess.TimeoutExpired:
                print("      ⚠️ Server did not respond, forcing shutdown.")
                server_process.kill()

if __name__ == "__main__":
    main()
