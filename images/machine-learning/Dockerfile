FROM ghcr.io/astral-sh/uv:0.11.2-python3.12-trixie

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy loose requirements and compile to lock file
COPY requirements.in .
RUN uv pip compile requirements.in -o requirements.txt --system && uv pip install --no-cache -r requirements.txt --system

# Default command
CMD ["python"]
