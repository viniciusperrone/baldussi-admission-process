import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config.db import db
from config.mongo import mongo


load_dotenv()

def initialize_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config["MONGO_URI"] = os.getenv('MONGO_URI')

    db.init_app(app)
    mongo.init_app(app)

    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    swagger = Swagger(app)

    import users
    import transcriptions

    mongo.db.transcriptions.create_index([('title', 'text'), ('transcription_text', 'text')])

    from users.routes import users_blueprint
    from authentication.routes import authentication_blueprint
    from audios.routes import audios_blueprint
    from transcriptions.routes import transcriptions_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(audios_blueprint)
    app.register_blueprint(transcriptions_blueprint)


    return app

if __name__ == "__main__":
    app = initialize_app()

    app.run(
        host="127.0.0.1",
        port=5000
    )
