FROM ghcr.io/israelicc/images_maker/analytics-db-orchestration:latest

USER root
# Install OpenCode
RUN curl -fsSL https://opencode.ai/install | bash

# Copy modified start script
COPY --chown=1000:1000 start.sh /start.sh

# Make start script executable
RUN chmod +x /start.sh

USER 1000:1000

# Default command to start both daemon and webserver with OpenCode
CMD ["/start.sh"]
