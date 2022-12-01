
class Book:
    def __init__(self, attrs: dict):
        self.id = attrs.get('id')
        self.title = attrs.get('title')
        self.author = attrs.get('author')
        self.genre = attrs.get('genre')
        self.grade = attrs.get('grade')
        self.opinion = attrs.get('opinion')
        self.is_finished = attrs.get('is_finished')

class BookDTO:
    def __init__(self, attrs: dict):
        self.id = attrs.get('id')
        self.title = attrs.get('title')
        self.author = attrs.get('author')
        self.genre = attrs.get('genre')
        self.grade = attrs.get('grade')
        self.opinion = attrs.get('opinion')
        self.is_finished = attrs.get('is_finished')         