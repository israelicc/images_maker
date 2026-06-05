FROM ghcr.io/linuxserver/code-server:4.123.0

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    bash \
    git \
    build-essential \
    nodejs \
    npm \
 && rm -rf /var/lib/apt/lists/*

RUN python3 --version && node -v && npm -v || true

USER abc