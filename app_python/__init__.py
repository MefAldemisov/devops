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

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
