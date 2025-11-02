"""Pytest configuration and shared fixtures."""

from typing import Any

import pytest


@pytest.fixture
def sample_topic() -> str:
    """Provide a sample topic for testing."""
    return "Effective Team Leadership"


@pytest.fixture
def mock_config() -> dict[str, Any]:
    """Provide a mock configuration for testing."""
    return {
        "api_key": "test-key",
        "model": "test-model",
        "max_length": 1000,
    }
