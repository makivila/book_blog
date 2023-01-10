from models import Book
from flask_sqlalchemy import SQLAlchemy
import time


class Repository:
    def __init__(self, db):
        self.__db = db

    def get_book_by_id(self, id) -> Book:
        return self.__db.get_or_404(Book, id)

    def get_all_books(self) -> list:
        return self.__db.session.execute(self.__db.select(Book))

    def create_book(self, book: Book):
        self.__db.session.add(book)
        self.__db.session.commit()

    def update_book(self):
        self.__db.session.commit() 
   
    def delete_book(self, book: Book):
        self.__db.session.delete(book)
        self.__db.session.commit()       
        
        
        