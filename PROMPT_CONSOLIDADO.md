# 🎯 PROMPT CONSOLIDADO: Docker-Compose en Producción (Agnóstico)

**Versión:** 1.0  
**Creado:** 2026-02-07  
**Aplicable a:** Cualquier proyecto con proxy inverso gestionado (Coolify, Kubernetes, Nomad, etc.)

---

## PROPÓSITO

Este documento es el **prompt maestro** que debe inyectarse en AGENTS.md de **cualquier nuevo proyecto** que use docker-compose en producción con proxy inverso. Sintetiza lecciones aprendidas de fallos reales (labels faltantes = `502 Bad Gateway`).

**Lección clave:** En producción con proxy gestionado, `docker-compose.yml` es **orquestación + configuración de routing**. Los **labels son obligatorios**.

---

## I. EL TRIÁNGULO CRÍTICO

```
┌────────────────────────────────────────┐
│  INTERNET (DNS, Cloudflare, etc.)     │
└──────────────┬─────────────────────────┘
               │ (Dominio)
               ↓
┌────────────────────────────────────────┐
│  PROXY INVERSO (Traefik, Nginx, etc.)  │
│  - Lee LABELS de contenedores          │
│  - Enruta por HOST/PATH                │
│  - Maneja TLS/HTTPS                    │
│  - Aplica middlewares                  │
└──────────────┬─────────────────────────┘
               │ (Red interna)
               ↓
┌────────────────────────────────────────┐
│  CONTENEDORES (docker-compose.yml)     │
│  - Escuchan en puerto interno          │
│  - Exponen LABELS para proxy           │
│  - Comunican por nombre de servicio    │
└────────────────────────────────────────┘
```

**Sin LABELS → proxy no sabe rutear → 502 Bad Gateway**

---

## II. ESTRUCTURA OBLIGATORIA

### A. Servicios (Contenedores)

```yaml
services:
  {nombre}:
    image: {imagen}:{version}           # ✅ Versión fija, nunca latest
    restart: unless-stopped              # ✅ Recuperación automática
    networks:
      - {red-nombre}                     # ✅ Red privada interna
    expose:
      - "{puerto-interno}"               # ✅ Documentar, no mapear
    environment:
      - VAR=${VAR}                       # ✅ Variables desde .env
    volumes:
      - {volumen}:/datos                 # ✅ Persistencia nombrada
    healthcheck:                         # ✅ Obligatorio en servicios críticos
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:{puerto}/"]
      interval: 30s
      timeout: 5s
      retries: 3
    depends_on:
      {dep}:
        condition: service_healthy       # ✅ Esperar a dependencias
    labels:                              # ⚠️ CRÍTICO: Routing para proxy
      - "traefik.enable=true"
      - "traefik.docker.network={red}"
      # ... (ver sección III)
```

### B. Redes

```yaml
networks:
  {red-nombre}:
    external: false                      # false: docker-compose crea
                                         # true: orquestador (Coolify) crea
    driver: bridge
```

### C. Volúmenes

```yaml
volumes:
  {vol-nombre}:                          # Volumen nombrado
    driver: local
```

---

## III. LABELS: LA CAPA DE ROUTING (CRÍTICO)

### ¿Por Qué Son Obligatorios?

**Sin labels, el proxy NO SABE:**
- Qué servicios publicar en internet
- Qué dominio enruta a qué contenedor
- Qué puerto interno escucha
- Si aplicar HTTPS/TLS
- Cómo gestionar redirects, autenticación

**Resultado:** Contenedor corre, pero error `502 Bad Gateway`.

### Estructura de Labels (4 Grupos)

```yaml
labels:
  # === GRUPO 1: ACTIVACIÓN ===
  - "traefik.enable=true"                        # Activar
  - "traefik.docker.network={red-nombre}"        # Red donde está

  # === GRUPO 2: ENRUTADOR (ROUTER) ===
  - "traefik.http.routers.{nombre-router}.rule=Host(`{dominio}`)"
  - "traefik.http.routers.{nombre-router}.entrypoints=https"
  - "traefik.http.routers.{nombre-router}.tls=true"
  - "traefik.http.routers.{nombre-router}.tls.certresolver=letsencrypt"

  # === GRUPO 3: SERVICIO (BACKEND) ===
  - "traefik.http.services.{nombre-servicio}.loadbalancer.server.port={puerto}"

  # === GRUPO 4: MIDDLEWARE (OPCIONAL) ===
  - "traefik.http.middlewares.{nombre}.redirectscheme.scheme=https"
```

### Variantes de Reglas

| Caso | Regla | Ejemplo |
|------|-------|---------|
| **Web por dominio** | `Host(\`ejemplo.com\`)` | Todo el tráfico a ese dominio |
| **API con ruta** | `Host(\`api.com\`) && PathPrefix(\`/api\`)` | Solo `/api/*` |
| **Múltiples subdominios** | Dos routers con mismo servicio | `api.com` y `backend.com` → mismo contenedor |
| **Interno (SIN labels)** | ❌ No incluir | Base de datos, Redis |
| **HTTP→HTTPS** | Router http + middleware | Redirigir automáticamente |

### Ejemplo Completo

```yaml
services:
  web:
    image: nginx:1.26-alpine
    expose: ["8080"]
    networks: [backend]
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=backend"
      
      # HTTPS
      - "traefik.http.routers.web-https.rule=Host(`ejemplo.com`)"
      - "traefik.http.routers.web-https.entrypoints=https"
      - "traefik.http.routers.web-https.tls=true"
      - "traefik.http.routers.web-https.tls.certresolver=letsencrypt"
      
      # HTTP → HTTPS
      - "traefik.http.routers.web-http.rule=Host(`ejemplo.com`)"
      - "traefik.http.routers.web-http.entrypoints=http"
      - "traefik.http.routers.web-http.middlewares=web-redirect"
      - "traefik.http.middlewares.web-redirect.redirectscheme.scheme=https"
      - "traefik.http.middlewares.web-redirect.redirectscheme.permanent=true"
      
      # SERVICIO
      - "traefik.http.services.web.loadbalancer.server.port=8080"

  api:
    image: myapp:1.0.0
    expose: ["8000"]
    networks: [backend]
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=backend"
      - "traefik.http.routers.api.rule=Host(`api.ejemplo.com`) && PathPrefix(`/api`)"
      - "traefik.http.routers.api.priority=100"        # ⚠️ Mayor prioridad
      - "traefik.http.routers.api.entrypoints=https"
      - "traefik.http.routers.api.tls=true"
      - "traefik.http.routers.api.tls.certresolver=letsencrypt"
      - "traefik.http.services.api.loadbalancer.server.port=8000"

  db:
    image: postgres:16-alpine
    expose: ["5432"]
    networks: [backend]
    # ❌ NO LABELS: acceso interno solo

networks:
  backend:
    external: false
```

---

## IV. PROHIBICIONES ABSOLUTAS

| ❌ NO HACER | ✅ HACER | Riesgo |
|------------|----------|--------|
| `ports: ["8080:8080"]` en web | Solo `expose: ["8080"]` | Abre puerto; inseguro; proxy no lo usa |
| `image: nginx:latest` | `nginx:1.26-alpine` | Cambios inesperados; incompatibilidades |
| Credenciales en compose | Variables `${VAR}` desde `.env` | Exposición en git; auditoría fallida |
| `network_mode: host` | Red bridge/overlay nombrada | Sin service discovery; conflictos |
| Labels malformados | Validar con `docker compose config` | Proxy ignora silenciosamente |
| Omitir labels en público | Labels completos (4 grupos) | Proxy no sabe rutear (502) |
| Puertos DB al host | Solo `expose:`, sin `ports:` | Acceso externo; security breach |
| Sin `restart` en prod | `restart: unless-stopped` | Caída sin recuperación |

---

## V. CHECKLIST PRE-DESPLIEGUE

```bash
# 1. SINTAXIS
docker compose config                    # ✅ Sin errores

# 2. SEGURIDAD
# ✅ No hay credenciales en compose
# ✅ Imágenes con versión fija (no latest)
# ✅ restart: unless-stopped en servicios críticos

# 3. LABELS Y ROUTING
docker inspect {container} | grep Labels # ✅ Labels presentes
# ✅ traefik.enable=true
# ✅ Router con regla (Host/PathPrefix)
# ✅ Servicio con puerto correcto
# ✅ TLS configurado

# 4. PERSISTENCIA
# ✅ Volúmenes nombrados para datos (no bind mount en prod)
# ✅ .env y credenciales en .gitignore

# 5. REDES
# ✅ Todos los servicios en la misma red
# ✅ traefik.docker.network coincide con networks:

# 6. CONECTIVIDAD
docker exec {container} wget -qO- http://127.0.0.1:{puerto}/
# ✅ Responde sin errores
```

---

## VI. DIAGNÓSTICO RÁPIDO (Si Falla)

### "502 Bad Gateway"

**Orden de verificación:**
1. ¿Labels presentes? → `docker inspect {container}`
2. ¿Puerto interno correcto? → `expose: ["8080"]` vs donde escucha app
3. ¿Red correcta? → `traefik.docker.network` == `networks:`
4. ¿Contenedor responde? → `docker exec {c} wget -qO- http://127.0.0.1:PUERTO`

**Causa más probable:** Labels ausentes o malformados.

### "Connection Refused"

- App escucha en `0.0.0.0` (no localhost)
- Puerto `expose:` coincide con config de app
- Healthcheck OK (app iniciada)

### "DNS no resuelve"

- Registro DNS apunta a proxy (Cloudflare, Route53)
- Proxy escucha en la IP correcta
- Dominio en label coincide con DNS

---

## VII. TEMPLATE REUTILIZABLE

```yaml
version: "3.9"

services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    image: {proyecto}_{servicio}:{version}
    restart: unless-stopped
    networks: [backend]
    expose: ["{puerto}"]
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-info}
      - SECRET_KEY=${SECRET_KEY}
      - DB_HOST=db
      - DB_PORT=5432
    volumes:
      - app_data:/data
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:{puerto}/health"]
      interval: 30s
      timeout: 5s
      retries: 3
    depends_on:
      db:
        condition: service_healthy
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=backend"
      # HTTPS
      - "traefik.http.routers.app-https.rule=Host(`{dominio}`)"
      - "traefik.http.routers.app-https.entrypoints=https"
      - "traefik.http.routers.app-https.tls=true"
      - "traefik.http.routers.app-https.tls.certresolver=letsencrypt"
      # HTTP → HTTPS
      - "traefik.http.routers.app-http.rule=Host(`{dominio}`)"
      - "traefik.http.routers.app-http.entrypoints=http"
      - "traefik.http.routers.app-http.middlewares=app-redirect"
      - "traefik.http.middlewares.app-redirect.redirectscheme.scheme=https"
      - "traefik.http.middlewares.app-redirect.redirectscheme.permanent=true"
      # SERVICIO
      - "traefik.http.services.app.loadbalancer.server.port={puerto}"

  db:
    image: postgres:16-alpine
    restart: unless-stopped
    networks: [backend]
    expose: ["5432"]
    environment:
      - POSTGRES_DB=${DB_NAME}
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
    # ❌ NO LABELS

volumes:
  app_data:
  db_data:

networks:
  backend:
    external: false
```

---

## VIII. VARIABLES DE ENTORNO (.env)

**Archivo:** `.env` (copiar de `.env.example`, NO commitar)

```
# Infraestructura
PROXY_NETWORK=backend

# Base de Datos
DB_NAME=appdb
DB_USER=dbuser
DB_PASSWORD=super_secret_password_change_in_prod

# Aplicación
LOG_LEVEL=info
SECRET_KEY=random_secret_key_change_in_prod
ADMIN_USER=admin
ADMIN_PASSWORD=admin_password_change_in_prod

# Dominio
DOMAIN_NAME=ejemplo.com
LE_EMAIL=admin@ejemplo.com
```

---

## IX. ANTI-PATTERNS COMUNES

### El Fallo Silencioso

**Síntoma:** Contenedor corre perfecto, pero `502 Bad Gateway` desde navegador

**Causa:** Labels ausentes o malformados. Proxy no sabe cómo rutear.

**Prevención:**
- Checklist: ¿tiene labels?
- Validar: `docker inspect {container}`
- Revisar: `docker compose config`

### Porteo Innecesario

**Síntoma:** "Abrí puerto 8080 pero no lo necesitaba"

**Causa:** En producción con proxy, el proxy maneja todo. `ports:` es solo dev local.

**Solución:** Usar solo `expose:` en producción.

### Red Externa Incorrecta

**Síntoma:** "El proxy no ve mi contenedor"

**Causa:** `traefik.docker.network` no coincide con red real en compose.

**Solución:** Verificar: ambos deben tener el mismo nombre.

---

## X. NOTAS PARA AGENTES IA

Cuando trabajes en un proyecto nuevo con este prompt:

1. **Siempre consulta el skill `docker-compose-production`** si vas a:
   - Crear/modificar `docker-compose.yml`
   - Añadir servicios públicos
   - Validar antes de deploy

2. **Si hay conectividad fallida ("502"):**
   - Primero piensa: "¿faltan labels?"
   - Valida: `docker inspect` + `docker compose config`
   - Debugging: sección VI de este prompt

3. **Labels NO son opcionales en producción:**
   - Sin ellos, proxy no sabe qué hacer
   - Es como tener dirección pero sin número de casa

4. **Estructura correcta: servicios → volúmenes → redes**
   - No olvides healthchecks en DBs
   - No olvides labels en públicos
   - Documenta variables en `.env.example`

5. **Antes de cualquier deploy:**
   - `docker compose config` (sintaxis)
   - `docker inspect {container}` (labels)
   - Checklist sección V

---

## XI. REFERENCIAS

- [Docker Compose Spec](https://github.com/compose-spec/compose-spec)
- [Traefik Docker Provider](https://docs.traefik.io/providers/docker/)
- [Docker Labels](https://docs.docker.com/config/labels-custom-metadata/)
- **Skill local:** `.opencode/skills/docker-compose-production/SKILL.md`

---

## XII. CÓMO USAR ESTE PROMPT

### Para Nuevos Proyectos

1. Copia este documento a `AGENTS.md` del nuevo proyecto
2. Personaliza placeholders: `{proyecto}`, `{dominio}`, `{puerto}`, etc.
3. Copia el skill `docker-compose-production` a `.opencode/skills/`
4. Crea `.env.example` con variables

### Para Equipos/Agentes IA

Este prompt va en **AGENTS.md** para que:
- Agentes lean la estructura y convenciones obligatorias
- Sepan POR QUÉ los labels son críticos (no solo QUÉ)
- Tengan checklist y templates listos
- Comprendan diagnóstico común

### Evolución

Si encuentras nuevo anti-patrón o aprendizaje, actualiza este prompt. Es vivo.

---

## 🎯 RESUMEN EN UNA FRASE

**En producción con proxy gestionado, `docker-compose.yml` es orquestación + routing. Los labels son la puente. Sin ellos, 502.**

---

*Generado a partir de lecciones reales. Última actualización: 2026-02-07*