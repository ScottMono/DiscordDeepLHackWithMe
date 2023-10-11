FROM python:3.10.6-alpine
LABEL authors="uu"

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

