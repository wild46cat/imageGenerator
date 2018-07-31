#sudo docker build -t image_generator:v1.0 .
#FROM ubuntu:18.04
FROM self_ubuntu:18.04

MAINTAINER xueyou <xueyou.wu@langtaojin.com>

RUN mkdir /space
RUN mkdir /space/imageGenerator
#copy程序到/space/imageGenerator
COPY ./demo/ /space/imageGenerator/demo/
COPY ./docker/ /space/imageGenerator/docker/
COPY ./html/ /space/imageGenerator/html/
COPY ./img/ /space/imageGenerator/img/
COPY ./test/ /space/imageGenerator/test/
COPY ./biz /space/imageGenerator/biz/
COPY ./app.py /space/imageGenerator/app.py
COPY ./run.sh /space/imageGenerator/run.sh


ENTRYPOINT ["/space/imageGenerator/run.sh"]
EXPOSE 60000
