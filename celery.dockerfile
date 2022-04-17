FROM python:3.10
ENV PYTHONUNBUFFERED 1

#ENV C_FORCE_ROOT true

#ENV APP_USER myapp
ENV APP_ROOT /code
ENV DEBUG False

RUN mkdir /code;

WORKDIR ${APP_ROOT}

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install --no-cache-dir -r /config/requirements.txt

ADD . ${APP_ROOT}
