"""Tests for AI summarizer module.

This module tests the NLP-based summarization functions that auto-populate
PLAN sections from task descriptions and context.
"""

from __future__ import annotations

from scripts.ai_tools.summarizer import (
    analyze_task_type_and_scope,
    extract_file_patterns,
    extract_objective_from_task_description,
    generate_context_summary,
    identify_risks_from_description,
)


class TestExtractObjectiveFromTaskDescription:
    """Tests for extract_objective_from_task_description function."""

    def test_extracts_objective_from_simple_task(self) -> None:
        """Test extraction from simple task description."""
        # Arrange
        task_name = "Add email validation to user registration"

        # Act
        objective = extract_objective_from_task_description(task_name)

        # Assert
        assert "email validation" in objective.lower()
        assert "user registration" in objective.lower()
        assert len(objective) > 20  # Should be a meaningful sentence

    def test_extracts_objective_from_fix_task(self) -> None:
        """Test extraction from bug fix task description."""
        # Arrange
        task_name = "Fix authentication error on login page"

        # Act
        objective = extract_objective_from_task_description(task_name)

        # Assert
        assert "fix" in objective.lower() or "resolve" in objective.lower()
        assert "authentication" in objective.lower()
        assert "login" in objective.lower()

    def test_extracts_objective_from_refactor_task(self) -> None:
        """Test extraction from refactor task description."""
        # Arrange
        task_name = "Refactor database connection pooling for better performance"

        # Act
        objective = extract_objective_from_task_description(task_name)

        # Assert
        assert "refactor" in objective.lower() or "improve" in objective.lower()
        assert "database" in objective.lower()
        assert "performance" in objective.lower()

    def test_handles_short_task_name(self) -> None:
        """Test handling of very short task names."""
        # Arrange
        task_name = "Add tests"

        # Act
        objective = extract_objective_from_task_description(task_name)

        # Assert
        assert "test" in objective.lower()
        assert len(objective) > 10  # Should expand on the short name

    def test_handles_technical_terms(self) -> None:
        """Test handling of technical terms and acronyms."""
        # Arrange
        task_name = "Implement JWT authentication with OAuth2 flow"

        # Act
        objective = extract_objective_from_task_description(task_name)

        # Assert
        assert "JWT" in objective or "authentication" in objective.lower()
        assert "OAuth" in objective or "oauth" in objective.lower()


class TestGenerateContextSummary:
    """Tests for generate_context_summary function."""

    def test_generates_context_with_no_existing_context(self) -> None:
        """Test context generation when no context files exist."""
        # Arrange
        task_name = "Add new feature"
        task_type = "feature"

        # Act
        context = generate_context_summary(task_name, task_type)

        # Assert
        assert "Recent Decisions" in context
        assert "Related Conventions" in context
        assert isinstance(context, str)
        assert len(context) > 50

    def test_generates_context_for_feature_task(self) -> None:
        """Test context generation for feature task type."""
        # Arrange
        task_name = "Add email validation"
        task_type = "feature"

        # Act
        context = generate_context_summary(task_name, task_type)

        # Assert
        assert "functionality" in context.lower() or "feature" in context.lower()
        assert "RECENT_DECISIONS.md" in context or "Recent Decisions" in context
        assert "CONVENTIONS.md" in context or "Conventions" in context

    def test_generates_context_for_bugfix_task(self) -> None:
        """Test context generation for bugfix task type."""
        # Arrange
        task_name = "Fix login error"
        task_type = "bugfix"

        # Act
        context = generate_context_summary(task_name, task_type)

        # Assert
        assert "bug" in context.lower() or "fix" in context.lower()
        assert "Recent Decisions" in context

    def test_includes_dependencies_section(self) -> None:
        """Test that context includes Dependencies section."""
        # Arrange
        task_name = "Add feature"
        task_type = "feature"

        # Act
        context = generate_context_summary(task_name, task_type)

        # Assert
        assert "Dependencies" in context or "dependencies" in context.lower()


class TestAnalyzeTaskTypeAndScope:
    """Tests for analyze_task_type_and_scope function."""

    def test_identifies_feature_task(self) -> None:
        """Test identification of feature tasks."""
        # Arrange
        task_name = "Add new email validation feature"

        # Act
        analysis = analyze_task_type_and_scope(task_name)

        # Assert
        assert analysis["type"] == "feature"
        assert "scope" in analysis
        assert "complexity" in analysis

    def test_identifies_bugfix_task(self) -> None:
        """Test identification of bugfix tasks."""
        # Arrange
        task_name = "Fix authentication error on login"

        # Act
        analysis = analyze_task_type_and_scope(task_name)

        # Assert
        assert analysis["type"] == "bugfix"

    def test_identifies_refactor_task(self) -> None:
        """Test identification of refactor tasks."""
        # Arrange
        task_name = "Refactor database connection pooling"

        # Act
        analysis = analyze_task_type_and_scope(task_name)

        # Assert
        assert analysis["type"] == "refactor"

    def test_identifies_docs_task(self) -> None:
        """Test identification of documentation tasks."""
        # Arrange
        task_name = "Update API documentation for authentication"

        # Act
        analysis = analyze_task_type_and_scope(task_name)

        # Assert
        assert analysis["type"] == "docs"

    def test_estimates_scope_from_keywords(self) -> None:
        """Test scope estimation from task keywords."""
        # Arrange
        task_name = "Complete rewrite of authentication system with OAuth2 and JWT"

        # Act
        analysis = analyze_task_type_and_scope(task_name)

        # Assert
        assert "scope" in analysis
        assert analysis["scope"] in ["small", "medium", "large"]

    def test_detects_complexity_indicators(self) -> None:
        """Test detection of complexity indicators."""
        # Arrange
        task_name = "Implement distributed caching with Redis cluster"

        # Act
        analysis = analyze_task_type_and_scope(task_name)

        # Assert
        assert "complexity" in analysis
        assert analysis["complexity"] in ["low", "medium", "high"]


class TestExtractFilePatterns:
    """Tests for extract_file_patterns function."""

    def test_extracts_python_file_patterns(self) -> None:
        """Test extraction of Python file patterns."""
        # Arrange
        task_name = "Add email validation to user_auth.py module"

        # Act
        patterns = extract_file_patterns(task_name)

        # Assert
        assert "user_auth.py" in patterns or "user_auth" in str(patterns)

    def test_extracts_module_patterns(self) -> None:
        """Test extraction of module name patterns."""
        # Arrange
        task_name = "Refactor authentication module"

        # Act
        patterns = extract_file_patterns(task_name)

        # Assert
        assert "authentication" in str(patterns).lower()

    def test_extracts_test_file_patterns(self) -> None:
        """Test extraction of test file patterns."""
        # Arrange
        task_name = "Add tests for email validation"

        # Act
        patterns = extract_file_patterns(task_name)

        # Assert
        assert any("test" in p.lower() for p in patterns)

    def test_returns_empty_list_for_generic_task(self) -> None:
        """Test handling of tasks without specific file references."""
        # Arrange
        task_name = "Improve code quality"

        # Act
        patterns = extract_file_patterns(task_name)

        # Assert
        assert isinstance(patterns, list)

    def test_extracts_multiple_file_patterns(self) -> None:
        """Test extraction of multiple file patterns."""
        # Arrange
        task_name = "Update user.py and auth.py for new validation"

        # Act
        patterns = extract_file_patterns(task_name)

        # Assert
        assert len(patterns) >= 1
        assert any("user" in p.lower() or "auth" in p.lower() for p in patterns)


class TestIdentifyRisksFromDescription:
    """Tests for identify_risks_from_description function."""

    def test_identifies_database_risks(self) -> None:
        """Test identification of database-related risks."""
        # Arrange
        task_name = "Refactor database schema for user tables"

        # Act
        risks = identify_risks_from_description(task_name)

        # Assert
        assert len(risks) > 0
        assert any("database" in r.lower() or "migration" in r.lower() for r in risks)

    def test_identifies_authentication_risks(self) -> None:
        """Test identification of authentication-related risks."""
        # Arrange
        task_name = "Update authentication system with new OAuth2 flow"

        # Act
        risks = identify_risks_from_description(task_name)

        # Assert
        assert len(risks) > 0
        assert any(
            "authentication" in r.lower() or "security" in r.lower() for r in risks
        )

    def test_identifies_api_breaking_risks(self) -> None:
        """Test identification of API breaking change risks."""
        # Arrange
        task_name = "Change API endpoint structure for user management"

        # Act
        risks = identify_risks_from_description(task_name)

        # Assert
        assert len(risks) > 0
        assert any("API" in r or "breaking" in r.lower() for r in risks)

    def test_identifies_performance_risks(self) -> None:
        """Test identification of performance-related risks."""
        # Arrange
        task_name = "Implement new caching layer for database queries"

        # Act
        risks = identify_risks_from_description(task_name)

        # Assert
        assert len(risks) > 0
        assert any("performance" in r.lower() or "cach" in r.lower() for r in risks)

    def test_returns_empty_for_low_risk_task(self) -> None:
        """Test handling of low-risk tasks."""
        # Arrange
        task_name = "Update documentation formatting"

        # Act
        risks = identify_risks_from_description(task_name)

        # Assert
        assert isinstance(risks, list)
        # May have minimal or no risks for simple doc updates

    def test_identifies_multiple_risk_categories(self) -> None:
        """Test identification of multiple risk types."""
        # Arrange
        task_name = "Migrate database to new schema and update authentication API"

        # Act
        risks = identify_risks_from_description(task_name)

        # Assert
        assert len(risks) >= 2  # Should identify multiple risk categories
