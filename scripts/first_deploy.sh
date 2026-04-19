#!/usr/bin/env bash
# ==============================================================================
# Da-TIca - Script de Primer Despliegue en VPS
# ==============================================================================
# Ejecutar UNA SOLA VEZ al configurar el servidor por primera vez
# ==============================================================================
set -euo pipefail

SCRIPT_DIR=$(cd $(dirname $0) && pwd)
PROJECT_DIR=$(dirname $SCRIPT_DIR)

echo '=============================================='
echo 'Da-TIca VPS - Primer Despliegue'
echo '=============================================='
echo ''

# --- Validaciones previas ---
cd $PROJECT_DIR

if [ ! -f .env ]; then
    echo '❌ ERROR: Falta el archivo .env'
    echo '   Ejecuta: cp .env.vps.example .env'
    echo '   Luego edita .env y coloca tu DOMAIN correcto'
    exit 1
fi

echo '[1/5] Validando configuración Docker Compose...'
docker compose -f docker-compose.vps.yml config > /dev/null
echo '   ✅ Configuración válida'

echo ''
echo '[2/5] Verificando puertos 80 y 443...'
if ss -tulpn | grep -E ':80|:443' | grep -v grep | grep -q docker; then
    echo '   ⚠️  Los puertos están siendo usados por Docker (correcto)'
else
    # Verificar que no haya otros servicios
    if ss -tulpn | grep ':80 ' | grep -v docker | grep -q .; then
        echo '   ❌ ERROR: Puerto 80 ocupado por otro servicio'
        echo '   Detén nginx/apache2 si están instalados:'
        echo '   sudo systemctl stop nginx apache2'
        echo '   sudo systemctl disable nginx apache2'
        exit 1
    fi
fi
echo '   ✅ Puertos disponibles'

echo ''
echo '[3/5] Construyendo imagen Docker...'
docker compose -f docker-compose.vps.yml build --no-cache web
echo '   ✅ Imagen construida'

echo ''
echo '[4/5] Levantando servicios...'
docker compose -f docker-compose.vps.yml up -d
echo '   ✅ Servicios iniciados'

echo ''
echo '[5/5] Verificando estado...'
sleep 3
docker compose -f docker-compose.vps.yml ps

echo ''
echo '=============================================='
echo '✅ DESPLIEGUE COMPLETADO'
echo '=============================================='
echo ''
echo 'Logs de Caddy (verificar certificados):'
docker compose -f docker-compose.vps.yml logs --tail=30 caddy
echo ''
echo 'Logs de Web:'
docker compose -f docker-compose.vps.yml logs --tail=20 web
echo ''
echo '=============================================='
echo 'VALIDACIÓN MANUAL'
echo '=============================================='
DOMAIN_VALUE=$(grep DOMAIN .env | cut -d '=' -f2)
echo ''
echo 'Desde el VPS, prueba:'
echo '  curl -I http://localhost'
echo ''
echo 'Desde tu navegador:'
echo '  https://'$DOMAIN_VALUE
echo ''
echo '=============================================='