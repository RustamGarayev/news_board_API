#FROM python:3.10
#
## Ensure that Python outputs everything that's printed inside
## the application rather than buffering it.
#ENV PYTHONUNBUFFERED 1
#ENV APP_ROOT /code
#
## Copy in your requirements file
#ADD requirements.txt /requirements.txt
#
## Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
#RUN pip install virtualenvwrapper
#RUN python3 -m venv /venv
#RUN /venv/bin/pip install -U pip
#RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt
#
## Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
#RUN mkdir ${APP_ROOT}
#WORKDIR ${APP_ROOT}
#ADD . ${APP_ROOT}
# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

ADD requirements.txt /requirements.txt

RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt

COPY . /code/
