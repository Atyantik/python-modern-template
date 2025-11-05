# Template Development Guide

This document explains the structure of this Copier template repository and how to work on it.

---

## Understanding the Dual AI_DOCS Structure

This repository has **TWO separate AI_DOCS directories** with different purposes:

### 1. Root `AI_DOCS/` - Template Development Instructions

**Purpose**: Instructions for AI agents working on **this template repository itself**.

**Location**: `/AI_DOCS/`

**Used by**: Claude Code, Cursor, and other AI agents when improving this template repository.

**Contains**:
- Session management workflow for template development
- TDD guidelines for template repository code
- Code conventions for template repository scripts
- Project context for this template repository

**Key Point**: These instructions reference `python_modern_template` as the package name because that's the name of THIS repository.

### 2. Template `AI_DOCS/` - Generated Project Instructions

**Purpose**: Instructions for AI agents working on **generated projects** created from this template.

**Location**: `/template/AI_DOCS/*.jinja`

**Used by**: Developers and AI agents working on projects created using this template.

**Contains**:
- Session management workflow for generated projects
- TDD guidelines for project development
- Code conventions for project code
- Project context with templated variables like `{{ package_name }}`

**Key Point**: These instructions use Jinja2 templating to customize for each generated project.

---

## Template Structure

```
python-modern-template/           # Template repository
├── AI_DOCS/                      # For template development (this repo)
│   ├── ai-tools.md
│   ├── tdd-workflow.md
│   └── ...
├── scripts/                      # Template repository scripts
│   └── ai_tools/
│       ├── templates/            # Task templates (must exist!)
│       │   ├── feature.md
│       │   ├── bugfix.md
│       │   └── ...
│       └── *.py
├── template/                     # What gets copied to new projects
│   ├── AI_DOCS/                  # For generated projects (gets copied)
│   │   ├── ai-tools.md.jinja
│   │   ├── tdd-workflow.md.jinja
│   │   └── ...
│   ├── scripts/                  # Project scripts (gets copied)
│   │   └── ai_tools/
│   │       ├── templates/        # ⚠️ MUST INCLUDE THIS!
│   │       │   ├── feature.md
│   │       │   ├── bugfix.md
│   │       │   └── ...
│   │       └── *.py.jinja
│   ├── CLAUDE.md.jinja           # Claude config for projects
│   ├── AGENTS.md.jinja           # Universal AI config for projects
│   └── ...
├── CLAUDE.md                     # Claude config for template repo
├── AGENTS.md                     # Universal AI config for template repo
└── copier.yml                    # Copier configuration
```

---

## Critical Files That Must Be Synced

When modifying template files, ensure these are kept in sync:

### 1. AI Tools Templates

**BOTH must exist and be identical:**
- `/scripts/ai_tools/templates/` (for this repo)
- `/template/scripts/ai_tools/templates/` (for generated projects)

**Files:**
- `__init__.py`
- `feature.md`
- `bugfix.md`
- `docs.md`
- `refactor.md`

**Why**: The `template_loader.py` script looks for these templates in `scripts/ai_tools/templates/`. If they don't exist in the generated project, you'll get:
```
TemplateNotFoundError: Template file not found: .../scripts/ai_tools/templates/feature.md
```

### 2. AI Configuration Files

**Root files (for template development):**
- `/CLAUDE.md`
- `/AGENTS.md`
- `/.cursorrules`
- etc.

**Template files (for generated projects):**
- `/template/CLAUDE.md.jinja`
- `/template/AGENTS.md.jinja`
- `/template/.cursorrules.jinja`
- etc.

**Sync rule**: When updating AI workflows, decide if changes apply to:
- Template development (update root files only)
- Generated projects (update template/ files only)
- Both (update both, using templating in template/ files)

---

## Testing Template Changes

### 1. Test with Copier

Create a test project to verify the template works:

```bash
# Navigate to parent directory
cd ..

# Create test project
copier copy ./python-modern-template ./test-project --data project_name="Test Project"

# Check the generated project
cd test-project
ls -la
ls -la scripts/ai_tools/templates/  # Must exist!

# Test AI tools work
uv sync --all-extras --dev
uv run ai-start-task "Test task"
```

### 2. Verify Key Features

In the generated project, verify:

- [ ] `scripts/ai_tools/templates/` directory exists with all .md files
- [ ] `AI_DOCS/` contains all documentation files (no .jinja extensions)
- [ ] `uv run ai-start-task` works without errors
- [ ] `make check` works
- [ ] All Jinja2 variables are properly substituted (no `{{ }}` in files)

### 3. Test with AI Agent

In the generated project, give Claude a task:

```bash
# Example from issue report
# Should work without TemplateNotFoundError
```

**Prompt**: "Create an example of different types of sorting strategies with dummy data."

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Forgetting to Copy Templates Directory

**Problem**: Adding templates to `/scripts/ai_tools/templates/` but not `/template/scripts/ai_tools/templates/`

**Result**: Generated projects will fail with `TemplateNotFoundError`

**Solution**: Always maintain both directories

### ❌ Mistake 2: Confusing AI_DOCS Purposes

**Problem**: Editing root `AI_DOCS/` thinking it affects generated projects

**Result**: Generated projects have outdated instructions

**Solution**: Remember the distinction - root is for template dev, template/ is for projects

### ❌ Mistake 3: Hardcoding Package Names in Template Files

**Problem**: Using `python_modern_template` in template/ files

**Result**: Generated projects reference wrong package name

**Solution**: Use `{{ package_name }}` in all .jinja files

### ❌ Mistake 4: Not Testing with Copier

**Problem**: Making changes without creating a test project

**Result**: Users encounter errors you didn't catch

**Solution**: Always test with `copier copy` before committing

---

## Development Workflow

### When Adding New Features

1. **Decide scope**: Template repo only, or generated projects too?
2. **Update root files**: For template development features
3. **Update template/ files**: For generated project features (with .jinja)
4. **Update AI_DOCS**: Update appropriate AI_DOCS directory
5. **Sync templates**: If adding new templates, copy to both locations
6. **Test with copier**: Create test project and verify
7. **Update documentation**: Update this guide if needed

### When Fixing Bugs

1. **Identify location**: Is bug in template repo or generated projects?
2. **Fix root or template/**: Fix in appropriate location
3. **Sync if needed**: If fix applies to both, update both
4. **Test with copier**: Verify fix works in generated projects
5. **Add regression test**: If applicable

### Before Committing

- [ ] Run `make check` in template repository
- [ ] Test with `copier copy` to create a new project
- [ ] Run `uv run ai-start-task "test"` in generated project
- [ ] Run `make check` in generated project
- [ ] Verify no `.jinja` extensions in generated files
- [ ] Verify all `{{ variables }}` are substituted

---

## File Naming Conventions

### In Template Repository Root

**Regular files**: Use normal extensions
- `CLAUDE.md` (not .jinja)
- `scripts/ai_tools/start_task.py` (not .jinja)

### In `/template/` Directory

**Files to be templated**: Use `.jinja` extension
- `CLAUDE.md.jinja` → generates `CLAUDE.md`
- `start_task.py.jinja` → generates `start_task.py`

**Files NOT to be templated**: Use `.jinja` but no variables
- Still need `.jinja` extension so Copier copies them
- Example: `__init__.py.jinja` with no Jinja2 syntax

**Static files**: Can omit `.jinja` if no templating needed
- `scripts/ai_tools/templates/feature.md` (no .jinja needed)

---

## Debugging Generated Projects

If users report issues:

### 1. Reproduce with Copier

```bash
copier copy ./python-modern-template ./debug-project --defaults
cd debug-project
```

### 2. Check File Structure

```bash
# Verify templates exist
ls -la scripts/ai_tools/templates/

# Verify AI_DOCS exist
ls -la AI_DOCS/

# Check for leftover .jinja files
find . -name "*.jinja"  # Should be empty!

# Check for unsubstituted variables
grep -r "{{ " . --include="*.md" --include="*.py"  # Should be empty!
```

### 3. Test AI Tools

```bash
uv sync --all-extras --dev
uv run ai-start-task "Debug test"
uv run ai-log "Testing"
uv run ai-finish-task --summary="Test complete"
```

### 4. Check Quality Tools

```bash
make check
```

---

## Getting Help

If you're confused about:

- **Template structure**: Read this document
- **AI_DOCS distinction**: See "Understanding the Dual AI_DOCS Structure" above
- **Copier usage**: See [Copier docs](https://copier.readthedocs.io/)
- **Testing changes**: See "Testing Template Changes" above

---

## Quick Reference

| Task | Command |
|------|---------|
| Test template locally | `copier copy . ../test-project` |
| Test from GitHub | `copier copy gh:Atyantik/python-modern-template test-project` |
| Update existing project | `copier update` (in project directory) |
| Test with defaults | `copier copy --defaults . ../test-project` |
| Force overwrite | `copier copy --force . ../test-project` |

---

**Remember**: When in doubt, test with copier! It's the only way to know if your changes actually work for users.
