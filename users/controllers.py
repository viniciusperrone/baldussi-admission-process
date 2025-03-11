from flask import jsonify, request

from config.db import db

from users.models import UserModel
from users.schemas import UserSchema


def create_user():
    data = request.get_json()

    user_schema = UserSchema()

    errors = user_schema.validate(data)

    if errors:
        return jsonify(errors), 400

    existing_registered_email = UserModel.query.filter_by(email=data["email"]).first()

    if existing_registered_email:
        return jsonify({"message": "Email already exist"}), 400


    new_user = UserModel(
        name=data["name"],
        email=data["email"],
    )

    new_user.set_password(data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()

        return jsonify(user_schema.dump(new_user)), 201

    except Exception as e:
        print(str(e))

        return jsonify({"message": "Internal Server Error"}), 500

def list_users():
    users = UserModel.query.all()

    user_schema = UserSchema(many=True)

    return jsonify(user_schema.dump(users)), 200
