from flask import Blueprint, current_app, jsonify, request
from models.model import Quote
from services.quote_service import QuoteService

quotes = Blueprint('quotes', __name__, url_prefix='/quotes')


@quotes.route('', methods=['GET', 'POST'])
def get_all_quotes():
    if request.method == 'POST':
        current_app.logger.info("Called POST quote/ API endpoint")
        content = request.json if request.json else {}

        body = content.get("body")
        author = content.get("author")
        category = content.get("category")

        if body and author and category:
            subcategory = content.get("subcategory")
            numeral = content.get("numeral")

            QuoteService().add(Quote(body=body, author=author, category=category,
                                     subcategory=subcategory, numeral=numeral))

            return jsonify(), 201
        else:
            return jsonify(), 400
    else:
        current_app.logger.info("Called GET quote/ API endpoint")
        result = QuoteService().get_all()
        return jsonify(result)


@quotes.route('/<int:id>', methods=['GET', 'DELETE'])
def id_quote(id):
    if request.method == 'DELETE':
        current_app.logger.info("Called quote/delete API endpoint")
        result = QuoteService().delete(id)
        return (jsonify(), 204) if result else (jsonify(), 404)
    else:
        current_app.logger.info(f"Called quote/{id} API endpoint")
        result = QuoteService().get_id(id)
        current_app.logger.info(f"Result: {result} API endpoint")
        return jsonify(result) if result else (jsonify(), 404)


@quotes.route('/random')
def random_quote():
    current_app.logger.info("Called quote/random API endpoint")
    result = QuoteService().get_random()
    current_app.logger.info(f"Result: {result} API endpoint")
    return jsonify(result)


@quotes.route('/first')
def first_quote():
    current_app.logger.info("Called quote/first API endpoint")
    result = QuoteService().get_first()

    return jsonify(result)
