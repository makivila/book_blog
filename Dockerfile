FROM python:3.10-buster

WORKDIR /app

COPY . .
RUN apt-get update
RUN apt-get install libmariadb-dev
RUN pip install -r requirements.txt

CMD ["python", "main.py"]