import json
from flask import Flask
from service import Service
from models import BookDTO
from flask import request, jsonify
from marshmallow import ValidationError
from validation_schemas import BookValidationSchema, ValidationResult


class Handler:
    def __init__(self, app: Flask, service: Service):
        self.service = service
        self.app = app
        self.init_routes()

    def init_routes(self):
        @self.app.route('/book/<int:id>/')
        def get_book_by_id(id):
            book = self.service.get_book_by_id(id)
            if not book:
                return 'Not found', 404
            return jsonify(book.__dict__)

        @self.app.route('/book/all/')
        def get_all_books():
            book_dicts = []
            book_dtos = self.service.get_all_books()
            if not book_dtos:
                return 'Not found', 404
            for book_dto in book_dtos:
                book_dicts.append(book_dto.__dict__)
            return jsonify(book_dicts)

        @self.app.route('/book/', methods=['POST'])
        def create_book():
            validation_result = self.validate(request.json)
            if not validation_result.status:
                return jsonify(validation_result.error_messages)
            book_dto = BookDTO(request.json)
            self.service.create_book(book_dto)
            return 'Book has added successfully'

        @self.app.route('/book/<int:id>/', methods=['PUT'])
        def update_book(id):
            validation_result = self.validate(request.json)
            if not validation_result.status:
                return jsonify(validation_result.error_messages)
            book_dto = BookDTO(request.json)
            self.service.update_book(id, book_dto)
            return 'Book has updated'      

        @self.app.route('/book/<int:id>/', methods=['DELETE'])
        def delete_book(id):
            self.service.delete_book(id)
            return 'Book has deleted'      

    def validate(self, json):
        schema = BookValidationSchema()
        try:
            schema.load(json)
            return ValidationResult(True)
        except ValidationError as e:
            return ValidationResult(False, e.messages)