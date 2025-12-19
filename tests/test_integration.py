"""
Integration tests for your package.

These tests may require external resources or configuration.
Skip them by default and run explicitly when needed.
"""

import pytest
from your_package.core import YourMainClass


# Mark all tests in this file as integration tests
pytestmark = pytest.mark.integration


@pytest.mark.skip(reason="Requires external configuration")
def test_integration_example():
    """
    Example integration test.
    
    This test demonstrates how to structure integration tests
    that require external resources or configuration.
    
    To run: pytest tests/test_integration.py -v -m integration
    """
    obj = YourMainClass(name="integration_test")
    
    # Example: Test with actual external service
    # result = obj.process_with_external_service(data)
    # assert result is not None
    
    assert obj.name == "integration_test"


@pytest.mark.skip(reason="Requires authentication")
def test_with_authentication():
    """
    Example test requiring authentication.
    
    You can check for environment variables or config files:
    
    import os
    if not os.getenv("API_KEY"):
        pytest.skip("API_KEY not set")
    """
    pass


class TestIntegrationWorkflow:
    """Test suite for end-to-end workflows."""
    
    @pytest.mark.skip(reason="Requires full setup")
    def test_complete_workflow(self):
        """Test a complete workflow from start to finish."""
        # Setup
        obj = YourMainClass(name="workflow_test")
        
        # Process
        result = obj.process("test_data")
        
        # Verify
        assert result is not None
    
    @pytest.fixture
    def integration_setup(self):
        """Fixture for integration test setup."""
        # Setup code (e.g., create test database, authenticate)
        yield
        # Teardown code (e.g., cleanup resources)
