FROM python:3.9.5-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
