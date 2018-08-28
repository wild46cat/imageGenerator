#sudo docker build -t image_generator:v1.0 .
#FROM ubuntu:18.04
FROM alpine-python-crawler:v1.0

MAINTAINER xueyou

RUN mkdir /space
RUN mkdir /space/imageGenerator
#copy程序到/space/imageGenerator
COPY ./* /space/imageGenerator/*

ENTRYPOINT ["/space/imageGenerator/run.sh"]
EXPOSE 60000
