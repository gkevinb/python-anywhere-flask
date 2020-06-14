from flask import Blueprint, current_app, jsonify, request
from models.model import Quote
from services.quote_service import QuoteService

quotes = Blueprint('quotes', __name__, url_prefix='/quotes')


@quotes.route('', methods=['GET', 'POST'])
def get_all_quotes():
    if request.method == 'POST':
        current_app.logger.info("Called POST quote/ API endpoint")
        content = request.json if request.json else {}

        quote = content.get("quote")
        author = content.get("author")
        category = content.get("category")

        if quote and author and category:
            QuoteService().add(Quote(body=quote, author=author, category=category))
            return jsonify("Success")
        else:
            return jsonify("Invalid request body")
    else:
        current_app.logger.info("Called GET quote/ API endpoint")
        result = QuoteService().get_all()
        return jsonify(result)


@quotes.route('/first')
def first_quote():
    current_app.logger.info("Called quote/first API endpoint")
    result = QuoteService().get_first()

    return jsonify(result)


@quotes.route('/<int:id>')
def id_quote(id):
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


# TODO: Need error handling
@quotes.route('/<string:author>')
def author_quote(author):
    current_app.logger.info("Called quote/<author> API endpoint")
    current_app.logger.info(author)
    quote = Quote.query.filter_by(author=author).first()
    if quote:
        return jsonify(quote.to_dict())


@quotes.route('/delete')
def delete_quote():
    current_app.logger.info("Called quote/delete API endpoint")
    result = QuoteService().delete(12)
    current_app.logger.info(f"Result: {result} API endpoint")
    return jsonify("Success")
