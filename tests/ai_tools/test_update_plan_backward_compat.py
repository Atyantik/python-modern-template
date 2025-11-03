"""Backward compatibility tests for ai-update-plan.

CRITICAL: These tests ensure that extending ai-update-plan with new editing
features does NOT break existing functionality. All existing commands must
continue to work exactly as before.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from scripts.ai_tools.update_plan import update_plan

# Patch targets - extracted to avoid Black/Ruff formatting conflicts
PATCH_GET_CURRENT_SESSION = "scripts.ai_tools.update_plan.get_current_session"
PATCH_GET_SESSION_FILES = "scripts.ai_tools.update_plan.get_session_files"


@pytest.fixture
def mock_session_setup(tmp_path: Path) -> tuple[str, Path]:
    """Set up mock session with plan file.

    Args:
        tmp_path: Pytest temporary directory

    Returns:
        Tuple of (session_id, plan_file_path)
    """
    session_id = "20251103120000"
    plan_content = """# Task Plan: Test

### Phase 1: Testing
- [ ] Write tests
- [ ] Run tests
- [x] Completed task

### Phase 2: Implementation
- [ ] Implement feature
"""

    # Create mock plan file
    plan_file = tmp_path / f"{session_id}-PLAN-test.md"
    plan_file.write_text(plan_content)

    return session_id, plan_file


class TestBackwardCompatibilityCheckboxMode:
    """Test that existing checkbox functionality still works."""

    def test_check_item_still_works(self, mock_session_setup: tuple[str, Path]) -> None:
        """Test that checking an item works exactly as before."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Old command: ai-update-plan "Write tests"
                update_plan(item="Write tests", check=True, session_id=session_id)

                # Verify item was checked
                updated_content = plan_file.read_text()
                assert "- [x] Write tests" in updated_content

    def test_uncheck_item_still_works(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that unchecking an item works exactly as before."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Old command: ai-update-plan "Completed task" --uncheck
                update_plan(item="Completed task", uncheck=True, session_id=session_id)

                # Verify item was unchecked
                updated_content = plan_file.read_text()
                assert "- [ ] Completed task" in updated_content

    def test_show_plan_still_works(
        self, mock_session_setup: tuple[str, Path], capsys: Any
    ) -> None:
        """Test that showing plan works exactly as before."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Old command: ai-update-plan --show
                update_plan(show=True, session_id=session_id)

                # Verify output contains plan
                captured = capsys.readouterr()
                assert "# Task Plan: Test" in captured.out
                assert "Progress:" in captured.out

    def test_default_behavior_unchanged(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that default behavior (check) is unchanged."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Old command: ai-update-plan "Run tests" (defaults to check=True)
                update_plan(item="Run tests", session_id=session_id)

                # Should check the item by default
                updated_content = plan_file.read_text()
                assert "- [x] Run tests" in updated_content

    def test_partial_match_still_works(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that partial matching still works as before."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Old behavior: partial match on "Implement"
                update_plan(item="Implement", session_id=session_id)

                # Should match "Implement feature"
                updated_content = plan_file.read_text()
                assert "- [x] Implement feature" in updated_content


class TestBackwardCompatibilityModeDetection:
    """Test that mode detection correctly identifies checkbox vs edit mode."""

    def test_no_edit_flags_uses_checkbox_mode(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that absence of edit flags uses checkbox mode."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # No edit flags provided = checkbox mode
                update_plan(item="Write tests", session_id=session_id)

                # Should toggle checkbox, not try to edit
                updated_content = plan_file.read_text()
                assert "- [x] Write tests" in updated_content
                # Plan structure unchanged
                assert "### Phase 1: Testing" in updated_content

    def test_item_parameter_alone_triggers_checkbox_mode(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that providing only item parameter triggers checkbox mode."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Just item parameter = checkbox mode (not edit mode)
                update_plan(item="Write tests", session_id=session_id)

                # Should check the item
                updated_content = plan_file.read_text()
                assert "- [x] Write tests" in updated_content


class TestBackwardCompatibilityErrorHandling:
    """Test that error handling is unchanged for existing functionality."""

    def test_item_not_found_error_unchanged(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that item not found error is unchanged."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Should exit with error when item not found
                with pytest.raises(SystemExit):
                    update_plan(item="Non-existent item", session_id=session_id)

    def test_no_session_error_unchanged(self) -> None:
        """Test that no session error is unchanged."""
        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:
            mock_session.return_value = None

            # Should exit with error when no session
            with pytest.raises(SystemExit):
                update_plan(item="Test item")

    def test_missing_item_without_show_error_unchanged(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that missing item parameter error is unchanged."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Should exit with error when item not provided and not showing
                with pytest.raises(SystemExit):
                    update_plan(item=None, show=False, session_id=session_id)


class TestBackwardCompatibilityOutputFormat:
    """Test that output format is unchanged for existing commands."""

    def test_success_message_format_unchanged(
        self, mock_session_setup: tuple[str, Path], capsys: Any
    ) -> None:
        """Test that success message format is unchanged."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                update_plan(item="Write tests", session_id=session_id)

                captured = capsys.readouterr()
                # Should contain session ID and progress
                assert session_id in captured.out
                assert "Progress:" in captured.out
                assert "items complete" in captured.out

    def test_progress_percentage_displayed(
        self, mock_session_setup: tuple[str, Path], capsys: Any
    ) -> None:
        """Test that progress percentage is still displayed."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                update_plan(item="Write tests", session_id=session_id)

                captured = capsys.readouterr()
                # Should show percentage (e.g., "50%")
                assert "%" in captured.out


class TestBackwardCompatibilityIntegration:
    """Integration tests for backward compatibility."""

    def test_multiple_checkbox_operations_work(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that multiple checkbox operations work sequentially."""
        session_id, plan_file = mock_session_setup

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Check first item
                update_plan(item="Write tests", session_id=session_id)
                content1 = plan_file.read_text()
                assert "- [x] Write tests" in content1

                # Check second item
                update_plan(item="Run tests", session_id=session_id)
                content2 = plan_file.read_text()
                assert "- [x] Run tests" in content2
                assert "- [x] Write tests" in content2  # First still checked

                # Uncheck first item
                update_plan(item="Write tests", uncheck=True, session_id=session_id)
                content3 = plan_file.read_text()
                assert "- [ ] Write tests" in content3
                assert "- [x] Run tests" in content3  # Second still checked

    def test_original_workflow_unchanged(
        self, mock_session_setup: tuple[str, Path]
    ) -> None:
        """Test that the original workflow is completely unchanged."""
        session_id, plan_file = mock_session_setup

        plan_file.read_text()

        with patch(PATCH_GET_CURRENT_SESSION) as mock_session:  # noqa: SIM117
            with patch(PATCH_GET_SESSION_FILES) as mock_files:
                mock_session.return_value = session_id
                mock_files.return_value = {"plan": plan_file}

                # Simulate original workflow: show, check, show
                update_plan(show=True, session_id=session_id)
                update_plan(item="Write tests", session_id=session_id)
                update_plan(show=True, session_id=session_id)

                # Verify plan structure unchanged (except for checked item)
                updated_content = plan_file.read_text()
                assert "# Task Plan: Test" in updated_content
                assert "### Phase 1: Testing" in updated_content
                assert "### Phase 2: Implementation" in updated_content
                # Only difference: Write tests is now checked
                assert "- [x] Write tests" in updated_content
