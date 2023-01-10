import os
from dotenv import load_dotenv
from repository import Repository
from service import Service
from handler import Handler
from flask import Flask
from models import db


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") 
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{DB_USER}:{DB_PASSWORD}@"\
                                        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"

db.init_app(app)

with app.app_context():
    db.create_all()



repository = Repository(db)
service = Service(repository)
handler = Handler(app, service)


if __name__ == "__main__":
    app.run()