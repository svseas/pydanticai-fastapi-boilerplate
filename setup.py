from setuptools import setup, find_packages

setup(
    name="pydanticai-fastapi-boilerplate",
    version="0.1.0",
    description="A package to generate boilerplate code for PydanticAI, FastAPI, and PostgreSQL stacks.",
    long_description=open('README.md').read(), # Use the README inside the package
    long_description_content_type="text/markdown",
    author="joe.tang",
    author_email="txt2408@gmail.com",
    url="https://github.com/svseas", # User's GitHub profile URL
    packages=find_packages(exclude=["tests*"]), # Automatically find packages
    install_requires=[
        "Jinja2>=3.0", # For rendering templates
    ],
    entry_points={
        'console_scripts': [
            'generate-boilerplate=pydanticai_fastapi_boilerplate.cli:main', # Updated entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # Choose appropriate license
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
    ],
    python_requires='>=3.8', # Specify minimum Python version
)