FROM python:3.9.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /code

COPY src /code/

COPY .env.docker ./

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080