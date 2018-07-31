#sudo docker build -t imageGenerator:v1.0 .
#FROM ubuntu:18.04
FROM self_unbuntu:18.04

MAINTAINER xueyou <xueyou.wu@langtaojin.com>

RUN mkdir /space
RUN mkdir /space/imageGenerator
#copy程序到/space/imageGenerator
COPY * /space/imageGenerator/


ENTRYPOINT ["/space/imageGenerator/run.sh"]
EXPOSE 60000
