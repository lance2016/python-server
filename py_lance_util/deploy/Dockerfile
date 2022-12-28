FROM python:3.9

LABEL maintainer="Lance"

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    vim


RUN pip3 install poetry

# RUN pip3 install -r requirements.txt

# 配置默认放置 App 的目录
RUN mkdir -p /app

WORKDIR /app

EXPOSE 28000-28004

COPY . .

ENV PYTHONPATH /app

RUN poetry install 

CMD ["bash", "-c", "cd /app && poetry run python3 py_lance_util/main.py"]

# ENTRYPOINT ["poetry run python3", "/"]
