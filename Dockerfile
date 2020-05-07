FROM ubuntu:bionic

ENV PYTHONPATH=${PYTHONPATH}:/code

# setup
RUN set -x \
    && apt-get -y update \
    && apt-get -y install less python3 python3-pip vim screen \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && pip install --upgrade pip \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

RUN export LC_ALL=C.UTF-8 && export LANG=C.UTF-8

# Copy and install requirements.txt
COPY requirements.txt /
WORKDIR /
RUN set -x && pip install -r requirements.txt

COPY root /
WORKDIR /code/

ENTRYPOINT [ "python" ]
