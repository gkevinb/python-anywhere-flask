import sys
import socket
from flask import Blueprint
from models import Person
import config

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
def hello_world():
    joe = Person.query.first()
    return 'Hello world, Flask: {0}! on {1} and db: {2}!'.format(sys.version, socket.gethostname(), joe.name)


@api_blueprint.route('/health')
def health():
    return f"This will be the health page. {config.load('HOST')}, {config.load('HOST_MACHINE')}"