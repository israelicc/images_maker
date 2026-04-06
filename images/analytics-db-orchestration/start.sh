#!/bin/bash
# this is to be copied to dockerfile to start webserver and daemon inside the same container.
set -e

echo "Starting Dagster daemon..."
dagster-daemon run -w /opt/workspace.yaml &
DAEMON_PID=$!

echo "Starting Dagster webserver..."
dagster-webserver -w /opt/workspace.yaml -h 0.0.0.0 -p 3000

wait
