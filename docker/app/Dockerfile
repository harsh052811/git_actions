FROM python:3.8-slim-buster

RUN apt-get update && \
    pip install -U pip && \
    apt-get install dos2unix gettext-base ;\
    apt-get install -y git gcc default-libmysqlclient-dev; \
    apt-get install -y ffmpeg


WORKDIR /app
COPY docker/app/requirements.txt /app
RUN pip install -r /app/requirements.txt
COPY docker/app/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
COPY src /app/src
RUN ln -sf /usr/local/bin/docker-entrypoint.sh /