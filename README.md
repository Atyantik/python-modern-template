# Modern Python Project Template

<div align="center">

A comprehensive [Copier](https://copier.readthedocs.io/) template for modern Python projects with quality enforcement, AI-assisted development, and extensive tooling support.

[![Python Version](https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

****New to Python or templates?** → **[Read the Complete Beginner's Guide](GETTING_STARTED.md)**

****Using AI coding assistants?** → **[See AI Setup Guide](#using-with-ai-coding-assistants)**

---

</div>

## Features

### Core Features
- **Modern Python**: Python 3.11-3.13 support with type hints
- **Fast Package Management**: Uses [uv](https://github.com/astral-sh/uv) for blazing-fast dependency management
- **Flexible Configuration**: 20+ customization options via Copier
- **Production Ready**: Docker, CI/CD, documentation out of the box

### ✅ Quality Enforcement (Optional)
- **Code Formatting**: Black + isort for consistent style
- **Linting**: Ruff + mypy + Pylint for code quality
- **Testing**: pytest with coverage enforcement (80%+ default)
- **Security**: Bandit for security vulnerability scanning
- **Pre-commit Hooks**: 12+ automated checks before commits
- **Single Source of Truth**: All configuration in `pyproject.toml`

### **AI-Assisted Development (Optional)
- **Session Management**: Track AI coding sessions with context
- **Multi-AI Support**: Works with Claude Code, Cursor, GitHub Copilot, Google Gemini, and Aider
- **TDD Workflow**: Integrated Test-Driven Development guidelines
- **Comprehensive Guides**: 5 detailed AI documentation files
- **Project Context**: Automatic context preservation across sessions

### Docker & Documentation (Optional)
- **Multi-stage Dockerfile**: Optimized production builds
- **Docker Compose**: Full service orchestration
- **MkDocs Material**: Beautiful documentation sites
- **Auto-generated API Docs**: Using mkdocstrings
- **GitHub Pages Ready**: Deploy docs with one command

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- [Copier](https://copier.readthedocs.io/) 9.0.0 or higher

### Installation

```bash
# Install Copier (choose one)
pip install copier
# or
uv tool install copier
```

### Create a New Project

#### Interactive Mode (Recommended)
```bash
copier copy gh:Atyantik/python-modern-template my-project
cd my-project
```

#### Non-Interactive (Use Defaults)
```bash
copier copy --defaults gh:Atyantik/python-modern-template my-project
```

#### Custom Configuration
```bash
copier copy \
  --data project_name="My Awesome Project" \
  --data include_quality_scripts=true \
  --data include_ai_tools=true \
  --data include_docker=true \
  gh:Atyantik/python-modern-template my-project
```

## Example Configurations

We provide 7 ready-to-use example configurations:

| Example | Files | Features | Best For |
|---------|-------|----------|----------|
| **Minimal** | 15 | Basic structure only | Quick prototypes |
| **CLI Tool** | 25 | Typer CLI + quality | Command-line apps |
| **Library** | 23 | 90% coverage, strict quality | PyPI packages |
| **Data Science** | 45 | Docker + docs + notebooks | ML/AI projects |
| **Web API** | 50 | Docker + PostgreSQL | REST APIs |
| **AI-Assisted** | 40 | Multi-AI + session mgmt | AI pair programming |
| **Full-Featured** | 68 | Everything enabled | Production apps |

See [examples/README.md](examples/README.md) for detailed guides and commands.

> **Note**: Example projects are generated locally on-demand using `examples/generate-all.sh` and are not tracked in git. This keeps the repository lightweight while providing fresh examples from the latest template.

## Configuration Options

### Project Settings
- `project_name`: Human-readable project name
- `project_description`: Short description
- `author_name`: Your name
- `author_email`: Your email
- `license`: MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, or Proprietary

### Python Settings
- `python_version`: 3.11, 3.12, or 3.13
- `min_python_version`: Minimum required version
- `line_length`: 79, 88, 100, or 120

### Feature Flags
- `include_quality_scripts`: Quality enforcement scripts (default: true)
- `include_ai_tools`: AI session management (default: true)
- `include_docker`: Docker support (default: false)
- `include_docs`: MkDocs documentation (default: false)
- `include_pre_commit`: Pre-commit hooks (default: true)
- `include_cli`: CLI framework (default: false)

### Quality Settings
- `min_coverage`: Minimum test coverage % (default: 80)

### AI Tools Presets
- `all`: All AI tools (Claude, Cursor, Copilot, Gemini, Aider)
- `minimal`: Just AGENTS.md (universal)
- `claude`: Claude Code only
- `cursor`: Cursor IDE only
- `custom`: Pick individually

## Project Structure

```
my-project/
├── src/
│   └── my_project/          # Your Python package
├── tests/                   # Test files
├── scripts/
│   ├── quality/            # Quality check scripts (optional)
│   └── ai_tools/           # AI session tools (optional)
├── docs/                   # Documentation (optional)
├── AI_DOCS/                # AI guides (optional)
├── .github/
│   └── workflows/          # CI/CD pipelines
├── pyproject.toml          # Project configuration
├── Makefile                # Common tasks
├── Dockerfile              # Docker config (optional)
├── docker-compose.yml      # Service orchestration (optional)
├── mkdocs.yml              # Docs config (optional)
└── README.md               # Project documentation
```

## Development Workflow

### Basic Commands

```bash
# Install dependencies
uv sync --all-extras --dev

# Run tests
make test

# Run all quality checks
make check

# Format code
make format

# Run linters
make lint

# View coverage report
make coverage

# Serve documentation (if enabled)
make docs-serve
```

### AI-Assisted Development (if enabled)

```bash
# Start a new coding session
make ai-start TASK="Add user authentication"

# Log progress
uv run ai-log "Implemented login endpoint"

# Update plan
uv run ai-update-plan "Complete login tests"

# Get context summary
make ai-context

# Finish session
make ai-finish
```

### Docker (if enabled)

```bash
# Build image
make docker-build

# Run container
make docker-run

# Start services
make docker-compose-up

# Stop services
make docker-compose-down
```

## **Using with AI Coding Assistants

This template is optimized for AI-powered development! Each AI assistant automatically reads its configuration file.

### Quick Setup by AI Tool

| AI Tool | How It Works | Configuration File |
|---------|--------------|-------------------|
| **Claude Code** | Automatically reads project instructions | `CLAUDE.md` |
| **Cursor IDE** | Loads rules on project open | `.cursorrules` |
| **GitHub Copilot** | VS Code extension reads instructions | `.github/copilot-instructions.md` |
| **Google Gemini** | Reads style guide | `.gemini/styleguide.md` |
| **Aider** | Uses YAML configuration | `.aider.conf.yml` |
| **Any AI** | Universal instructions | `AGENTS.md` |

### What AI Assistants Know

When you open your project with an AI assistant, it automatically understands:
- ✅ **Test-Driven Development** - Write tests before code
- ✅ **Quality Standards** - Type hints, docstrings, 80%+ coverage
- ✅ **Project Structure** - Where to put files
- ✅ **Make Commands** - `make test`, `make check`, etc.
- ✅ **Session Tracking** - Track progress across sessions (if AI tools enabled)

### Step-by-Step: First Session with Claude Code

1. **Create your project:**
   ```bash
   copier copy gh:Atyantik/python-modern-template my-project
   cd my-project
   ```

2. **Open in Claude Code:**
   - Claude automatically reads `CLAUDE.md`
   - It knows to write tests first, follow TDD

3. **Start coding with AI:**
   ```bash
   make ai-start TASK="Add user authentication"
   ```

4. **Let AI help you code:**
   - Ask: "Create a User class with email and password"
   - Claude will write tests first, then implementation
   - It will run `make test` to verify

5. **Run quality checks:**
   ```bash
   make check
   ```

6. **Finish the session:**
   ```bash
   make ai-finish
   ```

### Step-by-Step: Using with Cursor

1. **Create and open project:**
   ```bash
   copier copy gh:Atyantik/python-modern-template my-project
   cursor my-project  # or open in Cursor IDE
   ```

2. **Cursor loads `.cursorrules` automatically**

3. **Start with Cmd+K or Cmd+L:**
   - Ask: "Add a function to validate email addresses"
   - Cursor follows TDD: writes tests first
   - It knows project conventions

4. **Test your changes:**
   ```bash
   make test
   make check
   ```

### Step-by-Step: Using with GitHub Copilot

1. **Create project and open in VS Code:**
   ```bash
   copier copy gh:Atyantik/python-modern-template my-project
   code my-project
   ```

2. **Copilot reads `.github/copilot-instructions.md`**

3. **Start coding:**
   - As you type, Copilot suggests code following project standards
   - Suggestions include type hints and docstrings
   - Test files suggested when creating new modules

4. **Verify with quality checks:**
   ```bash
   make check
   ```

### For Complete Beginners

If terms like "TDD" or "make commands" are unfamiliar:

**[Read the Complete Beginner's Guide](GETTING_STARTED.md)** - Step-by-step explanations of everything!

## Documentation

### For Template Users
- **[Getting Started Guide](GETTING_STARTED.md)**: Complete beginner's guide (START HERE!)
- **[Examples Guide](examples/README.md)**: 7 example configurations with full commands
- **[Project Summary](PROJECT_SUMMARY.md)**: Implementation details and statistics
- **[AI Tools Guide](AI_DOCS/ai-tools.md)**: AI session management (if enabled)
- **[TDD Workflow](AI_DOCS/tdd-workflow.md)**: Test-Driven Development guide (if enabled)
- **[Code Conventions](AI_DOCS/code-conventions.md)**: Style and best practices (if enabled)

### For Template Developers
- **[Template Development Guide](TEMPLATE_DEVELOPMENT.md)**: Working on this template repository

## Why This Template?

### For Solo Developers
- ✅ Quality enforcement built-in
- ✅ AI coding assistant integration
- ✅ TDD workflow for better code
- ✅ Production-ready from day one

### For Teams
- ✅ Consistent project structure
- ✅ Automated quality checks
- ✅ Comprehensive documentation
- ✅ CI/CD pipelines included

### For Learning
- ✅ Best practices enforced
- ✅ Modern Python patterns
- ✅ Type hints everywhere
- ✅ Well-documented examples

## Advanced Usage

### Update Existing Project

```bash
cd my-project
copier update
```

### Generate Examples Locally

Want to see the example projects in action? Generate all 7 configurations locally:

```bash
cd examples
./generate-all.sh
```

This creates:
- `01-minimal-package/` - Basic structure (25 files)
- `02-cli-tool/` - CLI with Typer (25 files)
- `03-library/` - Library with 90% coverage (23 files)
- `04-data-science/` - Data science with Docker (45 files)
- `05-web-api/` - Web API with Docker (50 files)
- `06-ai-assisted/` - AI tools enabled (40 files)
- `07-full-featured/` - Everything enabled (68 files)

Each example is a fully working project you can explore and test.

### Customize Template

1. Fork this repository
2. Modify files in `template/` directory
3. Update `copier.yml` configuration
4. Test with `copier copy . test-project`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Copyright © 2025 [Atyantik Technologies Private Limited](https://www.atyantik.com)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Copier](https://copier.readthedocs.io/)
- Powered by [uv](https://github.com/astral-sh/uv)
- Quality tools: [Black](https://black.readthedocs.io/), [Ruff](https://docs.astral.sh/ruff/), [mypy](https://mypy.readthedocs.io/), [Pylint](https://pylint.org/)
- Testing: [pytest](https://pytest.org/)
- Documentation: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- Inspired by modern Python best practices

## Contact

- **Website**: [www.atyantik.com](https://www.atyantik.com)
- **Email**: contact@atyantik.com
- **Issues**: [GitHub Issues](https://github.com/Atyantik/python-modern-template/issues)

---

<div align="center">

**[Star this repo](https://github.com/Atyantik/python-modern-template)** if you find it useful!

Made with  by [Atyantik Technologies](https://www.atyantik.com)

</div>
