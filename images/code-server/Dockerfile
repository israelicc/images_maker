FROM ghcr.io/linuxserver/code-server:4.123.0

USER root

# base tools
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    curl \
    bash \
    git \
    build-base

# install Node.js + npm (Alpine repo)
RUN apk add --no-cache nodejs npm

# optional: upgrade pip
RUN python3 -m pip install --upgrade pip

# verify installs
RUN python3 --version && node -v && npm -v

USER abc