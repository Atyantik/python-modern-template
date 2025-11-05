# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-05

### Added

#### Core Features
- **Modern Python Template**: Comprehensive Copier template for Python 3.11-3.13 projects
- **Fast Package Management**: Integration with [uv](https://github.com/astral-sh/uv) for blazing-fast dependency management
- **Flexible Configuration**: 20+ customization options via Copier with smart defaults
- **Smart Folder Name Defaults**: Automatically derives project name and package name from folder name

#### Quality Enforcement (Optional)
- **Code Formatting**: Black + isort for consistent code style
- **Linting Suite**: Ruff + mypy + Pylint for comprehensive code quality checks
- **Testing Framework**: pytest with coverage enforcement (80%+ default, configurable)
- **Security Scanning**: Bandit for security vulnerability detection
- **Pre-commit Hooks**: 12+ automated checks before commits
- **Single Source of Truth**: All configuration centralized in `pyproject.toml`
- **Quality Scripts**: Unified quality check commands (`make check`)

#### AI-Assisted Development (Optional)
- **Session Management**: Track AI coding sessions with context preservation
- **Multi-AI Support**: Integrated support for Claude Code, Cursor, GitHub Copilot, Google Gemini, and Aider
- **TDD Workflow**: Comprehensive Test-Driven Development guidelines
- **AI Documentation**: 5 detailed AI documentation files (ai-tools.md, tdd-workflow.md, code-conventions.md, project-context.md, documentation-sync-rules.md)
- **Project Context**: Automatic context preservation across AI sessions
- **AI Session Tools**: Commands for `ai-start-task`, `ai-log`, `ai-update-plan`, `ai-finish-task`, `ai-context-summary`, `ai-check-conflicts`, `ai-add-decision`, `ai-add-convention`, `ai-validate-docs`
- **Session Templates**: Task-specific templates (feature, bugfix, refactor, documentation, security)

#### Docker & Documentation (Optional)
- **Multi-stage Dockerfile**: Optimized production builds
- **Docker Compose**: Full service orchestration support
- **MkDocs Material**: Beautiful documentation site generation
- **Auto-generated API Docs**: Using mkdocstrings
- **GitHub Pages Ready**: Deploy documentation with one command

#### Example Configurations
- **7 Example Projects**: Minimal, CLI Tool, Library, Data Science, Web API, AI-Assisted, Full-Featured
- **Example Generator**: Script to generate all examples locally on-demand
- **Comprehensive README**: Detailed documentation for each example configuration

#### Developer Experience
- **Makefile Commands**: Common tasks (`make test`, `make check`, `make format`, `make lint`, etc.)
- **Type Hints**: Full type hint support with strict mypy configuration
- **Docstring Standards**: Google-style docstrings enforced
- **CI/CD Pipelines**: GitHub Actions workflows included
- **License Options**: MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, or Proprietary
- **Getting Started Guide**: Complete beginner's guide (GETTING_STARTED.md)

#### Recent Enhancements
- **Improved Copier UX**: Better folder name handling and default inference
- **Enhanced AI finish-task**: Improved usability and validation
- **AI Task Management**: 4 critical enhancements to session tracking
- **Documentation Sync**: Automatic validation of AI documentation synchronization
- **Dependency Upgrades**: Latest versions of Black, Ruff, mypy, pytest, and other tools
- **Template Generation Fixes**: Jinja2 placeholder escaping and test improvements
- **Backward Compatibility**: Maintained for existing AI tool users

### Technical Details
- **Python Version Support**: 3.11, 3.12, and 3.13
- **Test Coverage**: 219 tests with 100% code coverage
- **Project Structure**: Clean separation of src/, tests/, scripts/, and docs/
- **Quality Tools**: All configured via pyproject.toml for consistency
- **Build System**: Modern setuptools with wheel support

### Documentation
- Complete README with quick start, configuration options, and examples
- Template Development Guide for contributors
- Project Summary with implementation statistics
- Comprehensive AI documentation for supported AI assistants
- Step-by-step guides for using with different AI tools

### Links
- **Repository**: https://github.com/Atyantik/python-modern-template
- **Issues**: https://github.com/Atyantik/python-modern-template/issues
- **Website**: https://www.atyantik.com
- **Contact**: contact@atyantik.com

---

**Full Changelog**: https://github.com/Atyantik/python-modern-template/commits/v1.0.0

[1.0.0]: https://github.com/Atyantik/python-modern-template/releases/tag/v1.0.0
