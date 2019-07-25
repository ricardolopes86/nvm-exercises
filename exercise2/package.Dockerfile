FROM python:3.6-alpine

LABEL author="Ricado Silva <r.lopesdasilva@outlook.com>"

WORKDIR /app

COPY ./*.* /app/

ENTRYPOINT [ "python", "/app/package.py" ]