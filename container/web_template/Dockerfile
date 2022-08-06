FROM python:3.7-slim-buster

RUN apt-get update && apt-get upgrade -y && apt-get install -y git
RUN pip3 install mlflow
RUN pip3 install boto3
RUN pip3 install psycopg2-binary

ENV WORKDIR=/app
ENV HOME=/app

RUN mkdir ${WORKDIR} && cd ${WORKDIR}
WORKDIR ${HOME}
