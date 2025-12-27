"""Pytest configuration and fixtures for Flask application testing."""

import pytest
from src import create_app


@pytest.fixture
def app():
    """
    Create and configure a test Flask application.

    Returns:
        Flask: Flask application configured for testing
    """
    app = create_app({'TESTING': True})
    return app


@pytest.fixture
def client(app):
    """
    Create a test client for the Flask application.

    Args:
        app: Flask application fixture

    Returns:
        FlaskClient: Test client for making requests to the application
    """
    return app.test_client()


@pytest.fixture
def app_context(app):
    """
    Create an application context for testing.

    Args:
        app: Flask application fixture

    Yields:
        AppContext: Application context for database access and other operations
    """
    with app.app_context():
        yield app
