from flask import jsonify, request
from flask_jwt_extended import jwt_required

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

@jwt_required()
def list_users():
    page = request.args.get('page', 1, type=int)
    items_per_page = request.args.get('per_page', 10, type=int)

    pagination_users = UserModel.query.paginate(
        page=page,
        per_page=items_per_page,
        error_out=False
    )

    users = pagination_users.items

    users_schema = UserSchema(many=True)

    return jsonify({
        "total": pagination_users.total,
        "page": pagination_users.page,
        "per_page": pagination_users.per_page,
        "pages": pagination_users.page,
        "has_next": pagination_users.has_next,
        "has_prev": pagination_users.has_prev,
        "users": users_schema.dump(users)
    }), 200

@jwt_required()
def detail_user(user_id):
    user = UserModel.query.get(user_id)

    user_schema = UserSchema()

    if not user:
        return jsonify({"message": "Doesn't match user with given id"}), 404

    return jsonify(user_schema.dump(user)), 200
