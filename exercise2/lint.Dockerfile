FROM python:3.6-alpine

LABEL author="Ricado Silva <r.lopesdasilva@outlook.com>"

RUN apk add build-base
RUN pip3 install -U setuptools
RUN pip3 install -U pylint
RUN pip3 install -U pytest

WORKDIR /app

COPY ./*.* /app/

ENTRYPOINT [ "pylint", "/app/exercise2.py", "--errors-only" ]