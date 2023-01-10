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

    def get_all_books(self):
        book_dtos = []
        books = self.repository.get_all_books()
        if not books:
            return None
        for book, in books:
            book_dto = BookDTO(book.__dict__)
            book_dtos.append(book_dto)
        return book_dtos 

    def create_book(self, book_dto: BookDTO):  
        book = Book(book_dto.__dict__)
        self.repository.create_book(book)

    def update_book(self, id, book_dto: BookDTO):
        book = self.repository.get_book_by_id(id)
        book.author = book_dto.author
        book.genre = book_dto.genre
        book.grade = book_dto.grade
        book.is_finished = book_dto.is_finished
        book.opinion = book_dto.opinion
        book.title = book_dto.title
        self.repository.update_book()     

    def delete_book(self, id):
        book = self.repository.get_book_by_id(id)
        self.repository.delete_book(book)