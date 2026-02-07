# PROJECT KNOWLEDGE BASE

**Generated:** 2026-02-07
**Branch:** main
**Commit:** 7db9a25

## OVERVIEW
Portal estático “da-tica” desplegable en Coolify (Traefik gestionado por Coolify) usando un único `docker-compose.yml` para producción.

## STRUCTURE
```
./
├── docker-compose.yml                 # Producción (Coolify): 1 servicio `web`
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
| Imagen producción del sitio | `web/Dockerfile` | `nginx:1.26.3-alpine`, escucha en `8080` |
| Routing Traefik local (opcional) | `traefik/dynamic.yml` | Solo si montas Traefik por tu cuenta en dev |
| Reglas “no negociables” | `instr.md` / `desa.md` | “vía negativa” (prohibiciones) |

## CONVENTIONS (DEVIATIONS)
- Producción (Coolify): no usar `ports:` en servicios web; Traefik/Coolify hace routing/TLS.
- Puerto interno estándar del servicio web: `8080` (`expose: "8080"`).
- Imágenes con versiones fijas (no `latest`).
- `restart: unless-stopped` en producción.
- `healthcheck` obligatorio; debe usar binarios presentes en la imagen (`wget` en `nginx:stable-alpine`).

## ANTI-PATTERNS (THIS PROJECT)
- No configurar Traefik manualmente en producción (Coolify lo gestiona).
- No añadir `network_mode: host`.
- No hardcodear credenciales en compose; usar variables/Coolify UI.
- No commitear `.env.local` ni llaves (`.ssh_deploy_key*`): están ignoradas por `.gitignore`.

## COMMANDS
```bash
# Producción (validación local de imagen)
docker compose -f docker-compose.yml build

docker compose -f docker-compose.yml up -d
```

## NOTES
- `web/Dockerfile` genera su propia config nginx inline; `web/default.conf` existe pero no se usa actualmente (solo referencia).
- `traefik/dynamic.yml` queda como referencia opcional para dev local; no se usa en producción.
