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
            book_json = json.dumps(book.__dict__, ensure_ascii=False)
            return book_json

    def init_routes(self):
        @self.app.route('/create', methods=['POST'])
        def create_book():
            book_dto = BookDTO(request.json)
            self.service.create_book(book_dto)
            return 'Book has added successfully'