from flask import request, jsonify
from flask_jwt_extended import create_access_token

from authentication.schemas import AuthenticationSchema
from users.models import UserModel


def login():
    data = request.get_json()

    authentication_schema = AuthenticationSchema()

    errors = authentication_schema.validate(data)

    if errors:
        return jsonify(errors), 400

    email = data["email"]
    password = data["password"]

    existing_user = UserModel.query.filter_by(email=email).first()

    if not existing_user or not existing_user.check_password(password):
        return jsonify({"message": "Invalid email or password"}), 404

    try:
        access_token = create_access_token(identity=email)

        return jsonify(access_token=access_token), 200

    except Exception as e:
        print("error", str(e))

        return jsonify({"message": "Internal Server Error"}), 500
