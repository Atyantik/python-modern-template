# Task Plan: {{task_name}}

**Session ID**: {{session_id}}
**Created**: {{timestamp}}
**Task Type**: feature
**Status**: 🚧 In Progress

---

## Objective

[Describe what needs to be accomplished]

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

### Phase 1: Research & Design
- [ ] Understand requirements thoroughly
- [ ] Review related code and patterns
- [ ] Identify affected components
- [ ] Design approach and architecture

### Phase 2: Write Tests (TDD)
- [ ] Identify test scenarios and edge cases
- [ ] Write test file(s)
- [ ] Run tests to confirm they fail

### Phase 3: Implementation
- [ ] Implement core functionality
- [ ] Run tests to confirm they pass
- [ ] Verify 80%+ coverage
- [ ] Handle edge cases and error conditions

### Phase 4: Quality Checks
- [ ] Run `make format`
- [ ] Run `make lint`
- [ ] Run `make test`
- [ ] Fix any issues found
- [ ] Run `make check` - all pass

### Phase 5: Documentation
- [ ] Update docstrings
- [ ] Add type hints to all functions
- [ ] Update README if user-facing change
- [ ] Add inline comments for complex logic

---

## Files to Change

- [ ] `src/` - Implementation files
- [ ] `tests/` - Test files
- [ ] `README.md` - If user-facing feature

---

## Risks & Considerations

- None identified yet

---

## Notes

[Track decisions, blockers, questions as you work]

<!--
CUSTOMIZATION REMINDER:
After creating this plan, use `ai-update-plan` to:
- Add task-specific steps: `ai-update-plan --add "Your specific step"`
- Remove irrelevant items: `ai-update-plan --remove "Irrelevant item"`
- Rename generic descriptions: `ai-update-plan --rename "Old" --to "Specific description"`
- Add notes about approach: `ai-update-plan --add-note "Your note" --section="Notes"`
-->
