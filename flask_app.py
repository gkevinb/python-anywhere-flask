import sys
import socket
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["DEBUG"] = True

hostname = socket.gethostname()

if hostname == "blue-liveweb2":
    sql_config = {
        "username": "gkevinb",
        "password": "64zd32xk",
        "hostname": "gkevinb.mysql.pythonanywhere-services.com",
        "databasename": "gkevinb$flask"
    }

if hostname == "flask607":
    sql_config = {
        "username": "root",
        "password": "admin",
        "hostname": "db123",
        "databasename": "db"
    }

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=sql_config.get("username"),
    password=sql_config.get("password"),
    hostname=sql_config.get("hostname"),
    databasename=sql_config.get("databasename"),
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/')
def hello_world():
    joe = Person.query.first()
    return 'Hello world, Flask: {0}! on {1} and db: {2}!'.format(sys.version, socket.gethostname(), joe.name)

@app.route('/health')
def health():
    return 'This will be the health page.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)