#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
PROJECT_DIR=$(dirname "$SCRIPT_DIR")

cd "$PROJECT_DIR"

docker compose -f docker-compose.vps.yml build web
docker compose -f docker-compose.vps.yml up -d
docker image prune -f
docker compose -f docker-compose.vps.yml ps
