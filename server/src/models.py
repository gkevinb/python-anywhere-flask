
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

UNUSED_SQL_ALCHEMY_KEY = "_sa_instance_state"


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Quote(db.Model):
    __tablename__ = "quote"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    subcategory = db.Column(db.String(255), nullable=True)
    numeral = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        quote_dictionary = vars(self)
        quote_dictionary.pop(UNUSED_SQL_ALCHEMY_KEY, None)
        return quote_dictionary
