"""Tests for AI_DOCS and template sync validation."""

from __future__ import annotations

import subprocess
from pathlib import Path

from scripts.ai_tools.validate_ai_docs_sync import (
    check_file_exists,
    compare_files,
    find_ai_doc_files,
    find_template_files,
    generate_sync_report,
    validate_sync,
)


class TestFindAIDocFiles:
    """Test cases for finding AI_DOCS files."""

    def test_find_ai_doc_files_in_real_directory(self) -> None:
        """Test finding actual AI_DOCS files."""
        # Act
        files = find_ai_doc_files()

        # Assert
        assert len(files) > 0
        assert any("ai-tools.md" in str(f) for f in files)
        assert any("tdd-workflow.md" in str(f) for f in files)
        assert any("code-conventions.md" in str(f) for f in files)

    def test_find_ai_doc_files_returns_path_objects(self) -> None:
        """Test that function returns Path objects."""
        # Act
        files = find_ai_doc_files()

        # Assert
        assert all(isinstance(f, Path) for f in files)


class TestFindTemplateFiles:
    """Test cases for finding template files."""

    def test_find_template_files_in_real_directory(self) -> None:
        """Test finding actual template files."""
        # Act
        files = find_template_files()

        # Assert
        assert len(files) > 0
        # Should find template versions
        assert any("CLAUDE.md.jinja" in str(f) for f in files)

    def test_find_template_files_returns_path_objects(self) -> None:
        """Test that function returns Path objects."""
        # Act
        files = find_template_files()

        # Assert
        assert all(isinstance(f, Path) for f in files)


class TestCheckFileExists:
    """Test cases for file existence checking."""

    def test_check_file_exists_with_existing_file(self, tmp_path: Path) -> None:
        """Test checking an existing file."""
        # Arrange
        test_file = tmp_path / "test.txt"
        test_file.write_text("content")

        # Act
        result = check_file_exists(test_file)

        # Assert
        assert result is True

    def test_check_file_exists_with_missing_file(self, tmp_path: Path) -> None:
        """Test checking a missing file."""
        # Arrange
        test_file = tmp_path / "nonexistent.txt"

        # Act
        result = check_file_exists(test_file)

        # Assert
        assert result is False


class TestCompareFiles:
    """Test cases for file comparison."""

    def test_compare_files_identical_content(self, tmp_path: Path) -> None:
        """Test comparing files with identical content."""
        # Arrange
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        file1.write_text("same content\n")
        file2.write_text("same content\n")

        # Act
        are_same, diff = compare_files(file1, file2)

        # Assert
        assert are_same is True
        assert diff == ""

    def test_compare_files_different_content(self, tmp_path: Path) -> None:
        """Test comparing files with different content."""
        # Arrange
        file1 = tmp_path / "file1.txt"
        file2 = tmp_path / "file2.txt"
        file1.write_text("content A\n")
        file2.write_text("content B\n")

        # Act
        are_same, diff = compare_files(file1, file2)

        # Assert
        assert are_same is False
        assert diff != ""
        assert "content A" in diff or "content B" in diff

    def test_compare_files_with_jinja_template(self, tmp_path: Path) -> None:
        """Test comparing with Jinja template (should handle template syntax)."""
        # Arrange
        doc_file = tmp_path / "doc.md"
        template_file = tmp_path / "doc.md.jinja"
        doc_file.write_text("# Title\nContent here\n")
        template_file.write_text("# Title\nContent here\n")

        # Act
        are_same, diff = compare_files(doc_file, template_file, is_template=True)

        # Assert
        assert are_same is True


class TestValidateSync:
    """Test cases for sync validation."""

    def test_validate_sync_with_real_files(self) -> None:
        """Test validation with actual project files."""
        # Act
        issues = validate_sync()

        # Assert
        # Issues list should be returned (empty or with items)
        assert isinstance(issues, list)
        # Each issue should be a dict with required keys
        for issue in issues:
            assert "type" in issue
            assert "file" in issue
            assert "message" in issue

    def test_validate_sync_returns_list(self) -> None:
        """Test that validate_sync returns a list."""
        # Act
        result = validate_sync()

        # Assert
        assert isinstance(result, list)


class TestGenerateSyncReport:
    """Test cases for report generation."""

    def test_generate_sync_report_with_no_issues(self) -> None:
        """Test report generation with no issues."""
        # Arrange
        issues: list[dict[str, str]] = []

        # Act
        report = generate_sync_report(issues)

        # Assert
        assert "✅" in report or "PASSED" in report
        assert "Issues Found:** 0" in report

    def test_generate_sync_report_with_issues(self) -> None:
        """Test report generation with issues."""
        # Arrange
        issues = [
            {
                "type": "missing",
                "file": "AI_DOCS/test.md",
                "message": "Missing template file",
            },
            {
                "type": "different",
                "file": "AI_DOCS/test2.md",
                "message": "Content differs",
            },
        ]

        # Act
        report = generate_sync_report(issues)

        # Assert
        assert "❌" in report or "FAILED" in report
        assert "Total Issues:** 2" in report
        assert "missing" in report.lower()
        assert "differences" in report.lower()
        assert "AI_DOCS/test.md" in report
        assert "AI_DOCS/test2.md" in report

    def test_generate_sync_report_returns_string(self) -> None:
        """Test that report generation returns a string."""
        # Arrange
        issues: list[dict[str, str]] = []

        # Act
        result = generate_sync_report(issues)

        # Assert
        assert isinstance(result, str)
        assert len(result) > 0

    def test_generate_sync_report_includes_file_types_checked(self) -> None:
        """Test report includes list of file types checked."""
        # Arrange
        issues: list[dict[str, str]] = []

        # Act
        result = generate_sync_report(issues)

        # Assert
        assert "AI_DOCS" in result
        assert "CLAUDE.md" in result
        assert "AGENTS.md" in result


class TestCLIInterface:
    """Test cases for CLI interface."""

    def test_cli_command_runs_successfully(self) -> None:
        """Test that ai-validate-docs CLI command runs."""
        # Act
        result = subprocess.run(
            ["uv", "run", "ai-validate-docs"],
            capture_output=True,
            text=True,
            check=False,
        )

        # Assert
        # Command should complete (exit code 0 if all valid, 1 if issues found)
        assert result.returncode in [0, 1]
        # Output should contain report
        assert "AI_DOCS Sync Validation Report" in result.stdout
        assert "Status:" in result.stdout

    def test_cli_output_format(self) -> None:
        """Test that CLI output has expected format."""
        # Act
        result = subprocess.run(
            ["uv", "run", "ai-validate-docs"],
            capture_output=True,
            text=True,
            check=False,
        )

        # Assert
        output = result.stdout
        # Should have markdown-style report
        assert "#" in output  # Markdown headers
        assert "**" in output  # Markdown bold
        # Should mention file types checked
        assert "AI_DOCS" in output or "Files Checked" in output
