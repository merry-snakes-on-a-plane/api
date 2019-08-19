FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE  1
ENV PYTHONBUFFERED 1

WORKDIR /code

RUN pip install pipenv 
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

COPY . /code/