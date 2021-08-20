"""
This module is responsible for the generation of the Flask instance
"""
from flask import Flask
from .main import blueprint


def create_app():
    """
    Factory of the Flask instance, the root of the project
    :return: the main Flask instance
    """
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app
