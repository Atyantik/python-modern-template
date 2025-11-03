# Task Plan: {{task_name}}

**Session ID**: {{session_id}}
**Created**: {{timestamp}}
**Task Type**: bugfix
**Status**: 🚧 In Progress

---

## Objective

[Describe the bug and expected fix]

---

## Context

**Recent Decisions**:
See RECENT_DECISIONS.md for latest decisions to follow.

**Related Conventions**:
See CONVENTIONS.md for coding standards.

**Dependencies**:
- [ ] None identified yet

---

## Implementation Steps

### Phase 1: Reproduce Bug
- [ ] Understand bug report and symptoms
- [ ] Identify steps to reproduce
- [ ] Reproduce bug locally
- [ ] Document current (incorrect) behavior

### Phase 2: Write Regression Test
- [ ] Write test that fails due to bug
- [ ] Verify test reproduces the issue
- [ ] Document expected (correct) behavior

### Phase 3: Fix Implementation
- [ ] Identify root cause of bug
- [ ] Implement minimal fix
- [ ] Run regression test - should pass
- [ ] Verify fix doesn't break other tests

### Phase 4: Verify Fix
- [ ] Test all related functionality
- [ ] Check for similar bugs elsewhere
- [ ] Verify 80%+ coverage maintained
- [ ] Manual testing if applicable

### Phase 5: Quality Checks
- [ ] Run `make format`
- [ ] Run `make lint`
- [ ] Run `make test`
- [ ] Fix any issues found
- [ ] Run `make check` - all pass

---

## Files to Change

- [ ] `src/` - Bug fix implementation
- [ ] `tests/` - Regression test

---

## Risks & Considerations

- Could this fix break other functionality?
- Are there similar bugs in related code?

---

## Notes

[Track root cause analysis, decisions, blockers as you work]

<!--
CUSTOMIZATION REMINDER:
After creating this plan, use `ai-update-plan` to:
- Add specific reproduction steps: `ai-update-plan --add "Reproduce with: <steps>"`
- Document root cause: `ai-update-plan --add-note "Root cause: ..." --section="Notes"`
- Add affected files: `ai-update-plan --add "Fix src/specific/file.py"`
-->
