FROM ubuntu:noble

RUN apt update
RUN DEBIAN_FRONTEND=noninteractive TZ=America/Los_Angeles apt install -y build-essential git vim nano nodejs tzdata sqlite3 libyaml-dev
RUN apt install -y rbenv ruby-build
RUN apt install -y sudo

COPY freedesktop.org.xml /usr/local/share/mime/packages/freedesktop.org.xml

ARG MYUID=1000
ARG MYGID=1000

RUN userdel -r ubuntu
RUN groupadd -g ${MYGID} user
RUN useradd -m -p "" -u ${MYUID} -g ${MYGID} -s /bin/bash user
RUN usermod -a -G sudo user
RUN chown user:user /home/user

USER user
WORKDIR /home/user

RUN rbenv install 3.1.2
RUN rbenv global 3.1.2
RUN rbenv rehash

ENV PATH="/home/user/.rbenv/shims:${PATH}"

RUN gem install rails
# This shouldn't be necessary, but `rails new` pukes without it
RUN gem install importmap-rails turbo-rails stimulus-rails web-console
# This downgrades bundler to something that works
RUN gem install bundler -v 2.5.4
RUN rbenv rehash

EXPOSE 3000

