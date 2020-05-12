FROM ubuntu:bionic

ENV PYTHONPATH=${PYTHONPATH}:/code

# setup
RUN set -x \
    && apt-get -y update \
    && apt-get -y install less python3 python3-pip vim screen locales \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && pip install --upgrade pip \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8

# Copy and install requirements.txt
COPY requirements.txt /
WORKDIR /
RUN set -x && pip install -r requirements.txt

COPY root /
WORKDIR /code/

ENTRYPOINT [ "/usr/bin/entrypoint" ]
