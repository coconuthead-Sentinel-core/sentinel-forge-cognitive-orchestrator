"""
Evaluation Script for Neurodivergent Cognitive Lenses (Task 5.5)

This script measures and demonstrates the output of the ADHD, Autism, and
Dyslexia cognitive lenses against a baseline (Neurotypical) text.

It processes a sample text through each lens and prints the transformed
output, along with some basic metrics to quantify the transformation.
"""

import sys
from pathlib import Path
import json

# Add project root to the Python path to allow importing from 'backend'
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from backend.services.adhd_lens import ADHDLens
from backend.services.autism_lens import AutismLens
from backend.services.dyslexia_lens import DyslexiaLens

# --- Sample Data ---

SAMPLE_TEXT = """The Sentinel Forge platform is a cognitive orchestration system designed for neurodivergent-aware AI processing. It utilizes a three-zone memory model (Active, Pattern, Crystallized) based on information entropy. The core processing is handled by the CognitiveOrchestrator, which applies different cognitive lenses like ADHD, Autism, and Dyslexia to adapt its analysis and responses. This allows the system to approach problems from multiple perspectives, enhancing creativity and precision. A platform is a base for building applications. The goal is to create a more intuitive and powerful AI interaction model.
"""

# --- Evaluation Functions ---

def evaluate_lens(lens_name, lens_instance, text):
    """Applies a lens and returns the transformed text and some metrics."""
    if lens_instance:
        transformed_text = lens_instance.transform_context(text)
    else:
        # Baseline (Neurotypical) is the original, unchanged text
        transformed_text = text
    
    metrics = {
        "word_count": len(transformed_text.split()),
        "line_count": len(transformed_text.split('\n')),
        "char_count": len(transformed_text)
    }
    
    return {
        "lens_name": lens_name,
        "transformed_text": transformed_text,
        "metrics": metrics
    }

def print_evaluation_result(result):
    """Prints the evaluation result in a readable format."""
    print("="*80)
    print(f"👁️ LENS: {result['lens_name']}")
    print("="*80)
    print("\n--- TRANSFORMED OUTPUT ---\n")
    print(result['transformed_text'])
    print("\n--- METRICS ---")
    print(f"  - Word Count:      {result['metrics']['word_count']}")
    print(f"  - Line Count:      {result['metrics']['line_count']}")
    print(f"  - Character Count: {result['metrics']['char_count']}")
    print("\n\n")

# --- Main Execution ---

def main():
    """
    Runs the evaluation for all cognitive lenses, prints the results to the
    console, and saves them to a JSON file.
    """
    print("🚀 Starting Cognitive Lens Evaluation...")

    lenses_to_evaluate = {
        "Neurotypical (Baseline)": None,
        "ADHD Burst": ADHDLens(),
        "Autism Precision": AutismLens(),
        "Dyslexia Spatial": DyslexiaLens(),
    }

    all_results = []

    for name, instance in lenses_to_evaluate.items():
        result = evaluate_lens(name, instance, SAMPLE_TEXT)
        print_evaluation_result(result)
        all_results.append(result)

    # Save results to a file
    output_path = root_dir / "evaluation" / "lens_evaluation_results.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"✅ Evaluation complete. Results saved to: {output_path}")


if __name__ == "__main__":
    main()
