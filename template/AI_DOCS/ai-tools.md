# AI Context Management Tools

> **Shared documentation for all AI coding assistants**
>
> This file is referenced by multiple AI tool configurations. Changes here automatically apply to all tools that support file references.

## 🚨 MANDATORY: Session Management

**Every AI session MUST start and end with these commands:**

```bash
# START (required first step)
uv run ai-start-task "Your task description"

# DURING (log progress)
uv run ai-log "Your progress message"
uv run ai-update-plan "Task item you completed"

# END (required last step)
uv run ai-finish-task --summary="What you accomplished"
```

**This is NOT optional!** Every AI agent must follow this workflow.

## 📚 All Available Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `ai-start-task` | Start new task session | **Always first** - before any work |
| `ai-log` | Log execution progress | During work - track milestones |
| `ai-update-plan` | Update task plan checkboxes | After completing each step |
| `ai-context-summary` | Show current context | When unsure what's happening |
| `ai-check-conflicts` | Check for task conflicts | Before starting parallel work |
| `ai-add-decision` | Document architectural decision | After making design choice |
| `ai-add-convention` | Add code convention | When establishing new pattern |
| `ai-finish-task` | End session and update context | **Always last** - when work complete |

## 🛠️ Tool Details

### 1. ai-start-task (REQUIRED FIRST)

**Start a new AI task session with full context loading.**

```bash
uv run ai-start-task "Add user authentication feature"
```

**What it does:**
- Creates unique session ID (timestamp-based)
- Generates three session files:
  - `PLAN-*.md` - Task plan with checkboxes
  - `SUMMARY-*.md` - Session summary template
  - `EXECUTION-*.md` - Execution log
- Displays last session summary
- Shows active tasks (checks for conflicts)
- Lists recent architectural decisions
- Shows key conventions to follow
- Adds task to `ACTIVE_TASKS.md`

**Options:**
```bash
# Specify task type
uv run ai-start-task "Fix bug in validator" --type=bugfix
uv run ai-start-task "Improve performance" --type=enhancement
uv run ai-start-task "Update docs" --type=documentation

# Default type is "feature"
```

**Output example:**
```
╔══════════════════════════════════════════════════════════╗
║          🚀 AI Task Session Started                      ║
╚══════════════════════════════════════════════════════════╝

📋 Task: Add user authentication feature
🆔 Session ID: 20250102123045
📁 Session files created:
   - .ai-context/sessions/20250102123045-PLAN-Add_user_authentication_feature.md
   - .ai-context/sessions/20250102123045-SUMMARY-Add_user_authentication_feature.md
   - .ai-context/sessions/20250102123045-EXECUTION-Add_user_authentication_feature.md

📊 Last Session Summary
────────────────────────
- Previous session: Implemented email validation
- Status: ✅ Complete
- Coverage: 100%

⚠️  Active Tasks
────────────────────────
No conflicting tasks in progress

📌 Recent Decisions (Last 5)
────────────────────────
1. Use Pydantic for data validation
2. Follow Google docstring format
3. Minimum 80% test coverage

🎯 Key Conventions
────────────────────────
- Always write tests first (TDD)
- Use type hints on all functions
- Run `make check` before committing
```

### 2. ai-log

**Log progress messages to the session execution log.**

```bash
uv run ai-log "Created test_auth.py with 8 test cases"
uv run ai-log "All tests passing" --level=success
uv run ai-log "Found mypy error in line 45" --level=warning
uv run ai-log "Build failed" --level=error
```

**Options:**
- `--level=info` (default) - Regular progress update
- `--level=success` - Success milestone
- `--level=warning` - Warning or concern
- `--level=error` - Error encountered
- `--session-id=<id>` - Log to specific session (defaults to latest)

**What it does:**
- Appends timestamped entry to `EXECUTION-*.md`
- Adds emoji based on level (ℹ️ 📝 ✅ ⚠️ ❌)
- Creates audit trail of work done

**Usage during work:**
```bash
# After writing tests
uv run ai-log "Created test_validators.py with 6 tests"

# After implementation
uv run ai-log "Implemented validate_email() function"

# After quality checks
uv run ai-log "All quality checks pass" --level=success

# If error found
uv run ai-log "Coverage at 78%, need 2 more tests" --level=warning
```

### 3. ai-update-plan

**Update checkboxes in task plan to track progress.**

```bash
# Mark item as done
uv run ai-update-plan "Write test file(s)"

# Show current progress
uv run ai-update-plan --show

# Specific session
uv run ai-update-plan "Implement functionality" --session-id=20250102123045
```

**What it does:**
- Toggles checkbox for matching task item
- Shows updated progress (X/Y completed)
- Helps track which steps are done

**Standard plan items:**
- [ ] Write test file(s)
- [ ] Run tests (should fail initially)
- [ ] Implement functionality
- [ ] Run tests again (should pass)
- [ ] Run make check
- [ ] Update documentation if needed
- [ ] Review code changes

**Usage:**
```bash
# After writing tests
uv run ai-update-plan "Write test file(s)"

# See progress
uv run ai-update-plan --show
# Output: ✅ Progress: 1/7 completed
```

### 4. ai-context-summary

**Display current AI context and important information.**

```bash
# Quick summary
uv run ai-context-summary

# Detailed summary
uv run ai-context-summary --detailed
```

**What it shows:**

**Quick mode:**
- Last session summary (brief)
- Active tasks count
- Recent decisions count
- Conventions count

**Detailed mode:**
- Full last session summary
- All active tasks with timestamps
- All recent decisions (up to 10)
- All code conventions
- Session files location

**When to use:**
- Unsure what was done previously
- Need to check active tasks
- Want to see recent decisions
- Starting work after break

### 5. ai-check-conflicts

**Check if proposed task conflicts with active tasks.**

```bash
uv run ai-check-conflicts "Add email validation"
```

**What it does:**
- Reads `ACTIVE_TASKS.md`
- Uses fuzzy matching (70% similarity threshold)
- Warns if similar tasks exist
- Prevents duplicate work

**Output example:**
```
🔍 Checking for conflicts with: "Add email validation"

⚠️  Potential Conflicts Found:
────────────────────────
- "Add user validation" (Started: 2025-01-02 10:30)
  Similarity: 75%

Recommendation: Check if these tasks overlap before proceeding.
```

### 6. ai-add-decision

**Document an architectural or design decision.**

```bash
uv run ai-add-decision
```

**Interactive prompts:**
1. Decision title
2. Context/problem
3. Decision made
4. Rationale
5. Consequences

**What it does:**
- Adds entry to `RECENT_DECISIONS.md`
- Timestamps decision
- Shows decision to future AI agents

**Example:**
```markdown
## 2025-01-02: Use Pydantic for Data Validation

**Context**: Need robust validation for API inputs

**Decision**: Use Pydantic v2 for all data validation

**Rationale**:
- Type-safe validation
- Great error messages
- Widely adopted

**Consequences**:
- Add pydantic dependency
- All data models extend BaseModel
- Validation errors are consistent
```

**When to use:**
- Chose between architectural approaches
- Made library/framework decision
- Established pattern for future use
- Changed existing approach significantly

### 7. ai-add-convention

**Add or update code conventions.**

```bash
uv run ai-add-convention
```

**Interactive prompts:**
1. Convention category (existing or new)
2. Convention description

**What it does:**
- Adds to `CONVENTIONS.md`
- Organizes by category
- Shows conventions to future AI agents

**Example:**
```markdown
## Error Handling

- Always use custom exception classes
- Never use bare `except:` clauses
- Log errors before re-raising

## Naming Conventions

- Use snake_case for functions and variables
- Use PascalCase for classes
- Prefix private methods with underscore
```

**When to use:**
- Established new coding pattern
- Created reusable approach
- Want consistency across codebase
- Made style decision

### 8. ai-finish-task (REQUIRED LAST)

**Finalize session and update all context files.**

```bash
uv run ai-finish-task --summary="Implemented email validation with 100% test coverage"
```

**What it does:**
- Updates `LAST_SESSION_SUMMARY.md` with:
  - Task description
  - What was accomplished
  - Files changed
  - Coverage/quality metrics
  - Status
- Removes task from `ACTIVE_TASKS.md`
- Archives old session files (keeps last 10)
- Prepares context for next AI agent

**Options:**
```bash
# Required: summary of work done
uv run ai-finish-task --summary="Fixed validation bug, added 3 tests"

# Specific session
uv run ai-finish-task --summary="Done" --session-id=20250102123045
```

**Output example:**
```
╔══════════════════════════════════════════════════════════╗
║          ✅ Task Session Complete                        ║
╚══════════════════════════════════════════════════════════╝

📋 Task: Add user authentication feature
🆔 Session ID: 20250102123045
✅ Status: Complete

📝 Summary Updated:
   .ai-context/LAST_SESSION_SUMMARY.md

🗂️  Old Sessions Archived:
   - Kept last 10 sessions
   - Removed 3 older sessions

🎯 Active Tasks: 0
```

## 📋 Complete Workflow Example

```bash
# ═══════════════════════════════════════════════════════
# STEP 1: START SESSION (Required)
# ═══════════════════════════════════════════════════════
uv run ai-start-task "Add phone number validation"

# Output shows:
# - Last session summary
# - No conflicts
# - Recent decisions: "Use Pydantic for validation"
# - Convention: "Write tests first"

# ═══════════════════════════════════════════════════════
# STEP 2: WORK (Following TDD)
# ═══════════════════════════════════════════════════════

# Write tests first
uv run ai-log "Starting TDD workflow"
# ... create tests/test_validators.py ...
uv run ai-log "Created test_validators.py with 6 parametrized tests"
uv run ai-update-plan "Write test file(s)"

# Run tests (should fail)
make test
uv run ai-log "Tests fail as expected - function doesn't exist"
uv run ai-update-plan "Run tests (should fail initially)"

# Implement function
# ... create src/{{ package_name }}/validators.py ...
uv run ai-log "Implemented validate_phone() function"
uv run ai-update-plan "Implement functionality"

# Run tests (should pass)
make test
uv run ai-log "All 6 tests now pass" --level=success
uv run ai-update-plan "Run tests again (should pass)"

# Run quality checks
make check
uv run ai-log "make check passes - 100% coverage" --level=success
uv run ai-update-plan "Run make check"

# Check progress
uv run ai-update-plan --show
# Output: ✅ Progress: 5/7 completed

# Update docs (if needed)
uv run ai-update-plan "Update documentation if needed"

# Review changes
uv run ai-update-plan "Review code changes"

# ═══════════════════════════════════════════════════════
# STEP 3: FINISH SESSION (Required)
# ═══════════════════════════════════════════════════════
uv run ai-finish-task --summary="Added phone validation with 6 tests, 100% coverage, all quality checks pass"

# Updates:
# - LAST_SESSION_SUMMARY.md (for next AI)
# - ACTIVE_TASKS.md (removes task)
# - Archives old sessions
```

## ⚠️ Critical Rules

1. **ALWAYS** run `ai-start-task` before ANY work
2. **ALWAYS** run `ai-finish-task` when complete
3. **NEVER** skip `ai-log` for important milestones
4. **ALWAYS** check `ai-context-summary` if unsure what to do
5. **NEVER** start a task without checking for conflicts first

## 📂 Context Files Location

All context files are in `.ai-context/`:

### Tracked in Git (Shared Across Team)
- `REQUIRED_READING.md` - Master checklist for all AI agents
- `LAST_SESSION_SUMMARY.md` - Most recent session summary
- `ACTIVE_TASKS.md` - Tasks currently in progress
- `RECENT_DECISIONS.md` - Architectural decisions made
- `CONVENTIONS.md` - Code patterns and standards

### Local Only (Not Committed)
- `sessions/YYYYMMDDHHMMSS-PLAN-*.md` - Task plan
- `sessions/YYYYMMDDHHMMSS-SUMMARY-*.md` - Task summary
- `sessions/YYYYMMDDHHMMSS-EXECUTION-*.md` - Execution log

## 🎯 Why Use AI Tools?

1. **Context Continuity**: Next AI agent (even different tool) knows what you did
2. **No Duplicate Work**: Prevents starting tasks already in progress
3. **Decision Tracking**: Important architectural choices are documented
4. **Quality Assurance**: Ensures all workflow steps are followed
5. **Team Coordination**: Multiple developers can see what AI has done

## 🔄 Session Handoff

When an AI agent finishes and another starts:

**Agent 1 (finishing):**
```bash
uv run ai-finish-task --summary="Implemented feature X, added 10 tests, 95% coverage"
```

**Agent 2 (starting):**
```bash
uv run ai-start-task "Add feature Y"
```

**What Agent 2 sees:**
```
📊 Last Session Summary
────────────────────────
Agent: Claude Code
Task: Implemented feature X
What was done:
- Added 10 tests
- 95% coverage
- All quality checks pass
Files changed:
- src/module.py
- tests/test_module.py
Status: ✅ Complete
```

This ensures perfect handoff between different AI tools!

## 🆘 Troubleshooting

### "Session not found"
```bash
# List available sessions
ls .ai-context/sessions/

# Specify session ID manually
uv run ai-log "Message" --session-id=20250102123045
```

### "No active session"
```bash
# Start a new session first
uv run ai-start-task "Your task"
```

### "Can't update plan - item not found"
```bash
# Show plan to see exact wording
uv run ai-update-plan --show

# Use exact text from plan
uv run ai-update-plan "Exact item text from plan"
```

---

**Remember**: Session management is mandatory. Start with `ai-start-task`, finish with `ai-finish-task`, log progress throughout.
