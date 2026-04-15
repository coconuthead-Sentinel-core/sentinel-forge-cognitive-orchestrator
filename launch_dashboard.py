#!/usr/bin/env python3
"""
Enhanced Dashboard Launcher with Built-in Web Server
Opens the dashboard via a local HTTP server to ensure browser compatibility.
Run: python launch_dashboard.py
"""
import http.server
import socketserver
import webbrowser
import threading
import time
from pathlib import Path
import sys

PORT = 8888

class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with reduced logging"""
    def log_message(self, format, *args):
        # Only log errors
        if args[1][0] != '2':  # Not a 2xx success code
            super().log_message(format, *args)

def start_server(port):
    """Start HTTP server in the project directory"""
    Handler = QuietHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", port), Handler) as httpd:
        print(f"🌐 Server running at http://127.0.0.1:{port}/")
        httpd.serve_forever()

def main():
    # Check if dashboard file exists
    dashboard_file = Path("dashboard_standalone.html")
    if not dashboard_file.exists():
        print(f"❌ Dashboard file not found: {dashboard_file.absolute()}")
        print("   Make sure you're in the project root directory.")
        sys.exit(1)
    
    # Start server in background thread
    server_thread = threading.Thread(target=start_server, args=(PORT,), daemon=True)
    server_thread.start()
    
    # Wait for server to start
    time.sleep(1)
    
    # Build dashboard URL
    dashboard_url = f"http://127.0.0.1:{PORT}/dashboard_standalone.html"
    
    print("=" * 60)
    print("🚀 Sentinel Forge Dashboard Launcher")
    print("=" * 60)
    print(f"\n✅ Server started successfully!")
    print(f"📂 Serving from: {Path.cwd()}")
    print(f"\n🌐 Dashboard URL: {dashboard_url}")
    print("\n" + "=" * 60)
    print("INSTRUCTIONS:")
    print("=" * 60)
    print("1. Copy the URL above")
    print("2. Paste it into your web browser")
    print("3. Press ENTER to view the dashboard")
    print("\nOR just press ENTER and the browser will open automatically")
    print("=" * 60)
    
    try:
        input("\nPress ENTER to open dashboard in browser (or Ctrl+C to exit)...")
        
        # Try to open browser
        print("\n🔍 Opening browser...")
        if webbrowser.open(dashboard_url):
            print("✅ Dashboard opened in your browser!")
        else:
            print("⚠️  Couldn't open browser automatically.")
            print(f"   Please manually visit: {dashboard_url}")
        
        print("\n" + "=" * 60)
        print("🟢 Dashboard is ready!")
        print("=" * 60)
        print(f"URL: {dashboard_url}")
        print("\nPress Ctrl+C to stop the server when you're done.")
        print("=" * 60 + "\n")
        
        # Keep server running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down dashboard server...")
        print("   Dashboard closed.\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
