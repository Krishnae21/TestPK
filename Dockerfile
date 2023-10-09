FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY /requirements.txt .

RUN pip install -r requirements.txt

RUN python3.10 tgbot

COPY . .