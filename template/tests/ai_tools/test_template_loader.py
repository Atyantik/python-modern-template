"""Tests for AI template loader module.

This module tests template loading and variable substitution for
task-specific plan templates.
"""

from __future__ import annotations

import pytest

from scripts.ai_tools.template_loader import (
    TemplateNotFoundError,
    get_template_path,
    load_template,
    substitute_variables,
)


class TestGetTemplatePath:
    """Test getting template file paths."""

    def test_feature_template_path(self) -> None:
        """Test getting path for feature template."""
        path = get_template_path("feature")
        assert path.name == "feature.md"
        assert "templates" in str(path)

    def test_bugfix_template_path(self) -> None:
        """Test getting path for bugfix template."""
        path = get_template_path("bugfix")
        assert path.name == "bugfix.md"

    def test_docs_template_path(self) -> None:
        """Test getting path for docs template."""
        path = get_template_path("docs")
        assert path.name == "docs.md"

    def test_refactor_template_path(self) -> None:
        """Test getting path for refactor template."""
        path = get_template_path("refactor")
        assert path.name == "refactor.md"

    def test_unknown_type_raises_error(self) -> None:
        """Test that unknown task type raises error."""
        with pytest.raises(TemplateNotFoundError) as exc_info:
            get_template_path("unknown_type")

        error_message = str(exc_info.value)
        assert "unknown_type" in error_message.lower()


class TestSubstituteVariables:
    """Test template variable substitution."""

    def test_substitute_session_id(self) -> None:
        """Test substituting session ID variable."""
        template = "Session: {{session_id}}"
        result = substitute_variables(
            template, session_id="20251103120000", task_name="Test", task_type="feature"
        )
        assert result == "Session: 20251103120000"

    def test_substitute_task_name(self) -> None:
        """Test substituting task name variable."""
        template = "Task: {{task_name}}"
        result = substitute_variables(
            template, session_id="123", task_name="Add validation", task_type="feature"
        )
        assert result == "Task: Add validation"

    def test_substitute_task_type(self) -> None:
        """Test substituting task type variable."""
        template = "Type: {{task_type}}"
        result = substitute_variables(
            template, session_id="123", task_name="Test", task_type="bugfix"
        )
        assert result == "Type: bugfix"

    def test_substitute_timestamp(self) -> None:
        """Test substituting timestamp variable."""
        template = "Created: {{timestamp}}"
        result = substitute_variables(
            template, session_id="123", task_name="Test", task_type="feature"
        )
        # Should contain a timestamp in format YYYY-MM-DD HH:MM:SS
        assert "Created: " in result
        assert len(result.split(": ")[1]) > 10  # Timestamp has length

    def test_substitute_multiple_variables(self) -> None:
        """Test substituting multiple variables at once."""
        template = "{{session_id}}: {{task_name}} ({{task_type}})"
        result = substitute_variables(
            template,
            session_id="20251103120000",
            task_name="Test task",
            task_type="feature",
        )
        assert result == "20251103120000: Test task (feature)"

    def test_substitute_same_variable_multiple_times(self) -> None:
        """Test substituting same variable appearing multiple times."""
        template = "Start: {{task_name}}, End: {{task_name}}"
        result = substitute_variables(
            template, session_id="123", task_name="Build", task_type="feature"
        )
        assert result == "Start: Build, End: Build"

    def test_no_variables_returns_unchanged(self) -> None:
        """Test template without variables returns unchanged."""
        template = "This is a plain template"
        result = substitute_variables(
            template, session_id="123", task_name="Test", task_type="feature"
        )
        assert result == template


class TestLoadTemplate:
    """Test loading complete templates."""

    def test_load_feature_template(self) -> None:
        """Test loading feature template with substitution."""
        result = load_template(
            task_type="feature",
            session_id="20251103120000",
            task_name="Add user authentication",
        )

        # Check structure
        assert "# Task Plan: Add user authentication" in result
        assert "**Session ID**: 20251103120000" in result
        assert "**Task Type**: feature" in result
        assert "**Status**: 🚧 In Progress" in result

        # Check phases specific to feature
        assert "Phase 1: Research & Design" in result
        assert "Phase 2: Write Tests (TDD)" in result
        assert "Phase 3: Implementation" in result
        assert "Phase 4: Quality Checks" in result
        assert "Phase 5: Documentation" in result

    def test_load_bugfix_template(self) -> None:
        """Test loading bugfix template with different phases."""
        result = load_template(
            task_type="bugfix",
            session_id="20251103120000",
            task_name="Fix validation bug",
        )

        # Check structure
        assert "# Task Plan: Fix validation bug" in result
        assert "**Task Type**: bugfix" in result

        # Check phases specific to bugfix
        assert "Phase 1: Reproduce Bug" in result
        assert "Phase 2: Write Regression Test" in result
        assert "Phase 3: Fix Implementation" in result
        assert "Phase 4: Verify Fix" in result
        assert "Phase 5: Quality Checks" in result

    def test_load_docs_template_no_testing_phase(self) -> None:
        """Test loading docs template doesn't include testing phase."""
        result = load_template(
            task_type="docs",
            session_id="20251103120000",
            task_name="Update README",
        )

        # Check structure
        assert "# Task Plan: Update README" in result
        assert "**Task Type**: docs" in result

        # Docs should NOT have testing phase
        assert "Write Tests" not in result
        assert "Write Regression Test" not in result

        # Should have docs-specific phases
        assert "Phase 1: Review Current Docs" in result or "Review" in result
        assert "Phase 2: Update Documentation" in result or "Update" in result

    def test_load_refactor_template(self) -> None:
        """Test loading refactor template."""
        result = load_template(
            task_type="refactor",
            session_id="20251103120000",
            task_name="Refactor validators",
        )

        # Check structure
        assert "# Task Plan: Refactor validators" in result
        assert "**Task Type**: refactor" in result

        # Check phases specific to refactor
        assert "Phase 1: Ensure Test Coverage" in result or "Test Coverage" in result
        assert "Phase 2: Refactor Code" in result or "Refactor" in result
        assert "Phase 3: Verify Tests Pass" in result or "Verify" in result

    def test_load_template_with_special_characters_in_name(self) -> None:
        """Test loading template with special characters in task name."""
        result = load_template(
            task_type="feature",
            session_id="20251103120000",
            task_name="Add email validation & phone verification",
        )

        # Should handle special characters properly
        assert "Add email validation & phone verification" in result

    def test_unknown_task_type_raises_error(self) -> None:
        """Test loading unknown task type raises appropriate error."""
        with pytest.raises(TemplateNotFoundError) as exc_info:
            load_template(
                task_type="invalid_type",
                session_id="123",
                task_name="Test",
            )

        error_message = str(exc_info.value)
        assert "invalid_type" in error_message.lower()
        assert "feature" in error_message.lower()  # Should suggest valid types


class TestTemplateContent:
    """Test that loaded templates have required sections."""

    @pytest.mark.parametrize(
        "task_type",
        ["feature", "bugfix", "docs", "refactor"],
    )
    def test_template_has_required_sections(self, task_type: str) -> None:
        """Test all templates have required sections."""
        result = load_template(task_type=task_type, session_id="123", task_name="Test")

        # All templates should have these sections
        required_sections = [
            "# Task Plan:",
            "**Session ID**:",
            "**Created**:",
            "**Task Type**:",
            "**Status**:",
            "## Objective",
            "## Context",
            "## Implementation Steps",
            "## Files to Change",
            "## Risks & Considerations",
            "## Notes",
        ]

        for section in required_sections:
            assert section in result, f"Template {task_type} missing section: {section}"

    @pytest.mark.parametrize(
        "task_type",
        ["feature", "bugfix", "docs", "refactor"],
    )
    def test_template_has_checkboxes(self, task_type: str) -> None:
        """Test all templates have checkbox items."""
        result = load_template(task_type=task_type, session_id="123", task_name="Test")

        # Should have multiple checkbox items
        checkbox_count = result.count("- [ ]")
        assert checkbox_count >= 5, f"Template {task_type} has too few checkboxes"

    def test_templates_are_different(self) -> None:
        """Test that different task types have different content."""
        feature = load_template(task_type="feature", session_id="123", task_name="Test")
        bugfix = load_template(task_type="bugfix", session_id="123", task_name="Test")
        docs = load_template(task_type="docs", session_id="123", task_name="Test")
        refactor = load_template(
            task_type="refactor", session_id="123", task_name="Test"
        )

        # Templates should be different
        assert feature != bugfix
        assert feature != docs
        assert feature != refactor
        assert bugfix != docs
