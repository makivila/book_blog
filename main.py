import mysql.connector
import os
from dotenv import load_dotenv
from repository import Repository
from service import Service
from handler import Handler
from flask import Flask


load_dotenv()
connection = mysql.connector.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                              host=os.getenv("DB_HOST"),
                              database=os.getenv("DB_NAME")) 
app = Flask(__name__)
repository = Repository(connection)
service = Service(repository)
handler = Handler(app, service)


if __name__ == "__main__":
    app.run()