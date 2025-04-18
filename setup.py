from setuptools import setup, find_packages

# Most metadata is now defined in pyproject.toml
# This file is kept for compatibility and to use find_packages

setup(
    packages=find_packages(), # Automatically find packages (like 'pydanticai_fastapi_boilerplate')
    include_package_data=True, # Include non-code files specified in MANIFEST.in or found by plugins
    # install_requires is now defined in pyproject.toml under [project.dependencies]
)