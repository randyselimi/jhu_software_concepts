from flask import Flask
from pages.home import home

def create_app():
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(home.bp)
    return app

def main():
    app = create_app()
    app.run(host='0.0.0.0', port=8080) 

if __name__ == '__main__':  
    main()
    