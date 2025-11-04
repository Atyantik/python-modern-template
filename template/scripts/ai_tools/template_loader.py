"""Template loader for task-specific plan templates.

This module provides functionality to load and customize plan templates
based on task type (feature, bugfix, docs, refactor).
"""

from __future__ import annotations

from pathlib import Path

from scripts.ai_tools.utils import format_timestamp


class TemplateNotFoundError(Exception):
    """Raised when requested template file is not found."""


def get_template_path(task_type: str) -> Path:
    """Get path to template file for given task type.

    Args:
        task_type: Type of task (feature, bugfix, docs, refactor)

    Returns:
        Path to template file

    Raises:
        TemplateNotFoundError: If task type is unknown
    """
    valid_types = ["feature", "bugfix", "docs", "refactor"]

    if task_type not in valid_types:
        error_message = (
            f"Unknown task type: {task_type}. Valid types: {', '.join(valid_types)}"
        )
        raise TemplateNotFoundError(error_message)

    # Get templates directory (same directory as this module)
    templates_dir = Path(__file__).parent / "templates"
    template_file = templates_dir / f"{task_type}.md"

    return template_file


def substitute_variables(
    template: str,
    session_id: str,
    task_name: str,
    task_type: str,
) -> str:
    """Substitute template variables with actual values.

    Args:
        template: Template content with {{variable}} placeholders
        session_id: Session ID for this task
        task_name: Name of the task
        task_type: Type of task

    Returns:
        Template with all variables substituted
    """
    # Get current timestamp
    timestamp = format_timestamp()

    # Perform substitutions
    result = template.replace("{{session_id}}", session_id)
    result = result.replace("{{task_name}}", task_name)
    result = result.replace("{{task_type}}", task_type)
    result = result.replace("{{timestamp}}", timestamp)

    return result


def load_template(
    task_type: str,
    session_id: str,
    task_name: str,
) -> str:
    """Load and customize template for given task.

    Args:
        task_type: Type of task (feature, bugfix, docs, refactor)
        session_id: Session ID for this task
        task_name: Name of the task

    Returns:
        Customized template content ready to use

    Raises:
        TemplateNotFoundError: If template file not found or task type unknown
    """
    # Get template path
    template_path = get_template_path(task_type)

    # Check if file exists
    if not template_path.exists():
        error_message = (
            f"Template file not found: {template_path}. "
            f"Task type '{task_type}' is valid but template file is missing."
        )
        raise TemplateNotFoundError(error_message)

    # Load template content
    template_content = template_path.read_text()

    # Substitute variables
    result = substitute_variables(
        template_content,
        session_id=session_id,
        task_name=task_name,
        task_type=task_type,
    )

    return result
