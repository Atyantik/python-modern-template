# Recent Architectural & Design Decisions

> **Purpose**: Document important decisions so future AI agents follow them

**Add new decisions at the TOP** (most recent first)

---

## [2025-11-02 15:00] AI Context Loading System

**Decision**: Implement mandatory context loading for all AI agents before task execution

**Rationale**:
- Enable seamless handoffs between different AI agents
- Maintain shared knowledge across sessions
- Prevent duplicate or conflicting work
- Create audit trail of all AI work

**Impact**:
- All AI agents must read context files before starting any task
- Context files (REQUIRED_READING, LAST_SESSION_SUMMARY, etc.) must be kept up to date
- Session files track every task with PLAN/SUMMARY/EXECUTION
- Last 5 sessions kept accessible, older ones archived

**Implementation**:
- Created `.ai-context/` directory structure
- Added `REQUIRED_READING.md` master checklist
- Created context files: LAST_SESSION_SUMMARY, ACTIVE_TASKS, RECENT_DECISIONS, CONVENTIONS
- Session tracking with timestamped files
- Makefile commands for session management

**Files Affected**:
- `.ai-context/` (new directory)
- All AI instruction files (updated with context workflow)
- `Makefile` (new session commands)
- `.gitignore` (context tracking rules)

**Status**: ✅ Implemented

**Related**:
- See `.ai-context/REQUIRED_READING.md` for complete workflow
- See `AI_INSTRUCTIONS_SUMMARY.md` for AI enforcement details

---

## [2025-11-02 14:30] AI Instruction Synchronization

**Decision**: All AI instruction files must be kept synchronized for critical changes

**Rationale**:
- Different developers use different AI tools
- Inconsistent instructions lead to different code quality
- Critical patterns must be followed universally

**Impact**:
- When updating testing patterns, update ALL AI files
- When changing architecture, update ALL AI files
- Validation script checks consistency
- CI/CD enforces this with automated checks

**Implementation**:
- Created 6 AI instruction files (.cursorrules, AGENTS.md, etc.)
- Added `scripts/validate_ai_instructions.py`
- Added `make validate-ai-docs` command
- Added CI/CD validation job

**Files Affected**:
- `.cursorrules`
- `AGENTS.md`
- `.claude/INSTRUCTIONS.md`
- `GEMINI.md`
- `.aider.conf.yml`
- `COPILOT_INSTRUCTIONS.md`

**Status**: ✅ Implemented and enforced in CI

---

## [2025-11-02 14:00] Test-Driven Development (TDD) Mandatory

**Decision**: All code must be written using Test-Driven Development - tests BEFORE implementation

**Rationale**:
- Prevents bugs before they're written
- Ensures code is testable
- Creates living documentation through tests
- Enables confident refactoring
- Industry best practice

**Impact**:
- AI agents must write tests first, always
- Implementation only after tests are written and failing
- Tests must use real code, minimize mocks
- 80% minimum coverage enforced

**Implementation**:
- Added to all AI instruction files
- Pytest configuration enforces 80% minimum
- Pre-commit hooks run tests
- CI/CD fails if tests don't pass

**Files Affected**:
- All AI instruction files
- `pyproject.toml` (pytest config)
- `.pre-commit-config.yaml`
- `.github/workflows/ci.yml`

**Status**: ✅ Enforced

**Related**: See `AGENTS.md` for complete TDD workflow

---

## [2025-11-02 14:00] Minimize Mocks - Use Real Code

**Decision**: Tests should use actual codebase functions instead of mocks whenever possible

**Rationale**:
- Mocks can hide integration bugs
- Real code tests are more reliable
- Changes to real code trigger test failures (good!)
- Better reflects actual usage

**Impact**:
- Only mock external dependencies (HTTP, DB, file I/O, time/random)
- Never mock internal functions
- Use actual implementations from codebase

**Implementation**:
- Documented in all AI instruction files
- Examples provided in Claude/Cursor instructions
- Test patterns show real code usage

**Files Affected**:
- All AI instruction files
- `tests/` directory (examples)

**Status**: ✅ Enforced through AI instructions

**When to Mock**:
- ✅ HTTP requests (requests.get, etc.)
- ✅ Database connections
- ✅ File system operations (destructive)
- ✅ Current time (datetime.now)
- ✅ Random values

**When NOT to Mock**:
- ❌ Internal project functions
- ❌ Pure functions
- ❌ Business logic
- ❌ Data transformations

---

## [2025-11-02 13:30] 80% Minimum Code Coverage

**Decision**: All code must maintain at least 80% test coverage, target 90%+

**Rationale**:
- Ensures code is well-tested
- Catches untested edge cases
- Industry standard for quality projects
- Prevents coverage regression

**Impact**:
- Pytest fails if coverage drops below 80%
- New code should aim for 100% coverage
- CI/CD blocks PRs with insufficient coverage

**Implementation**:
- `pyproject.toml` pytest config: `--cov-fail-under=80`
- Coverage reports in HTML and XML
- Codecov integration in CI

**Files Affected**:
- `pyproject.toml`
- `.github/workflows/ci.yml`
- All test files

**Status**: ✅ Enforced

---

## [2025-11-02 13:00] Type Hints Required (mypy Strict Mode)

**Decision**: All functions must have type hints, mypy strict mode enforced

**Rationale**:
- Catches type errors at development time
- Self-documenting code
- Better IDE support
- Prevents common bugs

**Impact**:
- All function parameters must have types
- All return values must have types
- mypy strict mode enabled
- CI/CD fails on type errors

**Implementation**:
- `pyproject.toml` mypy config with strict mode
- Pre-commit hook runs mypy
- CI/CD runs mypy check

**Files Affected**:
- `pyproject.toml` (mypy config)
- All `.py` files must have types
- `.pre-commit-config.yaml`

**Status**: ✅ Enforced

**Example**:
```python
# ✅ Correct
def process(data: str, count: int = 5) -> bool:
    return len(data) > count

# ❌ Wrong
def process(data, count=5):
    return len(data) > count
```

---

## [2025-11-02 12:00] Run `make check` Before Completion

**Decision**: AI agents must run `make check` before marking any task as complete

**Rationale**:
- Ensures all quality gates pass
- Catches issues before completion
- Consistent quality standard
- Automated validation

**Impact**:
- All code must pass: format + lint + test
- No task is "done" until `make check` passes
- Prevents broken code from being committed

**Implementation**:
- `make check` runs: Black, isort, Ruff, mypy, Pylint, pytest
- All AI instruction files enforce this
- Pre-commit hooks catch issues

**Files Affected**:
- `Makefile` (check target)
- All AI instruction files

**Status**: ✅ Enforced

**What `make check` Runs**:
1. `make format` - Black + isort
2. `make lint` - Ruff + mypy + Pylint
3. `make test` - pytest with coverage

---

## [2025-11-01] Project Structure: src Layout

**Decision**: Use `src/` layout with package under `src/leadership_blog_generator/`

**Rationale**:
- Prevents accidental imports from wrong location
- Ensures tests run against installed package
- Industry best practice
- Better for distribution

**Impact**:
- All code goes in `src/leadership_blog_generator/`
- Tests in `tests/` directory
- No root-level scripts (use entry points)

**Implementation**:
- `pyproject.toml` defines package structure
- Entry points in `[project.scripts]`

**Files Affected**:
- `src/leadership_blog_generator/` (all code)
- `tests/` (all tests)
- `pyproject.toml`

**Status**: ✅ Implemented

---

## Template for New Decisions

When adding a new decision, use this template:

```markdown
## [YYYY-MM-DD HH:MM] Decision Title

**Decision**: [One sentence describing the decision]

**Rationale**:
- [Why this decision was made]
- [Problems it solves]
- [Benefits it provides]

**Impact**:
- [How this affects development]
- [What developers must do differently]
- [What gets enforced/validated]

**Implementation**:
- [How this decision is implemented]
- [Tools/configs involved]
- [Automation added]

**Files Affected**:
- [List of files that were changed]
- [List of files that must follow this]

**Status**: [✅ Implemented | 🚧 In Progress | ⏸️  Paused | ❌ Rejected]

**Related**: [Links to other decisions or documentation]
```

---

**Last Updated**: 2025-11-02 15:00:00
**Updated By**: Claude Code

**How to Use**:
1. Read this file before starting any task
2. Follow all decisions marked ✅ Implemented
3. Add new decisions at the TOP when making important choices
4. Update LAST_SESSION_SUMMARY.md when adding decisions
5. Keep decisions concise but complete

**Note**: This file is committed to git so the whole team sees architectural decisions.
