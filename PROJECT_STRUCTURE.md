# Project Structure Details

## Current Structure

```
leadership-blog-generator/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI/CD
├── src/
│   └── leadership_blog_generator/
│       ├── __init__.py            # Package initialization & version
│       └── main.py                # CLI and core functionality
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures
│   └── test_main.py               # Test files
├── .gitignore                     # Git ignore patterns
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── pyproject.toml                 # Project metadata & tool configs
├── Makefile                       # Development commands
├── README.md                      # Main documentation
└── uv.lock                        # Dependency lock file
```

## Key Design Decisions

### No Root main.py
We don't have a `main.py` file at the root level. Instead, we use proper Python package entry points defined in `pyproject.toml`. This is the modern, best-practice approach for Python packages.

### src Layout
Using a `src/` directory prevents accidental imports from the wrong location and ensures that tests run against the installed package, not the local directory.

### Single Package
All code is organized under `src/leadership_blog_generator/`. This keeps the structure simple and focused.

### CLI via Entry Points
The `leadership-blog-generator` command is defined in `pyproject.toml` under `[project.scripts]`. This automatically creates a command-line tool when the package is installed.

### Centralized Configuration
All tool configurations (Black, isort, Ruff, mypy, pytest, etc.) are centralized in `pyproject.toml` following PEP 518 standards.

## Files Removed

- **root main.py**: Removed in favor of proper entry points
- **src/__init__.py**: Removed as unnecessary (version now in the actual package)
- **docs/**: Removed empty directory (can be added when documentation is needed)

## Why This Structure?

1. **Standards Compliance**: Follows PEP 517/518 for modern Python packaging
2. **Tool Integration**: Works seamlessly with uv, pip, and other Python tools
3. **Testing Isolation**: src layout ensures tests run against installed package
4. **Simplicity**: Minimal structure with no unnecessary files
5. **Scalability**: Easy to add more modules as the project grows
