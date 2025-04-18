# PydanticAI-FastAPI Boilerplate Generator

[![PyPI version](https://badge.fury.io/py/pydanticai-fastapi-boilerplate.svg)](https://badge.fury.io/py/pydanticai-fastapi-boilerplate) <!-- Placeholder badge -->

This package provides a command-line tool (`generate-boilerplate`) to quickly generate a project structure for applications using:

*   **FastAPI:** For the web framework.
*   **PydanticAI:** For LLM integration with function calling (via OpenRouter).
*   **PostgreSQL:** For the database (using asyncpg).
*   **Pydantic Settings:** For configuration management via environment variables.

## Installation

```bash
pip install pydanticai-fastapi-boilerplate
```

*(Note: This command will only work after the package is published to PyPI.)*

Alternatively, for development, clone the repository and install in editable mode:

```bash
git clone <repository_url> # Replace with your repo URL
cd pydanticai-fastapi-boilerplate
pip install -e .
```

## Usage

Once installed, use the `generate-boilerplate` command to create a new project:

```bash
generate-boilerplate <your_project_name> [--output-dir <path>]
```

**Arguments:**

*   `<your_project_name>` (Required): The name for your new project directory.
*   `--output-dir <path>` (Optional): The directory where the new project folder will be created. Defaults to the current directory (`.`).

**Example:**

```bash
# Generate a project named 'my_cool_app' in the current directory
generate-boilerplate my_cool_app

# Generate a project named 'another_app' inside a '~/dev' directory
generate-boilerplate another_app --output-dir ~/dev
```

This will create a new directory (`<your_project_name>`) containing the boilerplate code structure and necessary configuration files based on the included templates. See the README file *within the generated project* for instructions on setting up and running the generated application.