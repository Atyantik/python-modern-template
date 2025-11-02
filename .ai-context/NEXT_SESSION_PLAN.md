# Implementation Plan: Automated AI Tools

> **Purpose**: Complete implementation plan for 8 CLI tools that automate the AI context workflow
> **Session Date**: TBD (Next Session)
> **Created By**: Claude Code
> **Status**: 🚧 Ready for Implementation

---

## Overview

This plan outlines the complete implementation of 8 CLI tools that automate the AI context management and session tracking workflow. These tools will be used by all AI agents (Cursor, Claude, Gemini, Copilot, Aider) to ensure consistent context loading and session tracking.

**Foundation Already Built**:
- ✅ `scripts/ai_tools/__init__.py` - Package initialization
- ✅ `scripts/ai_tools/utils.py` - All shared utilities (300+ lines)
- ✅ `.ai-context/` directory structure
- ✅ All context files (REQUIRED_READING, LAST_SESSION_SUMMARY, etc.)

**What Remains**:
- 🚧 Implement 8 CLI tools
- 🚧 Add entry points to `pyproject.toml`
- 🚧 Update all 6 AI instruction files with tools usage
- 🚧 Update README.md with tools documentation
- 🚧 Test complete workflow end-to-end

---

## Tool Specifications

### Tool 1: `ai-start-task`

**Purpose**: Automate context loading and session creation

**Command**:
```bash
ai-start-task "Add email validation"
# or
ai-start-task "Fix user authentication bug" --type=bugfix
```

**Function Signature**:
```python
def start_task(task_name: str, task_type: str = "feature") -> None:
    """Start a new AI task with full context loading.

    Args:
        task_name: Name of the task (used in session filename)
        task_type: Type of task (feature, bugfix, refactor, docs)
    """
```

**Behavior**:
1. Create session ID (YYYYMMDDHHMMSS)
2. Read and display all context files:
   - `.ai-context/LAST_SESSION_SUMMARY.md`
   - `.ai-context/ACTIVE_TASKS.md`
   - `.ai-context/RECENT_DECISIONS.md` (last 3 decisions)
   - `.ai-context/CONVENTIONS.md` (key sections)
   - Last 5 session summaries
3. Check for task conflicts in `ACTIVE_TASKS.md`
4. Create three session files:
   - `{session_id}-PLAN-{slug}.md` (from template)
   - `{session_id}-SUMMARY-{slug}.md` (from template)
   - `{session_id}-EXECUTION-{slug}.md` (with start timestamp)
5. Add task to `ACTIVE_TASKS.md` as "In Progress"
6. Display session info and next steps

**Output Example**:
```
🎯 Starting Task: Add email validation
📝 Session ID: 20251102150000

📚 Context Loaded:
  ✅ Last session summary
  ✅ Active tasks (2 in progress, 1 blocked)
  ✅ Recent decisions (TDD mandatory, minimize mocks)
  ✅ Conventions (Python naming, test structure)
  ✅ Last 5 sessions reviewed

⚠️  IMPORTANT DECISIONS TO FOLLOW:
  • TDD: Write tests BEFORE implementation
  • Minimize mocks: Use real code
  • Run make check before completion
  • 80% minimum coverage

📋 Session Files Created:
  • .ai-context/sessions/20251102150000-PLAN-add-email-validation.md
  • .ai-context/sessions/20251102150000-SUMMARY-add-email-validation.md
  • .ai-context/sessions/20251102150000-EXECUTION-add-email-validation.md

✨ Ready to start! Follow TDD workflow:
  1. Write tests first
  2. Implement code
  3. Run make check
  4. Use ai-log to track progress
  5. Use ai-finish-task when complete
```

**Template for PLAN file**:
```markdown
# Task Plan: {task_name}

**Session ID**: {session_id}
**Created**: {timestamp}
**Task Type**: {task_type}
**Status**: 🚧 In Progress

---

## Objective

[Describe what needs to be accomplished]

---

## Context

**Recent Decisions**:
{relevant_decisions}

**Related Conventions**:
{relevant_conventions}

**Dependencies**:
- [ ] None identified yet

---

## Implementation Steps

### Phase 1: Write Tests (TDD)
- [ ] Identify test cases
- [ ] Write test file(s)
- [ ] Run tests to confirm they fail

### Phase 2: Implementation
- [ ] Implement functionality
- [ ] Run tests to confirm they pass
- [ ] Verify 80%+ coverage

### Phase 3: Quality Checks
- [ ] Run `make format`
- [ ] Run `make lint`
- [ ] Run `make test`
- [ ] Fix any issues
- [ ] Run `make check` - all pass

### Phase 4: Documentation
- [ ] Update docstrings
- [ ] Add type hints
- [ ] Update README if needed

---

## Files to Change

- [ ] `src/`
- [ ] `tests/`

---

## Risks & Considerations

- None identified yet

---

## Notes

[Track decisions, blockers, questions as you work]
```

**Template for SUMMARY file**:
```markdown
# Task Summary: {task_name}

**Session ID**: {session_id}
**Created**: {timestamp}
**Status**: 🚧 In Progress

---

## What Was Done

[To be filled at end of session]

---

## Decisions Made

[To be filled at end of session]

---

## Files Changed

[To be filled at end of session]

---

## Next Steps

[To be filled at end of session]

---

## Notes

[Any important context for future sessions]
```

**Template for EXECUTION file**:
```markdown
# Execution Log: {task_name}

**Session ID**: {session_id}
**Started**: {timestamp}

---

## Log

[{timestamp}] 🎯 Task started: {task_name}
[{timestamp}] 📚 Context loaded successfully
[{timestamp}] ✅ Session files created

```

**File Location**: `scripts/ai_tools/start_task.py`

**Dependencies**:
- `scripts/ai_tools/utils.py` (all utility functions)
- `argparse` for CLI parsing
- `.ai-context/` files for context

**Error Handling**:
- If session already exists, ask to resume or create new
- If task name conflicts with active task, warn and ask for confirmation
- If context files missing, create with defaults and warn

---

### Tool 2: `ai-log`

**Purpose**: Log execution progress to current session's EXECUTION file

**Command**:
```bash
ai-log "Created test_email_validator.py with 5 test cases"
ai-log "All tests passing, coverage at 92%"
ai-log "Fixed mypy error in validation function" --level=warning
```

**Function Signature**:
```python
def log_execution(
    message: str,
    level: str = "info",
    session_id: str | None = None,
) -> None:
    """Log execution progress to EXECUTION file.

    Args:
        message: Log message
        level: Log level (info, warning, error, success)
        session_id: Session ID (default: most recent)
    """
```

**Behavior**:
1. Get current session ID (most recent if not specified)
2. Find EXECUTION file for session
3. Append timestamped log entry
4. Use emoji based on level:
   - `info`: 📝
   - `warning`: ⚠️
   - `error`: ❌
   - `success`: ✅
5. Display confirmation

**Output Example**:
```
✅ Logged to session 20251102150000:
   [2025-11-02 15:30:45] ✅ All tests passing, coverage at 92%
```

**Log Format**:
```
[{timestamp}] {emoji} {message}
```

**File Location**: `scripts/ai_tools/log_execution.py`

**Dependencies**:
- `scripts/ai_tools/utils.py` (get_current_session, append_to_file, format_timestamp)
- `argparse` for CLI parsing

**Error Handling**:
- If no active session, suggest running `ai-start-task` first
- If session ID not found, list available sessions
- If file is locked/inaccessible, retry with backoff

---

### Tool 3: `ai-update-plan`

**Purpose**: Update checkboxes in PLAN file

**Command**:
```bash
ai-update-plan "Write test file(s)"
ai-update-plan "Run make check" --check
ai-update-plan --show  # Show current plan with progress
```

**Function Signature**:
```python
def update_plan(
    item: str | None = None,
    check: bool = True,
    uncheck: bool = False,
    show: bool = False,
    session_id: str | None = None,
) -> None:
    """Update checkboxes in PLAN file.

    Args:
        item: Text of the checkbox item to update
        check: Check the box (default)
        uncheck: Uncheck the box
        show: Show current plan with progress
        session_id: Session ID (default: most recent)
    """
```

**Behavior**:
1. Find PLAN file for session
2. If `--show`, display plan with progress statistics
3. If `item` provided, find matching checkbox
4. Update checkbox state (`[ ]` ↔ `[x]`)
5. Display updated plan section
6. Log to EXECUTION file

**Output Example**:
```
✅ Updated plan for session 20251102150000:

### Phase 1: Write Tests (TDD)
- [x] Identify test cases
- [x] Write test file(s)
- [ ] Run tests to confirm they fail

Progress: 2/3 items complete (67%)
```

**Checkbox Matching**:
- Fuzzy match on item text
- Case-insensitive
- Match on partial text

**File Location**: `scripts/ai_tools/update_plan.py`

**Dependencies**:
- `scripts/ai_tools/utils.py`
- `re` for checkbox pattern matching

**Error Handling**:
- If item not found, show similar items
- If multiple matches, list all and ask which one
- If PLAN file malformed, show error with line number

---

### Tool 4: `ai-finish-task`

**Purpose**: Finalize session and update all context files

**Command**:
```bash
ai-finish-task
ai-finish-task --summary="Implemented email validation with tests"
```

**Function Signature**:
```python
def finish_task(
    summary: str | None = None,
    session_id: str | None = None,
) -> None:
    """Finalize task and update all context files.

    Args:
        summary: Brief summary (default: prompt user)
        session_id: Session ID (default: most recent)
    """
```

**Behavior**:
1. Get current session files
2. If summary not provided, prompt user for it
3. Read EXECUTION log to extract:
   - Files changed
   - Decisions made
   - Completion status
4. Update SUMMARY file with:
   - Summary paragraph
   - Decisions made
   - Files changed
   - Next steps (if any)
5. Update `LAST_SESSION_SUMMARY.md` with this session
6. Update `ACTIVE_TASKS.md`:
   - Remove from "In Progress"
   - Add to completed list
7. Ask if any decisions should be added to `RECENT_DECISIONS.md`
8. Ask if any conventions should be added to `CONVENTIONS.md`
9. Archive old sessions (keep last 5)
10. Display completion message with summary

**Output Example**:
```
✅ Task Completed: Add email validation

📝 Summary:
Implemented email validation with comprehensive tests.
Added validate_email() function with regex pattern matching.
Tests cover valid emails, invalid formats, edge cases.
All tests pass with 95% coverage.

📁 Files Changed:
  • src/leadership_blog_generator/validators.py (new)
  • tests/test_validators.py (new)
  • README.md (updated)

🎯 Decisions Made:
  • Use regex for email validation (standard RFC 5322 pattern)
  • Raise ValidationError for invalid emails

📚 Context Updated:
  ✅ LAST_SESSION_SUMMARY.md
  ✅ ACTIVE_TASKS.md (task marked complete)
  ✅ Archived 3 old sessions

🗂️  Session archived:
  .ai-context/sessions/archive/20251102150000-*

✨ Ready for next task! Run ai-start-task to begin.
```

**Interactive Prompts**:
```
📋 Any architectural decisions to record? [y/N]: y
Decision: Use regex for email validation
Rationale: Standard RFC 5322 pattern, well-tested
Impact: All email validation uses this function
Status: ✅ Implemented

✅ Added to RECENT_DECISIONS.md

📋 Any new conventions to add? [y/N]: n
```

**Archive Logic**:
- Keep last 5 SUMMARY files in `sessions/`
- Move older sessions to `sessions/archive/`
- Include all 3 files (PLAN, SUMMARY, EXECUTION)

**File Location**: `scripts/ai_tools/finish_task.py`

**Dependencies**:
- `scripts/ai_tools/utils.py`
- `shutil` for file operations

**Error Handling**:
- If PLAN not 100% complete, warn and ask for confirmation
- If `make check` not logged in EXECUTION, warn
- If no session active, error

---

### Tool 5: `ai-context-summary`

**Purpose**: Quick one-screen overview of current context

**Command**:
```bash
ai-context-summary
ai-context-summary --detailed  # Show more context
```

**Function Signature**:
```python
def show_context_summary(detailed: bool = False) -> None:
    """Show quick context summary.

    Args:
        detailed: Show detailed view with more information
    """
```

**Behavior**:
1. Read all context files
2. Display summary:
   - Last session (1-line summary)
   - Active tasks (count + list)
   - Recent decisions (last 3)
   - Key conventions
   - Recent sessions (last 5 titles)
3. If `--detailed`, show more from each section

**Output Example (Normal)**:
```
📚 AI Context Summary
════════════════════════════════════════════════════════════

📝 Last Session:
  [2025-11-02 15:00] Implemented AI instruction files with TDD
  Status: ✅ Complete | Files: 12 changed

🚧 Active Tasks:
  • 2 in progress
  • 1 blocked (waiting for API keys)
  • 0 queued

🎯 Recent Decisions (Last 3):
  1. [2025-11-02 14:00] TDD Mandatory
  2. [2025-11-02 13:30] 80% Minimum Coverage
  3. [2025-11-02 13:00] Type Hints Required (mypy strict)

📋 Key Conventions:
  • Tests before code (TDD)
  • Use real code, minimize mocks
  • Run make check before completion
  • Type hints required (mypy strict)
  • 80% minimum coverage

📂 Recent Sessions:
  1. [20251102150000] AI instruction files
  2. [20251102140000] Context management system
  3. [20251102130000] Project structure cleanup
  4. [20251102120000] Tool integration
  5. [20251102110000] Initial setup

════════════════════════════════════════════════════════════
💡 Tip: Run 'ai-start-task "task name"' to begin work
```

**Output Example (Detailed)**:
```
[Same as above but with full text of decisions, more convention details, etc.]
```

**File Location**: `scripts/ai_tools/context_summary.py`

**Dependencies**:
- `scripts/ai_tools/utils.py`
- `textwrap` for formatting

**Error Handling**:
- If context files missing, show warning but continue
- If files malformed, show partial data with error note

---

### Tool 6: `ai-check-conflicts`

**Purpose**: Check for task conflicts before starting work

**Command**:
```bash
ai-check-conflicts "Add email validation"
ai-check-conflicts  # Check all active tasks
```

**Function Signature**:
```python
def check_conflicts(task_name: str | None = None) -> None:
    """Check for task conflicts.

    Args:
        task_name: Task to check (default: check all active)
    """
```

**Behavior**:
1. Read `ACTIVE_TASKS.md`
2. If task_name provided:
   - Check if similar task already in progress
   - Check if task is blocked
   - Check if task was recently completed
3. If no task_name:
   - List all active tasks with potential conflicts
4. Use fuzzy matching for task names
5. Check file conflicts (two tasks modifying same files)

**Output Example**:
```
⚠️  Potential Conflict Detected!

Task: "Add email validation"

🚧 Similar active task found:
  • "Email validation improvements" (session 20251102140000)
    Started: 2025-11-02 14:00
    Files: src/validators.py, tests/test_validators.py

📋 Recommendation:
  • Check if tasks overlap before proceeding
  • Consider combining into one task
  • Or coordinate which files each task modifies

Continue anyway? [y/N]:
```

**Conflict Detection**:
- Fuzzy match task names (> 70% similarity)
- File overlap detection
- Blocked task dependencies

**File Location**: `scripts/ai_tools/check_conflicts.py`

**Dependencies**:
- `scripts/ai_tools/utils.py`
- `difflib` for fuzzy matching

**Error Handling**:
- If ACTIVE_TASKS.md missing, create it
- If no conflicts, show "All clear!" message

---

### Tool 7: `ai-add-decision`

**Purpose**: Add architectural/design decision to RECENT_DECISIONS.md

**Command**:
```bash
ai-add-decision
ai-add-decision --title="Use PostgreSQL for storage"
```

**Function Signature**:
```python
def add_decision(
    title: str | None = None,
    rationale: list[str] | None = None,
    impact: list[str] | None = None,
    status: str = "Implemented",
) -> None:
    """Add decision to RECENT_DECISIONS.md.

    Args:
        title: Decision title (default: prompt)
        rationale: List of rationale points (default: prompt)
        impact: List of impact points (default: prompt)
        status: Decision status (default: Implemented)
    """
```

**Behavior**:
1. If arguments not provided, prompt for each:
   - Title (one line)
   - Rationale (multiple points)
   - Impact (multiple points)
   - Implementation details
   - Files affected
   - Status (✅/🚧/⏸️/❌)
2. Format using template
3. Add to TOP of RECENT_DECISIONS.md (most recent first)
4. Display formatted decision
5. Log to current EXECUTION file

**Interactive Prompt Example**:
```
📋 Add Architectural Decision

Title: Use PostgreSQL for storage

Rationale (one point per line, empty line to finish):
> Industry-standard relational database
> ACID compliance for data integrity
> Rich ecosystem and tooling
>

Impact (one point per line, empty line to finish):
> All data persistence uses PostgreSQL
> Need to handle database migrations
> Connection pooling for performance
>

Implementation details:
> Using SQLAlchemy ORM for database access
> Alembic for migrations
> Connection pool with 10 max connections

Files affected:
> pyproject.toml (add dependencies)
> src/database/ (new module)
> tests/test_database.py (new tests)

Status [Implemented/In Progress/Paused/Rejected]: Implemented

✅ Decision added to RECENT_DECISIONS.md
```

**Template**:
```markdown
## [{timestamp}] {title}

**Decision**: {one_sentence_summary}

**Rationale**:
{rationale_points}

**Impact**:
{impact_points}

**Implementation**:
{implementation_details}

**Files Affected**:
{files_list}

**Status**: {status_emoji} {status}

**Related**: {related_links}

---
```

**File Location**: `scripts/ai_tools/add_decision.py`

**Dependencies**:
- `scripts/ai_tools/utils.py`
- `datetime` for timestamps

**Error Handling**:
- If RECENT_DECISIONS.md missing, create with header
- Validate status is one of allowed values

---

### Tool 8: `ai-add-convention`

**Purpose**: Add code convention to CONVENTIONS.md

**Command**:
```bash
ai-add-convention
ai-add-convention --section="Error Handling" --title="Always use specific exceptions"
```

**Function Signature**:
```python
def add_convention(
    section: str | None = None,
    title: str | None = None,
    description: str | None = None,
    examples: dict[str, str] | None = None,
) -> None:
    """Add convention to CONVENTIONS.md.

    Args:
        section: Section name (default: prompt)
        title: Convention title (default: prompt)
        description: Convention description (default: prompt)
        examples: Dict of {"correct": "...", "wrong": "..."} (default: prompt)
    """
```

**Behavior**:
1. If arguments not provided, prompt for each:
   - Section (existing or new)
   - Title
   - Description
   - Examples (correct/wrong)
2. If section exists, add to it
3. If new section, create with header
4. Format with examples using code blocks
5. Display formatted convention
6. Log to current EXECUTION file

**Interactive Prompt Example**:
```
📋 Add Code Convention

Existing sections:
  1. File Naming Conventions
  2. Code Naming Conventions
  3. Import Conventions
  4. Type Hint Conventions
  5. Docstring Conventions
  6. Test Conventions
  7. [Create new section]

Select section [1-7]: 1

Title: Session files naming

Description:
> Session files use timestamp-based naming for chronological sorting
> Format: YYYYMMDDHHMMSS-TYPE-slug.md

Correct example:
> 20251102150000-PLAN-add-email-validation.md

Wrong example:
> email-validation-plan.md

✅ Convention added to CONVENTIONS.md (File Naming Conventions section)
```

**Template**:
```markdown
### {title}
```python
# {description}

# ✅ Correct
{correct_example}

# ❌ Wrong
{wrong_example}
```
```

**File Location**: `scripts/ai_tools/add_convention.py`

**Dependencies**:
- `scripts/ai_tools/utils.py`
- `re` for section matching

**Error Handling**:
- If CONVENTIONS.md missing, create with standard sections
- If section doesn't exist, create it
- Validate section format

---

## Implementation Order

Implement in this order for incremental testing:

1. **Tool 5: `ai-context-summary`** (Easiest, no dependencies)
   - Can test immediately with existing context files
   - Validates context file reading logic

2. **Tool 2: `ai-log`** (Simple append operation)
   - Can test with manual session files
   - Validates log writing logic

3. **Tool 3: `ai-update-plan`** (Checkbox manipulation)
   - Can test with manual PLAN file
   - Validates file editing logic

4. **Tool 6: `ai-check-conflicts`** (Read-only)
   - Uses ACTIVE_TASKS.md
   - No state changes, safe to test

5. **Tool 7: `ai-add-decision`** (Single file update)
   - Tests template formatting
   - Interactive prompts

6. **Tool 8: `ai-add-convention`** (Section-based update)
   - More complex file editing
   - Section navigation

7. **Tool 1: `ai-start-task`** (Most complex, depends on templates)
   - Creates all session files
   - Integrates context loading
   - Updates ACTIVE_TASKS.md

8. **Tool 4: `ai-finish-task`** (Finale, touches everything)
   - Updates multiple context files
   - Archives sessions
   - Calls other tools

---

## Testing Strategy

### Unit Tests (TDD Approach)

For each tool:
1. Write tests FIRST
2. Test happy path
3. Test error cases
4. Test edge cases
5. Achieve 100% coverage

**Test file structure**:
```
tests/ai_tools/
├── __init__.py
├── conftest.py              # Shared fixtures
├── test_start_task.py
├── test_log_execution.py
├── test_update_plan.py
├── test_finish_task.py
├── test_context_summary.py
├── test_check_conflicts.py
├── test_add_decision.py
└── test_add_convention.py
```

**Shared fixtures** (in conftest.py):
```python
@pytest.fixture
def temp_context_dir(tmp_path: Path) -> Path:
    """Create temporary .ai-context directory."""
    context_dir = tmp_path / ".ai-context"
    context_dir.mkdir()
    (context_dir / "sessions").mkdir()
    (context_dir / "sessions" / "archive").mkdir()
    return context_dir

@pytest.fixture
def sample_session_files(temp_context_dir: Path) -> dict[str, Path]:
    """Create sample session files for testing."""
    session_id = "20251102150000"
    slug = "test-task"

    plan_file = temp_context_dir / "sessions" / f"{session_id}-PLAN-{slug}.md"
    summary_file = temp_context_dir / "sessions" / f"{session_id}-SUMMARY-{slug}.md"
    execution_file = temp_context_dir / "sessions" / f"{session_id}-EXECUTION-{slug}.md"

    # Write sample content
    plan_file.write_text("# Plan\n- [ ] Task 1\n- [ ] Task 2\n")
    summary_file.write_text("# Summary\nTo be filled\n")
    execution_file.write_text("# Execution\n[2025-11-02 15:00] Started\n")

    return {
        "plan": plan_file,
        "summary": summary_file,
        "execution": execution_file,
    }
```

### Integration Tests

Test complete workflow:
```python
def test_complete_workflow(temp_context_dir: Path) -> None:
    """Test complete task lifecycle."""
    # 1. Start task
    start_task("Test feature")

    # 2. Log progress
    log_execution("Created tests")
    log_execution("Implemented code")

    # 3. Update plan
    update_plan("Write tests", check=True)
    update_plan("Implement code", check=True)

    # 4. Finish task
    finish_task(summary="Completed test feature")

    # 5. Verify context updates
    assert "Test feature" in read_context_file("LAST_SESSION_SUMMARY.md")
    assert session_archived(session_id)
```

### Manual Testing Checklist

- [ ] Run `ai-context-summary` to see initial state
- [ ] Run `ai-start-task "Manual test"` to create session
- [ ] Run `ai-log "Test message"` to log
- [ ] Run `ai-update-plan "Write tests" --check` to update
- [ ] Run `ai-check-conflicts` to check for conflicts
- [ ] Run `ai-add-decision` interactively
- [ ] Run `ai-add-convention` interactively
- [ ] Run `ai-finish-task` to complete
- [ ] Verify all context files updated correctly
- [ ] Verify old sessions archived

---

## Entry Points Configuration

Add to `pyproject.toml`:

```toml
[project.scripts]
leadership-blog-generator = "leadership_blog_generator.main:main"

# AI Tools
ai-start-task = "ai_tools.start_task:main"
ai-log = "ai_tools.log_execution:main"
ai-update-plan = "ai_tools.update_plan:main"
ai-finish-task = "ai_tools.finish_task:main"
ai-context-summary = "ai_tools.context_summary:main"
ai-check-conflicts = "ai_tools.check_conflicts:main"
ai-add-decision = "ai_tools.add_decision:main"
ai-add-convention = "ai_tools.add_convention:main"
```

**Note**: Tools are in `scripts/ai_tools/` but entry points reference `ai_tools` module directly.

This works because we'll add to `pyproject.toml`:
```toml
[tool.setuptools.packages.find]
where = ["src", "scripts"]
```

---

## AI Instruction Files Updates

Each of the 6 AI instruction files needs a new section:

### Section to Add: "AI Tools Available"

```markdown
## AI Tools Available

To streamline the AI context workflow, use these automated tools:

### Starting a Task
```bash
ai-start-task "task name"
```
- Loads all context files
- Creates session files (PLAN, SUMMARY, EXECUTION)
- Shows important decisions and conventions
- Adds task to ACTIVE_TASKS.md

### During Work
```bash
ai-log "progress message"              # Log to EXECUTION file
ai-update-plan "task item" --check      # Update PLAN checkboxes
ai-check-conflicts "task name"          # Check for conflicts
```

### After Completing Task
```bash
ai-finish-task
```
- Updates SUMMARY file
- Updates LAST_SESSION_SUMMARY.md
- Updates ACTIVE_TASKS.md
- Archives old sessions
- Prompts for decisions/conventions

### Adding Context
```bash
ai-add-decision      # Add to RECENT_DECISIONS.md
ai-add-convention    # Add to CONVENTIONS.md
```

### Viewing Context
```bash
ai-context-summary          # Quick overview
ai-context-summary --detailed  # Full context
```

**Workflow**:
1. Run `ai-start-task "task name"` before ANY work
2. Follow the TDD workflow shown in PLAN file
3. Use `ai-log` to track progress
4. Use `ai-update-plan` as you complete steps
5. Run `ai-finish-task` when complete
6. Add decisions/conventions if needed

**All tools are already configured and ready to use!**
```

**Files to Update**:
1. `.cursorrules`
2. `AGENTS.md`
3. `.claude/INSTRUCTIONS.md`
4. `GEMINI.md`
5. `.aider.conf.yml` (add to comments)
6. `COPILOT_INSTRUCTIONS.md`

---

## README.md Updates

Add section to README.md:

```markdown
## AI Context Management

This project uses automated AI context management to enable seamless collaboration between different AI agents.

### For AI Agents

Before starting any task, run:
```bash
ai-start-task "task description"
```

This will:
- Load all necessary context (decisions, conventions, recent work)
- Create session tracking files
- Show you what to follow (TDD, coverage, etc.)

### Available Tools

- `ai-start-task` - Start new task with context loading
- `ai-log` - Log progress to execution file
- `ai-update-plan` - Update plan checkboxes
- `ai-finish-task` - Complete task and update context
- `ai-context-summary` - View current context
- `ai-check-conflicts` - Check for task conflicts
- `ai-add-decision` - Add architectural decision
- `ai-add-convention` - Add code convention

### Context Files

Located in `.ai-context/`:
- `REQUIRED_READING.md` - Master checklist for AI agents
- `LAST_SESSION_SUMMARY.md` - Most recent work
- `ACTIVE_TASKS.md` - In-progress tasks
- `RECENT_DECISIONS.md` - Architectural decisions
- `CONVENTIONS.md` - Code standards

Session files (local only) in `.ai-context/sessions/`:
- `{timestamp}-PLAN-{task}.md` - Task plan
- `{timestamp}-SUMMARY-{task}.md` - Task summary
- `{timestamp}-EXECUTION-{task}.md` - Execution log

See `.ai-context/REQUIRED_READING.md` for complete workflow.
```

---

## Makefile Additions (Optional)

Add convenience commands:

```makefile
## AI Tools
.PHONY: ai-help
ai-help: ## Show AI tools help
	@echo "AI Context Management Tools:"
	@echo "  ai-start-task       - Start new task"
	@echo "  ai-log              - Log progress"
	@echo "  ai-update-plan      - Update plan"
	@echo "  ai-finish-task      - Finish task"
	@echo "  ai-context-summary  - View context"
	@echo "  ai-check-conflicts  - Check conflicts"
	@echo "  ai-add-decision     - Add decision"
	@echo "  ai-add-convention   - Add convention"

.PHONY: ai-context
ai-context: ## Show current AI context
	uv run ai-context-summary

.PHONY: ai-new
ai-new: ## Start new AI task (usage: make ai-new TASK="task name")
	uv run ai-start-task "$(TASK)"

.PHONY: ai-done
ai-done: ## Finish current AI task
	uv run ai-finish-task
```

---

## Quality Checklist

Before considering tools complete:

### Code Quality
- [ ] All 8 tools implemented
- [ ] Type hints on all functions (mypy strict)
- [ ] Docstrings for all public functions
- [ ] 100% test coverage on all tools
- [ ] All tests pass
- [ ] `make check` passes (format, lint, test)
- [ ] Pylint score 10/10

### Functionality
- [ ] All tools work with real data
- [ ] Error handling comprehensive
- [ ] Interactive prompts user-friendly
- [ ] Output formatting clear and helpful
- [ ] File operations safe (backups, atomic writes)

### Documentation
- [ ] All 6 AI instruction files updated
- [ ] README.md updated
- [ ] Makefile shortcuts added
- [ ] Usage examples in docstrings
- [ ] Error messages helpful

### Integration
- [ ] Entry points in pyproject.toml
- [ ] Tools installed via `uv pip install -e .`
- [ ] Commands available in PATH
- [ ] Cross-platform compatible (macOS, Linux, Windows)

### Testing
- [ ] Unit tests for each tool (TDD)
- [ ] Integration test for complete workflow
- [ ] Manual testing completed
- [ ] Edge cases covered
- [ ] Error cases tested

---

## Success Criteria

Tools are considered complete when:

1. All 8 tools are fully implemented with tests
2. Complete workflow can be executed successfully:
   ```bash
   ai-start-task "Test workflow"
   ai-log "Step 1 complete"
   ai-update-plan "Write tests" --check
   ai-finish-task --summary="Workflow validated"
   ```
3. All context files are correctly updated
4. Sessions are properly archived
5. All AI instruction files document the tools
6. README.md has clear usage documentation
7. `make check` passes with 100% coverage
8. Tools feel natural and helpful to use

---

## Notes

- **Start with TDD**: Write tests for each tool BEFORE implementing
- **Use real data**: Test with actual `.ai-context/` files
- **Incremental testing**: Test each tool as it's completed
- **User experience**: Tools should be intuitive and helpful
- **Error messages**: Should guide user to fix issues
- **Performance**: Tools should be fast (< 1 second for most operations)

---

**Ready to Implement!** 🚀

Follow the implementation order, write tests first, and verify each tool works before moving to the next.
