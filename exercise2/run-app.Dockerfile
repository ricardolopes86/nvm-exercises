FROM python:alpine3.10

MAINTAINER Ricado Silva<r.lopesdasilva@outlook.com>

RUN pip3 install -U pytest

WORKDIR /app

COPY ./exercise2.py /app/run.py

ENTRYPOINT [ "python3", "/app/run.py" ]