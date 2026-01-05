# Sentinel Forge Dashboard - Quick Start

## 🚀 Instant Launch (No Installation Required!)

### Option 1: Enhanced Launcher with Web Server (RECOMMENDED)
```bash
python launch_dashboard.py
```
This starts a local web server and opens your browser automatically. **Use this if other methods don't work!**

### Option 2: Quick Scripts
**Windows:** Double-click `start_dashboard.bat`
**Linux/Mac:** Run `./start_dashboard.sh` or `bash start_dashboard.sh`

### Option 3: Simple Python Launcher
```bash
python run_dashboard.py
```

### Option 4: Direct File Open
Just double-click `dashboard_standalone.html` in your file manager, or open it in any web browser.

### Option 5: Command Line
```bash
# Linux/Mac
open dashboard_standalone.html

# Windows
start dashboard_standalone.html
```

## 📊 What You'll See

The dashboard displays real-time metrics for:

- **Memory Zones**: Active processing, pattern emergence, and crystallized storage
- **Cognitive Lenses**: Efficiency metrics for ADHD, Autism, Dyslexia, and Neurotypical processing
- **System Health**: Response times, error rates, uptime, and active sessions
- **Recent Activity**: Live activity feed with timestamps

## ✨ Features

- ✅ **Zero Dependencies**: Works offline, no server required
- ✅ **Live Updates**: Data refreshes every 3 seconds
- ✅ **Interactive Charts**: Beautiful visualizations using Chart.js
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile

## 🛠️ For Developers

### Running the Full Server Dashboard

If you want the full backend-connected dashboard:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the dashboard server:**
   ```bash
   uvicorn app.main:app --reload --port 8001
   ```

3. **Open in browser:**
   ```
   http://localhost:8001/dashboard
   ```

### Troubleshooting

**Browser doesn't open automatically:**
1. Try `python launch_dashboard.py` (enhanced version with web server)
2. Copy the URL shown in the terminal
3. Paste it into your browser manually
4. Common URL: `http://127.0.0.1:8888/dashboard_standalone.html`

**Dashboard shows old data:**
- The standalone version simulates live data
- For real data, use the server version (see above)

**Charts not loading:**
- Ensure internet connection for Chart.js CDN
- If using `launch_dashboard.py`, charts should load correctly
- Direct file:// URLs may have CDN restrictions

**Python launcher doesn't work:**
- Requires Python 3.6+
- Try the enhanced launcher: `python launch_dashboard.py`
- Windows users: Use `start_dashboard.bat`
- Linux/Mac users: Use `./start_dashboard.sh`

**"Dashboard file not found" error:**
- Make sure you're in the project root directory
- The file `dashboard_standalone.html` must exist in current directory

**Port already in use (8888):**
- Edit `launch_dashboard.py` and change `PORT = 8888` to another number (e.g., 8889)
- Or stop other programs using port 8888

## 📝 Files

- `launch_dashboard.py` - **Enhanced launcher with web server (RECOMMENDED)**
- `start_dashboard.bat` - Windows batch script (double-click to run)
- `start_dashboard.sh` - Linux/Mac shell script
- `dashboard_standalone.html` - Standalone dashboard (no server needed)
- `run_dashboard.py` - Simple Python launcher script
- `templates/dashboard.html` - Server-connected version
- `app/main.py` - Dashboard server application

## 🎯 Next Steps

1. ✅ View the dashboard (you're ready!)
2. 📊 Customize metrics in the HTML file
3. 🔌 Connect to backend API for real data
4. 🎨 Modify colors and styles to your preference

---

**Need help?** The standalone dashboard works out of the box - just open the HTML file!
