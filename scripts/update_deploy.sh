#!/usr/bin/env bash
# ==============================================================================
# Da-TIca - Script de Actualización
# ==============================================================================
# Ejecutar cada vez que se actualice el código del sitio
# ==============================================================================
set -euo pipefail

SCRIPT_DIR=$(cd $(dirname $0) && pwd)
PROJECT_DIR=$(dirname $SCRIPT_DIR)

echo '=============================================='
echo 'Da-TIca VPS - Actualización'
echo '=============================================='
echo ''

cd $PROJECT_DIR

echo '[1/5] Asegurando que los servicios están corriendo...'
docker compose -f docker-compose.vps.yml ps

echo ''
echo '[2/5] Reconstruyendo imagen web...'
docker compose -f docker-compose.vps.yml build web

echo ''
echo '[3/5] Recargando servicios...'
docker compose -f docker-compose.vps.yml up -d

echo ''
echo '[4/5] Limpiando imágenes sin uso...'
docker image prune -f

echo ''
echo '[5/5] Estado final:'
docker compose -f docker-compose.vps.yml ps

echo ''
echo '=============================================='
echo '✅ ACTUALIZACIÓN COMPLETADA'
echo '=============================================='
echo ''
echo 'Logs recientes de Caddy:'
docker compose -f docker-compose.vps.yml logs --tail=20 caddy
echo ''
echo 'Logs recientes de Web:'
docker compose -f docker-compose.vps.yml logs --tail=20 web