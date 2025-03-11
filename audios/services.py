import os

from werkzeug.utils import secure_filename
from utils.helpers_files import UPLOAD_FOLDER


class AudioSaveService():

    def __init__(self, file) -> None:
        self.file = file
        self.filename = None

    def __generate_security_filename(self):
        self.filename = secure_filename(self.file.filename)

    def __ensure_upload_folder_exists(self):
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

    def save_file_local(self):
        self.__ensure_upload_folder_exists()

        self.__generate_security_filename()

        filepath = os.path.join(UPLOAD_FOLDER, self.filename)

        self.file.save(filepath)

        return filepath
