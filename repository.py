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


    # @BaseRepository.cursor_handler
    # def change_read_status(self, cursor, is_finished, id):
    #     query = """UPDATE book SET is_finished = %s   
    #                          WHERE id= %s """
    #     query_args = (is_finished, id)
    #     cursor.execute(query, query_args)      
    #     return cursor.fetchall() 

   
    # @cursor_handler
    # def get_opinion(self, cursor, id):
    #     query = """SELECT opinion FROM opinion_about_book WHERE id = %s"""
    #     query_args = (id, )                    
    #     cursor.execute(query, query_args)
    #     result = cursor.fetchone()
    #     if result:
    #         return result['opinion'] 
    #     else:
    #         return None

    # @cursor_handler
    # def get_sorted_books(self, cursor, sorted_type, is_finished):
    #     query = """SELECT *
    #                 WHERE is_finished = %s
    #                 ORDER BY %s"""
    #     query_args = (is_finished, sorted_type)
    #     cursor.execute(query, query_args)
    #     return cursor.fetchall() 

    # @cursor_handler
    # def create_opinion(self, cursor, opinion) -> None:
    #     query = """INSERT INTO opinion_about_book (opinion) 
    #         VALUES (%s)"""
    #     query_args = (opinion, )     
    #     cursor.execute(query, query_args)
    #     query = """SELECT LAST_INSERT_ID() AS id""" 
    #     cursor.execute(query)
    #     return cursor.fetchone()['id']

    # @cursor_handler
    # def delete_book(self, cursor, id):
    #     query = """DELETE FROM book 
    #                             WHERE id = %s"""
    #     query_args = (id)
    #     cursor.execute(query, query_args)
    #     return cursor.fetchall() 


    # @cursor_handler
    # def show_all_book(self, cursor, id, title, author, genre, grade, opinion, opinion_id, is_finished):
    #     query = """SELECT * FROM book INNER JOIN opinion_about_book 
    #     ON book.opinion_id = opinion_about_book.id"""
    #     query_args = (title, id, title, author, genre, grade, opinion, opinion_id, is_finished)
    #     cursor.execute(query, query_args)
    #     return cursor.fetchall()     


    # @cursor_handler
    # def get_book_by_id(self, cursor, id):
    #     query = """SELECT * FROM book WHERE id = %s"""
    #     query_args = (id, )
    #     cursor.execute(query, query_args)
    #     result = cursor.fetchone()     
    #     if not result:
    #         return None
    #     return Book(result)




    # @BaseRepository.cursor_handler
    # def add_grade(self, cursor, grade, id):
    #     query = """UPDATE book SET grade = %s   
    #                          WHERE id= %s """
    #     query_args = (grade, id)
    #     cursor.execute(query, query_args)
    #     return cursor.fetchall() 

        






    # @cursor_handler
    # def show_finished_book(self, cursor, title, author, genre, opinion, grade):
    #     query = """SELECT title, author, genre, opinion, grade FROM book (title, author) 
    #                                     VALUES (%s,%s,%s)"""
    #     query_args = (title, author, genre)
    #     cursor.execute(query, query_args)
    #     return cursor.fetchall() 