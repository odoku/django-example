FROM python:3.6-alpine

ENV PROJECT_ROOT /app
RUN mkdir -p $PROJECT_ROOT
WORKDIR $PROJECT_ROOT

RUN apk add --update --no-cache \
      openssl-dev \
      tzdata

ADD pip_requirements.txt /tmp/pip_requirements.txt
RUN pip install -U setuptools pip \
    && pip install --no-cache-dir -r /tmp/pip_requirements.txt
