FROM python:3.14.7-alpine3.24

RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver tzdata

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.36.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.36.0/allure-commandline-2.36.0.tgz && \
    tar -zxvf allure-2.36.0.tgz -C /opt/ && \
    ln -sf /opt/allure-2.36.0/bin/allure /usr/bin/allure && \
    rm allure-2.36.0.tgz

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace

RUN pip3 install --no-cache-dir -r requirements.txt