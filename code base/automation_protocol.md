# AI Agent Automation Protocol

This document outlines the protocol for the AI coding agent to follow when it requires a new command-line tool to complete a task.

## Guiding Principle

The primary goal is to enable the AI agent to autonomously identify, install, and utilize necessary command-line tools to fulfill user requests, while always maintaining user oversight and control. This process must be transparent and require explicit user consent before any system modifications are made.

## Protocol Steps

1. **Tool Identification**:
    * When a user request requires a command-line tool that is not part of the standard environment, the agent will identify the specific tool needed (e.g., `ffmpeg`, `jq`, `pandoc`).

2. **Installation Check**:
    * The agent must first attempt to verify if the tool is already installed and available in the system's PATH.
    * This can be done by running a command like `Get-Command <tool_name>` on PowerShell or `command -v <tool_name>` on Linux/macOS, or simply trying to run the tool with a version flag (e.g., `<tool_name> --version`).

3. **User Consent for Installation**:
    * If the tool is not found, the agent **must not** proceed with installation unilaterally.
    * It must present its plan to the user, clearly stating:
        * The name of the tool it needs.
        * The reason why the tool is necessary.
        * The exact command it intends to use for installation (e.g., `winget install ffmpeg`, `choco install jq`, `sudo apt-get install pandoc`).
    * The agent will then explicitly ask for the user's permission to proceed with the installation.

4. **Execution**:
    * Upon receiving explicit user approval (e.g., "Yes", "OK", "Proceed"), the agent will execute the proposed installation command.
    * If the installation is successful, the agent will then proceed to use the tool to complete the original user request.

5. **Error Handling**:
    * If the installation fails, the agent will report the failure to the user, including any error messages, and will not proceed with the task that required the tool.

## Scope and Limitations

* **Command-Line Only**: This protocol applies exclusively to command-line interface (CLI) tools. The agent cannot install or operate applications that require a graphical user interface (GUI).
* **Package Managers**: The agent should prefer using standard, trusted package managers for the operating system (e.g., Winget, Chocolatey for Windows; Homebrew for macOS; APT, YUM for Linux).

## Example Workflow

**User**: "Please convert the `data/report.docx` file to a PDF."

**Agent**:

1. *Identifies* the need for a tool like `pandoc`.
2. *Checks* for `pandoc` by running `Get-Command pandoc`. It's not found.
3. *Asks for consent*: "To convert this document, I need to use the `pandoc` command-line tool. It does not appear to be installed. I can install it by running the command: `winget install pandoc`. Is it okay to proceed?"
4. **User**: "Yes, go ahead."
5. *Executes*: Runs `winget install pandoc`.
6. *Completes task*: Runs `pandoc "data/report.docx" -o "data/report.pdf"`.
7. *Confirms completion*: "I have successfully converted the file to `data/report.pdf`."

## Pre-approval for Automated Installation

To streamline the workflow and grant the AI agent permission to install necessary command-line tools without asking for consent each time, a pre-approval mechanism can be used.

* **Activation**: If a file named `.ai-auto-approve` exists in the root directory of this project, the agent has standing permission to proceed with tool installation (Step 3 of the protocol is automatically approved).
* **Revocation**: To revoke this permission, simply delete the `.ai-auto-approve` file. The agent will then revert to the standard protocol and ask for consent before every installation.

When this pre-approval is active, the agent will still inform the user which tool it is installing and for what reason, but it will not wait for a response before proceeding.

## Automated Error Correction

To enable rapid, semi-automated error correction, the agent can be granted pre-approval to fix detected problems in the workspace.

* **Activation**: If a file named `.ai-auto-fix` exists in the root directory of this project, the agent has standing permission to automatically correct any errors it finds via the "Problems" view.
* **Workflow**:
    1. The user initiates the process with a request like "fix errors" or "correct problems."
    2. The agent checks for the `.ai-auto-fix` file.
    3. If present, the agent will get the list of problems, analyze them, and apply the necessary code changes to fix them without asking for confirmation for each one.
    4. The agent will report a summary of the fixes it applied.
* **Revocation**: To revoke this permission, simply delete the `.ai-auto-fix` file. The agent will then revert to explaining the errors and asking for permission before applying each fix.
