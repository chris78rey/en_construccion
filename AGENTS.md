# PROJECT KNOWLEDGE BASE

**Generated:** 2026-02-07
**Branch:** main
**Commit:** 7db9a25

## OVERVIEW
Portal estático “da-tica” desplegable en Coolify (Traefik gestionado por Coolify) con `docker-compose.yml` para producción y `docker-compose.coolify-local.yml` para simular Traefik en local.

## STRUCTURE
```
./
├── docker-compose.yml                 # Producción (Coolify): 1 servicio `web`
├── docker-compose.coolify-local.yml   # Local: Traefik + `web` (servidor Node inline)
├── web/                               # Sitio estático + imagen nginx (puerto interno 8080)
│   ├── Dockerfile
│   ├── default.conf
│   └── index.html
├── traefik/
│   └── dynamic.yml                    # Config Traefik local (solo dev)
├── directo_coolify.md                 # Estándar/guía de despliegue Coolify
├── instr.md                           # Prompt consolidado: reglas obligatorias
├── desa.md                            # Prompt unificado: local vs producción
└── construir_skills.md                # Guía para skills en OMO
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Despliegue producción en Coolify | `docker-compose.yml` | Sin `ports:`; usa `expose: 8080` + `healthcheck` |
| Simular Traefik/Coolify en local | `docker-compose.coolify-local.yml` | Traefik en `8081/8443`; dashboard `8080` |
| Imagen producción del sitio | `web/Dockerfile` | `nginx:stable-alpine`, escucha en `8080` |
| Routing Traefik local | `traefik/dynamic.yml` | Apunta a `portal_web_local:8080` |
| Reglas “no negociables” | `instr.md` / `desa.md` | “vía negativa” (prohibiciones) |

## CONVENTIONS (DEVIATIONS)
- Producción (Coolify): no usar `ports:` en servicios web; Traefik/Coolify hace routing/TLS.
- Puerto interno estándar del servicio web: `8080` (`expose: "8080"`).
- Imágenes con versiones fijas (no `latest`).
- `restart: unless-stopped` en producción.
- `healthcheck` obligatorio; debe usar binarios presentes en la imagen (`wget` en `nginx:stable-alpine`).

## ANTI-PATTERNS (THIS PROJECT)
- No configurar Traefik manualmente en producción (solo aplica a `docker-compose.coolify-local.yml`).
- No añadir `network_mode: host`.
- No hardcodear credenciales en compose; usar variables/Coolify UI.
- No commitear `.env.local` ni llaves (`.ssh_deploy_key*`): están ignoradas por `.gitignore`.

## COMMANDS
```bash
# Producción (validación local de imagen)
docker compose -f docker-compose.yml build

docker compose -f docker-compose.yml up -d

# Local (Traefik simulado; entrada por http://localhost:8081)
docker compose -f docker-compose.coolify-local.yml up -d --build
```

## NOTES
- `web/Dockerfile` genera su propia config nginx inline; `web/default.conf` existe pero no se usa actualmente (solo referencia).
- `docker-compose.coolify-local.yml` usa un servidor Node inline para servir archivos desde `./web` (bind mount), no la imagen nginx de producción.
