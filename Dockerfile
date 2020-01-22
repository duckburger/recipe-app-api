# Version of the docker image tha
FROM python:3.8.1-alpine3.11
MAINTAINER Kirill Murawski

# Makes sure that python runs unbuffered which is recommended in docker instances
ENV PYTHONUNBUFFERED 1

# Copies requirements file to the images's requirements and then installs what's in it using python
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Makes a dir app and makes it the work dir from which the app will run
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Adding a new user and then switching to it, -D means a user that will be used for running apps only and not logging into it
# If this is not done then the app will run using the root user which can be used in an attack
RUN adduser -D user
USER user
