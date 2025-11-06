# AI Documentation Synchronization Rules

**Golden Rule: When ANY AI documentation changes, ALL AI agents must be synchronized.**

This document defines the mandatory synchronization requirements for maintaining consistency across all AI coding assistant configurations.

---

## Overview

This project supports **7 AI agents** across **multiple documentation locations**:

### AI Agents
1. **Claude Code** - CLAUDE.md + .claude/
2. **Cursor IDE** - .cursorrules
3. **Aider AI** - .aider.conf.yml
4. **Gemini CLI** - GEMINI.md (root file for terminal usage)
5. **Gemini Code Assist** - .gemini/styleguide.md (IDE/GitHub integration)
6. **GitHub Copilot** - .github/copilot-instructions.md
7. **Universal** - AGENTS.md

### Documentation Locations
- **Shared docs**: `AI_DOCS/*.md` (single source of truth)
- **Agent configs**: Root-level config files
- **Claude automation**: `.claude/skills/` and `.claude/agents/`
- **Templates**: `template/AI_DOCS/*.md.jinja`

---

## Synchronization Matrix

| AI Agent | Config File(s) | Supports References | Sync Method |
|----------|---------------|---------------------|-------------|
| Claude Code | `CLAUDE.md` | ✅ Yes (`@AI_DOCS/`) | Auto-reference |
| Cursor IDE | `.cursorrules` | ✅ Yes (`@AI_DOCS/`) | Auto-reference |
| Aider AI | `.aider.conf.yml` | ✅ Yes (YAML `read:`) | Auto-reference |
| Universal | `AGENTS.md` | ✅ Yes (`@AI_DOCS/`) | Auto-reference |
| Gemini CLI | `GEMINI.md` | ✅ Partial (file references) | Manual reference |
| Gemini Code Assist | `.gemini/styleguide.md` | ❌ No | Manual duplicate + warning |
| GitHub Copilot | `.github/copilot-instructions.md` | ❌ No | Manual duplicate + warning |

---

## Mandatory Synchronization Checklist

**BEFORE completing ANY task that modifies documentation:**

### Step 1: Identify Changed Documentation

Check if changes affect:
- [ ] `AI_DOCS/*.md` (shared documentation)
- [ ] `CLAUDE.md` (Claude Code)
- [ ] `.cursorrules` (Cursor IDE)
- [ ] `.aider.conf.yml` (Aider AI)
- [ ] `AGENTS.md` (universal)
- [ ] `GEMINI.md` (Gemini CLI)
- [ ] `.gemini/styleguide.md` (Gemini Code Assist)
- [ ] `.github/copilot-instructions.md` (GitHub Copilot)
- [ ] `.claude/skills/*/SKILL.md` (Claude skills)
- [ ] `.claude/agents/*.md` (Claude agents)

### Step 2: Validate Reference-Supporting Agents

For agents that **support references** (Claude, Cursor, Aider, AGENTS.md, Gemini CLI):

- [ ] Verify all `@AI_DOCS/filename.md` references exist
- [ ] Check YAML `read:` entries in `.aider.conf.yml`
- [ ] Check file references in `GEMINI.md` point to existing files
- [ ] Ensure references point to correct files
- [ ] Validate no broken references

**Script:** `uv run ai-validate-docs`

### Step 3: Update Manual Reference Files

For files that **need manual updates** (GEMINI.md, .gemini/styleguide.md, Copilot):

**IF shared docs changed:**
- [ ] Update `GEMINI.md` file references if structure changed
- [ ] Update `.gemini/styleguide.md` with essential excerpts
- [ ] Update `.github/copilot-instructions.md` with essential excerpts
- [ ] Add/update sync warning comments at top of file
- [ ] Keep content minimal - only critical excerpts
- [ ] Reference full docs for complete information

**Sync Warning Format:**
```markdown
<!-- ⚠️ SYNC WARNING: This file duplicates content from AI_DOCS/*.md -->
<!-- When AI_DOCS changes, update essential excerpts here manually -->
<!-- Last synced: YYYY-MM-DD -->
<!-- Changes: Brief description of what was updated -->
```

### Step 4: Update Claude Skills/Agents

**IF changes affect skills or agent workflows:**

- [ ] Review `.claude/skills/*/SKILL.md` for outdated information
- [ ] Review `.claude/agents/*.md` for outdated instructions
- [ ] Update skill descriptions if capabilities changed
- [ ] Update agent instructions if process changed
- [ ] Keep skill/agent docs aligned with `AI_DOCS/ai-skills.md`

**Example scenarios:**
- New quality tool added → Update `quality-fixer` skill
- TDD workflow changed → Update `tdd-reviewer` agent
- New AI tool added → Update `session-template` skill

### Step 5: Update Template Files

**IF changes should apply to new projects:**

- [ ] Update `template/AI_DOCS/*.md.jinja` files
- [ ] Add template variables where needed (e.g., `{{project_name}}`)
- [ ] Test template rendering with `copier copy`
- [ ] Ensure template variables are properly substituted

### Step 6: Validate Synchronization

**Run validation script:**
```bash
uv run ai-validate-docs
```

**Should report:**
- ✅ All references exist
- ✅ No broken links
- ✅ Template files match source files
- ⚠️ Manual sync files have recent sync date (if applicable)

### Step 7: Document Changes

**Update this checklist:**
- [ ] If new AI agent added, update synchronization matrix
- [ ] If new doc location added, update checklist
- [ ] If sync process changed, update instructions

---

## Synchronization Workflows

### Workflow 1: Updating Shared Documentation (AI_DOCS/*.md)

**Scenario:** Changed `AI_DOCS/tdd-workflow.md`

**Steps:**
1. ✅ Update `AI_DOCS/tdd-workflow.md`
2. ✅ No action needed for Claude, Cursor, Aider, Gemini/AGENTS.md (auto-reference)
3. ⚠️ Review `.gemini/styleguide.md` - update if critical excerpts changed
4. ⚠️ Review `.github/copilot-instructions.md` - update if critical excerpts changed
5. ✅ Update sync warning comment dates if duplicated
6. ✅ Update `template/AI_DOCS/tdd-workflow.md.jinja` with same changes
7. ✅ Run validation script
8. ✅ Commit with message: `docs: update TDD workflow and sync all agents`

### Workflow 2: Adding New Shared Documentation

**Scenario:** Created `AI_DOCS/new-feature.md`

**Steps:**
1. ✅ Create `AI_DOCS/new-feature.md`
2. ✅ Add reference to `CLAUDE.md`: `- @AI_DOCS/new-feature.md`
3. ✅ Add reference to `.cursorrules`: `@AI_DOCS/new-feature.md`
4. ✅ Add to `.aider.conf.yml` `read:` list: `- AI_DOCS/new-feature.md`
5. ✅ Add reference to `AGENTS.md`
6. ⚠️ Evaluate if `.gemini/styleguide.md` needs excerpt
7. ⚠️ Evaluate if `.github/copilot-instructions.md` needs excerpt
8. ✅ Update `AI_DOCS/README.md` index
9. ✅ Create `template/AI_DOCS/new-feature.md.jinja`
10. ✅ Run validation script
11. ✅ Commit

### Workflow 3: Updating Claude Skills/Agents

**Scenario:** Enhanced quality-fixer skill

**Steps:**
1. ✅ Update `.claude/skills/quality-fixer/SKILL.md`
2. ✅ Update `AI_DOCS/ai-skills.md` with new capabilities
3. ✅ No action for other agents (they reference ai-skills.md)
4. ✅ Update template if applicable
5. ✅ Run validation script
6. ✅ Commit

### Workflow 4: Agent-Specific Changes

**Scenario:** Updated Cursor-specific keyboard shortcuts in `.cursorrules`

**Steps:**
1. ✅ Update `.cursorrules` agent-specific section
2. ✅ No action for other agents (tool-specific)
3. ✅ Don't update shared docs (not universal)
4. ✅ Commit with message: `config: update Cursor keyboard shortcuts`

---

## Validation Script

**Location:** `scripts/ai_tools/validate_ai_docs_sync.py`

**What it checks:**
1. All `@AI_DOCS/` references point to existing files
2. All YAML `read:` entries point to existing files
3. Template files match source files
4. No duplicate content in reference-supporting agent configs
5. Manual sync files have recent sync date warnings

**Usage:**
```bash
# Run validation
uv run ai-validate-docs

# Expected output (all passing):
✅ All AI_DOCS files found
✅ All @AI_DOCS references valid
✅ All YAML read: entries valid
✅ Template files in sync
⚠️ Manual sync files checked (warnings for stale dates)

# Exit code 0 = success, 1 = failures found
```

**Run automatically:**
- Before `ai-finish-task` completes
- In pre-commit hooks (optional)
- In CI/CD pipeline

---

## Template Synchronization Script

**Location:** `sync_template.py` (root directory)

**Purpose:** Automated synchronization of source files to Copier template with Jinja variable replacement.

**What it syncs:**
- Quality tests (5 files): `tests/quality/*.py` → `template/tests/quality/*.py.jinja`
- Project tests (4 files): `tests/test_*.py` → `template/tests/test_*.py.jinja`
- Quality scripts (6 files): `scripts/quality/*.py` → `template/scripts/quality/*.py.jinja`
- AI tools scripts (12 files): `scripts/ai_tools/*.py` → `template/scripts/ai_tools/*.py.jinja`

**Note:** AI tools tests are NOT synced to the template. They remain in the template repository only, as they test template infrastructure that users typically won't modify.

**Jinja variable replacement:**
- `python_modern_template` → `{{ package_name }}`
- `python-modern-template` → `{{ project_name }}`

**Usage:**
```bash
# Run template sync
python sync_template.py

# Expected output:
# ✅ SYNC COMPLETE: 34 files synced
```

**When to run:**
1. After modifying any test files in `tests/`
2. After modifying any scripts in `scripts/quality/` or `scripts/ai_tools/`
3. Before releasing a new template version

**What it doesn't sync (intentionally):**
- AI_DOCS/*.md files (already synced via separate workflow)
- Project-specific configuration files
- Git hooks and CI/CD workflows
- Template-specific Jinja files

**Verification after sync:**
```bash
# Generate a test project
copier copy --trust --defaults . /tmp/test_project

# Verify quality checks pass
cd /tmp/test_project
make check
```

**Expected results:**
- ✅ Formatting passes
- ✅ Linting passes (mypy, ruff, pylint)
- ⚠️ Some tests may fail (project-specific paths like `.claude/skills/session-template/templates/`)
  - These failures are expected for generated projects
  - Source project should still pass all tests (200/200)

**Integration with quality gates:**
- Add to checklist: "Run `python sync_template.py` if modified tests or scripts"
- Verify generated projects pass linting and formatting
- Document any expected test failures in template README

---

## Quality Gate Integration

This synchronization check is **MANDATORY** before completing any task.

### Added to Quality Checklist

In `AI_DOCS/code-conventions.md` and all agent configs, add:

**Quality Gates Checklist:**
- [ ] Tests written BEFORE implementation (TDD)
- [ ] Tests initially failed (verified red phase)
- [ ] Implementation makes tests pass (green phase)
- [ ] Type hints on all functions
- [ ] Docstrings on public functions
- [ ] `make test` passes
- [ ] Coverage ≥ 80%
- [ ] `make format` passes
- [ ] `make lint` passes
- [ ] `make check` passes
- [ ] **AI documentation synchronized** ⭐ NEW
  - [ ] Validated with `uv run ai-validate-docs`
  - [ ] Updated manual sync files if needed
  - [ ] Updated .claude/skills or .claude/agents if needed
  - [ ] Updated template files if needed

### Integration with ai-finish-task

Before `ai-finish-task` completes, it should:
1. Run `uv run ai-validate-docs`
2. If validation fails, prompt to fix or continue with `--yes`
3. Log validation results to EXECUTION file

---

## File Structure Reference

```
project/
├── AI_DOCS/                           # Shared documentation (source of truth)
│   ├── README.md                      # Documentation index
│   ├── ai-tools.md                    # Session management
│   ├── ai-skills.md                   # Skills and agents
│   ├── tdd-workflow.md                # TDD process
│   ├── code-conventions.md            # Code standards
│   ├── project-context.md             # Tech stack
│   ├── documentation-first-approach.md # Documentation discovery workflow
│   └── documentation-sync-rules.md    # This file
│
├── AGENTS.md                          # Universal AI agent config (supports @AI_DOCS)
├── CLAUDE.md                          # Claude Code config (supports @AI_DOCS)
├── GEMINI.md                          # Gemini CLI config (file references)
├── .cursorrules                       # Cursor IDE config (supports @AI_DOCS)
├── .aider.conf.yml                    # Aider AI config (YAML read:)
│
├── .gemini/
│   └── styleguide.md                  # Gemini Code Assist (manual sync + warning)
│
├── .github/
│   └── copilot-instructions.md        # GitHub Copilot (manual sync + warning)
│
├── .claude/
│   ├── skills/                        # Claude Code skills (automated)
│   │   ├── coverage-analyzer/SKILL.md
│   │   ├── quality-fixer/SKILL.md
│   │   ├── test-generator/SKILL.md
│   │   └── session-template/SKILL.md
│   └── agents/                        # Claude Code agents (automated)
│       ├── tdd-reviewer.md
│       └── quality-enforcer.md
│
├── template/                          # Copier templates for new projects
│   ├── AI_DOCS/
│   │   ├── ai-tools.md.jinja
│   │   ├── ai-skills.md.jinja
│   │   ├── tdd-workflow.md.jinja
│   │   ├── code-conventions.md.jinja
│   │   ├── project-context.md.jinja
│   │   ├── documentation-first-approach.md.jinja
│   │   └── documentation-sync-rules.md.jinja
│   ├── GEMINI.md.jinja                # Gemini CLI template
│   └── .gemini/
│       └── styleguide.md.jinja        # Gemini Code Assist template
│
└── scripts/ai_tools/
    └── validate_ai_docs_sync.py       # Validation script (CLI: ai-validate-docs)
```

---

## Common Mistakes to Avoid

### ❌ Don't Do This

1. **Update AI_DOCS without checking agents**
   ```bash
   # Wrong: Only update shared docs
   vim AI_DOCS/tdd-workflow.md
   git commit -m "Updated TDD workflow"
   # Missing: Sync to Gemini/Copilot, validate, update templates
   ```

2. **Duplicate content in reference-supporting agents**
   ```markdown
   <!-- Wrong in CLAUDE.md -->
   ## TDD Workflow
   [Full TDD workflow duplicated here - 500 lines]

   <!-- Correct -->
   ## TDD Workflow
   See @AI_DOCS/tdd-workflow.md for complete TDD process.
   ```

3. **Forget template files**
   ```bash
   # Wrong: Update source but not template
   vim AI_DOCS/code-conventions.md
   # Missing: template/AI_DOCS/code-conventions.md.jinja
   ```

4. **Stale manual sync files**
   ```markdown
   <!-- Wrong in .gemini/styleguide.md -->
   <!-- Last synced: 2024-01-01 -->
   <!-- Actual AI_DOCS changed 6 months ago! -->
   ```

### ✅ Do This Instead

1. **Use the validation script**
   ```bash
   # After any doc change
   uv run ai-validate-docs
   ```

2. **Reference, don't duplicate**
   ```markdown
   <!-- Correct -->
   See @AI_DOCS/tdd-workflow.md for complete TDD process.
   ```

3. **Keep manual sync files minimal**
   ```markdown
   <!-- Correct in .gemini/styleguide.md -->
   ## TDD (Essential Excerpt)

   Write tests FIRST, always.

   For complete TDD workflow, see AI_DOCS/tdd-workflow.md

   <!-- Last synced: 2025-11-03 -->
   ```

4. **Update templates together**
   ```bash
   # Correct: Update both
   vim AI_DOCS/code-conventions.md
   vim template/AI_DOCS/code-conventions.md.jinja
   uv run ai-validate-docs
   ```

---

## Summary

**The Golden Rule:** When ANY AI documentation changes, ALL AI agents must be synchronized.

**Quick Checklist:**
1. ✅ Update the changed file
2. ✅ Run `uv run ai-validate-docs`
3. ⚠️ Update manual sync files if needed (Gemini/Copilot)
4. ✅ Update .claude/skills or .claude/agents if relevant
5. ✅ Update template files
6. ✅ Commit with descriptive message

**Remember:** This is not optional. It's a **mandatory quality gate** to ensure all AI agents have consistent, up-to-date information.

---

**Last updated:** 2025-11-03
**Version:** 1.0
**Maintained by:** All AI coding assistants working on this project
