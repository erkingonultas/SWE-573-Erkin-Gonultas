FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./lydianAPI/requirements.txt /app/
RUN pip install -r ./lydianAPI/requirements.txt

COPY . /app

ENTRYPOINT [ "gunicorn", "lydian.wsgi", "-b", "0.0.0.0:8000"]