"""
This module is responsible for the generation of the `pytest.fixture`s
"""
import pytest
from app_python import create_app


@pytest.fixture
def app():
    """
    The 'app' instance generator
    :return: the Flask instance with the app
    """
    application = create_app()
    yield application


@pytest.fixture
def client():
    """
    The 'client' instance generator
    :param app: the Flask app, which will be called by a client
    :return: the Client instance
    """
    return create_app().test_client()
