"""AI Summarizer - NLP-based auto-population of PLAN sections.

This module provides intelligent extraction and summarization of task
information to auto-populate PLAN file sections.
"""

from __future__ import annotations

import re

from scripts.ai_tools.utils import read_context_file


def extract_objective_from_task_description(task_name: str) -> str:
    """Extract and expand objective from task description.

    Analyzes the task name and creates a clear, detailed objective
    statement that describes what needs to be accomplished.

    Args:
        task_name: The task name/description provided by user

    Returns:
        Expanded objective statement
    """
    # Normalize task name
    task_lower = task_name.lower().strip()

    # Identify action verb
    action_verbs = {
        "add": "Implement",
        "create": "Create",
        "fix": "Resolve",
        "update": "Update",
        "refactor": "Refactor",
        "improve": "Enhance",
        "implement": "Implement",
        "remove": "Remove",
        "delete": "Remove",
        "optimize": "Optimize",
        "enhance": "Enhance",
    }

    # Find the action verb in task name
    action = "Implement"  # Default
    for verb, replacement in action_verbs.items():
        if task_lower.startswith(verb):
            action = replacement
            break

    # Build objective statement
    # Keep the original task name but ensure it's a complete sentence
    objective = f"{action} {task_name.strip()}"

    # If task doesn't end with punctuation, add period
    if not objective.endswith((".", "!", "?")):
        objective += "."

    # Make first letter uppercase if needed
    if objective[0].islower():
        objective = objective[0].upper() + objective[1:]

    # Add context about what will be delivered
    if "test" in task_lower and "add" in task_lower:
        objective += "\n\nThis will include comprehensive test coverage following TDD principles."
    elif any(word in task_lower for word in ["authentication", "security", "auth"]):
        objective += "\n\nThis will ensure security best practices are followed."
    elif "refactor" in task_lower:
        objective += "\n\nThis will improve code quality while maintaining existing functionality."
    elif "fix" in task_lower or "bug" in task_lower:
        objective += (
            "\n\nThis will resolve the identified issue and prevent regression."
        )

    return objective


def generate_context_summary(task_name: str, task_type: str) -> str:
    """Generate context summary for PLAN file.

    Creates a context section that includes recent decisions,
    conventions, and dependencies relevant to the task.

    Args:
        task_name: The task name/description
        task_type: Type of task (feature, bugfix, refactor, docs)

    Returns:
        Formatted context section content
    """
    context_parts = []

    # Read existing context files
    recent_decisions = read_context_file("RECENT_DECISIONS.md")
    conventions = read_context_file("CONVENTIONS.md")

    # Build context summary
    context_parts.append("**Recent Decisions**:")
    if recent_decisions and len(recent_decisions.strip()) > 0:
        context_parts.append(
            "See ./ai-context/RECENT_DECISIONS.md for latest decisions to follow."
        )
    else:
        context_parts.append("No recent decisions recorded yet.")

    context_parts.append("")
    context_parts.append("**Related Conventions**:")
    if conventions and len(conventions.strip()) > 0:
        context_parts.append("See ./AI_DOCS/code-conventions.md for coding standards.")
    else:
        context_parts.append("Standard coding conventions apply.")

    # Add task-type specific context
    context_parts.append("")
    context_parts.append("**Task Type Context**:")

    task_type_context = {
        "feature": "New functionality - ensure comprehensive tests and documentation.",
        "bugfix": "Bug resolution - reproduce issue first, then fix with tests.",
        "refactor": "Code improvement - maintain behavior, add tests if missing.",
        "docs": "Documentation update - ensure accuracy and completeness.",
    }

    context_parts.append(
        f"- {task_type_context.get(task_type, 'General task - follow TDD workflow.')}"
    )

    # Add dependencies section
    context_parts.append("")
    context_parts.append("**Dependencies**:")

    # Try to infer dependencies from task name
    task_lower = task_name.lower()
    dependencies_found = False

    if "database" in task_lower or "migration" in task_lower:
        context_parts.append("- [ ] Database schema/migration review")
        dependencies_found = True

    if any(word in task_lower for word in ["api", "endpoint", "integration"]):
        context_parts.append("- [ ] API contract review")
        dependencies_found = True

    if "authentication" in task_lower or "auth" in task_lower:
        context_parts.append("- [ ] Security review")
        dependencies_found = True

    if not dependencies_found:
        context_parts.append("- [ ] None identified yet")

    return "\n".join(context_parts)


def analyze_task_type_and_scope(task_name: str) -> dict[str, str]:
    """Analyze task to determine type and scope.

    Uses keyword analysis to classify the task and estimate its
    complexity and scope.

    Args:
        task_name: The task name/description

    Returns:
        Dictionary with 'type', 'scope', and 'complexity' keys
    """
    task_lower = task_name.lower()

    # Determine task type
    task_type = "feature"  # Default

    if any(word in task_lower for word in ["fix", "bug", "error", "issue"]):
        task_type = "bugfix"
    elif any(word in task_lower for word in ["refactor", "improve", "optimize"]):
        task_type = "refactor"
    elif any(word in task_lower for word in ["document", "docs", "readme", "guide"]):
        task_type = "docs"

    # Estimate scope based on keywords
    scope_indicators = {
        "large": [
            "complete",
            "entire",
            "system",
            "rewrite",
            "migration",
            "overhaul",
        ],
        "medium": ["module", "component", "service", "integration", "update"],
        "small": ["fix", "add", "update", "minor", "simple"],
    }

    scope = "medium"  # Default
    for size, keywords in scope_indicators.items():
        if any(keyword in task_lower for keyword in keywords):
            scope = size
            break

    # Estimate complexity based on technical indicators
    complexity_indicators = {
        "high": [
            "distributed",
            "concurrent",
            "async",
            "cluster",
            "scaling",
            "architecture",
        ],
        "medium": [
            "database",
            "authentication",
            "api",
            "integration",
            "caching",
        ],
        "low": ["documentation", "formatting", "style", "typo", "comment"],
    }

    complexity = "medium"  # Default
    for level, keywords in complexity_indicators.items():
        if any(keyword in task_lower for keyword in keywords):
            complexity = level
            break

    return {
        "type": task_type,
        "scope": scope,
        "complexity": complexity,
    }


def extract_file_patterns(task_name: str) -> list[str]:
    """Extract file and module patterns from task description.

    Identifies specific files, modules, or patterns mentioned in
    the task description.

    Args:
        task_name: The task name/description

    Returns:
        List of file/module patterns found
    """
    patterns = []

    # Pattern 1: Explicit file names (*.py, *.md, etc.)
    file_pattern = r"\b([a-zA-Z0-9_]+\.(py|md|txt|yml|yaml|toml|json))\b"
    file_matches = re.findall(file_pattern, task_name)
    patterns.extend([match[0] for match in file_matches])

    # Pattern 2: Module names with underscores
    module_pattern = r"\b([a-z][a-z0-9_]+)\b"
    words = task_name.lower().split()

    # Common module/package indicators
    module_indicators = [
        "module",
        "package",
        "component",
        "service",
        "handler",
        "manager",
        "controller",
        "model",
        "view",
        "utils",
        "helpers",
    ]

    for i, word in enumerate(words):
        if word in module_indicators and i > 0:
            # Previous word might be the module name
            prev_word = words[i - 1]
            if re.match(module_pattern, prev_word):
                patterns.append(prev_word)

    # Pattern 3: Test file patterns
    if "test" in task_name.lower():
        patterns.append("tests/")

    # Remove duplicates while preserving order
    seen = set()
    unique_patterns = []
    for pattern in patterns:
        if pattern not in seen:
            seen.add(pattern)
            unique_patterns.append(pattern)

    return unique_patterns


def identify_risks_from_description(task_name: str) -> list[str]:
    """Identify potential risks from task description.

    Analyzes the task to identify common risk categories and
    potential issues to watch out for.

    Args:
        task_name: The task name/description

    Returns:
        List of identified risks and considerations
    """
    risks = []
    task_lower = task_name.lower()

    # Database-related risks
    if any(word in task_lower for word in ["database", "schema", "migration", "db"]):
        risks.append(
            "Database changes may require migration and could affect existing data"
        )
        risks.append("Consider backup and rollback strategy")

    # Authentication/Security risks
    if any(
        word in task_lower for word in ["authentication", "auth", "security", "oauth"]
    ):
        risks.append("Security implications - ensure thorough review and testing")
        risks.append("May affect existing user sessions or authentication flows")

    # API-related risks
    if any(word in task_lower for word in ["api", "endpoint", "interface"]):
        if any(
            word in task_lower
            for word in ["change", "update", "modify", "refactor", "break"]
        ):
            risks.append("API changes may break existing clients - versioning needed")
        risks.append("Ensure backward compatibility or provide migration path")

    # Performance-related risks
    if any(
        word in task_lower
        for word in ["performance", "optimization", "caching", "scaling"]
    ):
        risks.append("Performance changes need benchmarking and testing")
        risks.append("May have different behavior under load")

    # Refactoring risks
    if "refactor" in task_lower:
        risks.append("Ensure comprehensive test coverage before refactoring")
        risks.append("Risk of introducing regressions - test thoroughly")

    # Integration risks
    if "integration" in task_lower or "external" in task_lower:
        risks.append(
            "External dependencies may have availability or reliability issues"
        )
        risks.append("Need error handling for third-party service failures")

    # Large scope risks
    if any(
        word in task_lower
        for word in ["complete", "entire", "system", "rewrite", "overhaul"]
    ):
        risks.append("Large scope - consider breaking into smaller tasks")
        risks.append("Extended development time may lead to merge conflicts")

    return risks
