# Required Reading - Python Modern Template

## What This Is

This is a **Copier template repository** for creating modern Python projects. It's not a project itself - it's a template that generates projects.

## For AI Assistants

When working on this template repository:

### 1. Template Structure
- `template/` directory contains files copied to generated projects
- Files with `.jinja` suffix use Jinja2 templating
- `copier.yml` defines template configuration

### 2. Testing Changes
- Test by generating a project: `copier copy . test-project`
- Verify generated project: `cd test-project && make check`
- Examples in `examples/` directory

### 3. Key Documentation
- README.md - Main template documentation
- GETTING_STARTED.md - Beginner's guide
- CLAUDE.md, AGENTS.md - AI configurations
- examples/README.md - Example configurations

### 4. Important Files
- `copier.yml` - Template configuration
- `template/` - All template files
- `scripts/quality/` - Quality tools
- `scripts/ai_tools/` - AI session management

## Current State

- Version: 1.0.0
- Status: Production ready
- Tests: 67/67 passing, 100% coverage
- Examples: 7 configurations available

## Development Guidelines

1. **Follow TDD** - Write tests before code
2. **Run `make check`** - Before committing
3. **No emojis** - Keep documentation professional
4. **Test generation** - Verify template produces working projects
