FROM daocloud.io/ubuntu:trusty

MAINTAINER Lance <lancefate@163.com>

FROM amazonlinux:latest

RUN yum update -y && \
yum install -y python3 python3-devel vim
RUN pip3 install --no-cache-dir numpy matplotlib pandas uvicorn fastapi

# 配置默认放置 App 的目录
RUN mkdir -p /app
WORKDIR /app
EXPOSE 8000
COPY . .
ENTRYPOINT ["python", "/app/main.py"]
