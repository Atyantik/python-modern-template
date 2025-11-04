"""Tests for Phase 3 enhanced features: fuzzy matching and validation.

This module tests advanced fuzzy matching using Levenshtein distance,
better error messages with suggestions, and validation features.
"""

from __future__ import annotations

from scripts.ai_tools.update_plan import (
    calculate_levenshtein_distance,
    find_similar_items,
    validate_no_duplicates,
)


class TestLevenshteinDistance:
    """Test Levenshtein distance calculation."""

    def test_identical_strings_return_zero(self) -> None:
        """Test that identical strings have distance 0."""
        assert calculate_levenshtein_distance("test", "test") == 0

    def test_completely_different_strings(self) -> None:
        """Test distance for completely different strings."""
        distance = calculate_levenshtein_distance("abc", "xyz")
        assert distance == 3  # 3 substitutions needed

    def test_one_character_difference(self) -> None:
        """Test distance for one character difference."""
        assert calculate_levenshtein_distance("test", "tset") == 2  # 2 ops (swap)
        assert calculate_levenshtein_distance("test", "text") == 1  # 1 substitution

    def test_insertion_distance(self) -> None:
        """Test distance when characters need to be inserted."""
        assert calculate_levenshtein_distance("test", "tests") == 1  # 1 insertion

    def test_deletion_distance(self) -> None:
        """Test distance when characters need to be deleted."""
        assert calculate_levenshtein_distance("tests", "test") == 1  # 1 deletion

    def test_empty_string_cases(self) -> None:
        """Test distance with empty strings."""
        assert calculate_levenshtein_distance("", "") == 0
        assert calculate_levenshtein_distance("test", "") == 4
        assert calculate_levenshtein_distance("", "test") == 4

    def test_case_sensitive(self) -> None:
        """Test that distance calculation is case sensitive."""
        assert calculate_levenshtein_distance("Test", "test") == 1


class TestFindSimilarItems:
    """Test finding similar items using fuzzy matching."""

    def test_find_exact_match(self) -> None:
        """Test finding exact match returns it first."""
        items = ["Run tests", "Write tests", "Format code"]
        result = find_similar_items("Run tests", items, threshold=0.6)

        assert len(result) > 0
        assert result[0][0] == "Run tests"
        assert result[0][1] == 1.0  # Perfect match

    def test_find_close_match(self) -> None:
        """Test finding close matches with typos."""
        items = ["Run tests", "Write tests", "Format code"]
        result = find_similar_items("Run tsets", items, threshold=0.6)

        assert len(result) > 0
        # "Run tests" should be most similar to "Run tsets"
        assert "Run tests" in [item for item, _ in result]

    def test_find_multiple_similar_items(self) -> None:
        """Test finding multiple similar items."""
        items = ["test_login", "test_logout", "test_signup", "format_code"]
        result = find_similar_items("test", items, threshold=0.5)

        # Should find all test_ items as similar
        similar_items = [item for item, _ in result]
        assert "test_login" in similar_items
        assert "test_logout" in similar_items
        assert "test_signup" in similar_items

    def test_threshold_filters_low_similarity(self) -> None:
        """Test that threshold filters out low similarity matches."""
        items = ["apple", "orange", "banana"]
        result = find_similar_items("test", items, threshold=0.8)

        # None of these should be similar enough to "test"
        assert len(result) == 0

    def test_returns_sorted_by_similarity(self) -> None:
        """Test that results are sorted by similarity (descending)."""
        items = ["tests", "test", "testing", "format"]
        result = find_similar_items("test", items, threshold=0.5)

        # Should be sorted with "test" first (exact match)
        assert result[0][0] == "test"
        assert result[0][1] == 1.0

        # Next items should have decreasing similarity
        if len(result) > 1:
            assert result[1][1] < result[0][1]

    def test_case_insensitive_matching(self) -> None:
        """Test that matching is case insensitive."""
        items = ["Run Tests", "Write Tests"]
        result = find_similar_items("run tests", items, threshold=0.6)

        assert len(result) > 0
        assert result[0][0] == "Run Tests"
        assert result[0][1] == 1.0  # Should match despite case

    def test_empty_items_list(self) -> None:
        """Test behavior with empty items list."""
        result = find_similar_items("test", [], threshold=0.6)
        assert result == []

    def test_partial_word_matching(self) -> None:
        """Test matching partial words."""
        items = ["Run make check", "Run make format", "Run tests"]
        result = find_similar_items("make", items, threshold=0.4)

        # Should find items containing "make"
        similar_items = [item for item, _ in result]
        assert "Run make check" in similar_items
        assert "Run make format" in similar_items


class TestValidateNoDuplicates:
    """Test duplicate validation."""

    def test_no_duplicates_returns_none(self) -> None:
        """Test that no duplicates returns None (valid)."""
        plan = """### Phase 1: Test
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3"""

        result = validate_no_duplicates(plan, "Item 4")
        assert result is None

    def test_exact_duplicate_detected(self) -> None:
        """Test that exact duplicate is detected."""
        plan = """### Phase 1: Test
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3"""

        result = validate_no_duplicates(plan, "Item 1")
        assert result is not None
        assert "Item 1" in result
        assert "already exists" in result.lower()

    def test_case_insensitive_duplicate_detected(self) -> None:
        """Test that case-insensitive duplicate is detected."""
        plan = """### Phase 1: Test
- [ ] Run Tests
- [ ] Write Tests"""

        result = validate_no_duplicates(plan, "run tests")
        assert result is not None
        assert "already exists" in result.lower()

    def test_similar_but_different_items_allowed(self) -> None:
        """Test that similar but different items are allowed."""
        plan = """### Phase 1: Test
- [ ] Run tests
- [ ] Write tests"""

        result = validate_no_duplicates(plan, "Run all tests")
        assert result is None  # Should be allowed (different enough)

    def test_duplicate_with_checkbox_state(self) -> None:
        """Test that duplicates are detected regardless of checkbox state."""
        plan = """### Phase 1: Test
- [x] Run tests
- [ ] Write tests"""

        result = validate_no_duplicates(plan, "Run tests")
        assert result is not None
        assert "already exists" in result.lower()

    def test_whitespace_normalized(self) -> None:
        """Test that whitespace is normalized for duplicate detection."""
        plan = """### Phase 1: Test
- [ ] Run  tests  here"""

        result = validate_no_duplicates(plan, "Run tests here")
        assert result is not None  # Should detect as duplicate

    def test_empty_plan(self) -> None:
        """Test validation with empty plan."""
        result = validate_no_duplicates("", "New item")
        assert result is None  # No duplicates in empty plan
