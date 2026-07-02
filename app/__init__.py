#Importing flask as this file will handle the initialization of the server.
from flask import Flask
#Importing dotenve and using load_dotenv so we can extract the secret key from the .env file.
from dotenv import load_dotenv
#Importing os so we can manipulate files on the computer.
import os

load_dotenv()

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
        )

    app.secret_key = os.getenv("SECRET_KEY", "placeholdersecretkey")

    from .routes import routes
    app.register_blueprint(routes)

    return app
