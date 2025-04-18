import argparse
import os
import sys
from pathlib import Path

# Import the core generation function
from .generator import generate_project

def main():
    """Main entry point for the boilerplate generator CLI."""
    parser = argparse.ArgumentParser(
        description="Generate boilerplate code for PydanticAI, FastAPI, and PostgreSQL projects."
    )
    parser.add_argument(
        "project_name",
        help="The name of the project to generate.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="The directory where the project structure will be created (default: current directory).",
    )
    # Add more arguments as needed, e.g., database name, specific features to include, etc.
    # parser.add_argument("--db-name", default="app_db", help="Name for the PostgreSQL database.")
    # parser.add_argument("--include-auth", action="store_true", help="Include basic authentication setup.")

    args = parser.parse_args()

    project_path = Path(args.output_dir) / args.project_name

    print(f"Generating project '{args.project_name}' in '{project_path}'...")

    if project_path.exists():
        print(f"Error: Directory '{project_path}' already exists. Please choose a different name or location.", file=sys.stderr)
        sys.exit(1)

    try:
        # Create the main project directory
        project_path.mkdir(parents=True, exist_ok=False)

        # Call the core generation function, passing parsed arguments
        # Convert Namespace to dict for easy use in generator
        generate_project(
            output_path=project_path,
            **vars(args) # Pass other CLI args as kwargs
        )

    except Exception as e:
        print(f"An error occurred during generation: {e}", file=sys.stderr)
        # Consider cleaning up partially created directories on failure
        # if project_path.exists():
        #     import shutil
        #     shutil.rmtree(project_path)
        sys.exit(1)

if __name__ == "__main__":
    main()