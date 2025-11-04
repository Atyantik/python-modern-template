"""Tests for dependency configuration sanity."""

from __future__ import annotations

import tomllib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_dev_dependency_versions_are_realistic() -> None:
    """Ensure dev dependencies pin to realistic, currently available versions."""

    data = tomllib.loads((PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    dev_deps: list[str] = data["dependency-groups"]["dev"]

    expected = [
        "black>=24.8.0",
        "isort>=5.13.2",
        "mypy>=1.11.2",
        "pre-commit>=3.8.0",
        "pylint>=3.2.7",
        "pytest>=8.3.3",
        "pytest-cov>=4.1.0",
        "pytest-mock>=3.14.0",
        "ruff>=0.6.5",
    ]

    assert dev_deps == expected
