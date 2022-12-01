import json
from flask import Flask
from service import Service
from models import BookDTO
from flask import request


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
                return 'Not found'
            book_json = json.dumps(book.__dict__, ensure_ascii=False)
            return book_json

        @self.app.route('/create', methods=['POST'])
        def create_book():
            book_dto = BookDTO(request.json)
            self.service.create_book(book_dto)
            return 'Book has added successfully'

        @self.app.route('/update/<int:id>/', methods=['PUT'])
        def update_book(id):
            book_dto = BookDTO(request.json)
            self.service.update_book(id, book_dto)
            return 'Book has updated'      

        @self.app.route('/delete/<int:id>/', methods=['DELETE'])
        def delete_book(id):
            self.service.delete_book(id)
            return 'Book has deleted'      