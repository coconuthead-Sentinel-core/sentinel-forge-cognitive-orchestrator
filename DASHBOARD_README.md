# Sentinel Forge Dashboard - Quick Start

## 🚀 Instant Launch (No Installation Required!)

### Option 1: Python Launcher (Recommended)
```bash
python run_dashboard.py
```

### Option 2: Direct File Open
Just double-click `dashboard_standalone.html` in your file manager, or open it in any web browser.

### Option 3: Command Line
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

**Dashboard shows old data:**
- The standalone version simulates live data
- For real data, use the server version (see above)

**Charts not loading:**
- Ensure internet connection for Chart.js CDN
- Or download Chart.js locally

**Python launcher doesn't work:**
- Requires Python 3.6+
- Just open the HTML file directly instead

## 📝 Files

- `dashboard_standalone.html` - Standalone dashboard (no server needed)
- `run_dashboard.py` - Python launcher script
- `templates/dashboard.html` - Server-connected version
- `app/main.py` - Dashboard server application

## 🎯 Next Steps

1. ✅ View the dashboard (you're ready!)
2. 📊 Customize metrics in the HTML file
3. 🔌 Connect to backend API for real data
4. 🎨 Modify colors and styles to your preference

---

**Need help?** The standalone dashboard works out of the box - just open the HTML file!
