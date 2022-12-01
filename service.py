from repository import Repository
from models import BookDTO
from models import Book

class Service:
    def __init__(self, repository: Repository):
        self.repository = repository
    
    def get_book_by_id(self, id):
        book = self.repository.get_book_by_id(id)
        if not book:
            return None
        book_dto = BookDTO(book.__dict__)
        return book_dto   

    def create_book(self, book_dto:BookDTO):  
        book = Book(book_dto.__dict__)
        self.repository.create_book(book)

    def update_book(self, id, book_dto:BookDTO):
        book = Book(book_dto.__dict__)
        self.repository.update_book(id, book)     

    def delete_book(self, id):
        self.repository.delete_book(id)