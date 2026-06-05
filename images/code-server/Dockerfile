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

# install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# make uv available globally
ENV PATH="/root/.local/bin:/root/.cargo/bin:$PATH"

RUN python3 --version && node -v && npm -v && uv --version || true

USER abc