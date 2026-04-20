# Migración realizada

## Fuente principal nueva
- `src/pages/*.astro`
- `src/components/*.astro`
- `src/components/*.vue`

## Publicación
- Coolify: `docker-compose.yml`
- VPS propio: `docker-compose.vps.yml`

## Qué deja de ser la fuente principal
- La carpeta `web/` ya no debe usarse como base editable del sitio.
- El sitio ahora se construye desde la raíz del proyecto y publica `dist/`.

## Puntos a revisar antes de pasar a producción
1. Reemplazar el WhatsApp placeholder en `src/data/site.js`
2. Añadir imágenes reales si se desean
3. Validar dominios en Coolify o VPS
4. Ejecutar build y revisar logs del contenedor
