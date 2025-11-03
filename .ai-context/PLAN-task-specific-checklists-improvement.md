# Execution Plan: Task-Specific Checklists with Dynamic Editing

**Status**: Draft for Review
**Created**: 2025-11-03
**Author**: AI Analysis based on user feedback

---

## Problem Statement

### Current Limitations

1. **Generic Plans**: All tasks get the same hardcoded 17-item TDD checklist
   - Documentation tasks include "Write tests" (not applicable)
   - Simple bugs include all 4 phases (overkill)
   - Complex features lack specific customization

2. **No Plan Editing**: Once `ai-start-task` creates a plan:
   - Cannot add task-specific steps
   - Cannot remove irrelevant steps
   - Cannot update descriptions as understanding evolves
   - Cannot adapt based on discoveries during work

3. **No Task Type Differentiation**:
   - Task types (feature, bugfix, docs, refactor) exist but unused
   - All get identical checklist regardless of type
   - Missed opportunity for specialized templates

4. **Value Gap**:
   - Plans become obsolete quickly
   - Real work deviates from generic template
   - Mechanical checkbox completion without real tracking value
   - AI agents can't customize to actual task needs

### User's Core Observation

> "After creating plan, there is no way to update the description or the checklist... which then does not add any value!"

This is correct. The system needs dynamic plan management, not static templates.

---

## Proposed Solution: Dynamic Task-Specific Plans

### Core Improvements

1. **Task-Specific Templates** - Different base templates per task type
2. **Dynamic Plan Editing** - New commands to modify plans during work
3. **AI-Driven Customization** - AI agents can adapt plans intelligently
4. **Plan Validation** - Ensure plans match actual work completed

---

## Detailed Design

### 1. Task-Specific Templates

#### Current: One Generic Template
```python
def get_plan_template(session_id, task_name, task_type):
    # Always returns same 17-item TDD template
    # Ignores task_type parameter
```

#### Proposed: Type-Specific Templates

**Template Structure**:
```python
TASK_TEMPLATES = {
    "feature": {
        "phases": [
            "Research & Design",
            "Write Tests (TDD)",
            "Implementation",
            "Quality Checks",
            "Documentation"
        ],
        "base_items": [...],  # Feature-specific checklist
        "optional_sections": ["Performance Testing", "Integration Tests"]
    },

    "bugfix": {
        "phases": [
            "Reproduce Bug",
            "Write Regression Test",
            "Fix Implementation",
            "Verify Fix",
            "Quality Checks"
        ],
        "base_items": [...],  # Bugfix-specific
        "optional_sections": ["Root Cause Analysis"]
    },

    "docs": {
        "phases": [
            "Review Current Docs",
            "Update Documentation",
            "Verify Examples",
            "Quality Checks"
        ],
        "base_items": [...],  # No testing phase
        "optional_sections": ["Add Diagrams", "Update README"]
    },

    "refactor": {
        "phases": [
            "Ensure Test Coverage",
            "Refactor Code",
            "Verify Tests Pass",
            "Quality Checks"
        ],
        "base_items": [...],  # Refactor-specific
        "optional_sections": ["Performance Benchmarks"]
    }
}
```

**Benefits**:
- Each task type gets relevant checklist
- No irrelevant items (docs tasks won't have "Write tests")
- Better initial plan that matches task type

### 2. Extended Plan Management (Enhanced `ai-update-plan`)

#### Approach: Extend Existing Command

**Decision**: Extend `ai-update-plan` rather than create separate `ai-edit-plan` command.

**Benefits**:
- Single command for all plan operations
- No new command to learn
- Natural evolution of existing tool
- Maintains workflow continuity

**Backward Compatibility**:
- All existing functionality preserved
- Old behavior: `ai-update-plan "item"` checks/unchecks (UNCHANGED)
- New behavior: Additional flags for editing operations
- If no editing flags, uses original checkbox toggle behavior

#### Enhanced `ai-update-plan` Capabilities

**Existing Functionality (Preserved)**:
```bash
# Check/uncheck items (EXISTING - unchanged)
uv run ai-update-plan "Write test file(s)"
uv run ai-update-plan "Run tests" --uncheck
uv run ai-update-plan --show
```

**New Editing Functionality (Added)**:
```bash
# Add new checklist items
uv run ai-update-plan --add "Benchmark memory usage"
uv run ai-update-plan --add "Setup test database" --phase="Phase 1"

# Remove items
uv run ai-update-plan --remove "Update README"

# Rename/update item descriptions
uv run ai-update-plan --rename "Run tests" --to "Run tests with verbose output"

# Add custom phase
uv run ai-update-plan --add-phase "Deployment Preparation"

# Add note to specific section
uv run ai-update-plan --add-note "Database migration required" --section="Risks"

# Interactive mode for complex edits
uv run ai-update-plan --interactive

# List all editing operations
uv run ai-update-plan --help-edit
```

#### Implementation Strategy

**Backward Compatible API**:
```python
# scripts/ai_tools/update_plan.py (ENHANCED)

def update_plan(
    # Existing parameters (PRESERVED)
    item: str | None = None,
    check: bool = True,
    uncheck: bool = False,
    show: bool = False,
    session_id: str | None = None,

    # New parameters (ADDED)
    add: str | None = None,
    remove: str | None = None,
    rename: str | None = None,
    to: str | None = None,
    add_phase: str | None = None,
    add_note: str | None = None,
    section: str | None = None,
    phase: str | None = None,
    interactive: bool = False,
    list_phases: bool = False,
) -> None:
    """Update plan: check items OR edit plan structure.

    Modes of operation:
    1. Checkbox mode (default): Check/uncheck items
    2. Edit mode: Add/remove/rename items and phases

    Args:
        item: Item to check/uncheck (checkbox mode)
        check: Check the box (checkbox mode)
        uncheck: Uncheck the box (checkbox mode)
        show: Show current plan with progress (both modes)
        session_id: Session ID (default: most recent)

        add: Add new checklist item (edit mode)
        remove: Remove checklist item (edit mode)
        rename: Rename existing item (edit mode)
        to: New name for renamed item (edit mode)
        add_phase: Add new phase section (edit mode)
        add_note: Add note to section (edit mode)
        section: Section for note (edit mode)
        phase: Target phase for new item (edit mode)
        interactive: Interactive editing (edit mode)
        list_phases: List all phases (both modes)
    """
    # Determine mode based on which parameters are provided
    is_edit_mode = any([add, remove, rename, add_phase, add_note, interactive])

    if is_edit_mode:
        # NEW: Edit mode
        edit_plan(...)
    else:
        # EXISTING: Checkbox mode (original behavior)
        toggle_checkbox_original(...)


# New functions (keep existing functions)

def edit_plan(...) -> None:
    """Handle plan editing operations."""
    if add:
        add_item_to_plan(plan_content, add, phase)
    elif remove:
        remove_item_from_plan(plan_content, remove)
    elif rename:
        rename_item_in_plan(plan_content, rename, to)
    elif add_phase:
        add_phase_to_plan(plan_content, add_phase)
    elif add_note:
        add_note_to_plan(plan_content, add_note, section)
    elif interactive:
        interactive_edit_plan(plan_content)

def add_item_to_plan(plan_content: str, item: str, phase: str | None) -> str:
    """Add checklist item to plan."""
    ...

def remove_item_from_plan(plan_content: str, item_pattern: str) -> str:
    """Remove checklist item matching pattern."""
    ...

def rename_item_in_plan(plan_content: str, old_item: str, new_item: str) -> str:
    """Rename existing item description."""
    ...

def add_phase_to_plan(plan_content: str, phase_name: str) -> str:
    """Add new phase section."""
    ...

def add_note_to_plan(plan_content: str, note: str, section: str) -> str:
    """Add note to specified section (Risks, Notes, Context)."""
    ...
```

#### Compatibility Matrix

| Usage | Mode | Behavior |
|-------|------|----------|
| `ai-update-plan "item"` | Checkbox | Check item (ORIGINAL) |
| `ai-update-plan "item" --uncheck` | Checkbox | Uncheck item (ORIGINAL) |
| `ai-update-plan --show` | Display | Show plan (ORIGINAL) |
| `ai-update-plan --add "new item"` | Edit | Add item (NEW) |
| `ai-update-plan --remove "item"` | Edit | Remove item (NEW) |
| `ai-update-plan --rename "old" --to "new"` | Edit | Rename item (NEW) |

**Key Design**: No mode flag needed. Command automatically detects mode based on parameters used.

### 3. AI-Driven Plan Customization

#### Automatic Plan Adaptation

**When AI agent starts work**:
```python
# In AI instructions (CLAUDE.md, AGENTS.md, etc.)

"""
After running ai-start-task, you MUST customize the plan:

1. Review the default checklist
2. Add task-specific items using ai-update-plan --add
3. Remove irrelevant items using ai-update-plan --remove
4. Rename items to be more specific using ai-update-plan --rename

Example:
  Task: "Add email validation to user registration"

  Default plan includes: "Write test file(s)"

  AI customizes to:
  uv run ai-update-plan --rename "Write test file(s)" --to "Write tests/test_validators.py with email format tests"
  uv run ai-update-plan --add "Test valid emails: user@domain.com, user+tag@domain.co.uk"
  uv run ai-update-plan --add "Test invalid emails: @domain, user@, user.com"
  uv run ai-update-plan --remove "Update README if needed"  # Not needed for this task
"""
```

**AI Workflow with Plan Customization**:
```
1. User: "Add phone validation"
2. AI: ai-start-task "Add phone validation"
3. AI: Reviews default plan (ai-update-plan --show)
4. AI: ai-update-plan --add "Test US format: (123) 456-7890"
5. AI: ai-update-plan --add "Test international formats"
6. AI: ai-update-plan --rename "Write test file(s)" --to "Write tests/test_validators.py::test_phone_formats"
7. AI: Proceeds with customized plan
8. AI: ai-update-plan "item" as work progresses (checkbox mode)
```

#### AI_DOCS Update Requirements

**CRITICAL**: All AI agent documentation MUST be updated to mandate plan customization.

**Files to Update**:
1. `AI_DOCS/ai-tools.md` - Add plan customization section
2. `AI_DOCS/tdd-workflow.md` - Include plan management in TDD cycle
3. `CLAUDE.md` - Add plan customization to workflow
4. `AGENTS.md` - Add plan customization requirements
5. `.cursorrules` - Add plan customization guidance
6. `.github/copilot-instructions.md` - Add plan customization for Copilot users
7. `.gemini/styleguide.md` - Add plan customization for Gemini

**Mandatory Workflow for ALL AI Agents**:
```markdown
## Session Management with Plan Customization (MANDATORY)

### Step 1: Start Task
```bash
uv run ai-start-task "Task description" --type=<feature|bugfix|docs|refactor>
```

### Step 2: Customize Plan (NEW - REQUIRED!)

**AFTER starting task, IMMEDIATELY customize the plan:**

```bash
# View default plan
uv run ai-update-plan --show

# Customize based on task
uv run ai-update-plan --add "Task-specific item"
uv run ai-update-plan --remove "Irrelevant item"
uv run ai-update-plan --rename "Generic item" --to "Specific description"
```

**Why this is MANDATORY**:
- Generic plans add no value
- Task-specific plans guide real work
- Validation will check if plan was customized
- Failure to customize will trigger warnings

### Step 3: Work and Track Progress
```bash
# Check off items as completed (checkbox mode)
uv run ai-update-plan "Completed item"

# Add new items discovered during work (edit mode)
uv run ai-update-plan --add "Newly discovered step"
```

### Step 4: Finish Task
```bash
uv run ai-finish-task --summary="What was accomplished"
```

**Validation checks**:
- Plan was customized (strict validation)
- Work matches plan items (strict validation)
- Quality checks completed (strict validation)
```

**Non-Compliance Consequences**:
- `ai-finish-task` will warn if plan not customized
- With strict validation (default), must confirm to proceed
- Plan validation metrics will track customization rate
- Low customization rate indicates agents not following workflow

### 4. Enhanced Plan Validation (Strict Mode)

#### Current: Basic Completion Check
```python
def check_plan_completion(plan_content):
    # Only checks: are all boxes checked?
    # Doesn't validate relevance
```

#### Proposed: Strict Intelligent Validation
```python
def validate_plan_relevance(
    plan_content: str,
    execution_content: str,
    task_type: str,
    strict: bool = True  # DEFAULT: Strict validation
) -> ValidationResult:
    """Validate plan matches actual work.

    Args:
        plan_content: Content of PLAN file
        execution_content: Content of EXECUTION log
        task_type: Type of task (feature, bugfix, docs, refactor)
        strict: If True, require plan customization (default)

    Returns:
        ValidationResult with checks, errors, warnings
    """

    validation = ValidationResult()

    # STRICT CHECK 1: Plan must be customized
    if is_generic_template(plan_content):
        if strict:
            validation.add_error(
                "Plan was NOT customized. Generic templates add no value. "
                "REQUIRED: Use 'ai-update-plan --add/--remove/--rename' after ai-start-task."
            )
        else:
            validation.add_warning("Plan was not customized")

    # STRICT CHECK 2: Work must match plan
    plan_items = extract_checked_items(plan_content)
    work_done = extract_work_from_log(execution_content)

    mismatch_items = []
    for item in plan_items:
        if not item_appears_in_log(item, work_done):
            mismatch_items.append(item)

    if mismatch_items:
        if strict:
            validation.add_error(
                f"Checked items not found in execution log: {mismatch_items}. "
                "REQUIRED: Plan items must match actual work completed."
            )
        else:
            validation.add_warning(f"Items may not match work: {mismatch_items}")

    # STRICT CHECK 3: Quality gates must be run
    if not check_make_check_ran(execution_content):
        if strict:
            validation.add_error(
                "'make check' not found in execution log. "
                "REQUIRED: Run 'make check' before finishing task."
            )
        else:
            validation.add_warning("'make check' not logged")

    # STRICT CHECK 4: All items must be checked
    is_complete, checked, total = check_plan_completion(plan_content)
    if not is_complete:
        if strict:
            validation.add_error(
                f"Plan not complete: {checked}/{total} items checked. "
                "REQUIRED: Complete all plan items or remove irrelevant ones."
            )
        else:
            validation.add_warning(f"Plan incomplete: {checked}/{total}")

    # STRICT CHECK 5: Task-type specific validation
    if not validate_task_type_requirements(plan_content, task_type):
        if strict:
            validation.add_error(
                f"Plan missing required sections for {task_type} tasks. "
                f"Check task-specific template requirements."
            )

    return validation


class ValidationResult:
    """Result of plan validation."""

    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.suggestions: list[str] = []

    def add_error(self, msg: str) -> None:
        """Add validation error (blocks completion in strict mode)."""
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        """Add validation warning (informational)."""
        self.warnings.append(msg)

    def add_suggestion(self, msg: str) -> None:
        """Add suggestion for improvement."""
        self.suggestions.append(msg)

    def has_errors(self) -> bool:
        """Check if validation failed."""
        return len(self.errors) > 0

    def has_warnings(self) -> bool:
        """Check if validation has warnings."""
        return len(self.warnings) > 0

    def is_valid(self) -> bool:
        """Check if validation passed."""
        return not self.has_errors()
```

#### Strict Validation Configuration

**Default Behavior**: Strict validation ENABLED

**Configuration in pyproject.toml**:
```toml
[tool.ai-tools]
strict_validation = true  # Default
require_plan_customization = true  # Default
require_work_match = true  # Default
require_quality_checks = true  # Default
```

**Override Options**:
```bash
# Finish with strict validation (default)
uv run ai-finish-task --summary="Task done"

# Override to lenient validation (not recommended)
uv run ai-finish-task --summary="Task done" --lenient

# Force finish (skip validation - emergency only)
uv run ai-finish-task --summary="Task done" --force
```

**Strict Validation Behavior**:
- Errors BLOCK task completion
- User must fix issues OR explicitly override
- Clear error messages explain what's required
- Suggestions provided for remediation

### 5. Plan Templates in Separate Files

**Structure**:
```
scripts/ai_tools/
├── templates/
│   ├── __init__.py
│   ├── feature.md           # Feature template
│   ├── bugfix.md            # Bugfix template
│   ├── docs.md              # Documentation template
│   ├── refactor.md          # Refactor template
│   └── custom.md            # Minimal custom template
├── edit_plan.py             # NEW: Plan editing tool
├── start_task.py            # Modified: Load templates
├── update_plan.py           # Enhanced: Better item matching
└── finish_task.py           # Enhanced: Plan validation
```

**Template Format** (feature.md):
```markdown
# Task Plan: {{task_name}}

**Session ID**: {{session_id}}
**Created**: {{timestamp}}
**Task Type**: feature
**Status**: 🚧 In Progress

---

## Objective

{{objective_placeholder}}

---

## Context

**Recent Decisions**:
See RECENT_DECISIONS.md

**Related Conventions**:
See CONVENTIONS.md

**Dependencies**:
- [ ] None identified yet

---

## Implementation Steps

### Phase 1: Research & Design
- [ ] Understand requirements
- [ ] Review related code
- [ ] Identify affected components
- [ ] Design approach

### Phase 2: Write Tests (TDD)
- [ ] Identify test scenarios
- [ ] Write test file(s)
- [ ] Run tests to confirm they fail

### Phase 3: Implementation
- [ ] Implement functionality
- [ ] Run tests to confirm they pass
- [ ] Verify 80%+ coverage
- [ ] Handle edge cases

### Phase 4: Quality Checks
- [ ] Run make format
- [ ] Run make lint
- [ ] Run make test
- [ ] Fix any issues
- [ ] Run make check - all pass

### Phase 5: Documentation
- [ ] Update docstrings
- [ ] Add type hints
- [ ] Update README if user-facing
- [ ] Add inline comments for complex logic

---

## Files to Change

- [ ] `src/` - Implementation
- [ ] `tests/` - Test files
- [ ] `README.md` - If user-facing

---

## Risks & Considerations

- None identified yet

---

## Notes

[Track decisions, blockers, questions as you work]

<!--
CUSTOMIZATION REMINDER:
After creating this plan, use `ai-edit-plan` to:
- Add task-specific steps
- Remove irrelevant items
- Update generic descriptions to be specific
- Add notes about approach
-->
```

---

## Implementation Phases

### Phase 1: Template System (Week 1)

**Goal**: Implement task-specific template loading

**Tasks**:
1. Create template directory structure
2. Write 4 base templates (feature, bugfix, docs, refactor)
3. Modify `start_task.py` to load templates based on task_type
4. Add template variables substitution
5. Write tests for template loading

**Files**:
- `scripts/ai_tools/templates/*.md` (NEW)
- `scripts/ai_tools/template_loader.py` (NEW)
- `scripts/ai_tools/start_task.py` (MODIFY)
- `tests/ai_tools/test_template_loader.py` (NEW)
- `tests/ai_tools/test_start_task.py` (MODIFY)

**Testing**:
```python
def test_load_feature_template():
    """Test feature template loads with correct sections."""
    template = load_template("feature", session_id="123", task_name="test")
    assert "Phase 1: Research & Design" in template
    assert "Phase 2: Write Tests (TDD)" in template

def test_load_docs_template_no_tests():
    """Test docs template doesn't include testing phase."""
    template = load_template("docs", session_id="123", task_name="test")
    assert "Write Tests" not in template
    assert "Update Documentation" in template
```

**Deliverables**:
- 4 task-type templates
- Template loading system
- 100% test coverage
- Updated `ai-start-task` using templates

### Phase 2: Extended Plan Management (Week 2)

**Goal**: Extend `ai-update-plan` with editing capabilities

**Tasks**:
1. Extend `update_plan.py` with new functions:
   - `add_item_to_plan()` - Add checklist items
   - `remove_item_from_plan()` - Remove items
   - `rename_item_in_plan()` - Rename/update items
   - `add_phase_to_plan()` - Add custom phases
   - `add_note_to_plan()` - Add notes to sections
2. Add new CLI argument flags (--add, --remove, --rename, etc.)
3. Implement mode detection (checkbox vs edit)
4. Implement interactive mode
5. Add plan format validation
6. Maintain full backward compatibility
7. Write comprehensive tests for new functionality
8. Test backward compatibility extensively

**Files**:
- `scripts/ai_tools/update_plan.py` (MAJOR ENHANCEMENT)
- `tests/ai_tools/test_update_plan.py` (EXTEND)
- `tests/ai_tools/test_update_plan_backward_compat.py` (NEW)

**API Design** (Extended):
```python
def update_plan(
    # EXISTING parameters (PRESERVED)
    item: str | None = None,
    check: bool = True,
    uncheck: bool = False,
    show: bool = False,
    session_id: str | None = None,

    # NEW parameters (ADDED)
    add: str | None = None,
    remove: str | None = None,
    rename: str | None = None,
    to: str | None = None,
    add_phase: str | None = None,
    add_note: str | None = None,
    section: str | None = None,
    phase: str | None = None,
    interactive: bool = False,
    list_phases: bool = False,
) -> None:
    """Update plan: check items OR edit plan structure.

    Backward compatible: defaults to checkbox mode.
    """
    # Auto-detect mode
    is_edit_mode = any([add, remove, rename, add_phase, add_note, interactive])

    if is_edit_mode:
        handle_edit_mode(...)
    else:
        handle_checkbox_mode(...)  # EXISTING code


# NEW functions

def add_item_to_plan(
    plan_content: str,
    item_text: str,
    phase: str | None = None
) -> str:
    """Add checklist item to plan.

    Args:
        plan_content: Current plan content
        item_text: Text of new item
        phase: Phase name (e.g., "Phase 1")

    Returns:
        Updated plan content
    """

def remove_item_from_plan(
    plan_content: str,
    item_pattern: str,
    confirm: bool = True
) -> str:
    """Remove checklist item from plan.

    Args:
        plan_content: Current plan content
        item_pattern: Pattern to match (fuzzy)
        confirm: Ask for confirmation before removing

    Returns:
        Updated plan content
    """

def rename_item_in_plan(
    plan_content: str,
    old_text: str,
    new_text: str
) -> str:
    """Rename existing checklist item.

    Args:
        plan_content: Current plan content
        old_text: Current item text (fuzzy match)
        new_text: New item text

    Returns:
        Updated plan content
    """
```

**Testing Strategy**:

**Backward Compatibility Tests**:
```python
def test_checkbox_mode_still_works():
    """Test original checkbox behavior unchanged."""
    # Ensure old commands still work exactly as before
    update_plan("Write tests")  # Should check item
    update_plan("Run tests", uncheck=True)  # Should uncheck
    update_plan(show=True)  # Should display plan

def test_no_edit_flags_means_checkbox_mode():
    """Test that absence of edit flags uses checkbox mode."""
    # If user provides item name only, use checkbox mode
    result = update_plan("Some item")
    # Should toggle checkbox, not try to edit
```

**New Functionality Tests**:
```python
def test_add_item_with_flag():
    """Test adding item with --add flag."""
    plan = create_test_plan()
    result = add_item_to_plan(plan, "New test item", phase="Phase 1")
    assert "- [ ] New test item" in result

def test_remove_item_with_flag():
    """Test removing item with --remove flag."""
    plan = create_plan_with_items()
    result = remove_item_from_plan(plan, "Update README")
    assert "Update README" not in result

def test_rename_item_with_flags():
    """Test renaming item with --rename and --to flags."""
    plan = create_plan_with_items()
    result = rename_item_in_plan(plan, "Write tests", "Write test_validators.py")
    assert "Write test_validators.py" in result
    assert "Write tests" not in result

def test_mode_detection_checkbox():
    """Test mode detection uses checkbox when no edit flags."""
    # No edit flags = checkbox mode
    assert detect_mode(item="test", check=True) == "checkbox"

def test_mode_detection_edit():
    """Test mode detection uses edit when edit flags present."""
    # Edit flag present = edit mode
    assert detect_mode(add="new item") == "edit"
    assert detect_mode(remove="old item") == "edit"
    assert detect_mode(rename="old", to="new") == "edit"
```

**CLI Testing**:
```bash
# Test backward compatibility
uv run ai-update-plan "Write tests"  # Should work as before
uv run ai-update-plan --show  # Should work as before

# Test new functionality
uv run ai-update-plan --add "New item"
uv run ai-update-plan --remove "Old item"
uv run ai-update-plan --rename "Generic" --to "Specific"
```

**Deliverables**:
- Extended `ai-update-plan` command
- Full backward compatibility
- Interactive editing mode
- Comprehensive tests (old + new functionality)
- Updated documentation
- Migration guide (none needed - fully compatible)

### Phase 3: Enhanced Update Tool (Week 3)

**Goal**: Improve `ai-update-plan` with better features

**Tasks**:
1. Add fuzzy matching for item text
2. Support checking multiple items at once
3. Add progress visualization
4. Add "--list-phases" option
5. Improve error messages

**Files**:
- `scripts/ai_tools/update_plan.py` (MODIFY)
- `tests/ai_tools/test_update_plan.py` (MODIFY)

**Enhancements**:
```python
# Current: Exact substring match
def find_checkbox_line(content, item_text):
    if item_lower in line_lower:  # Rigid

# Proposed: Fuzzy matching
from difflib import SequenceMatcher

def find_checkbox_line(content, item_text, threshold=0.7):
    """Find checkbox with fuzzy matching."""
    best_match = None
    best_score = 0.0

    for i, line in enumerate(lines):
        if is_checkbox(line):
            score = similarity(item_text, line)
            if score > threshold and score > best_score:
                best_match = (i, line)
                best_score = score

    return best_match
```

**New Features**:
```bash
# Check multiple items
uv run ai-update-plan "Write tests" "Run tests"

# List all phases and items
uv run ai-update-plan --list-phases

# Check all items in a phase
uv run ai-update-plan --check-phase "Phase 1"

# Show detailed progress by phase
uv run ai-update-plan --show --detailed
```

**Deliverables**:
- Fuzzy matching
- Batch operations
- Better UX
- Full test coverage

### Phase 4: Plan Validation (Week 4)

**Goal**: Add intelligent plan validation to `ai-finish-task`

**Tasks**:
1. Implement plan relevance checking
2. Detect generic vs. customized plans
3. Validate work matches plan
4. Add validation warnings/suggestions
5. Allow override with confirmation

**Files**:
- `scripts/ai_tools/finish_task.py` (MODIFY)
- `scripts/ai_tools/plan_validator.py` (NEW)
- `tests/ai_tools/test_plan_validator.py` (NEW)

**Validation Logic**:
```python
def validate_plan(
    plan_content: str,
    execution_content: str,
    task_type: str
) -> ValidationResult:
    """Validate plan quality and relevance."""

    checks = {
        "is_complete": check_all_items_done(plan_content),
        "is_customized": check_plan_customized(plan_content),
        "work_matches": check_work_matches_plan(plan_content, execution_content),
        "quality_checks_run": check_make_check_logged(execution_content),
        "plan_updated_during_work": check_plan_modifications(plan_content)
    }

    warnings = []
    suggestions = []

    if not checks["is_customized"]:
        warnings.append(
            "Plan appears to be generic template - "
            "consider using ai-edit-plan to customize"
        )
        suggestions.append(
            "Future: Run ai-edit-plan after ai-start-task to add task-specific items"
        )

    if not checks["work_matches"]:
        warnings.append(
            "Some checked items don't appear in execution log"
        )
        suggestions.append(
            "Ensure plan is kept up-to-date as work progresses"
        )

    return ValidationResult(checks, warnings, suggestions)
```

**Enhanced Finish Flow**:
```python
def finish_task(summary, session_id):
    """Finish task with validation."""

    # ... existing code ...

    # NEW: Validate plan
    validation = validate_plan(plan_content, execution_content, task_type)

    if validation.has_warnings():
        print_warning("Plan Validation Issues:")
        for warning in validation.warnings:
            print(f"  • {warning}")
        print()

        if validation.has_suggestions():
            print("Suggestions for next time:")
            for suggestion in validation.suggestions:
                print(f"  • {suggestion}")
            print()

        response = input("Continue anyway? [y/N]: ").lower()
        if response != 'y':
            sys.exit(0)

    # ... existing code ...
```

**Deliverables**:
- Plan validation system
- Smart warnings
- Helpful suggestions
- Full test coverage

### Phase 5: AI Instructions Update (Week 5) - CRITICAL

**Goal**: Update ALL AI agent instructions to MANDATE plan customization

**CRITICAL**: This phase ensures ALL AI agents implement the new workflow.

**Tasks**:
1. Update `AI_DOCS/ai-tools.md` - Add plan customization as MANDATORY step
2. Update `AI_DOCS/tdd-workflow.md` - Include plan management in TDD cycle
3. Update `CLAUDE.md` - Add plan customization to session workflow
4. Update `AGENTS.md` - Add plan customization requirements
5. Update `.cursorrules` - Add plan management for Cursor
6. Update `.github/copilot-instructions.md` - Add plan customization for Copilot
7. Update `.gemini/styleguide.md` - Add plan customization for Gemini
8. Create enforcement mechanisms in documentation
9. Add examples of good vs bad plan customization

**Files** (ALL MUST BE UPDATED):
- `AI_DOCS/ai-tools.md` (MAJOR UPDATE - PRIMARY)
- `AI_DOCS/tdd-workflow.md` (MODIFY - Add plan step)
- `CLAUDE.md` (MODIFY - Add customization step)
- `AGENTS.md` (MODIFY - Add requirements)
- `.cursorrules` (MODIFY - Add guidance)
- `.github/copilot-instructions.md` (MODIFY - Add workflow)
- `.gemini/styleguide.md` (MODIFY - Add workflow)

**New AI Workflow Documentation** (For ALL Agent Docs):

```markdown
## Session Management with Plan Customization (MANDATORY)

### Step 1: Start Task
```bash
uv run ai-start-task "Add email validation" --type=feature
```

### Step 2: Customize Plan (REQUIRED!)

**IMMEDIATELY after starting, you MUST customize the plan:**

```bash
# Review default plan
uv run ai-update-plan --show

# Add task-specific items
uv run ai-update-plan --add "Test valid: user@example.com"
uv run ai-update-plan --add "Test invalid: @example.com"

# Remove irrelevant items
uv run ai-update-plan --remove "Update README"  # Not needed

# Rename generic to specific
uv run ai-update-plan --rename "Write test file(s)" --to "Write tests/test_validators.py"
```

**Why REQUIRED**:
- Generic plans have NO VALUE
- Strict validation will ERROR if plan not customized
- Plan guides your actual work
- Demonstrates understanding of task

### Step 3: Work & Track Progress
As you work, check off completed items (checkbox mode):
```bash
uv run ai-update-plan "Test valid: user@example.com"
uv run ai-update-plan "Test invalid: @example.com"
```

Add new items discovered during work (edit mode):
```bash
uv run ai-update-plan --add "Handle edge case: empty string"
```

### Step 4: Finish Task
```bash
uv run ai-finish-task --summary="Added email validation with comprehensive tests"
```

**Strict Validation Checks**:
- ERROR if plan was not customized
- ERROR if work doesn't match plan items
- ERROR if quality checks not completed
- ERROR if plan not 100% complete

Must fix errors OR use `--lenient` override (not recommended).
```

**Documentation Structure** (Each agent file):

1. **STOP! Section** - ai-start-task command
2. **Plan Customization** - NEW MANDATORY section
3. **TDD Workflow** - Including plan integration
4. **Quality Gates** - Including plan validation

**Enforcement in AI_DOCS**:

Add to `AI_DOCS/ai-tools.md`:
```markdown
## CRITICAL: Plan Customization is MANDATORY

After running ai-start-task, you MUST customize the plan.

### Why This is Not Optional

1. Generic plans add ZERO value
2. Strict validation enforces customization
3. Demonstrates task understanding
4. Guides actual work effectively

### How to Customize

Use ai-update-plan with edit flags:
- --add: Add task-specific items
- --remove: Remove irrelevant items
- --rename: Make generic items specific

### Validation

ai-finish-task validates:
- Plan was customized (REQUIRED)
- Work matches plan (REQUIRED)
- Quality checks run (REQUIRED)

Failure = ERROR, not warning
```

**Deliverables**:
- Updated AI instructions
- Plan customization workflow
- Examples and best practices
- Clear guidance for AI agents

### Phase 6: Documentation & Examples (Week 6)

**Goal**: Complete documentation and provide examples

**Tasks**:
1. Create user guide for new commands
2. Add workflow examples
3. Update README.md
4. Create CHANGELOG entry
5. Add migration guide

**Files**:
- `AI_DOCS/ai-tools.md` (MAJOR UPDATE)
- `README.md` (MODIFY)
- `CHANGELOG.md` (ADD)
- `docs/ai-plan-customization-guide.md` (NEW)

**Documentation Sections**:

1. **User Guide**: How to use ai-edit-plan
2. **Workflow Examples**: Common scenarios
3. **Template Reference**: Available templates
4. **Best Practices**: When to customize, what to add
5. **Migration Guide**: For existing sessions

**Deliverables**:
- Complete documentation
- Workflow examples
- Migration guide
- Updated README

---

## Testing Strategy

### Unit Tests (Per Phase)

**Phase 1: Templates**
- Template loading
- Variable substitution
- Task type routing
- Error handling

**Phase 2: Edit Plan**
- Add items
- Remove items
- Update items
- Add phases
- Fuzzy matching
- Edge cases

**Phase 3: Update Plan**
- Enhanced matching
- Batch operations
- Phase operations
- Progress display

**Phase 4: Validation**
- Customization detection
- Work matching
- Quality checks
- Warning generation

### Integration Tests

```python
def test_full_workflow_with_customization():
    """Test complete workflow with plan customization."""

    # Start task
    start_task("Add phone validation", task_type="feature")

    # Customize plan
    add_item("Test US format")
    add_item("Test international format")
    remove_item("Update README")

    # Update as work progresses
    update_plan("Write test file(s)")
    update_plan("Test US format")

    # Finish with validation
    result = finish_task("Phone validation complete")

    assert result.validation_passed
    assert result.plan_was_customized
```

### Manual Testing Scenarios

1. **Feature Development**:
   - Start feature task
   - Customize plan with specific test cases
   - Work through customized checklist
   - Finish with validation

2. **Bug Fix**:
   - Start bugfix task
   - Get bugfix-specific template
   - Add reproduction steps
   - Complete and validate

3. **Documentation**:
   - Start docs task
   - Get docs template (no testing)
   - Customize with sections to update
   - Finish

4. **Refactoring**:
   - Start refactor task
   - Ensure tests exist
   - Customize with affected components
   - Validate no test breakage

---

## Migration Strategy

### For Existing Sessions

**Option 1: No Migration (Recommended)**
- Old sessions keep working
- New features only for new sessions
- Clean cut-over

**Option 2: Template Upgrade**
- Add `ai-upgrade-plan` command
- Convert generic plan to task-specific template
- Preserve checked items
- Add customization reminder

**Implementation**:
```bash
# For old sessions that want new features
uv run ai-upgrade-plan --session-id=20251103102706

# Interactive: asks which items to keep
# Applies appropriate template
# Preserves progress
```

### Backward Compatibility

**Ensure**:
- Old plan format still works
- `ai-update-plan` works with old plans
- `ai-finish-task` validates both formats
- No breaking changes to existing sessions

---

## Success Metrics

### Quantitative

1. **Template Usage**:
   - 100% of new tasks use task-specific templates
   - Each task type has appropriate default items

2. **Plan Customization**:
   - Target: 70%+ of tasks have customized plans
   - Measure: Count modified plans vs. generic

3. **Plan Relevance**:
   - Target: 90%+ of checked items appear in execution log
   - Measure: Validation pass rate

4. **Test Coverage**:
   - All new code: 100% coverage
   - Modified code: Maintain 100% coverage

### Qualitative

1. **User Feedback**:
   - Plans feel relevant to actual work
   - Customization is easy and natural
   - AI agents effectively use plan editing

2. **AI Agent Behavior**:
   - AI agents customize plans appropriately
   - Plans reflect actual work being done
   - Plan items are specific, not generic

3. **Value Addition**:
   - Plans are actively used, not ignored
   - Checklists guide work effectively
   - Progress tracking is meaningful

---

## Timeline

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| Phase 1: Templates | Week 1 | Task-specific templates, template loader |
| Phase 2: Edit Plan | Week 2 | ai-edit-plan command, tests |
| Phase 3: Enhanced Update | Week 3 | Improved ai-update-plan |
| Phase 4: Validation | Week 4 | Plan validation, warnings |
| Phase 5: AI Instructions | Week 5 | Updated agent instructions |
| Phase 6: Documentation | Week 6 | Complete docs, examples |

**Total**: 6 weeks

**Fast Track Option**: 3 weeks (combine related phases)

---

## Risks & Mitigation

### Risk 1: Complexity

**Risk**: Adding too many features makes system complex

**Mitigation**:
- Start with simple template system
- Add editing incrementally
- Keep commands simple and focused
- Extensive documentation

### Risk 2: AI Adoption

**Risk**: AI agents don't use customization features

**Mitigation**:
- Clear instructions in agent docs
- Examples of good customization
- Validation encourages customization
- Templates are good defaults

### Risk 3: Backward Compatibility

**Risk**: Breaking existing sessions

**Mitigation**:
- Support both old and new formats
- No forced migration
- Gradual rollout
- Comprehensive testing

### Risk 4: Over-Engineering

**Risk**: Solution more complex than problem

**Mitigation**:
- Start with minimal viable solution
- Phase 1-2 solve core problem
- Phases 3-6 are enhancements
- Can stop after Phase 2 if sufficient

---

## Next Steps

### Immediate (For User Review)

1. **Review this plan**:
   - Does it address your concerns?
   - Are task-specific templates the right approach?
   - Is ai-edit-plan the right solution?
   - Any missing requirements?

2. **Decide on scope**:
   - Full implementation (all 6 phases)?
   - Minimal version (Phases 1-2)?
   - Custom priority?

3. **Approve approach**:
   - Template-based system OK?
   - New command (ai-edit-plan) acceptable?
   - Validation approach makes sense?

### After Approval

1. **Start Phase 1**: Implement task-specific templates
2. **TDD throughout**: Write tests first
3. **Incremental delivery**: Each phase is usable
4. **Iterate based on feedback**: Adjust as needed

---

## Decisions Based on User Feedback

### User Feedback Received:

1. **Problem Solving**: ✅ Yes, this solves the "no value" concern
2. **AI_DOCS Updates**: ✅ MUST update AI_DOCS so ALL agents implement new tools
3. **Scope**: ✅ Full 6-phase implementation
4. **Design - Command**: ✅ Extend ai-update-plan (not create new command)
5. **Design - Compatibility**: ✅ Must accommodate both old and new implementation
6. **Design - Templates**: ✅ Markdown templates (preferred)
7. **Design - Validation**: ✅ Strict validation (preferred)
8. **Timeline**: ✅ 6 weeks acceptable
9. **Status**: ⏳ Adjustments needed first

### Plan Adjustments Made:

1. **Command Approach**:
   - ✅ Changed from separate `ai-edit-plan` to extended `ai-update-plan`
   - ✅ Maintains full backward compatibility
   - ✅ Auto-detects mode based on flags used
   - ✅ Single command for all plan operations

2. **Validation Approach**:
   - ✅ Changed to strict validation by default
   - ✅ Validation errors BLOCK task completion
   - ✅ Override requires explicit `--lenient` or `--force` flag
   - ✅ Clear error messages with remediation guidance

3. **AI_DOCS Requirements**:
   - ✅ Added CRITICAL section for AI_DOCS updates
   - ✅ Plan customization is MANDATORY, not optional
   - ✅ ALL agent documentation files must be updated
   - ✅ Enforcement through strict validation

4. **Implementation Details**:
   - ✅ Markdown templates in separate files
   - ✅ Strict validation with configuration options
   - ✅ Backward compatibility extensively tested
   - ✅ Phase 5 emphasizes AI_DOCS updates

### Outstanding Questions:

None - all major decisions confirmed by user.

---

## Appendix: Alternative Approaches Considered

### Alternative 1: AI Generates Plans

**Approach**: AI agent generates custom plan based on task description

**Pros**:
- Fully customized to each task
- No generic templates

**Cons**:
- Requires AI involvement (not all tools)
- Inconsistent plan quality
- Hard to test/validate
- More complex implementation

**Decision**: Rejected in favor of templates + editing

### Alternative 2: Extend ai-update-plan

**Approach**: Add editing features to ai-update-plan instead of new command

**Pros**:
- Single command
- Less to learn

**Cons**:
- Command becomes overloaded
- Confusing API (update vs edit)
- Harder to document

**Decision**: Separate ai-edit-plan is clearer

### Alternative 3: Configuration-Based Templates

**Approach**: YAML/TOML config defines templates

**Pros**:
- Easy to modify without code
- User-customizable

**Cons**:
- More complexity
- Harder to validate
- Template logic in config

**Decision**: Markdown templates simpler

### Alternative 4: No Templates, Full Editing

**Approach**: Start with minimal plan, build entirely through editing

**Pros**:
- Maximum flexibility
- No template maintenance

**Cons**:
- More work per task
- No guidance
- Inconsistent plans

**Decision**: Templates + editing balances both

---

## Summary

### The Problem
Current system provides generic, unchangeable plans that don't add value because they can't be adapted to actual work.

### The Solution (Updated Based on Feedback)
1. **Task-Specific Templates**: Different base plans for features, bugs, docs, refactors (Markdown files)
2. **Extended ai-update-plan**: Backward-compatible editing capabilities (not new command)
3. **AI-Driven Customization**: MANDATORY plan customization enforced through ALL AI agents
4. **Strict Validation**: Errors block completion if plan not customized properly

### Key Benefits
- Plans are relevant from the start (task-specific templates)
- Plans adapt as understanding evolves (extended ai-update-plan)
- Plans guide actual work (MANDATORY AI customization)
- Plans have real value (strict validation ensures quality)
- Single command for all operations (backward compatible)

### Implementation
6 phases, 6 weeks, fully tested, comprehensive documentation, ALL AI agents updated.

### User-Approved Decisions
- ✅ Extend ai-update-plan (not create new command)
- ✅ Full backward compatibility
- ✅ Markdown templates
- ✅ Strict validation by default
- ✅ ALL AI_DOCS files must be updated
- ✅ Plan customization is MANDATORY, not optional
- ✅ Full 6-phase implementation
- ✅ 6-week timeline acceptable

**Deliverable**: Task management system that adds real value through task-specific, dynamically editable, strictly validated plans that ALL AI agents are required to customize.

---

**Status**: Plan adjusted per user feedback - Ready for implementation approval
**Next**: User final approval to proceed with implementation
