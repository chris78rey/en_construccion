# WEB (STATIC SITE)

## OVERVIEW
Contenido estático + imagen de producción basada en `nginx:stable-alpine` sirviendo en puerto interno `8080`.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Build de imagen prod | `web/Dockerfile` | Sirve `COPY . /usr/share/nginx/html` |
| HTML principal | `web/index.html` | Portal autocontenido (CSS inline fallback) |
| Config nginx (referencia) | `web/default.conf` | No se usa si el Dockerfile sigue generando conf inline |

## CONVENTIONS
- El servidor debe escuchar en `0.0.0.0:8080` (para Traefik/Coolify).
- Producción: no exponer puertos de host en compose; solo `EXPOSE 8080` + `expose: "8080"` en `docker-compose.yml`.
- Mantener el sitio “autocontenido”: evitar dependencias de build que requieran runtime Node en producción.

## ANTI-PATTERNS
- No introducir secretos en archivos estáticos (HTML/JS) ni en el Dockerfile.
- No asumir que `web/default.conf` está activo: hoy la fuente de verdad es el heredoc en `web/Dockerfile`.
