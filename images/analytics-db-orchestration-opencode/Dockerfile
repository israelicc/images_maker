FROM ghcr.io/israelicc/images_maker/analytics-db:latest

USER root

# Install OpenCode
RUN curl -fsSL https://opencode.ai/install | bash

# Copy requirements and install Dagster packages
COPY --chown=1000:1000 requirements.in /requirements.in
RUN uv pip compile /requirements.in -o /requirements.txt && \
    uv pip install --no-cache -r /requirements.txt

# Copy start script and workspace config
COPY --chown=1000:1000 start.sh /start.sh
COPY --chown=1000:1000 workspace.yaml /opt/workspace.yaml
COPY --chown=1000:1000 definitions.py /opt/definitions.py

# Make start script executable
RUN chmod +x /start.sh

# Create /opt directory if it doesn't exist and set permissions
RUN mkdir -p /opt && chown 1000:1000 /opt

# Expose webserver port
EXPOSE 3000

USER 1000:1000

# Default command to start both daemon and webserver
CMD ["/start.sh"]
