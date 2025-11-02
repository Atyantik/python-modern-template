# Getting Started - Complete Beginner's Guide

**New to Python or project templates?** This guide walks you through everything step-by-step, from installation to creating your first project.

## Table of Contents

- [What is This?](#what-is-this)
- [Prerequisites](#prerequisites)
- [Step 1: Install Python](#step-1-install-python)
- [Step 2: Install UV (Package Manager)](#step-2-install-uv-package-manager)
- [Step 3: Install Copier (Template Tool)](#step-3-install-copier-template-tool)
- [Step 4: Create Your First Project](#step-4-create-your-first-project)
- [Step 5: Understanding Your New Project](#step-5-understanding-your-new-project)
- [Step 6: Run Quality Checks](#step-6-run-quality-checks)
- [Using with AI Coding Assistants](#using-with-ai-coding-assistants)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)

---

## What is This?

This is a **project template** - think of it as a cookie cutter for creating new Python projects. Instead of setting up folders, configuration files, and tools manually every time you start a new project, this template does it all for you automatically.

**What you get:**
- ✅ Pre-configured project structure
- ✅ Testing framework set up
- ✅ Code quality tools configured
- ✅ Documentation templates ready
- ✅ Optional Docker, AI tools, and more

**Real-world analogy:** It's like using a Microsoft Word template instead of creating a document from scratch every time.

---

## Prerequisites

### Required Knowledge
- **None!** This guide assumes you're completely new to Python development
- If you can use a command line/terminal, you're good to go

### What You'll Need
1. A computer (Windows, macOS, or Linux)
2. Internet connection (for downloading tools)
3. About 15 minutes

---

## Step 1: Install Python

### Check if Python is Already Installed

**Open your terminal:**
- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **macOS**: Press `Cmd + Space`, type `terminal`, press Enter
- **Linux**: Press `Ctrl + Alt + T`

**Check Python version:**
```bash
python3 --version
```

**What to expect:**
- ✅ If you see `Python 3.11.x` or higher → You're good! Skip to Step 2
- ❌ If you see `command not found` or version below 3.11 → Continue below

### Install Python (If Needed)

#### Windows
1. Visit https://www.python.org/downloads/
2. Click "Download Python 3.13" (or latest 3.11+)
3. Run the installer
4. ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"
6. Restart your terminal and verify: `python3 --version`

#### macOS
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.13
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.13 python3-pip
```

**Verify installation:**
```bash
python3 --version
# Should show: Python 3.13.x or similar
```

---

## Step 2: Install UV (Package Manager)

**What is UV?** UV is a modern, fast package manager for Python. Think of it like an app store for Python tools and libraries.

### Install UV

#### Windows
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**After installation, restart your terminal** and verify:
```bash
uv --version
# Should show: uv 0.x.x or similar
```

**If you see "command not found":**
- Close and reopen your terminal
- On macOS/Linux, run: `source ~/.bashrc` or `source ~/.zshrc`

---

## Step 3: Install Copier (Template Tool)

**What is Copier?** Copier is the tool that takes this template and creates a new project from it.

**Install Copier:**
```bash
uv tool install copier
```

**Verify installation:**
```bash
copier --version
# Should show: Copier 9.x.x or similar
```

---

## Step 4: Create Your First Project

Now comes the fun part - creating your project!

### Interactive Mode (Recommended for Beginners)

This mode will ask you questions about your project:

```bash
# Navigate to where you want to create your project
cd ~/Documents  # or any folder you prefer

# Create the project (will ask questions)
copier copy gh:Atyantik/python-modern-template my-first-project
```

**You'll be asked questions like:**
- **Project name**: My First Project
- **Description**: My first Python project
- **Your name**: John Doe
- **Your email**: john@example.com
- **Python version**: 3.13 (or whatever you installed)
- **Include quality scripts**: yes (recommended)
- **Include AI tools**: yes (if you use AI coding assistants)
- **Include Docker**: no (unless you know you need it)

**Answer each question and press Enter.** Use the default (in brackets) if unsure!

### Quick Start Mode (Use Defaults)

If you want to skip questions and use sensible defaults:

```bash
copier copy --defaults gh:Atyantik/python-modern-template my-first-project
```

### What Just Happened?

Copier created a folder called `my-first-project` with all the files you need:

```bash
cd my-first-project
ls -la  # See all the files created
```

---

## Step 5: Understanding Your New Project

### Project Structure Explained

```
my-first-project/
├── src/                    # Your Python code goes here
│   └── my_first_project/   # Main package folder
│       ├── __init__.py     # Marks this as a Python package
│       └── main.py         # Your main program
├── tests/                  # Test files go here
│   └── test_main.py        # Example test file
├── pyproject.toml          # Project configuration (like a control panel)
├── Makefile                # Shortcuts for common commands
└── README.md               # Project documentation
```

### Key Files Explained

**pyproject.toml** - The master configuration file
- Lists all dependencies (libraries your project needs)
- Configures all tools (testing, formatting, etc.)
- Defines project metadata (name, version, etc.)

**Makefile** - Command shortcuts
- `make test` instead of typing long commands
- `make check` runs all quality checks
- `make help` shows all available commands

**src/** - Your actual code
- This is where you write your Python programs
- Organized by package name

**tests/** - Test files
- Ensures your code works correctly
- Run with `make test`

---

## Step 6: Run Quality Checks

Let's verify everything works!

### Install Dependencies

First, install all required packages:

```bash
cd my-first-project
uv sync --all-extras --dev
```

**What does this do?**
- `sync` - Installs packages listed in pyproject.toml
- `--all-extras` - Includes optional features
- `--dev` - Includes development tools (testing, formatting, etc.)

**Wait for it to finish** (might take 30-60 seconds first time)

### Run Tests

```bash
make test
```

**What you should see:**
```
============================= test session starts ==============================
...
tests/test_main.py::test_version PASSED                                  [100%]
============================== 5 passed in 0.05s ===============================
```

✅ **All tests passed!** Your project is working correctly.

### Run All Quality Checks

```bash
make check
```

**This runs:**
1. **Format check** - Ensures code style is consistent
2. **Lint** - Finds potential bugs and code issues
3. **Type check** - Verifies type hints are correct
4. **Tests** - Ensures code works
5. **Security scan** - Checks for security issues

**Expected output:**
```
✅ Format check: passed
✅ Lint: passed
✅ Tests: passed (100% coverage)
✅ Security: passed

 All checks passed!
```

### View Available Commands

```bash
make help
```

**Common commands:**
- `make test` - Run tests
- `make format` - Auto-format your code
- `make lint` - Check code quality
- `make check` - Run everything
- `make run` - Run your program

---

## Using with AI Coding Assistants

This template works great with AI coding assistants! Here's how to use it with different tools:

### With Claude Code

1. **Open your project in Claude Code**
2. **Claude will automatically read** `CLAUDE.md` for instructions
3. **Key commands:**
   ```bash
   make ai-start TASK="Add new feature"  # Start a coding session
   make test                              # Run tests
   make check                             # Full quality check
   ```

### With Cursor IDE

1. **Open your project in Cursor**
2. **Cursor will read** `.cursorrules` automatically
3. **The AI will follow TDD practices** (write tests first)
4. **Same commands work:** `make test`, `make check`, etc.

### With GitHub Copilot

1. **Open project in VS Code with Copilot**
2. **Copilot reads** `.github/copilot-instructions.md`
3. **Code suggestions will follow** project conventions
4. **Use same Make commands** for testing and checks

### With Aider

1. **In your project folder, run:**
   ```bash
   aider
   ```
2. **Aider reads** `.aider.conf.yml` configuration
3. **It knows to run tests before committing**
4. **Commands:**
   ```
   /help           # See Aider commands
   /test           # Run tests
   /add src/**/*.py  # Add files to context
   ```

### AI Tools Session Management

If you enabled AI tools, you can track your coding sessions:

```bash
# Start a new task
make ai-start TASK="Add user authentication"

# Log your progress
uv run ai-log "Implemented login function"

# Update your plan
uv run ai-update-plan "Complete login tests"

# Get context summary
make ai-context

# Finish the task
make ai-finish
```

**Why use session management?**
- Keeps track of what you're working on
- Maintains context across sessions
- Documents decisions and progress
- Helps AI assistants understand your project better

---

## Troubleshooting

### Common Issues

#### "command not found: python3"
**Solution:** Python isn't installed or not in PATH
- Reinstall Python with "Add to PATH" option checked
- Restart terminal after installation

#### "command not found: uv"
**Solution:** UV not installed or terminal not restarted
```bash
# Reinstall UV
curl -LsSf https://astral.sh/uv/install.sh | sh
# Close and reopen terminal
```

#### "command not found: copier"
**Solution:** Copier not installed
```bash
uv tool install copier
```

#### "command not found: make"
**Solution (Windows):** Make isn't installed on Windows by default

**Option 1 - Use UV directly:**
```bash
# Instead of: make test
uv run pytest

# Instead of: make check
uv run quality-check
```

**Option 2 - Install Make for Windows:**
```bash
# Using Chocolatey
choco install make

# Or download from: https://gnuwin32.sourceforge.net/packages/make.htm
```

#### Tests are failing
**Check you're in the right directory:**
```bash
pwd  # Should show your project directory
ls   # Should show pyproject.toml, Makefile, etc.
```

**Reinstall dependencies:**
```bash
uv sync --all-extras --dev
```

#### "No module named ..."
**Solution:** Dependencies not installed
```bash
uv sync --all-extras --dev
```

---

## Next Steps

### Learn the Basics

1. **Read your project's README.md**
   ```bash
   cat README.md
   ```

2. **Explore the example code**
   ```bash
   cat src/my_first_project/main.py
   cat tests/test_main.py
   ```

3. **Run your program**
   ```bash
   make run
   ```

### Make Your First Change

1. **Open `src/my_first_project/main.py` in your favorite editor**

2. **Make a small change** (e.g., change the hello message)

3. **Run tests** to make sure it works
   ```bash
   make test
   ```

4. **Run quality checks**
   ```bash
   make check
   ```

5. **Commit your change** (if using git)
   ```bash
   git add .
   git commit -m "My first change"
   ```

### Explore Example Configurations

Want to see different project setups?

```bash
cd examples
./generate-all.sh
```

This creates 7 example projects showing different configurations:
- Minimal (bare bones)
- CLI Tool (command-line app)
- Library (for sharing code)
- Data Science (ML/AI projects)
- Web API (REST APIs)
- AI-Assisted (with AI tools)
- Full-Featured (everything!)

**Explore any example:**
```bash
cd 01-minimal-package
ls -la
make test
```

### Learn More

- **[README.md](README.md)** - Full documentation
- **[examples/README.md](examples/README.md)** - Example configurations
- **[AI_DOCS/tdd-workflow.md](AI_DOCS/tdd-workflow.md)** - Test-Driven Development guide
- **[AI_DOCS/code-conventions.md](AI_DOCS/code-conventions.md)** - Code style guide

### Get Help

- **Questions?** Open an issue: https://github.com/Atyantik/python-modern-template/issues
- **Email:** contact@atyantik.com
- **Documentation:** All guides are in the project folders

---

## Quick Reference Card

### Essential Commands

```bash
# Create a new project
copier copy gh:Atyantik/python-modern-template my-project

# Set up project
cd my-project
uv sync --all-extras --dev

# Development
make test          # Run tests
make format        # Format code
make lint          # Check code quality
make check         # Run all quality checks
make run           # Run your program

# AI Sessions (if enabled)
make ai-start TASK="description"
uv run ai-log "progress update"
make ai-finish

# Help
make help          # Show all Make commands
uv --help          # UV help
copier --help      # Copier help
```

### File Structure Quick Reference

```
my-project/
├── src/              → Your code
├── tests/            → Test files
├── pyproject.toml    → Configuration
├── Makefile          → Command shortcuts
├── README.md         → Documentation
└── .git/             → Git repository
```

### When Something Goes Wrong

1. ✅ Check you're in project directory: `pwd`
2. ✅ Check Python version: `python3 --version`
3. ✅ Reinstall dependencies: `uv sync --all-extras --dev`
4. ✅ Check command spelling: `make help`
5. ✅ Restart terminal
6. ✅ Read error message carefully

---

## Success Checklist

After following this guide, you should be able to:

- ✅ Create a new Python project from the template
- ✅ Install dependencies with UV
- ✅ Run tests successfully
- ✅ Run quality checks
- ✅ Make code changes
- ✅ Use AI coding assistants with your project
- ✅ Understand the project structure
- ✅ Know where to find help

**Congratulations!**  You're ready to start building Python projects!

---

**Remember:** Every expert was once a beginner. Don't hesitate to:
- Experiment and break things (that's how you learn!)
- Read error messages carefully (they're usually helpful)
- Ask for help when stuck (that's what communities are for!)
- Take breaks when frustrated (fresh eyes solve problems faster)

Happy coding!

---

**Made with  by [Atyantik Technologies](https://www.atyantik.com)**
