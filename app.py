from flask import Flask, Blueprint, jsonify
from flask_restx import Api
from ma import ma
from db import db

from resources.book import Book, BookList, book_ns
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(Book, '/books/<int:id>')
api.add_resource(BookList, '/books')

db.init_app(app)

if __name__ == '__main__':
    server.run()

with app.app_context():
    db.create_all()
    ma.init_app(app)
