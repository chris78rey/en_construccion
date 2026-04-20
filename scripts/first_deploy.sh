#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
PROJECT_DIR=$(dirname "$SCRIPT_DIR")

cd "$PROJECT_DIR"

if [ ! -f .env ]; then
  echo 'ERROR: falta el archivo .env'
  echo 'Ejecuta: cp .env.vps.example .env'
  exit 1
fi

echo '[1/5] Validando compose'
docker compose -f docker-compose.vps.yml config >/dev/null

echo '[2/5] Construyendo imagen Astro'
docker compose -f docker-compose.vps.yml build --no-cache web

echo '[3/5] Levantando servicios'
docker compose -f docker-compose.vps.yml up -d

echo '[4/5] Estado actual'
docker compose -f docker-compose.vps.yml ps

echo '[5/5] Logs recientes'
docker compose -f docker-compose.vps.yml logs --tail=30 caddy
docker compose -f docker-compose.vps.yml logs --tail=20 web
