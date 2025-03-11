from flask import Blueprint

from users.controllers import create_user, list_users, detail_user


users_blueprint = Blueprint('users', __name__)

users_blueprint.add_url_rule('/users', view_func=create_user, methods=['POST'])
users_blueprint.add_url_rule('/users', view_func=list_users, methods=['GET'])
users_blueprint.add_url_rule('/users/<int:user_id>/', view_func=detail_user, methods=['GET'])
