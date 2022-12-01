from models import Book
import time


class Repository:
    def __init__(self, db):
        self.db = db
    
    def cursor_handler(func):
        def decorator(self, *args, **kwargs):
            if not self.db.is_connected():
                self.db.reconnect()
            cursor = self.db.cursor(dictionary=True)
            result = func(self, cursor, *args, **kwargs)
            cursor.close()
            self.db.commit()
            return result
        return decorator

    @cursor_handler
    def get_book_by_id(self, cursor, id) -> Book:
        query = """SELECT * FROM book WHERE id = %s"""
        query_args = (id, )
        cursor.execute(query, query_args)
        result = cursor.fetchone()     
        if not result:
            return None
        return Book(result)  

    @cursor_handler
    def create_book(self, cursor, book:Book):
        query = """INSERT INTO book (title, author, grade, is_finished, opinion, genre) 
                                         VALUES (%s,%s,%s,%s,%s,%s)"""
        query_args = (book.title, book.author, book.grade, book.is_finished, book.opinion, book.genre)
        cursor.execute(query, query_args)

    @cursor_handler
    def update_book(self, cursor, id, book:Book):
        query = """UPDATE book SET title = %s,
                                   author = %s,
                                   genre = %s,
                                   grade = %s,
                                   opinion = %s,
                                   is_finished = %s 
                                    WHERE id= %s """
        query_args = (book.title, book.author, book.genre, book.grade, book.opinion, book.is_finished, id)
        cursor.execute(query, query_args)
   
    @cursor_handler
    def delete_book(self, cursor, id):
        query = """DELETE FROM book WHERE id = %s """
        query_args = (id, )
        cursor.execute(query, query_args)