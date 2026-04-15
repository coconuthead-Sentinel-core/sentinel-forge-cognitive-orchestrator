# Prime Directive: Sentinel Forge Task Execution Protocol

This document outlines the mandatory operational methodology for all tasks performed on the Sentinel Forge codebase. Each task, without exception, must follow this protocol.

## Core Methodology

For every task undertaken, the following framework must be applied and explicitly documented in the response to the user.

### 1. Three Verifiable Proofs

Before any action is taken, three distinct, verifiable pieces of evidence must be presented to establish the necessity and context of the task. These proofs must be grounded in observable data from the workspace.

- **Proof 1:** Direct evidence from terminal output, error logs, or application behavior.
- **Proof 2:** Specific lines of code from a relevant file that are the source of the issue or the target of the improvement.
- **Proof 3:** The execution context, such as the command used to run a process or the architectural pattern that dictates the required change.

### 2. Three Actionable Next Steps

Based on the verifiable proofs, three distinct and actionable next steps must be proposed. These options should represent different valid approaches to addressing the task.

### 3. Eisenhower Matrix Prioritization

The three actionable steps must be placed into an Eisenhower Matrix to determine the correct priority. The reasoning for each placement must be explicitly stated, referencing the verifiable proofs.

| | **Urgent** | **Not Urgent** |
| :--- | :--- | :--- |
| **Important** | **Quadrant 1: Do** | **Quadrant 2: Decide / Schedule** |
| **Not Important** | **Quadrant 3: Delegate** | **Quadrant 4: Delete / Eliminate** |

The action residing in **Quadrant 1** is the one that must be executed.

## Task Execution Cycle

1. **Initiate Task:** State the task clearly.
2. **Analyze & Report:** Present the "Three Verifiable Proofs" and the "Eisenhower Matrix" analysis for the three proposed actions.
3. **Execute:** Perform the **Quadrant 1** action.
4. **Confirm & Refer:** After the action is complete, confirm its success. State explicitly: "Referring to `PRIME_DIRECTIVE.md`."
5. **Proceed:** Move to the next logical task and repeat the entire protocol.
