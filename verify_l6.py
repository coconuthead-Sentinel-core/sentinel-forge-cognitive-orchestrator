import json
import os
import time

def verify_firewall():
    print("???  INITIATING L6 FIREWALL DIAGNOSTIC...")
    time.sleep(1)

    file_path = os.path.join("meta_context", "l6_ethical_firewall.json")

    # 1. Check if the file exists
    if not os.path.exists(file_path):
        print(f" ERROR: Firewall config not found at {file_path}")
        return

    # 2. Read the configuration
    try:
        with open(file_path, "r") as f:
            config = json.load(f)
            data = config.get("ethical_firewall_l6", {})
            
            # 3. Verify Vital Stats
            status = data.get("status", "UNKNOWN")
            standard = data.get("compliance_standard", "UNKNOWN")
            constraints = data.get("neurodivergent_constraints", {})
            entropy_limit = constraints.get("complexity_threshold", {}).get("limit", 0.0)

            print(f" CONFIG LOADED: {file_path}")
            time.sleep(0.5)
            print(f"    STATUS:      {status}")
            print(f"    STANDARD:    {standard}")
            print(f"    ENTROPY MAX: {entropy_limit} (Stillwater Threshold)")
            
            # 4. Final Verdict
            if status == "ACTIVE" and entropy_limit == 0.89:
                print("\n L6 FIREWALL IS FULLY OPERATIONAL.")
                print("   The system is now protected against cognitive overload.")
            else:
                print("\n WARNING: Firewall parameters do not match Master Grid specs.")

    except json.JSONDecodeError:
        print(" ERROR: The JSON file is corrupted or not formatted correctly.")

if __name__ == "__main__":
    verify_firewall()
