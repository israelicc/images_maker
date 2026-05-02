#!/bin/bash
set -e

echo "Starting OpenCode..."
opencode &
OPENCODE_PID=$!

echo "Starting Dagster daemon..."
dagster-daemon run -w /opt/workspace.yaml &
DAEMON_PID=$!

echo "Starting Dagster webserver..."
dagster-webserver -w /opt/workspace.yaml -h 0.0.0.0 -p 3000 &
WEB_PID=$!

trap "echo Shutting down...; kill $OPENCODE_PID $DAEMON_PID $WEB_PID" SIGTERM SIGINT

wait -n