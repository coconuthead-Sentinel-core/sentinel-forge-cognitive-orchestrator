# Phase 2 Dashboard Templates

This directory contains Jinja2 templates for the Quantum Nexus Forge Phase 2 dashboard.

## Files

- **dashboard.html** - Main Phase 2 dashboard with real-time metrics visualization

## Dashboard Features

### Three-Zone Memory System Integration
- **Active Zone (Green)**: High entropy items (>0.7) - Real-time processing
- **Pattern Zone (Yellow)**: Mid entropy items (0.3-0.7) - Pattern emergence
- **Crystallized Zone (Red)**: Low entropy items (<0.3) - Stable storage
- Real-time entropy tracking and zone distribution visualization

### Cognitive Lenses
- **Neurotypical**: Baseline processing mode
- **ADHD Burst**: Dynamic burst processing with rapid context-switching
- **Autism Precision**: Precision pattern recognition with detail-focused analysis
- **Dyslexia Spatial**: Multi-dimensional symbol interpretation
- Live lens usage statistics and switching metrics

### System Health Monitoring
- Real-time system status (green/yellow/red)
- Active pools and processor counts
- Performance metrics (latency, memory usage)
- Heap stale ratio monitoring

### Real-time Visualizations
- **Chart.js Integration**: All charts update every 3 seconds
- Zone distribution doughnut chart
- Lens usage bar chart
- Latency timeline
- Multi-zone entropy timeline
- Recent activity feed

## Blueprint Mapping

Based on the Quantum Nexus Blueprint:

- **dep_A1_to_V1**: `/api/dashboard` endpoint serves dashboard.html template
- **dep_AllFiles_L2R_to_Z1**: `/api/metrics` provides structured data for visualization

## Technical Details

- **Framework**: Jinja2 templates with FastAPI
- **Styling**: Pure CSS with gradient backgrounds and glassmorphism effects
- **Charts**: Chart.js 4.4.0 from CDN
- **Update Interval**: 3 seconds (configurable in JavaScript)
- **Responsive Design**: Grid layout adapts to screen size

## Integration

The dashboard integrates with:
1. `quantum_nexus_forge_v5_2_enhanced.py` - Three-zone memory system (Zone enum: GREEN, YELLOW, RED)
2. `backend/services/memory_zones.py` - ThreeZoneMemory manager
3. `backend/services/cognitive_orchestrator.py` - Cognitive lens orchestration
4. `backend/service.py` - Core metrics and status

## Usage

Access the dashboard at: `http://localhost:8000/api/dashboard`

The dashboard automatically polls `/api/metrics` every 3 seconds for real-time updates.
