#!/usr/bin/env python3
"""
Simple Dashboard Launcher
Opens the standalone dashboard in your default browser.
No dependencies required - just run: python run_dashboard.py
"""
import webbrowser
from pathlib import Path
import sys

def main():
    dashboard_file = Path(__file__).parent / "recursive_nexus_sigil_dashboard_unified.html"
    
    if not dashboard_file.exists():
        print(f"❌ Dashboard file not found: {dashboard_file}")
        sys.exit(1)
    
    dashboard_url = f"file://{dashboard_file.absolute()}"
    
    print("🚀 Launching Sentinel Forge Dashboard...")
    print(f"📂 Location: {dashboard_file}")
    print(f"🌐 URL: {dashboard_url}")
    print("\n✅ Dashboard opened in your default browser!")
    print("   If it didn't open automatically, copy this URL:")
    print(f"   {dashboard_url}\n")
    
    webbrowser.open(dashboard_url)

if __name__ == "__main__":
    main()
