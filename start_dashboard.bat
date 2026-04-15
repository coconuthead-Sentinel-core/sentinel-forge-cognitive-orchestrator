@echo off
REM Windows Batch Script to Launch Dashboard
echo ========================================
echo Sentinel Forge Dashboard Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

REM Check if dashboard file exists
if not exist "dashboard_standalone.html" (
    echo ERROR: dashboard_standalone.html not found
    echo Make sure you're in the correct directory
    pause
    exit /b 1
)

echo Starting dashboard server...
echo.
python launch_dashboard.py

pause
