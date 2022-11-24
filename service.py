from repository import Repository
from models import BookDTO
from models import Book

class Service:
    def __init__(self, repository: Repository):
        self.repository = repository
    
    def get_book_by_id(self, id):
        book = self.repository.get_book_by_id(id)
        opinion =  self.repository.get_opinion(book.opinion_id)
        book_dto = BookDTO(book.__dict__)
        book_dto.opinion = opinion
        return book_dto   

    def create_book(self, book_dto:BookDTO):  
        book = Book(book_dto.__dict__)
        if book_dto.opinion:
            opinion_id_created = self.repository.create_opinion(book_dto.opinion)
            book.opinion_id = opinion_id_created
        self.repository.create_book(book)
                    







