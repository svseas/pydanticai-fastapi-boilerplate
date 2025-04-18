import os
import sys # Import the sys module
from pathlib import Path
import shutil
import jinja2

# Setup Jinja2 environment
TEMPLATE_DIR = Path(__file__).parent / "templates"
try:
    template_loader = jinja2.FileSystemLoader(searchpath=str(TEMPLATE_DIR))
    # Configure Jinja2 environment
    template_env = jinja2.Environment(
        loader=template_loader,
        autoescape=jinja2.select_autoescape(['html', 'xml', 'j2']), # Enable autoescaping for relevant file types
        trim_blocks=True, # Remove first newline after a block
        lstrip_blocks=True # Strip leading spaces from line to block start
    )
    print(f"Jinja2 environment loaded successfully from: {TEMPLATE_DIR}")
except ImportError:
    print("Error: Jinja2 is required but not installed. Please install it (`pip install Jinja2`).", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error loading Jinja2 templates from {TEMPLATE_DIR}: {e}", file=sys.stderr)
    sys.exit(1)


def render_template(template_name: str, context: dict, target_path: Path):
    """Renders a Jinja2 template and writes it to the target path."""
    try:
        template = template_env.get_template(template_name)
        rendered_content = template.render(context)
        # Ensure parent directory exists
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(rendered_content)
        print(f"  Rendered '{template_name}' to '{target_path}'")
    except jinja2.TemplateNotFound:
        print(f"Error: Template '{template_name}' not found in {TEMPLATE_DIR}", file=sys.stderr)
    except Exception as e:
        print(f"Error rendering template {template_name}: {e}", file=sys.stderr)


def generate_project(project_name: str, output_path: Path, **kwargs):
    """
    Generates the project structure and files.

    Args:
        project_name: The name of the project being generated.
        output_path: The Path object representing the target directory.
        **kwargs: Additional configuration options (e.g., db_name, features).
    """
    print(f"Starting generation for '{project_name}' at {output_path}...")
    print(f"Options received: {kwargs}")

    # --- Core Generation Logic ---
    # 1. Define the target directory structure.
    # 2. Copy static files/directories.
    # 3. Render template files using Jinja2 (or similar) with context from kwargs.
    # 4. Write rendered templates to the target directory.

    # --- Template Processing Logic ---
    context = {
        "project_name": project_name,
        **kwargs # Include other CLI args in context
    }

    print(f"Processing templates from {TEMPLATE_DIR}...")

    for item_path in TEMPLATE_DIR.rglob('*'): # Iterate recursively
        relative_path = item_path.relative_to(TEMPLATE_DIR)
        target_path = output_path / relative_path

        if item_path.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
            # print(f"  Created directory '{target_path}'") # Optional: verbose logging
        elif item_path.is_file():
            if item_path.suffix == '.j2':
                # It's a template file, render it
                template_name = str(relative_path) # Use relative path for get_template
                target_file_path = target_path.with_suffix('') # Remove .j2 extension
                render_template(template_name, context, target_file_path)
            else:
                # It's a static file, copy it
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item_path, target_path)
                print(f"  Copied static file '{item_path.name}' to '{target_path}'")

    print(f"\nProject '{project_name}' generated successfully at '{output_path}'.")

# Helper function example (optional)
# def render_template(template_name: str, context: dict, target_path: Path):
#     """Renders a Jinja2 template and writes it to the target path."""
#     if not template_env:
#         print(f"Skipping render for {template_name}: Jinja2 not available.")
#         return
#     try:
#         template = template_env.get_template(template_name)
#         rendered_content = template.render(context)
#         target_path.write_text(rendered_content)
#         print(f"Rendered '{template_name}' to '{target_path}'")
#     except jinja2.TemplateNotFound:
#         print(f"Error: Template '{template_name}' not found in {TEMPLATE_DIR}")
#     except Exception as e:
#         print(f"Error rendering template {template_name}: {e}")