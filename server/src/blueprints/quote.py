from flask import Blueprint, current_app, jsonify
from models import Quote
from quote_service import QuoteService

quote = Blueprint('quote', __name__, url_prefix='/quote')


@quote.route('/')
def get_all_quotes():
    current_app.logger.info("Called quote/ API endpoint")
    result = QuoteService().get_all()

    return jsonify(result)


@quote.route('/first')
def first_quote():
    current_app.logger.info("Called quote/first API endpoint")
    result = QuoteService().get_first()

    return jsonify(result)


@quote.route('/<int:id>')
def id_quote(id):
    current_app.logger.info(f"Called quote/{id} API endpoint")
    result = QuoteService().get_id(id)
    current_app.logger.info(f"Result: {result} API endpoint")
    return jsonify(result) if result else (jsonify(), 404)


@quote.route('/random')
def random_quote():
    current_app.logger.info("Called quote/random API endpoint")
    result = QuoteService().get_random()
    current_app.logger.info(f"Result: {result} API endpoint")
    return jsonify(result)


# TODO: Need error handling
@quote.route('/<string:author>')
def author_quote(author):
    current_app.logger.info("Called quote/<author> API endpoint")
    current_app.logger.info(author)
    quote = Quote.query.filter_by(author=author).first()

    return jsonify(quote.to_json())
