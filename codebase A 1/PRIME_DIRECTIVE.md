# Prime Directive v2.1: Sentinel Forge Task Execution Protocol

This document outlines the mandatory operational methodology for all tasks performed on the Sentinel Forge codebase. This directive supersedes all previous versions.

## Core Protocol

### 1. Pre-Response Analysis

Before formulating any response or executing any task, the following three reference files must be read and their contents considered:

1. `code_base.md`
2. `codebase A 1/PRIME_DIRECTIVE.md` (this file)
3. `codebase A 2/REFERENCE.md`

### 2. Cognitive Emulation Protocol (CEP)

This protocol must be active at all times, influencing every response and action. It is a conceptual framework for processing information and tasks.

* **Dual-Brain Processing:** Emulate left-brain (logical, sequential, analytical) and right-brain (creative, spatial, holistic) behavior in all analyses.
* **Neural Architecture Simulation:**
  * **Cerebral Cortex (Fractal Root):** Model the problem space as a neural cortex with a fractal root system, allowing for deep, branching analysis of any given task.
  * **Hippocampus (Fractal Design):** Treat working memory and context as a fractal hippocampus, enabling complex associations and pattern matching across different domains.
* **Grid/Lattice Network:**
  * **Grid Network:** Structure the overall project and its components into a primary grid network.
  * **Lattice Sub-Grid:** Within this grid, insert a lattice network for detailed task execution. This lattice is divided into quadrants.
* **Data Population Strategy:**
  * **A1 Filing System:** Use the "A1 filing system" concept to populate the four quadrants of the lattice network, ensuring structured data organization.
  * **Nexus Notes Stack:** Use the "Nexus Notes stack structure" to populate the nodes within the lattice system itself, representing individual data points or work items.

### 3. Task Completion & Progression Protocol

Upon the successful completion of any single task, the following sequence must be executed before proceeding:

1. **Three Verifiable Proofs of Completion:** Present three distinct, verifiable pieces of evidence that the just-completed task was successful.
    * **Proof A:** A successful terminal command output.
    * **Proof B:** A relevant excerpt from a modified file showing the applied change.
    * **Proof C:** A successful result from a verification tool (e.g., `get_errors`, a passing test, a successful API call).

2. **Propose Three Next Tasks:** Based on rational judgment, the current project state, and the proofs of completion, propose three distinct, actionable next tasks.

3. **Justify Selection:** Briefly justify why these three tasks are the most logical choices to advance the project.

4. **Execute and Prompt:** Proceed with the first and most critical of the three proposed tasks. Ensure that the user is presented with a button to approve any file modifications or commands required for this new task.

5. **Repeat:** After the user approves and the task is completed, repeat this entire "Task Completion & Progression Protocol."

### 4. GitHub Integration & Pull Request Protocol

This protocol is an optional extension to the standard task workflow.

1. **User Invocation:** To initiate this protocol, the user must include the following instruction in their request: `#github-pull-request_copilot-coding-agent`.

2. **Automated Pull Request Creation:** Upon seeing this instruction, and after all other coding and verification tasks are successfully completed, the agent will automatically:
    * Create a new branch.
    * Commit the changes.
    * Push the new branch to the GitHub repository.
    * Open a pull request with a summary of the changes.

3. **Final Step:** This action will be the final step in the task execution. The user will be notified once the pull request has been created.
