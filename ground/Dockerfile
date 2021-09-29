FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH ${PROJECT_SOURCE}:$PYTHONPATH

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt --no-cache

COPY . /code/

CMD python3 manage.py runserver 0.0.0.0:8000