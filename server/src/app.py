from flask import Flask
import config


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username=config.load("DB_USERNAME"),
        password=config.load("DB_PASSWORD"),
        hostname=config.load("DB_HOSTNAME"),
        databasename=config.load("DB_NAME"),
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from models import db
    db.init_app(app)

    from api import api_blueprint

    app.register_blueprint(api_blueprint)

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
