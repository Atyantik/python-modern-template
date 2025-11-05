# Task Plan: {{task_name}}

**Session ID**: {{session_id}}
**Created**: {{timestamp}}
**Task Type**: refactor
**Status**: 🚧 In Progress

---

## Objective

[Describe what needs to be refactored and why]

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

### Phase 1: Ensure Test Coverage
- [ ] Review existing tests for code to refactor
- [ ] Ensure 80%+ coverage before starting
- [ ] Add missing tests if needed
- [ ] Run tests to establish baseline

### Phase 2: Refactor Code
- [ ] Apply refactoring incrementally
- [ ] Run tests after each change
- [ ] Maintain or improve code quality
- [ ] Follow DRY and SOLID principles

### Phase 3: Verify Tests Pass
- [ ] Run full test suite
- [ ] Verify all tests still pass
- [ ] Check coverage hasn't decreased
- [ ] Verify behavior unchanged

### Phase 4: Quality Checks
- [ ] Run `make format`
- [ ] Run `make lint`
- [ ] Run `make test`
- [ ] Fix any issues found
- [ ] Run `make check` - all pass

---

## Files to Change

- [ ] `src/` - Files being refactored
- [ ] `tests/` - Update tests if needed

---

## Risks & Considerations

- Will refactoring break existing functionality?
- Is test coverage sufficient to catch regressions?

---

## Notes

[Track refactoring decisions, patterns applied as you work]

<!--
CUSTOMIZATION REMINDER:
After creating this plan, use `ai-update-plan` to:
- Add specific refactoring goals: `ai-update-plan --add "Extract duplicate validation logic"`
- Document patterns: `ai-update-plan --add-note "Using Strategy pattern" --section="Notes"`
- Add affected components: `ai-update-plan --add "Refactor src/validators.py"`
-->
