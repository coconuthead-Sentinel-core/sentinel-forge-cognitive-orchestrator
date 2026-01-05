#!/bin/bash
# Linux/Mac Shell Script to Launch Dashboard

echo "========================================"
echo "Sentinel Forge Dashboard Launcher"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "ERROR: Python is not installed"
    echo "Please install Python 3"
    exit 1
fi

# Use python3 if available, otherwise python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Check if dashboard file exists
if [ ! -f "dashboard_standalone.html" ]; then
    echo "ERROR: dashboard_standalone.html not found"
    echo "Make sure you're in the correct directory"
    exit 1
fi

echo "Starting dashboard server..."
echo ""
$PYTHON_CMD launch_dashboard.py
