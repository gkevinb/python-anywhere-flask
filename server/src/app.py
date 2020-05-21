import socket
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

    from blueprints.quote import quote
    app.register_blueprint(quote)

    from blueprints.system import system
    app.register_blueprint(system)

    return app


def get_config():
    if socket.gethostname() == DevConfig.HOST_MACHINE:
        return DevConfig.CONFIG_NAME
    if socket.gethostname() == ProdConfig.HOST_MACHINE:
        return ProdConfig.CONFIG_NAME


app = create_app(get_config())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    app.logger = logging.getLogger(__name__)
    app.logger.setLevel(logging.DEBUG)
