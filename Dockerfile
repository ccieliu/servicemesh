FROM alpine:latest

COPY . /data/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.sjtug.sjtu.edu.cn/g' /etc/apk/repositories && apk add --no-cache gcc g++ linux-headers build-base python3 python3-dev py3-pip && pip config set global.index-url "https://mirrors.sjtug.sjtu.edu.cn/pypi/web/simple" && pip install -r /data/requirements.txt && apk del gcc g++ build-base


ENV PYTHONPATH /data/
ENV APP_VERSION ""
WORKDIR /data/