from flask import Flask
from pages.home import home
from pages.contact import contact
from pages.publications import publications

def create_app():
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(contact.bp)
    app.register_blueprint(publications.bp)

    return app

def main():
    app = create_app()
    app.run(host='0.0.0.0') 

if __name__ == '__main__':  
    main()
    