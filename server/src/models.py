
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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

    def to_json(self):
        return {
            "id": self.id,
            "body": self.body,
            "author": self.author,
            "category": self.category,
            "subcategory": self.subcategory,
            "numeral": self.numeral
        }
