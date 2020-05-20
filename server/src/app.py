import socket
import os
import logging
from flask import Flask
from config import DevConfig, ProdConfig


def create_app(current_config):
    app = Flask(__name__)
    app.config.from_object(current_config)

    from flask_cors import CORS
    CORS(app, resources={r"/quote/*": {"origins": "*"}})

    from models import db
    db.init_app(app)

    from api import api_blueprint
    app.register_blueprint(api_blueprint)

    return app


def get_config():
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    if socket.gethostname() == DevConfig.HOST_MACHINE:
        return DevConfig.CONFIG_NAME
    if socket.gethostname() == ProdConfig.HOST_MACHINE:
        return ProdConfig.CONFIG_NAME


app = create_app(get_config())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    app.logger = logging.getLogger(__name__)
    app.logger.setLevel(logging.DEBUG)
