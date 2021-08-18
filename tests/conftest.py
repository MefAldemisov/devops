import pytest
from app_python import create_app


@pytest.fixture
def app():
    """
    The 'app' instance generator
    :return: the Flask instance with the app
    """
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """
    The 'client' instance generator
    :param app: the Flask app, which will be called by a client
    :return: the Client instance
    """
    return app.test_client()
