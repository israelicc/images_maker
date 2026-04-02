FROM ghcr.io/astral-sh/uv:0.11.2-python3.12-trixie

# Create non-root user and group
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m -s /bin/bash appuser

# Create app directory and set ownership
RUN mkdir -p /app && chown -R 1000:1000 /app

WORKDIR /app

# Install system dependencies (as root)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    unixodbc-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER 1000:1000

# Create virtual environment
RUN uv venv .venv

# Copy loose requirements and compile to lock file
COPY --chown=1000:1000 requirements.in .
RUN uv pip compile requirements.in -o requirements.txt && uv pip install --no-cache -r requirements.txt

# Default command
CMD ["python"]
