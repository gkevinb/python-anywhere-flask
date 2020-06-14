import logging
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("env.py")

    if app.config["ENV"] == "DEV":
        from flask_cors import CORS
        CORS(app, resources={r"/quotes/*": {"origins": "*"}})

    from models.model import db
    db.init_app(app)

    from blueprints.quotes import quotes
    app.register_blueprint(quotes)

    from blueprints.system import system
    app.register_blueprint(system)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    app.logger = logging.getLogger(__name__)
    app.logger.setLevel(logging.DEBUG)
