"""Tests for Phase 4 strict validation features.

This module tests validation features that prevent common mistakes:
- Empty item validation
- Phase existence validation
"""

from __future__ import annotations

from scripts.ai_tools.update_plan import (
    validate_item_not_empty,
    validate_phase_exists,
)


class TestValidateItemNotEmpty:
    """Test empty item validation."""

    def test_valid_item_returns_none(self) -> None:
        """Test that valid item text returns None (valid)."""
        result = validate_item_not_empty("Write tests")
        assert result is None

    def test_empty_string_returns_error(self) -> None:
        """Test that empty string returns error message."""
        result = validate_item_not_empty("")
        assert result is not None
        assert "empty" in result.lower()

    def test_whitespace_only_returns_error(self) -> None:
        """Test that whitespace-only string returns error."""
        result = validate_item_not_empty("   ")
        assert result is not None
        assert "empty" in result.lower()

    def test_tabs_only_returns_error(self) -> None:
        """Test that tabs-only string returns error."""
        result = validate_item_not_empty("\t\t")
        assert result is not None
        assert "empty" in result.lower()

    def test_newlines_only_returns_error(self) -> None:
        """Test that newlines-only string returns error."""
        result = validate_item_not_empty("\n\n")
        assert result is not None
        assert "empty" in result.lower()

    def test_mixed_whitespace_returns_error(self) -> None:
        """Test that mixed whitespace returns error."""
        result = validate_item_not_empty(" \t\n ")
        assert result is not None
        assert "empty" in result.lower()

    def test_single_character_is_valid(self) -> None:
        """Test that single character is valid."""
        result = validate_item_not_empty("a")
        assert result is None

    def test_item_with_leading_trailing_whitespace_is_valid(self) -> None:
        """Test that item with whitespace around text is valid."""
        result = validate_item_not_empty("  Write tests  ")
        assert result is None


class TestValidatePhaseExists:
    """Test phase existence validation."""

    def test_existing_phase_returns_none(self) -> None:
        """Test that existing phase returns None (valid)."""
        plan = """### Phase 1: Test
- [ ] Item 1

### Phase 2: Implementation
- [ ] Item 2"""

        result = validate_phase_exists(plan, "Phase 1")
        assert result is None

    def test_nonexistent_phase_returns_error(self) -> None:
        """Test that non-existent phase returns error."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = validate_phase_exists(plan, "Phase 2")
        assert result is not None
        assert "does not exist" in result.lower() or "not found" in result.lower()

    def test_case_insensitive_phase_matching(self) -> None:
        """Test that phase matching is case insensitive."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = validate_phase_exists(plan, "phase 1")
        assert result is None

    def test_partial_phase_name_matching(self) -> None:
        """Test that partial phase name matches."""
        plan = """### Phase 1: Research & Design
- [ ] Item 1"""

        result = validate_phase_exists(plan, "Phase 1")
        assert result is None

    def test_empty_plan_returns_error(self) -> None:
        """Test that empty plan returns error for any phase."""
        result = validate_phase_exists("", "Phase 1")
        assert result is not None

    def test_plan_without_phases_returns_error(self) -> None:
        """Test that plan without phase headers returns error."""
        plan = """# Some Plan
- [ ] Item 1
- [ ] Item 2"""

        result = validate_phase_exists(plan, "Phase 1")
        assert result is not None

    def test_phase_2_exists_when_multiple_phases(self) -> None:
        """Test finding Phase 2 when multiple phases exist."""
        plan = """### Phase 1: First
- [ ] Item 1

### Phase 2: Second
- [ ] Item 2

### Phase 3: Third
- [ ] Item 3"""

        result = validate_phase_exists(plan, "Phase 2")
        assert result is None

    def test_error_message_suggests_available_phases(self) -> None:
        """Test that error message suggests available phases."""
        plan = """### Phase 1: Test
- [ ] Item 1

### Phase 2: Implementation
- [ ] Item 2"""

        result = validate_phase_exists(plan, "Phase 3")
        assert result is not None
        # Should suggest available phases
        assert "Phase 1" in result or "Phase 2" in result

    def test_none_phase_name_returns_none(self) -> None:
        """Test that None phase name returns None (no validation needed)."""
        plan = """### Phase 1: Test
- [ ] Item 1"""

        result = validate_phase_exists(plan, None)
        assert result is None  # None means "add to last phase", which is valid
