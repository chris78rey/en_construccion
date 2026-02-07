# TRAEFIK (LOCAL DEV ONLY)

## OVERVIEW
Configuración dinámica de Traefik para simular routing de Coolify en entorno local.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Ruteo local HTTP | `traefik/dynamic.yml` | Router `portal-router` → `portal-service` |
| Compose dev con Traefik | (no incluido) | Si lo necesitas, crea un compose dev que monte `./traefik/dynamic.yml` |

## CONVENTIONS
- Solo aplica en local (dev). En producción, Traefik lo gestiona Coolify.
- `traefik/dynamic.yml` apunta a `http://portal_web_local:8080`; si lo usas, asegúrate de que tu contenedor `web` tenga ese `container_name`.

## ANTI-PATTERNS
- No copiar esta config a producción.
- No asumir reglas de host de producción aquí; esto es solo para `localhost` / `portal.localhost`.
