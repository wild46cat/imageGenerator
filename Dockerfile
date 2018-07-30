#sudo docker build -t imageGenerator:v1.0 .
#FROM ubuntu:18.04
FROM self_unbuntu:18.04

MAINTAINER xueyou <xueyou.wu@langtaojin.com>

#COPY docker/sources.list /etc/apt/sources.list
#COPY docker/98tsinghuasource /etc/apt/apt.conf.d/98tsinghuasource
## APT 自动安装相关的依赖包，如需其他依赖包在此添加
#RUN apt-get update && \
#      apt-get install -y python \
#                       python-dev \
#                       python-pip  \
#		       libx11-dev \
#		       libnss3-dev \
#    && pip install pillow \
#    && pip install flask \
#    && pip install selenium

RUN mkdir /space
RUN mkdir /space/imageGenerator
#copy程序到/space/imageGenerator
COPY * /space/imageGenerator/


ENTRYPOINT ["/space/imageGenerator/run.sh"]
EXPOSE 60000
