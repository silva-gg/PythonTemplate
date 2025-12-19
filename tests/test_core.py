"""
Unit tests for core module.

These tests use mocking to avoid external dependencies.
"""

import pytest
from unittest.mock import Mock, patch
from your_package.core import YourMainClass, your_utility_function


class TestYourMainClass:
    """Test suite for YourMainClass."""
    
    def test_init_default(self):
        """Test initialization with default parameters."""
        obj = YourMainClass(name="test")
        assert obj.name == "test"
        assert obj.config == {}
    
    def test_init_with_config(self):
        """Test initialization with custom configuration."""
        config = {"key": "value", "number": 42}
        obj = YourMainClass(name="test", config=config)
        assert obj.name == "test"
        assert obj.config == config
    
    def test_process(self):
        """Test process method."""
        obj = YourMainClass(name="test")
        result = obj.process("data")
        assert result == "Processed: data"
    
    def test_process_different_types(self):
        """Test process method with different input types."""
        obj = YourMainClass(name="test")
        
        # Test with string
        assert obj.process("text") == "Processed: text"
        
        # Test with number
        assert obj.process(123) == "Processed: 123"
        
        # Test with None
        assert obj.process(None) == "Processed: None"
    
    def test_get_info(self):
        """Test get_info method."""
        config = {"key": "value"}
        obj = YourMainClass(name="test", config=config)
        info = obj.get_info()
        
        assert info["name"] == "test"
        assert info["config"] == config


class TestUtilityFunctions:
    """Test suite for utility functions."""
    
    def test_utility_function_default(self):
        """Test utility function with default parameters."""
        result = your_utility_function("hello")
        assert result == "hello"
    
    def test_utility_function_uppercase(self):
        """Test utility function with uppercase option."""
        result = your_utility_function("hello", uppercase=True)
        assert result == "HELLO"
    
    def test_utility_function_empty_string(self):
        """Test utility function with empty string."""
        result = your_utility_function("")
        assert result == ""
        
        result = your_utility_function("", uppercase=True)
        assert result == ""


@pytest.fixture
def mock_instance():
    """Fixture providing a mock YourMainClass instance."""
    return YourMainClass(name="mock", config={"test": True})


def test_with_fixture(mock_instance):
    """Test using the fixture."""
    assert mock_instance.name == "mock"
    assert mock_instance.config["test"] is True


@pytest.mark.parametrize("input_value,expected", [
    ("test", "Processed: test"),
    (123, "Processed: 123"),
    (None, "Processed: None"),
])
def test_process_parametrized(input_value, expected):
    """Parametrized test for process method."""
    obj = YourMainClass(name="test")
    assert obj.process(input_value) == expected
