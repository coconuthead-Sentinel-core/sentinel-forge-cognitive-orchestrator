import json
import os
import time

def render_hologram():
    print("\n INITIATING VR HOLOGRAPHIC RENDER...")
    time.sleep(1)
    
    path = os.path.join("meta_context", "vr_studios_capstone_v110.json")
    
    if not os.path.exists(path):
        print(f" ERROR: Blueprint not found at {path}")
        return

    with open(path, "r") as f:
        data = json.load(f)

    meta = data.get("project_metadata", {})
    matrix = data.get("capstone_matrix", [])

    print(f"\n PROJECT: {meta.get("project_name")}")
    print(f"   VERSION: {meta.get("version")}")
    print("="*60)
    print(f"{ "ID":<20} | { "COORDS (X,Y,Z)":<20} | { "DEPTH":<5}")
    print("-" * 60)

    for node in matrix:
        coords = node.get("vr_coordinates", {})
        c_str = f"[{coords.get("x")}, {coords.get("y")}, {coords.get("z")}]"
        depth = node.get("fractal_depth", 1)
        depth_icon = "" * depth
        
        print(f"{node.get("section_id"):<20} | {c_str:<20} | {depth_icon}")
        time.sleep(0.2)

    print("="*60)
    print(" HOLOGRAM STABLE. READY FOR UNITY DEPLOYMENT.")

if __name__ == "__main__":
    render_hologram()
