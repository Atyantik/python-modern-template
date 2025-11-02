"""Configuration loader for quality tools - single source of truth."""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path to the project root (directory containing pyproject.toml)
    """
    # Start from this file's location and search upward
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent

    # Fallback to current working directory
    return Path.cwd()


def load_quality_config() -> dict[str, Any]:
    """Load quality configuration from pyproject.toml.

    Returns:
        Dictionary containing quality tool configuration

    Raises:
        FileNotFoundError: If pyproject.toml is not found
        KeyError: If [tool.quality] section is missing
    """
    project_root = get_project_root()
    pyproject_path = project_root / "pyproject.toml"

    if not pyproject_path.exists():
        raise FileNotFoundError(f"pyproject.toml not found at {pyproject_path}")

    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)

    if "tool" not in data or "quality" not in data["tool"]:
        raise KeyError(
            "[tool.quality] section not found in pyproject.toml. "
            "Please add quality configuration."
        )

    quality_config: dict[str, Any] = data["tool"]["quality"]
    return quality_config


def get_code_paths() -> list[str]:
    """Get list of paths to format and lint.

    Returns:
        List of directory paths to check
    """
    config = load_quality_config()
    paths: list[str] = config.get("code_paths", ["src", "tests"])
    return paths


def get_test_paths() -> list[str]:
    """Get list of paths containing tests.

    Returns:
        List of test directory paths
    """
    config = load_quality_config()
    paths: list[str] = config.get("test_paths", ["tests"])
    return paths


def get_min_coverage() -> int:
    """Get minimum coverage percentage required.

    Returns:
        Minimum coverage percentage (0-100)
    """
    config = load_quality_config()
    min_cov: int = config.get("min_coverage", 80)
    return min_cov


if __name__ == "__main__":
    # CLI for debugging/inspection
    print("Quality Tool Configuration")
    print("=" * 50)
    print(f"Project Root: {get_project_root()}")
    print(f"Code Paths: {get_code_paths()}")
    print(f"Test Paths: {get_test_paths()}")
    print(f"Min Coverage: {get_min_coverage()}%")
