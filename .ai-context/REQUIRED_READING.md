# AI Agent Pre-Task Checklist

> **MANDATORY**: Read this file and all referenced files BEFORE starting ANY task!

## Purpose

This checklist ensures every AI agent (Cursor, Claude, Gemini, Copilot, Aider) has the necessary context before executing tasks. It prevents:
- ❌ Duplicate work
- ❌ Conflicting implementations
- ❌ Ignoring established patterns
- ❌ Breaking recent decisions

## 🚨 BEFORE Starting ANY Task

### Phase 1: Read Context Files (In This Order)

- [ ] **Step 1**: Read `.ai-context/LAST_SESSION_SUMMARY.md`
  - What was done in the last session
  - Who worked on it
  - What files were changed
  - Important notes for the next AI

- [ ] **Step 2**: Read `.ai-context/ACTIVE_TASKS.md`
  - What tasks are currently in progress
  - What tasks are blocked
  - What tasks are queued
  - Check if your task conflicts with active work

- [ ] **Step 3**: Read `.ai-context/RECENT_DECISIONS.md`
  - Architectural decisions made recently
  - Design patterns chosen
  - Technologies selected
  - Standards established

- [ ] **Step 4**: Read `.ai-context/CONVENTIONS.md`
  - Project-specific naming conventions
  - Code patterns to follow
  - File organization rules
  - Testing patterns

- [ ] **Step 5**: Read Last 5 Session Summaries
  - Check `.ai-context/sessions/` for recent SUMMARY files
  - Understand the trajectory of recent work
  - Identify related tasks
  - Learn from recent successes/issues

### Phase 2: Create Session Files

After reading context, create your session tracking files:

```bash
# This will create timestamped PLAN, SUMMARY, and EXECUTION files
make new-session --name="your-task-description"
```

This creates:
- `YYYYMMDDHHMMSS-PLAN-your-task.md` - Your task breakdown
- `YYYYMMDDHHMMSS-SUMMARY-your-task.md` - What you accomplished
- `YYYYMMDDHHMMSS-EXECUTION-your-task.md` - Real-time log

### Phase 3: Fill Out Your PLAN

In your newly created PLAN file:
1. **Reference relevant decisions** from RECENT_DECISIONS.md
2. **Note related tasks** from ACTIVE_TASKS.md
3. **Follow conventions** from CONVENTIONS.md
4. **Break down task** into testable chunks (TDD)
5. **List files to modify**

### Phase 4: Execute Task (Following TDD)

1. Write tests FIRST (mandatory)
2. Log progress to EXECUTION file
3. Update PLAN checkboxes as you complete items
4. Run `make check` before marking complete
5. Maintain 80%+ code coverage

### Phase 5: Update Context on Completion

When task is complete, you MUST update:

1. **SUMMARY file**: Finalize what you did
2. **LAST_SESSION_SUMMARY.md**: Update with your session info
3. **ACTIVE_TASKS.md**:
   - Remove your task if completed
   - Add follow-up tasks if needed
4. **RECENT_DECISIONS.md**: Add any important decisions you made
5. **CONVENTIONS.md**: Add any new patterns you established
6. **Archive old sessions**: `make archive-sessions` (keeps last 5)

## 📋 Quick Checklist

Before starting:
- [ ] Read LAST_SESSION_SUMMARY.md
- [ ] Read ACTIVE_TASKS.md
- [ ] Read RECENT_DECISIONS.md
- [ ] Read CONVENTIONS.md
- [ ] Read last 5 session summaries
- [ ] Create session files (`make new-session`)
- [ ] Fill out PLAN with context references

During execution:
- [ ] Follow TDD (tests first)
- [ ] Log to EXECUTION file
- [ ] Update PLAN checkboxes
- [ ] Run `make check` frequently

After completion:
- [ ] Finalize SUMMARY file
- [ ] Update LAST_SESSION_SUMMARY.md
- [ ] Update ACTIVE_TASKS.md
- [ ] Add to RECENT_DECISIONS.md (if applicable)
- [ ] Add to CONVENTIONS.md (if applicable)
- [ ] Archive old sessions (`make archive-sessions`)

## 🔍 Example Workflow

```
User: "Add user authentication"

AI Agent (following this checklist):
1. ✅ Read LAST_SESSION_SUMMARY.md
   - Last task: Added email validation
   - No conflicts with my task

2. ✅ Read ACTIVE_TASKS.md
   - Nothing in progress
   - No blockers

3. ✅ Read RECENT_DECISIONS.md
   - Decision: "Tests must be written first (TDD)"
   - Decision: "80% minimum coverage required"
   - Decision: "Use type hints everywhere"

4. ✅ Read CONVENTIONS.md
   - Convention: "Test files mirror src/ structure"
   - Convention: "Use pytest fixtures in conftest.py"
   - Convention: "Import from package, not src prefix"

5. ✅ Read last 5 sessions
   - Pattern: Write 4-6 test cases minimum
   - Pattern: Use parametrize for similar tests
   - Note: Previous work had good coverage

6. ✅ Create session: make new-session --name="add-user-authentication"

7. ✅ Fill PLAN:
   - Reference RECENT_DECISIONS (TDD requirement)
   - Follow CONVENTIONS (test structure)
   - Break into testable chunks

8. ✅ Execute with TDD
   - Write tests first
   - Log to EXECUTION file
   - Update PLAN checkboxes

9. ✅ Complete & Update:
   - Finalize SUMMARY
   - Update LAST_SESSION_SUMMARY.md
   - Add to RECENT_DECISIONS.md: "Auth: JWT tokens in headers"
   - Add to CONVENTIONS.md: "Auth decorator pattern"
   - Archive old sessions
```

## 🚨 What Happens If You Skip This?

- ❌ You might duplicate work someone else just did
- ❌ You might violate a decision that was just made
- ❌ You might use patterns that were just deprecated
- ❌ You might break someone's in-progress work
- ❌ Next AI won't know what you did
- ❌ Knowledge is lost across sessions

## ✅ Benefits of Following This

- ✅ Continuity across different AI agents
- ✅ Shared knowledge base
- ✅ Consistent patterns and decisions
- ✅ Historical audit trail
- ✅ Easy handoffs between AI sessions
- ✅ No duplicate or conflicting work

## 📚 File Locations

```
.ai-context/
├── REQUIRED_READING.md        ← You are here
├── LAST_SESSION_SUMMARY.md    ← Read this first
├── ACTIVE_TASKS.md             ← Check for conflicts
├── RECENT_DECISIONS.md         ← Follow these
├── CONVENTIONS.md              ← Use these patterns
└── sessions/                   ← Review recent work
    ├── 20251102143045-PLAN-*.md
    ├── 20251102143045-SUMMARY-*.md
    └── 20251102143045-EXECUTION-*.md
```

## 🎯 Your Responsibility

As an AI agent, you are responsible for:
1. **Reading** all context before starting
2. **Creating** session files for your work
3. **Following** established decisions and conventions
4. **Updating** context for the next AI
5. **Maintaining** the knowledge base

This ensures smooth collaboration across AI agents and sessions!

---

**Last Updated**: 2025-11-02
**System**: AI Context Loading v1.0
