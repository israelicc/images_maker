FROM ghcr.io/israelicc/images_maker/analytics-db-orchestration:latest

USER root

# install node (correct way)
RUN apt-get update && apt-get install -y curl \
 && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
 && apt-get install -y nodejs

# install opencode
RUN npm install -g opencode-ai@latest

ENV PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/lib/node_modules/.bin:$PATH"

# verify install
RUN opencode --help

COPY --chown=1000:1000 start.sh /start.sh
RUN chmod +x /start.sh

USER 1000:1000

CMD ["/start.sh"]