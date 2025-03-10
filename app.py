from flask import Flask


def initialize_app():
    app = Flask(__name__)

    return app

if __name__ == "__main__":
    app = initialize_app()

    app.run(
        host="127.0.0.1",
        port=5000
    )