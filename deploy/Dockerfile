FROM registry.cn-hangzhou.aliyuncs.com/lance0515/lance-test:base_python

LABEL maintainer="Lance"

FROM amazonlinux:latest

RUN yum update -y && yum install -y python3 python3-devel vim

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# 配置默认放置 App 的目录
RUN mkdir -p /app

WORKDIR /app

EXPOSE 28000-28004

COPY . .

ENV PYTHONPATH /app

ENTRYPOINT ["python3", "/app/main.py"]
