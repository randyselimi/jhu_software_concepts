"""
Registers blueprints and runs web app
"""
from flask import Flask
from pages.home import home
from pages.contact import contact
from pages.publications import publications

def create_app():
    """
    Creates a web app and registers blueprints
    """
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(contact.bp)
    app.register_blueprint(publications.bp)

    return app

def main():
    """
    Runs the web app
    """
    app = create_app()
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
