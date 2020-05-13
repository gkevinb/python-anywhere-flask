import sys
import socket
from flask import Blueprint, current_app
from models import Person, Quote

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
def hello_world():
    joe = Person.query.first()
    return 'Hello world, Flask: {0}! on {1} and db: {2}!'.format(sys.version, socket.gethostname(), joe.name)


@api_blueprint.route('/health')
def health():
    return f"This will be the health page. {current_app.config['HOST']}, {current_app.config['HOST_MACHINE']}"


@api_blueprint.route('/quote/first')
def first_quote():
    quote1 = Quote.query.first()
    return f"The first quote is: '{quote1.body}' by {quote1.author} in {quote1.category}!"
