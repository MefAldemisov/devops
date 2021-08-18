"""
This module is responsible for the generation of the Flask instance
"""
from flask import Flask
from app_python import main


def create_app():
    """
    Factory of the Flask instance, the root of the project
    :return: the main Flask instance
    """
    app = Flask(__name__)
    app.register_blueprint(main.blueprint)
    return app
