FROM python:3.9.0b1-alpine3.12
MAINTAINER Ronan Duddy <ronanduddy@live.ie>

ENV BUILD_PACKAGES build-base entr

RUN apk update && \
    apk upgrade && \
    apk add --no-cache $BUILD_PACKAGES

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./scrubbish.py" ]
