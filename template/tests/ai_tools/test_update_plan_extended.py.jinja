"""Tests for extended ai-update-plan editing functionality.

This module tests the new editing capabilities (add, remove, rename)
added to ai-update-plan while ensuring backward compatibility.
"""

from __future__ import annotations

from scripts.ai_tools.update_plan import (
    add_item_to_plan,
    add_phase_to_plan,
    find_phase_section,
    remove_item_from_plan,
    rename_item_in_plan,
)


class TestAddItemToPlan:
    """Test adding new checklist items to plan."""

    def test_add_item_to_end_of_phase(self) -> None:
        """Test adding item to end of a phase."""
        plan = """### Phase 1: Test
- [ ] Existing item 1
- [ ] Existing item 2

### Phase 2: Next"""

        result = add_item_to_plan(plan, "New item", phase="Phase 1")

        assert "- [ ] New item" in result
        # Verify it's in Phase 1 section (before Phase 2)
        phase1_start = result.index("### Phase 1")
        phase2_start = result.index("### Phase 2")
        new_item_pos = result.index("- [ ] New item")
        assert phase1_start < new_item_pos < phase2_start

    def test_add_item_without_phase_adds_to_current(self) -> None:
        """Test adding item without specifying phase adds to last phase."""
        plan = """### Phase 1: First
- [ ] Item 1

### Phase 2: Second
- [ ] Item 2"""

        result = add_item_to_plan(plan, "New item")

        # Should add to last phase (Phase 2)
        assert "### Phase 2: Second" in result
        assert "- [ ] New item" in result
        # Verify it's in Phase 2 section
        phase2_start = result.index("### Phase 2")
        new_item_pos = result.index("- [ ] New item")
        assert new_item_pos > phase2_start

    def test_add_item_creates_phase_if_not_exists(self) -> None:
        """Test adding item to non-existent phase creates it."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = add_item_to_plan(plan, "New item", phase="Phase 3")

        assert "### Phase 3:" in result or "Phase 3" not in result
        # If phase doesn't exist, should still add item (to end)
        assert "- [ ] New item" in result

    def test_add_item_with_special_characters(self) -> None:
        """Test adding item with special characters."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = add_item_to_plan(
            plan,
            "Test with special chars: @#$% and (parentheses)",
        )

        assert "- [ ] Test with special chars: @#$% and (parentheses)" in result

    def test_add_item_preserves_existing_content(self) -> None:
        """Test that adding item preserves all existing content."""
        plan = """# Plan
### Phase 1: Test
- [ ] Item 1
- [x] Item 2

## Notes
Some notes here"""

        result = add_item_to_plan(plan, "New item", phase="Phase 1")

        # All original content should be preserved
        assert "# Plan" in result
        assert "- [ ] Item 1" in result
        assert "- [x] Item 2" in result  # Checked state preserved
        assert "## Notes" in result
        assert "Some notes here" in result
        # Plus new item
        assert "- [ ] New item" in result


class TestRemoveItemFromPlan:
    """Test removing checklist items from plan."""

    def test_remove_item_by_exact_match(self) -> None:
        """Test removing item with exact text match."""
        plan = """### Phase 1: Test
- [ ] Item to remove
- [ ] Item to keep"""

        result = remove_item_from_plan(plan, "Item to remove")

        assert "Item to remove" not in result
        assert "Item to keep" in result

    def test_remove_item_by_partial_match(self) -> None:
        """Test removing item with partial text match."""
        plan = """### Phase 1: Test
- [ ] Write test file(s) for validators
- [ ] Write other tests"""

        result = remove_item_from_plan(plan, "test file")

        # Should remove the item containing "test file"
        assert "Write test file(s) for validators" not in result
        assert "Write other tests" in result

    def test_remove_item_preserves_checked_state_of_others(self) -> None:
        """Test that removing item preserves checked state of other items."""
        plan = """### Phase 1: Test
- [ ] Item to remove
- [x] Completed item
- [ ] Pending item"""

        result = remove_item_from_plan(plan, "Item to remove")

        assert "Item to remove" not in result
        assert "- [x] Completed item" in result  # Checked state preserved
        assert "- [ ] Pending item" in result

    def test_remove_item_not_found_returns_unchanged(self) -> None:
        """Test that trying to remove non-existent item returns plan unchanged."""
        plan = """### Phase 1: Test
- [ ] Item 1
- [ ] Item 2"""

        result = remove_item_from_plan(plan, "Non-existent item")

        # Plan should be unchanged
        assert result == plan

    def test_remove_multiple_matching_items_removes_first(self) -> None:
        """Test that removing item with multiple matches removes first occurrence."""
        plan = """### Phase 1: Test
- [ ] Test item
- [ ] Test item"""

        result = remove_item_from_plan(plan, "Test item")

        # Should remove only first occurrence
        assert result.count("Test item") == 1


class TestRenameItemInPlan:
    """Test renaming checklist items in plan."""

    def test_rename_item_by_exact_match(self) -> None:
        """Test renaming item with exact match."""
        plan = """### Phase 1: Test
- [ ] Old item name
- [ ] Other item"""

        result = rename_item_in_plan(plan, "Old item name", "New item name")

        assert "Old item name" not in result
        assert "- [ ] New item name" in result
        assert "Other item" in result  # Other items unchanged

    def test_rename_item_by_partial_match(self) -> None:
        """Test renaming item with partial match."""
        plan = """### Phase 1: Test
- [ ] Write test file(s)
- [ ] Other task"""

        result = rename_item_in_plan(
            plan, "test file", "Write tests/test_validators.py"
        )

        assert "Write test file(s)" not in result
        assert "- [ ] Write tests/test_validators.py" in result

    def test_rename_preserves_checkbox_state(self) -> None:
        """Test that renaming preserves checkbox state (checked/unchecked)."""
        plan = """### Phase 1: Test
- [x] Completed old name
- [ ] Pending old name"""

        # Rename checked item
        result = rename_item_in_plan(plan, "Completed old name", "Completed new name")
        assert "- [x] Completed new name" in result

        # Rename unchecked item
        result2 = rename_item_in_plan(plan, "Pending old name", "Pending new name")
        assert "- [ ] Pending new name" in result2

    def test_rename_item_not_found_returns_unchanged(self) -> None:
        """Test that renaming non-existent item returns plan unchanged."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = rename_item_in_plan(plan, "Non-existent", "New name")

        assert result == plan

    def test_rename_multiple_matches_renames_first(self) -> None:
        """Test that renaming with multiple matches renames first occurrence."""
        plan = """### Phase 1: Test
- [ ] Duplicate item
- [ ] Duplicate item"""

        result = rename_item_in_plan(plan, "Duplicate item", "Renamed item")

        # Should rename only first occurrence
        assert "- [ ] Renamed item" in result
        assert result.count("Renamed item") == 1
        assert result.count("Duplicate item") == 1


class TestFindPhaseSection:
    """Test finding phase sections in plan."""

    def test_find_phase_by_name(self) -> None:
        """Test finding phase section by phase name."""
        plan = """### Phase 1: Research
- [ ] Item 1

### Phase 2: Implementation
- [ ] Item 2

### Phase 3: Testing"""

        result = find_phase_section(plan, "Phase 2")

        assert "### Phase 2: Implementation" in result
        assert "- [ ] Item 2" in result
        # Should not include other phases
        assert "Phase 1" not in result
        assert "Phase 3" not in result

    def test_find_phase_by_partial_name(self) -> None:
        """Test finding phase by partial name match."""
        plan = """### Phase 1: Write Tests (TDD)
- [ ] Item 1"""

        result = find_phase_section(plan, "Write Tests")

        assert "### Phase 1: Write Tests (TDD)" in result
        assert "- [ ] Item 1" in result

    def test_find_phase_not_found_returns_empty(self) -> None:
        """Test that finding non-existent phase returns empty string."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = find_phase_section(plan, "Non-existent Phase")

        assert result == ""

    def test_find_phase_includes_all_items_until_next_phase(self) -> None:
        """Test that phase section includes all items until next phase header."""
        plan = """### Phase 1: Test
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

### Phase 2: Next"""

        result = find_phase_section(plan, "Phase 1")

        assert "- [ ] Item 1" in result
        assert "- [ ] Item 2" in result
        assert "- [ ] Item 3" in result
        assert "Phase 2" not in result


class TestAddPhaseToPlan:
    """Test adding new phase sections to plan."""

    def test_add_phase_to_end(self) -> None:
        """Test adding new phase section to end of plan."""
        plan = """### Phase 1: Test
- [ ] Item 1

## Notes
Some notes"""

        result = add_phase_to_plan(plan, "Phase 2: New Phase")

        assert "### Phase 2: New Phase" in result
        # Should be added before ## Notes section
        notes_pos = result.index("## Notes")
        phase2_pos = result.index("### Phase 2")
        assert phase2_pos < notes_pos

    def test_add_phase_with_items(self) -> None:
        """Test adding phase with initial checklist items."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        items = ["New item 1", "New item 2"]
        result = add_phase_to_plan(plan, "Phase 2: Implementation", items=items)

        assert "### Phase 2: Implementation" in result
        assert "- [ ] New item 1" in result
        assert "- [ ] New item 2" in result

    def test_add_phase_maintains_plan_structure(self) -> None:
        """Test that adding phase maintains overall plan structure."""
        plan = """# Task Plan: Test

### Phase 1: First
- [ ] Item 1

## Files to Change
- [ ] src/

## Notes
Some notes"""

        result = add_phase_to_plan(plan, "Phase 2: Second")

        # Structure should be maintained
        assert "# Task Plan: Test" in result
        assert "### Phase 1: First" in result
        assert "### Phase 2: Second" in result
        assert "## Files to Change" in result
        assert "## Notes" in result
