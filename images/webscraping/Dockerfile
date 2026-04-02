FROM ghcr.io/astral-sh/uv:0.11.2-python3.12-trixie

# Install system dependencies for browsers (as root)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    chromium \
    chromium-driver \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright dependencies (as root)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user and set up /app (as root)
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m -s /bin/bash appuser && \
    mkdir -p /app && \
    chown -R 1000:1000 /app

WORKDIR /app

# Switch to non-root user for all Python operations
USER 1000:1000

# Create venv as user 1000 (owned by user 1000)
RUN uv venv /app/venv

# Set PATH so all commands use venv by default
ENV PATH="/app/venv/bin:$PATH"

# Copy and install dependencies (as user 1000, inside venv)
COPY --chown=1000:1000 requirements.in .
RUN uv pip compile requirements.in -o requirements.txt && \
    uv pip install --no-cache -r requirements.txt

# Install Playwright browsers (venv)
RUN playwright install chromium

# Default command
CMD ["python"]
