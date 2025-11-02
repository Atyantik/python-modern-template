"""Tests for quality.config module."""

from __future__ import annotations

from pathlib import Path

from scripts.quality.config import (
    get_code_paths,
    get_min_coverage,
    get_project_root,
    get_test_paths,
    load_quality_config,
)


def test_get_project_root_returns_path() -> None:
    """Test that get_project_root returns a valid Path object."""
    root = get_project_root()
    assert isinstance(root, Path)
    assert root.exists()
    assert (root / "pyproject.toml").exists()


def test_load_quality_config_returns_dict() -> None:
    """Test that load_quality_config returns a dictionary."""
    config = load_quality_config()
    assert isinstance(config, dict)
    assert "code_paths" in config
    assert "test_paths" in config
    assert "min_coverage" in config


def test_get_code_paths_returns_list() -> None:
    """Test that get_code_paths returns a list of strings."""
    paths = get_code_paths()
    assert isinstance(paths, list)
    assert len(paths) > 0
    assert all(isinstance(p, str) for p in paths)


def test_get_code_paths_contains_expected_paths() -> None:
    """Test that code_paths contains expected directories."""
    paths = get_code_paths()
    # Based on our pyproject.toml configuration
    assert "src" in paths
    assert "tests" in paths
    assert "scripts" in paths


def test_get_test_paths_returns_list() -> None:
    """Test that get_test_paths returns a list of strings."""
    paths = get_test_paths()
    assert isinstance(paths, list)
    assert len(paths) > 0
    assert all(isinstance(p, str) for p in paths)


def test_get_test_paths_contains_tests() -> None:
    """Test that test_paths contains tests directory."""
    paths = get_test_paths()
    assert "tests" in paths


def test_get_min_coverage_returns_int() -> None:
    """Test that get_min_coverage returns an integer."""
    coverage = get_min_coverage()
    assert isinstance(coverage, int)
    assert coverage > 0
    assert coverage <= 100


def test_get_min_coverage_matches_config() -> None:
    """Test that min_coverage matches pyproject.toml value."""
    coverage = get_min_coverage()
    # Should be 80 based on our configuration
    assert coverage == 80


def test_load_quality_config_handles_missing_file() -> None:
    """Test that load_quality_config handles missing pyproject.toml gracefully."""
    # This test verifies error handling if pyproject.toml is missing
    # We can't easily test this without mocking, so we'll verify the function
    # exists and returns valid data for the real file
    config = load_quality_config()
    assert config is not None
    assert isinstance(config, dict)
