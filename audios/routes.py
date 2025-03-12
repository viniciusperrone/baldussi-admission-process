from flask import Blueprint

from audios.controllers import upload_file


audios_blueprint = Blueprint('audios', __name__)

audios_blueprint.add_url_rule('/audios/upload', view_func=upload_file, methods=['POST'])
