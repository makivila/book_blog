from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class BookDTO:
    def __init__(self, attrs: dict):
        self.id = attrs.get('id')
        self.title = attrs.get('title')
        self.author = attrs.get('author')
        self.genre = attrs.get('genre')
        self.grade = attrs.get('grade')
        self.opinion = attrs.get('opinion')
        self.is_finished = attrs.get('is_finished')         

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    opinion = db.Column(db.String(2000), nullable=False)
    is_finished = db.Column(db.Integer, nullable=False)

    def __init__(self, data: dict) -> None:
        self.title = data.get('title')
        self.author = data.get('author')
        self.genre = data.get('genre')
        self.grade = data.get('grade')
        self.opinion = data.get('opinion')
        self.is_finished = data.get('is_finished')
