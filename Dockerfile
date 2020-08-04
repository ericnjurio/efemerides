# FROM ubuntu:18.04

FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY . /project/
WORKDIR /project/

RUN ./tools/install.sh

# RUN pip install pipenv
# RUN pipenv install --system

EXPOSE 8000
