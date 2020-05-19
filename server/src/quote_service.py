import random
from models import Quote


class QuoteService:
    def __init__(self):
        self.Quote = Quote

    def get_all(self):
        quotes = self.Quote.query.all()
        return [quote.to_dict() for quote in quotes]

    def get_first(self):
        return self.Quote.query.first().to_dict()

    def get_id(self, id):
        quote = Quote.query.get(id)
        if quote:
            return quote.to_dict()

    def get_random(self):
        quotes = self.Quote.query.all()
        i = random.randint(0, len(quotes) - 1)

        return quotes[i].to_dict()
