# TRAEFIK (LOCAL DEV ONLY)

## OVERVIEW
Configuración dinámica de Traefik para simular routing de Coolify en entorno local.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Ruteo local HTTP | `traefik/dynamic.yml` | Router `portal-router` → `portal-service` |
| Compose local con Traefik | `docker-compose.coolify-local.yml` | Monta `./traefik/dynamic.yml` en Traefik |

## CONVENTIONS
- Solo aplica en local (dev). En producción, Traefik lo gestiona Coolify.
- `traefik/dynamic.yml` apunta a `http://portal_web_local:8080`; debe coincidir con `container_name` del servicio `web` en `docker-compose.coolify-local.yml`.

## ANTI-PATTERNS
- No copiar esta config a producción.
- No asumir reglas de host de producción aquí; esto es solo para `localhost` / `portal.localhost`.
