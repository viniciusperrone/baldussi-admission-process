from flask import Blueprint

from audios.controllers import upload_file, list_transcriptions, detail_transcription, update_transcription, delete_transcription


audios_blueprint = Blueprint('audios', __name__)

audios_blueprint.add_url_rule('/audios/upload', view_func=upload_file, methods=['POST'])

audios_blueprint.add_url_rule('/transcriptions/list', view_func=list_transcriptions, methods=['GET'])
audios_blueprint.add_url_rule('/transcriptions/<string:transcription_id>/', view_func=detail_transcription, methods=['GET'])
audios_blueprint.add_url_rule('/transcriptions/<string:transcription_id>/', view_func=update_transcription, methods=['PUT'])
audios_blueprint.add_url_rule('/transcriptions/<string:transcription_id>/', view_func=delete_transcription, methods=['DELETE'])
