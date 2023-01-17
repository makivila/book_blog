FROM python:3.10-buster

WORKDIR /app

COPY . .
RUN apt-get update
RUN apt-get install libmariadb-dev
RUN pip install -r requirements.txt
RUN 

EXPOSE 5000

CMD ["python", "main.py"]