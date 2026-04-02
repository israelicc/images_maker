FROM ghcr.io/astral-sh/uv:0.11.2-python3.12-trixie

# Install system dependencies (as root)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy loose requirements and compile to lock file
COPY requirements.in .
RUN uv pip compile requirements.in -o requirements.txt --system && uv pip install --no-cache -r requirements.txt --system

# Download spaCy models (system python)
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md

# Create non-root user for running
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m -s /bin/bash appuser && \
    chown -R 1000:1000 /app
USER 1000:1000

# Default command
CMD ["python"]
