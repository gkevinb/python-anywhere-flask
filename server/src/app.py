import sys
import socket
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import models


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

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    joe = models.Person.query.first()
    return 'Hello world, Flask: {0}! on {1} and db: {2}!'.format(sys.version, socket.gethostname(), joe.name)

@app.route('/health')
def health():
    return f"This will be the health page. {config.load('HOST')}, {config.load('HOST_MACHINE')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)