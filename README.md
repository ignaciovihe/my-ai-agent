# My AI Agent (Experimental Project)

> [!WARNING]  
> **CRITICAL SECURITY NOTICE:** This repository is a **proof of concept** and a **testing project**. It is **NOT** production-ready and lacks comprehensive security measures. The codebase includes tools for file system manipulation and external code execution (such as `run_python_file.py`), which can be dangerous if used in an untrusted environment [1]. **Use this code at your own risk and never deploy it without a thorough security audit.**

## Overview

This project is an experimental AI agent developed 100% in **Python** [2]. It demonstrates a modular architecture for an agentic system capable of interacting with its environment through mathematical tools and file management capabilities.

## 🛠 Project Structure

Based on the repository files, the project is organized as follows [1]:

*   **`main.py`**: The core entry point for the application.
*   **`functions/`**: Contains the logic for the agent's tools and operations.
*   **`calculator/`**: A dedicated module for mathematical functions.
*   **`config.py`**: Handles project configuration and environment variables.
*   **`prompts.py`**: Stores the AI instructions and system prompts.
*   **`pyproject.toml` & `uv.lock`**: Configuration for dependency management using **uv**.

## 🚀 Getting Started

### Prerequisites

*   Python 3.x (managed via `.python-version`) [1].
*   [uv](https://github.com/astral-sh/uv) package manager.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ignaciovihe/my-ai-agent.git
    cd my-ai-agent
    ```

2.  **Sync dependencies:**
    ```bash
    uv sync
    ```

3.  **Run the agent:**
    ```bash
    uv run main.py
    ```

## 🧪 Testing

The repository includes several test scripts to validate core functionalities [1]:
*   `test_get_file_content.py`
*   `test_get_files_info.py`
*   `test_run_python_file.py`
*   `test_write_file.py`


> [!WARNING]
## ⚖️ Disclaimer
[!CAUTION] This project is for educational purposes only. Executing arbitrary code or allowing an AI to modify your local file system is inherently risky. Always run this project in a sandboxed environment.
