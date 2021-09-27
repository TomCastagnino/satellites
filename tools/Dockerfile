FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH ${PROJECT_SOURCE}:$PYTHONPATH

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt --no-cache

COPY . /code/
