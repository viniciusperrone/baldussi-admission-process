import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from mongoengine import connect

from config.db import db

import users
import audios

from users.routes import users_blueprint
from authentication.routes import authentication_blueprint
from audios.routes import audios_blueprint


load_dotenv()

def initialize_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config["MONGO_URI"] = os.getenv('MONGO_URI')

    connect(host=os.getenv("MONGO_URI"))

    db.init_app(app)

    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    mongo = PyMongo(app)

    app.register_blueprint(users_blueprint)
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(audios_blueprint)

    return app

if __name__ == "__main__":
    app = initialize_app()

    app.run(
        host="127.0.0.1",
        port=5000
    )
