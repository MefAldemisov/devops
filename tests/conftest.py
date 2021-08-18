import pytest
from app_python import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()