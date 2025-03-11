import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from config.db import db

import users

from users.routes import users_blueprint


load_dotenv()

def initialize_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO')

    db.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(users_blueprint)

    return app

if __name__ == "__main__":
    app = initialize_app()

    app.run(
        host="127.0.0.1",
        port=5000
    )
