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

WORKDIR /app

# Copy loose requirements and compile to lock file
COPY requirements.in .
RUN uv pip compile requirements.in -o requirements.txt --system && uv pip install --no-cache -r requirements.txt --system

# Install Playwright browsers (system)
RUN playwright install chromium

# Create non-root user for running
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m -s /bin/bash appuser && \
    chown -R 1000:1000 /app
USER 1000:1000

# Default command
CMD ["python"]
