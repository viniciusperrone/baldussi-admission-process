

UPLOAD_FOLDER = "uploads/audios"
ALLOWED_EXTENSIONS = {"mp3", "wav", "ogg", "mov"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
