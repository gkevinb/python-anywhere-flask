import sys
import socket
from flask import Blueprint, current_app, jsonify, redirect
from models import Person, Quote
from quote_service import QuoteService

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
def index():
    return redirect(current_app.config.get("WEB_HOST"), code=301)


@api_blueprint.route('/info')
def hello_world():
    return 'Hello world, Flask: {0}! on {1}!'.format(sys.version, socket.gethostname())


@api_blueprint.route('/health')
def health():
    return f"This will be the health page. {current_app.config['HOST']}, {current_app.config['HOST_MACHINE']}"


@api_blueprint.route('/quote')
def get_all_quotes():
    current_app.logger.info("Called quote/ API endpoint")
    result = QuoteService().get_all()

    return jsonify(result)


@api_blueprint.route('/quote/first')
def first_quote():
    current_app.logger.info("Called quote/first API endpoint")
    result = QuoteService().get_first()

    return jsonify(result)


@api_blueprint.route('/quote/<int:id>')
def id_quote(id):
    current_app.logger.info(f"Called quote/{id} API endpoint")
    result = QuoteService().get_id(id)
    current_app.logger.info(f"Result: {result} API endpoint")
    return jsonify(result) if result else (jsonify(), 404)


@api_blueprint.route('/quote/random')
def random_quote():
    current_app.logger.info("Called quote/random API endpoint")
    result = QuoteService().get_random()
    current_app.logger.info(f"Result: {result} API endpoint")
    return jsonify(result)


# TODO: Need error handling
@api_blueprint.route('/quote/<string:author>')
def author_quote(author):
    current_app.logger.info("Called quote/<author> API endpoint")
    current_app.logger.info(author)
    quote = Quote.query.filter_by(author=author).first()

    return jsonify(quote.to_json())
