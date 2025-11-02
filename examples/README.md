# Template Examples

This directory contains example projects demonstrating different configurations of the Modern Python Project Template.

> **Note**: The example projects themselves (directories `01-minimal-package` through `07-full-featured`) are **not tracked in git**. They are generated on-demand using `./generate-all.sh` to keep the repository lightweight and ensure examples are always fresh from the latest template.

## Generate Examples

To create all 7 example projects locally:

```bash
./generate-all.sh
```

This will create fully working projects that you can explore, test, and use as reference.

## Quick Navigation

| Example | Description | Use Case |
|---------|-------------|----------|
| [minimal-package](#1-minimal-package) | Bare minimum setup | Simple scripts, small utilities |
| [cli-tool](#2-cli-tool) | CLI application with Typer | Command-line tools |
| [library](#3-library) | Reusable library with quality | Shared libraries, packages |
| [data-science](#4-data-science) | Data science project | Analysis, ML projects |
| [web-api](#5-web-api) | Web API project | REST APIs, web services |
| [ai-assisted](#6-ai-assisted) | AI-assisted development | AI-powered coding |
| [full-featured](#7-full-featured) | Everything enabled | Production applications |

## Examples

### 1. Minimal Package

**Use Case**: Simple Python package without extra tooling

**Features**:
- ✅ Basic package structure
- ✅ Simple tests
- ✅ MIT License
- ❌ No quality scripts
- ❌ No AI tools
- ❌ No Docker
- ❌ No docs

**Generate**:
```bash
copier copy \
  --data project_name="My Minimal Package" \
  --data project_description="A minimal Python package" \
  --data include_quality_scripts=false \
  --data include_ai_tools=false \
  --data include_docker=false \
  --data include_docs=false \
  --data include_pre_commit=false \
  gh:Atyantik/python-modern-template minimal-package
```

**Files**: ~15 files
**Setup Time**: < 30 seconds

**Perfect For**:
- Quick scripts
- Learning projects
- Small utilities
- Prototypes

---

### 2. CLI Tool

**Use Case**: Command-line application with argument parsing

**Features**:
- ✅ Typer CLI framework
- ✅ Quality scripts
- ✅ Pre-commit hooks
- ✅ GitHub Actions
- ❌ No AI tools
- ❌ No Docker

**Generate**:
```bash
copier copy \
  --data project_name="My CLI Tool" \
  --data project_description="A command-line tool" \
  --data include_cli=true \
  --data cli_framework=typer \
  --data include_quality_scripts=true \
  --data include_ai_tools=false \
  --data include_docker=false \
  --data include_docs=false \
  gh:Atyantik/python-modern-template cli-tool
```

**Files**: ~25 files
**Setup Time**: 1-2 minutes

**Perfect For**:
- CLI applications
- Developer tools
- Automation scripts
- System utilities

**Key Commands**:
```bash
make test      # Run tests
make check     # Quality checks
make install   # Install CLI
my-cli-tool --help
```

---

### 3. Library

**Use Case**: Reusable library with strict quality standards

**Features**:
- ✅ Quality scripts (format, lint, test)
- ✅ 90% test coverage enforced
- ✅ Pre-commit hooks
- ✅ GitHub Actions CI
- ✅ Type hints enforced
- ❌ No AI tools
- ❌ No Docker

**Generate**:
```bash
copier copy \
  --data project_name="My Library" \
  --data project_description="A reusable Python library" \
  --data include_quality_scripts=true \
  --data min_coverage=90 \
  --data include_pre_commit=true \
  --data include_ai_tools=false \
  --data include_docker=false \
  --data include_docs=false \
  gh:Atyantik/python-modern-template my-library
```

**Files**: ~23 files
**Setup Time**: 1-2 minutes

**Perfect For**:
- Shared libraries
- PyPI packages
- Internal tools
- Framework extensions

**Quality Gates**:
- ✅ Black formatting
- ✅ Ruff + mypy + Pylint
- ✅ 90% test coverage
- ✅ Type hints required
- ✅ Security scanning

---

### 4. Data Science

**Use Case**: Data science and ML projects with notebooks

**Features**:
- ✅ Quality scripts
- ✅ Documentation with MkDocs
- ✅ Docker for reproducibility
- ✅ Pre-commit hooks
- ❌ No AI tools
- ❌ No CLI

**Generate**:
```bash
copier copy \
  --data project_name="Data Science Project" \
  --data project_description="ML and data analysis project" \
  --data include_quality_scripts=true \
  --data include_docker=true \
  --data include_docs=true \
  --data include_ai_tools=false \
  --data min_coverage=70 \
  gh:Atyantik/python-modern-template ds-project
```

**Files**: ~45 files
**Setup Time**: 2-3 minutes

**Perfect For**:
- ML experiments
- Data analysis
- Research projects
- Jupyter workflows

**Key Commands**:
```bash
docker-compose up       # Start environment
make docs-serve         # View documentation
make test              # Run tests
```

---

### 5. Web API

**Use Case**: REST API or web service

**Features**:
- ✅ Quality scripts
- ✅ Docker + docker-compose
- ✅ Documentation
- ✅ Pre-commit hooks
- ✅ GitHub Actions
- ❌ No AI tools

**Generate**:
```bash
copier copy \
  --data project_name="My API" \
  --data project_description="RESTful API service" \
  --data include_quality_scripts=true \
  --data include_docker=true \
  --data include_docs=true \
  --data include_pre_commit=true \
  --data include_ai_tools=false \
  gh:Atyantik/python-modern-template my-api
```

**Files**: ~50 files
**Setup Time**: 2-3 minutes

**Perfect For**:
- REST APIs
- GraphQL services
- Microservices
- Web backends

**Docker Stack**:
- ✅ Multi-stage build
- ✅ PostgreSQL ready
- ✅ Redis ready
- ✅ Production config

---

### 6. AI-Assisted

**Use Case**: Development with AI coding assistants

**Features**:
- ✅ AI session management
- ✅ Multi-AI support (Claude, Cursor, Copilot)
- ✅ TDD workflow integrated
- ✅ Quality scripts
- ✅ Comprehensive AI docs
- ❌ No Docker

**Generate**:
```bash
copier copy \
  --data project_name="AI Assisted Project" \
  --data project_description="AI-powered development" \
  --data include_ai_tools=true \
  --data ai_tools_preset=all \
  --data include_quality_scripts=true \
  --data include_docker=false \
  --data include_docs=false \
  gh:Atyantik/python-modern-template ai-project
```

**Files**: ~40 files
**Setup Time**: 2 minutes

**Perfect For**:
- AI pair programming
- Learning TDD
- Context-aware coding
- Team collaboration

**AI Tools**:
```bash
# Session management
make ai-start TASK="Feature X"
make ai-context
make ai-finish

# Development
uv run ai-log "Progress update"
uv run ai-update-plan "Step done"
uv run ai-add-decision
```

**AI Configs Available**:
- ✅ Claude Code (CLAUDE.md)
- ✅ Cursor IDE (.cursorrules)
- ✅ GitHub Copilot
- ✅ Google Gemini
- ✅ Aider (.aider.conf.yml)
- ✅ Universal (AGENTS.md)

---

### 7. Full-Featured

**Use Case**: Production application with everything

**Features**:
- ✅ Quality scripts
- ✅ AI tools
- ✅ Docker + docker-compose
- ✅ MkDocs documentation
- ✅ Pre-commit hooks (12+)
- ✅ GitHub Actions CI/CD
- ✅ CLI framework

**Generate**:
```bash
copier copy \
  --data project_name="Full Featured App" \
  --data project_description="Production-ready application" \
  --data include_quality_scripts=true \
  --data include_ai_tools=true \
  --data include_docker=true \
  --data include_docs=true \
  --data include_pre_commit=true \
  --data include_cli=true \
  --data cli_framework=typer \
  gh:Atyantik/python-modern-template full-app
```

**Files**: 62 files
**Setup Time**: 3-4 minutes

**Perfect For**:
- Production applications
- Enterprise projects
- Complex systems
- Long-term projects

**Everything Included**:
- ✅ 26 Make commands
- ✅ Quality enforcement
- ✅ AI assistance
- ✅ Docker deployment
- ✅ Auto-generated docs
- ✅ 12+ pre-commit hooks
- ✅ CI/CD pipelines

## Comparison Matrix

| Feature | Minimal | CLI | Library | Data Sci | Web API | AI | Full |
|---------|---------|-----|---------|----------|---------|-------|------|
| **Files** | 15 | 25 | 23 | 45 | 50 | 40 | 62 |
| **Setup Time** | 30s | 1-2m | 1-2m | 2-3m | 2-3m | 2m | 3-4m |
| Quality Scripts | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AI Tools | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Docker | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| Documentation | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| Pre-commit | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| CLI Framework | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Coverage Min | 80% | 80% | 90% | 70% | 80% | 80% | 80% |

## Quick Start Guide

### 1. Choose Your Example

Pick the example that matches your use case from the table above.

### 2. Copy the Command

Copy the `copier copy` command from the example.

### 3. Customize

Modify the command with your project details:
- `project_name`: Your project name
- `project_description`: Brief description
- `author_name`: Your name
- `author_email`: Your email

### 4. Generate

Run the command in your terminal:

```bash
copier copy [flags] gh:Atyantik/python-modern-template my-project
cd my-project
```

### 5. Develop

```bash
# Install dependencies
uv sync --all-extras --dev

# Run tests
make test

# Run all quality checks
make check

# Start development
make run
```

## Generating Examples Locally

To generate all examples locally for testing:

```bash
cd examples
./generate-all.sh
```

This creates:
```
examples/
├── 01-minimal-package/
├── 02-cli-tool/
├── 03-library/
├── 04-data-science/
├── 05-web-api/
├── 06-ai-assisted/
└── 07-full-featured/
```

## Tips for Choosing

### Choose **Minimal** if:
- ✅ You need something quick
- ✅ It's a learning project
- ✅ You want minimal dependencies
- ✅ You'll add tools later

### Choose **CLI Tool** if:
- ✅ Building command-line apps
- ✅ You need argument parsing
- ✅ Want quality enforcement
- ✅ It's a developer tool

### Choose **Library** if:
- ✅ Building reusable code
- ✅ Publishing to PyPI
- ✅ Need strict quality
- ✅ It's shared code

### Choose **Data Science** if:
- ✅ ML/AI projects
- ✅ Need reproducibility
- ✅ Using notebooks
- ✅ Sharing research

### Choose **Web API** if:
- ✅ Building REST APIs
- ✅ Need Docker deployment
- ✅ It's a web service
- ✅ Microservices architecture

### Choose **AI-Assisted** if:
- ✅ Using AI coding tools
- ✅ Want session tracking
- ✅ Learning TDD
- ✅ Team with AI tools

### Choose **Full-Featured** if:
- ✅ Production application
- ✅ Long-term project
- ✅ Need everything
- ✅ Enterprise use

## Common Modifications

### Change Python Version

```bash
--data python_version=3.12 \
--data min_python_version=3.11
```

### Increase Coverage

```bash
--data min_coverage=95
```

### Change Line Length

```bash
--data line_length=100
```

### Use Click Instead of Typer

```bash
--data cli_framework=click
```

### Select Specific AI Tools

```bash
--data ai_tools_preset=custom \
--data include_claude=true \
--data include_cursor=false
```

## Need Help?

- [Main README](../README.md)
- [Template Guide](../TEMPLATE_GUIDE.md)
- [GitHub Discussions](https://github.com/Atyantik/python-modern-template/discussions)
- [Report Issues](https://github.com/Atyantik/python-modern-template/issues)

---

**Ready to start?** Pick an example and run the command!
