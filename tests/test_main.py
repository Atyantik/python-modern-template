"""Tests for the main module."""

from python_modern_template import __version__, main


class TestPackage:
    """Test package-level attributes."""

    def test_version(self) -> None:
        """Test that version is set correctly."""
        assert __version__ == "1.0.0"


class TestMain:
    """Test cases for the main function."""

    def test_main_returns_zero(self) -> None:
        """Test that main function returns 0."""
        result = main()
        assert result == 0

    def test_main_is_callable(self) -> None:
        """Test that main function is callable."""
        assert callable(main)
