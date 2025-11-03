# Task Plan: {{task_name}}

**Session ID**: {{session_id}}
**Created**: {{timestamp}}
**Task Type**: docs
**Status**: 🚧 In Progress

---

## Objective

[Describe what documentation needs to be updated or created]

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

### Phase 1: Review Current Docs
- [ ] Review existing documentation
- [ ] Identify outdated or missing content
- [ ] Check for broken links or examples
- [ ] Note user pain points or confusion

### Phase 2: Update Documentation
- [ ] Update or create markdown files
- [ ] Add code examples where helpful
- [ ] Update docstrings if needed
- [ ] Ensure examples are accurate

### Phase 3: Verify Examples
- [ ] Test all code examples work
- [ ] Verify links are not broken
- [ ] Check formatting renders correctly
- [ ] Ensure clarity and completeness

### Phase 4: Quality Checks
- [ ] Run `make format` (if code examples)
- [ ] Run `make lint` (if code changes)
- [ ] Spell check documentation
- [ ] Review for clarity and accuracy

---

## Files to Change

- [ ] `README.md` - Main documentation
- [ ] `AI_DOCS/` - AI agent documentation
- [ ] `docs/` - Detailed documentation
- [ ] Docstrings in code (if applicable)

---

## Risks & Considerations

- Will users understand the updated docs?
- Are examples complete and working?

---

## Notes

[Track documentation decisions, user feedback as you work]

<!--
CUSTOMIZATION REMINDER:
After creating this plan, use `ai-update-plan` to:
- Add specific sections: `ai-update-plan --add "Update Installation section"`
- Remove irrelevant items: `ai-update-plan --remove "Update docstrings"` (if not needed)
- Add specific files: `ai-update-plan --add "Update AI_DOCS/api-reference.md"`
-->
