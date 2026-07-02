#Importing flask as this file will handle the initialization of the server.
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import routes
    app.register_blueprint(routes)

    return app
