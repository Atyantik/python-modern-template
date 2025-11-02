"""Tests for the main module."""

import sys
from unittest.mock import patch

import pytest
from pytest import CaptureFixture

from leadership_blog_generator import __version__, generate_blog, main


class TestPackage:
    """Test package-level attributes."""

    def test_version(self) -> None:
        """Test that version is set correctly."""
        assert __version__ == "0.1.0"


class TestMain:
    """Test cases for the main function."""

    def test_main_no_args(self, capsys: CaptureFixture[str]) -> None:
        """Test that main without arguments shows welcome message."""
        with patch.object(sys, "argv", ["leadership-blog-generator"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Welcome to Leadership Blog Generator!" in captured.out

    def test_main_with_topic(self, capsys: CaptureFixture[str]) -> None:
        """Test main with topic argument."""
        with patch.object(
            sys, "argv", ["leadership-blog-generator", "--topic", "Leadership"]
        ):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Leadership" in captured.out
            assert "500 words" in captured.out

    def test_main_with_topic_and_length(self, capsys: CaptureFixture[str]) -> None:
        """Test main with topic and length arguments."""
        with patch.object(
            sys,
            "argv",
            ["leadership-blog-generator", "--topic", "Test Topic", "--length", "1000"],
        ):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Test Topic" in captured.out
            assert "1000 words" in captured.out


class TestGenerateBlog:
    """Test cases for the generate_blog function."""

    def test_generate_blog_with_topic(self, sample_topic: str) -> None:
        """Test blog generation with a topic."""
        result = generate_blog(sample_topic)
        assert sample_topic in result
        assert "500 words" in result

    def test_generate_blog_with_custom_length(self, sample_topic: str) -> None:
        """Test blog generation with custom length."""
        custom_length = 750
        result = generate_blog(sample_topic, length=custom_length)
        assert sample_topic in result
        assert str(custom_length) in result

    @pytest.mark.parametrize(
        "topic",
        [
            "Leadership in Crisis",
            "Building Trust",
            "Remote Team Management",
        ],
    )
    def test_generate_blog_various_topics(self, topic: str) -> None:
        """Test blog generation with various topics."""
        result = generate_blog(topic)
        assert topic in result
        assert isinstance(result, str)
