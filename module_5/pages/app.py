"""
Simple Flask app that uses a blueprint for routing.

This module sets up a Flask web application and registers a blueprint for handling routes.
"""

from flask import Flask
from pages import home

def create_app():
    """
    Create and return a Flask app instance.
    """
    app = Flask(__name__)
    app.register_blueprint(home.bp)
    return app

def main():
    """
    Run the Flask app.
    """
    app = create_app()
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
