# Coding Conventions

## Python Style

1. **No Emojis** - Keep all code and documentation professional
2. **Type Hints** - Required for all functions
3. **Docstrings** - Google style for all public functions
4. **Line Length** - 88 characters (Black default)
5. **Import Order** - stdlib, third-party, local (isort)

## Testing

1. **TDD Required** - Write tests before implementation
2. **Coverage** - Minimum 80%, target 100%
3. **Test Structure** - Mirror src/ directory
4. **Naming** - test_*.py files, test_* functions
5. **Real Code** - Prefer real functions over mocks

## Documentation

1. **No Decorative Emojis** - Professional appearance only
2. **Functional Markers** - Keep ✅ ❌ for checkboxes
3. **Clear Headers** - Use markdown hierarchy
4. **Code Examples** - Always include working examples
5. **Beginner-Friendly** - Explain technical terms

## File Organization

1. **Source Code** - In `src/package_name/`
2. **Tests** - In `tests/` mirroring src structure
3. **Scripts** - In `scripts/` for tooling
4. **Docs** - Root level .md files

## Git Commits

1. **Clear Messages** - Describe what and why
2. **Run Tests** - `make check` before committing
3. **Atomic Commits** - One logical change per commit
4. **No WIP** - Complete features before pushing
