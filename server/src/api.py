import sys
import socket
from flask import Blueprint, current_app, jsonify
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
    current_app.logger.info("Called quote/first API endpoint")
    quote1 = Quote.query.first()
    return jsonify(quote1.to_json())


@api_blueprint.route('/quote/<id>')
def id_quote(id):
    current_app.logger.info("Called quote/<id> API endpoint")
    quote1 = Quote.query.get(id)
    return jsonify(quote1.to_json())
