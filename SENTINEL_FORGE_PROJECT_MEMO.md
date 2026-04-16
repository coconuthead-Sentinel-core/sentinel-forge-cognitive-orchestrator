# MEMORANDUM: SENTINEL FORGE PROJECT STATUS & EXECUTION PLAN

**TO:** NotebookLM Assistant / Project Lead
**FROM:** Sentinel Forge Development Team (Copilot)
**DATE:** December 29, 2025
**SUBJECT:** Phase IV Execution Strategy: Sentient City Dashboard Integration

---

## 1. EXECUTIVE SUMMARY

The **Sentinel Forge** project has successfully reached the **Standalone Prototype** phase. The Python backend (`uvicorn`) is operational, and the "Live Fire" simulation has validated the core cognitive logic (12-hour shift compression). The frontend dashboard (`recursive_nexus_sigil_dashboard_unified.html`) has been upgraded to **v4.2**, featuring the visual framework for the "Cognitive Exoskeleton" (Karaoke-style TTS, Microphone controls).

**Current Status:**

- **Backend:** ✅ Online (FastAPI + WebSocket endpoints active).
- **Frontend:** ⚠️ Disconnected (UI exists but uses mock data; no real-time WebSocket link).
- **AI Integration:** ⚠️ Partial (TTS/STT logic exists in JS but is not wired to the `CognitiveOrchestrator`).

---

## 2. EISENHOWER MATRIX: TASK PRIORITIZATION

We have categorized the remaining tasks to optimize the path to a fully "Sentient" dashboard.

| **URGENT** | **NOT URGENT** |
| :--- | :--- |
| **QUADRANT 1: DO FIRST (Critical Infrastructure)**<br>_The "Synapse" - Essential for System Life_<br><br>1. **WebSocket Integration**: Connect Dashboard to `/ws/cognitive`.<br>2. **API Key Handshake**: Secure the connection.<br>3. **Real-Time Metrics**: Bind DOM elements to live backend data.<br>4. **Voice-to-API Pipeline**: Wire the Microphone input to `POST /api/chat`. | **QUADRANT 2: SCHEDULE (Strategic Value)**<br>_The "Soul" - High Impact, Complex_<br><br>1. **Cognitive Lenses**: Fully implement ADHD/Autism/Dyslexia CSS toggles.<br>2. **Neuro-Adaptive UI**: Auto-switch lenses based on backend Persona.<br>3. **Smart TTS Response**: Feed AI responses back into the "Karaoke" engine. |
| **QUADRANT 3: DELEGATE (Enhancements)**<br>_The "Sigil" - Visual Polish_<br><br>1. **Dynamic Sigil**: Replace static emoji with pulsing Canvas/SVG.<br>2. **L7 Singularity View**: 3D/Particle visualization of the "City Bloom". | **QUADRANT 4: ELIMINATE/LATER**<br>_Maintenance_<br><br>1. **Dockerization**: Final container polish (currently functional).<br>2. **Final Smoke Test**: End-to-end validation run. |

---

## 3. DETAILED IMPLEMENTATION PLAN

### PHASE A: THE SYNAPSE (Quadrant 1)

**Objective:** Establish a nervous system between the Python Brain and the HTML Body.

- **Task A1: WebSocket Wiring**
  - **Action:** Modify `recursive_nexus_sigil_dashboard_unified.html` to open a `WebSocket` connection to `ws://localhost:8000/ws/cognitive`.
  - **Logic:** Listen for `cognitive.state` and `zone.transition` events.
  - **Target File:** `recursive_nexus_sigil_dashboard_unified.html`

- **Task A2: Real-Time Data Binding**
  - **Action:** Update `#latency`, `#jitter`, and Zone Lists (`<ul>`) dynamically upon receiving JSON packets.
  - **Target File:** `recursive_nexus_sigil_dashboard_unified.html`

### PHASE B: THE VOICE (Quadrant 1 & 2)

**Objective:** Enable two-way intelligent communication.

- **Task B1: Voice-to-API Pipeline**
  - **Action:** Inside the `recognition.onresult` function, fetch `POST /api/chat` with the user's transcript.
  - **Target File:** `recursive_nexus_sigil_dashboard_unified.html`

- **Task B2: Intelligent Response (Karaoke)**
  - **Action:** Pass the JSON response from `/api/chat` into the existing `speak()` function to trigger the visual highlighting.
  - **Target File:** `recursive_nexus_sigil_dashboard_unified.html`

### PHASE C: THE LENS (Quadrant 2)

**Objective:** Neuro-divergent accessibility and adaptation.

- **Task C1: Lens Toggles**
  - **Action:** Create CSS classes (`.lens-adhd`, `.lens-autism`) that override root variables (colors, animations).
  - **Target File:** `recursive_nexus_sigil_dashboard_unified.html`

---

## 4. SOURCE FILE INVENTORY

The following files are critical for the completion of these tasks. Please reference them in your planning.

1. **`recursive_nexus_sigil_dashboard_unified.html`**
    - _Role:_ The primary interface. Contains all JS logic for WebSockets, TTS, and STT.
    - _Status:_ Needs wiring to backend.

2. **`backend/ws_api.py`**
    - _Role:_ The WebSocket endpoint definition.
    - _Status:_ Ready. Defines the `/ws/cognitive` route and event subscription.

3. **`backend/api.py`**
    - _Role:_ The REST API for Chat.
    - _Status:_ Ready. Defines `POST /chat`.

4. **`backend/services/cognitive_orchestrator.py`**
    - _Role:_ The brain processing the input.
    - _Status:_ Ready.

---

**NEXT ACTION:**
Proceed immediately with **Phase A (The Synapse)**. Connect the dashboard to the live backend to cease "Mock Mode" operations.
