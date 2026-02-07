---
name: docker-compose-production
description: Plantilla agnóstica para docker-compose en producción con proxy inverso, incluyendo labels obligatorios para routing, validación, seguridad y best practices independientes de la infraestructura específica.
license: MIT
---

# Skill: Docker Compose para Producción (Agnóstico)

## 1. INTRODUCCIÓN: POR QUÉ ESTE SKILL EXISTE

Cuando trabajas con **proxy inversos gestionados** (Traefik en Coolify, Nginx Ingress en Kubernetes, etc.), el `docker-compose.yml` **no es solo orquestación de contenedores**: es también **configuración de enrutamiento**.

**Lección aprendida:** Muchos despliegues fallan silenciosamente porque falta la **capa de configuración de routing** (labels). El proxy no sabe cómo acceder a tu servicio. El contenedor corre perfectamente, pero no es alcanzable desde internet.

Este skill previene ese problema proporcionando una estructura probada y agnóstica.

---

## 2. ARQUITECTURA CONCEPTUAL

### El Triángulo de Despliegue en Producción

```
┌─────────────────────────────────────────┐
│  INTERNET / DNS / CDN                   │
│  (Cloudflare, Route53, etc.)            │
└──────────────┬──────────────────────────┘
               │ (Dominio + DNS records)
               ↓
┌─────────────────────────────────────────┐
│  PROXY INVERSO (Traefik, Nginx, etc.)   │
│  - Lee labels de contenedores           │
│  - Enruta tráfico por HOST/PATH         │
│  - Gestiona SSL/TLS                     │
│  - Aplica middlewares (auth, redirect)  │
└──────────────┬──────────────────────────┘
               │ (Red interna)
               ↓
┌─────────────────────────────────────────┐
│  CONTENEDORES (docker-compose)          │
│  - Escuchan en puerto interno           │
│  - Exponen metadatos (labels)           │
│  - Comunican entre sí por nombre        │
└─────────────────────────────────────────┘
```

**Conclusión clave:** Sin labels, el proxy no entiende cómo rutear. Es como tener una dirección de casa pero no un número en la puerta.

---

## 3. ESTRUCTURA OBLIGATORIA (Independiente de la Infraestructura)

### Nivel 1: Definición de Servicios (Contenedores)

```yaml
services:
  {nombre-servicio}:
    image: {imagen}:{version-fija}      # ✅ Versión específica, NO latest
    restart: unless-stopped              # ✅ Recuperación automática en prod
    networks:
      - {nombre-red}                     # ✅ Red privada (no ports!)
    expose:
      - "{puerto-interno}"               # ✅ Documentar puerto, no mapear
    environment:
      - VAR_CRITICA=${VAR_CRITICA}       # ✅ Variables desde .env, no hardcodeadas
    volumes:
      - {volumen}:/ruta/persistencia     # ✅ Datos persistentes
    healthcheck:                         # ✅ Obligatorio en servicios críticos
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:{puerto}/health"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
    depends_on:                          # ✅ Ordenamiento de inicio
      {dependencia}:
        condition: service_healthy
    labels:                              # ⚠️ CRÍTICO: Labels para proxy inverso
      - "traefik.enable=true"
      # ... (ver sección 4)
```

---

### Nivel 2: Definición de Redes (Comunicación Interna)

```yaml
networks:
  {nombre-red}:                          # Red privada para comunicación interna
    external: true                       # True si la crea Coolify/Kubernetes
                                         # False si docker-compose la crea
    driver: bridge                       # (Opcional) Especificar driver
```

**Importante:**
- **Nunca** exponer puertos del host (`ports:`) en servicios web.
- La comunicación entre contenedores es **por nombre de servicio** y puerto interno (ej. `http://api:8000`).
- El proxy inverso está en la misma red y accede usando el puerto definido en `expose:`.

---

### Nivel 3: Definición de Volúmenes (Persistencia)

```yaml
volumes:
  {nombre-volumen}:                      # Volumen nombrado (managed by Docker)
    driver: local                        # (Opcional)
  # O
  {ruta-local}:/ruta/contenedor         # Bind mount (cuidado en prod)
```

**Regla de oro:**
- DBs, archivos, logs → volúmenes nombrados.
- Configuración inmutable → bind mount o COPY en Dockerfile.
- Nunca commitear datos en la imagen.

---

## 4. LABELS PARA PROXY INVERSO (La Parte Crítica)

### ¿Por Qué Labels Son Obligatorios?

Sin labels, el proxy inverso **no sabe:**
- Qué servicios publicar en internet.
- Qué dominio/subdominio enruta a qué contenedor.
- Qué puerto interno escucha cada servicio.
- Si aplicar HTTPS/TLS.
- Cómo gestionar redirects, autenticación, cachés.

**Resultado sin labels:** Contenedor corre, pero no es alcanzable. Error `502 Bad Gateway` o `Connection Refused`.

---

### Estructura de Labels (Agnóstico, Aplica a Traefik/Nginx/Kong/etc.)

Aunque usamos nomenclatura Traefik, el **patrón conceptual** aplica a cualquier proxy:

```yaml
labels:
  # === GRUPO 1: ACTIVACIÓN Y CONTEXTO ===
  - "traefik.enable=true"                           # Activar exposición
  - "traefik.docker.network={nombre-red}"           # Red donde existe el contenedor
  
  # === GRUPO 2: DEFINIR EL ENRUTADOR (Router/Ingress) ===
  - "traefik.http.routers.{nombre-router}.rule=Host(`{dominio}`)"
  - "traefik.http.routers.{nombre-router}.entrypoints=https"
  - "traefik.http.routers.{nombre-router}.tls=true"
  - "traefik.http.routers.{nombre-router}.tls.certresolver=letsencrypt"
  
  # === GRUPO 3: DEFINIR EL SERVICIO (Backend / Load Balancer) ===
  - "traefik.http.services.{nombre-servicio}.loadbalancer.server.port={puerto-interno}"
  
  # === GRUPO 4: MIDDLEWARES (Opcional pero común) ===
  - "traefik.http.middlewares.{nombre-middleware}.{tipo}.{config}=valor"
```

---

### Variantes de Reglas (Agnóstico)

La regla (rule) define **cuándo** el proxy enruta a este contenedor.

| Caso | Regla Traefik | Concepto | Ejemplo Real |
|------|---------------|----------|--------------|
| **Web pública por dominio** | `Host(\`ejemplo.com\`)` | Todo lo que llegue a ese dominio → aquí | Blog estático en `blog.ejemplo.com` |
| **API bajo ruta específica** | `Host(\`api.ejemplo.com\`) && PathPrefix(\`/api\`)` | Dominio + prefijo de ruta | API con versionamiento: `/v1/users`, `/v1/products` |
| **Múltiples subdominios, mismo servicio** | Dos routers con mismo `{nombre-servicio}` | Redundancia/alias | `api.ejemplo.com` y `backend.ejemplo.com` → mismo contenedor |
| **Servicio interno (SIN exposición)** | ❌ NO incluir labels | No publicar | Base de datos, Redis, cola de trabajo |
| **Redireccionamiento HTTP → HTTPS** | Dos routers: uno en `http`, otro en `https` con middleware | Seguridad + UX | Usuario escribe `http://ejemplo.com` → automáticamente `https://` |

---

### Ejemplo Práctico: Estructura Completa

```yaml
services:
  frontend:
    image: nginx:1.26-alpine
    expose:
      - "8080"
    networks:
      - backend
    labels:
      # Activación
      - "traefik.enable=true"
      - "traefik.docker.network=backend"
      
      # Router HTTPS (seguro)
      - "traefik.http.routers.web-https.rule=Host(`ejemplo.com`,`www.ejemplo.com`)"
      - "traefik.http.routers.web-https.entrypoints=https"
      - "traefik.http.routers.web-https.tls=true"
      - "traefik.http.routers.web-https.tls.certresolver=letsencrypt"
      
      # Router HTTP → HTTPS (redirigir)
      - "traefik.http.routers.web-http.rule=Host(`ejemplo.com`,`www.ejemplo.com`)"
      - "traefik.http.routers.web-http.entrypoints=http"
      - "traefik.http.routers.web-http.middlewares=web-redirect"
      
      # Middleware: redireccionamiento
      - "traefik.http.middlewares.web-redirect.redirectscheme.scheme=https"
      - "traefik.http.middlewares.web-redirect.redirectscheme.permanent=true"
      
      # Servicio (backend)
      - "traefik.http.services.web.loadbalancer.server.port=8080"

  api:
    image: myapp:2.0.1
    expose:
      - "8000"
    networks:
      - backend
    environment:
      - DB_HOST=postgres
      - DB_PORT=5432
    depends_on:
      postgres:
        condition: service_healthy
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=backend"
      
      # Router con prefijo de ruta (prioridad alta)
      - "traefik.http.routers.api.rule=Host(`api.ejemplo.com`) && PathPrefix(`/api`)"
      - "traefik.http.routers.api.entrypoints=https"
      - "traefik.http.routers.api.tls=true"
      - "traefik.http.routers.api.tls.certresolver=letsencrypt"
      - "traefik.http.routers.api.priority=100"  # ⚠️ Mayor prioridad que web
      
      # Servicio
      - "traefik.http.services.api.loadbalancer.server.port=8000"

  postgres:
    image: postgres:16-alpine
    expose:
      - "5432"
    networks:
      - backend
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    # ❌ NO LABELS: base de datos es solo acceso interno
    # ❌ NO ports: no se expone al host ni a internet

volumes:
  postgres_data:

networks:
  backend:
    external: false  # docker-compose crea la red
```

---

## 5. ANTI-PATRONES CRÍTICOS (PROHIBICIONES)

| ❌ Antipatrón | ✅ Corrección | Consecuencia del Error |
|---------------|-------------|----------------------|
| `ports: ["8080:8080"]` en servicio web | Usar solo `expose: ["8080"]` | Abre puerto al host; proxy no lo usa; inseguro |
| `latest` en image tag | Versión fija: `nginx:1.26-alpine` | Cambios inesperados; incompatibilidades; no reproducible |
| Credenciales hardcodeadas en labels | `environment: [DB_PASSWORD=${DB_PASSWORD}]` | Exposición en versión control; auditoría fallida |
| Servicios en `network_mode: host` | Usar red bridge/overlay named | Conflictos de puerto; imposible aislar; sin service discovery |
| Labels mal formateados (comillas, sintaxis) | Validar con `docker compose config` | Labels ignorados silenciosamente; proxy no sabe rutear |
| Mismo nombre de router en dos servicios | Nombres únicos con sufijo: `{servicio}-{variante}` | Conflicto de configuración; rutas impredecibles |
| `priority` sin documentar | Documentar: "Frontend: priority=1, API: priority=100" | Routeo ambiguo; comportamiento inesperado |
| Omitir `restart: unless-stopped` en prod | Incluir siempre en servicios críticos | Caída sin recuperación automática |
| Healthcheck solo con `curl` en Alpine | Usar `wget` o herramienta presente en imagen | Healthcheck falla; servicio marcado como unhealthy |

---

## 6. VALIDACIÓN PRE-DESPLIEGUE (CHECKLIST)

### Antes de `docker compose up -d`:

**Sintaxis:**
- ✅ `docker compose config` ejecuta sin errores.
- ✅ No hay comillas innecesarias en labels.
- ✅ Backticks (`) en reglas de Traefik: `Host(\`ejemplo.com\`)`.

**Seguridad:**
- ✅ No hay credenciales en el archivo (solo variables `${VAR}`).
- ✅ `restart: unless-stopped` en todos los servicios críticos.
- ✅ Imágenes tienen versión fija (no `latest`).
- ✅ Bases de datos **NO** tienen labels de Traefik.
- ✅ Puertos internos (5432, 6379, etc.) NO expuestos al host.

**Redes y Comunicación:**
- ✅ Todos los servicios están en la misma red.
- ✅ La red existe o está marcada para ser creada (`external: false/true`).
- ✅ Servicios se referencia por nombre: `postgres`, no `localhost`.

**Labels y Routing:**
- ✅ Servicios públicos tienen `traefik.enable=true`.
- ✅ Router names son únicos y kebab-case.
- ✅ `loadbalancer.server.port` coincide con `expose:`.
- ✅ `traefik.docker.network` coincide con `networks:`.
- ✅ TLS está activado para HTTPS (`tls=true`).
- ✅ Redirecciones HTTP→HTTPS están presentes.
- ✅ Prioridades definidas si hay múltiples routers por dominio.

**Persistencia:**
- ✅ Volúmenes nombrados para datos (DB, uploads).
- ✅ Volúmenes NO están gitignored (no hardcodear datos).

**Dependencias:**
- ✅ `depends_on` con `condition: service_healthy`.
- ✅ Servicios esperan a que dependencias estén listas.

**Logging y Observabilidad:**
- ✅ Healthchecks presentes en servicios críticos.
- ✅ Variables de debug/log están documentadas.

---

## 7. FLUJO DE DIAGNÓSTICO (Si Algo Falla)

### Escenario: "Mi contenedor corre pero no es alcanzable desde internet"

```bash
# 1. Verificar que el contenedor está up
docker compose ps

# 2. Verificar que el contenedor responde localmente
docker exec {nombre-contenedor} wget -qO- http://127.0.0.1:{puerto}/

# 3. Revisar logs del proxy (ej. Traefik)
docker logs {nombre-contenedor-traefik}

# 4. Validar sintaxis del compose
docker compose config

# 5. Revisar labels específicos
docker inspect {nombre-contenedor} | grep -A 50 '"Labels"'

# 6. Probar conectividad entre contenedores
docker exec {api-container} ping postgres
```

**Causas comunes (en orden de probabilidad):**
1. **Labels malformados o ausentes** → El proxy no sabe que el servicio existe.
2. **Puerto interno incorrecto** → `expose: ["8080"]` pero la app escucha en `3000`.
3. **Red incorrecta** → `traefik.docker.network` no coincide con `networks:`.
4. **Dominio no apunta al proxy** → DNS/Cloudflare no configurado.
5. **Proxy está down** → El proxy inverso mismo tiene problemas.

---

## 8. TEMPLATE REUTILIZABLE (Copia y Adapta)

```yaml
# docker-compose.yml
# Proyecto: {Nombre}
# Ambiente: Production
# Proxy Inverso: Traefik (Coolify / On-Premise)
# Generado: {fecha}

version: "3.9"

services:
  # APLICACIÓN PRINCIPAL
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    image: {proyecto}_{servicio}:{version}
    restart: unless-stopped
    networks:
      - {red-nombre}
    expose:
      - "{puerto}"
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-info}
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - {vol-nombre}:/ruta/datos
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
      - "traefik.docker.network={red-nombre}"
      - "traefik.http.routers.app-https.rule=Host(`{dominio}`)"
      - "traefik.http.routers.app-https.entrypoints=https"
      - "traefik.http.routers.app-https.tls=true"
      - "traefik.http.routers.app-https.tls.certresolver=letsencrypt"
      - "traefik.http.routers.app-http.rule=Host(`{dominio}`)"
      - "traefik.http.routers.app-http.entrypoints=http"
      - "traefik.http.routers.app-http.middlewares=app-redirect"
      - "traefik.http.middlewares.app-redirect.redirectscheme.scheme=https"
      - "traefik.http.middlewares.app-redirect.redirectscheme.permanent=true"
      - "traefik.http.services.app.loadbalancer.server.port={puerto}"

  # BASE DE DATOS (SIN EXPOSICIÓN)
  db:
    image: postgres:16-alpine
    restart: unless-stopped
    networks:
      - {red-nombre}
    expose:
      - "5432"
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

volumes:
  {vol-nombre}:
  db_data:

networks:
  {red-nombre}:
    external: false  # O true si Coolify la crea
```

---

## 9. MEJORES PRÁCTICAS POR ESCENARIO

### Escenario A: Sitio Estático + API REST bajo el mismo dominio

```yaml
# Dos servicios, mismo dominio, rutas diferentes
# api.ejemplo.com/api/* → API container (puerto 8000, priority=100)
# api.ejemplo.com/ → Frontend estático (puerto 8080, priority=1)

services:
  frontend:
    # ... (nginx con HTML/CSS/JS)
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=app"
      - "traefik.http.routers.web.rule=Host(`api.ejemplo.com`)"
      - "traefik.http.routers.web.priority=1"  # Baja prioridad
      - "traefik.http.routers.web.entrypoints=https"
      - "traefik.http.routers.web.tls=true"
      - "traefik.http.routers.web.tls.certresolver=letsencrypt"
      - "traefik.http.services.web.loadbalancer.server.port=8080"

  api:
    # ... (Node.js, Python, Go, etc.)
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=app"
      - "traefik.http.routers.api.rule=Host(`api.ejemplo.com`) && PathPrefix(`/api`)"
      - "traefik.http.routers.api.priority=100"  # Alta prioridad (evaluado primero)
      - "traefik.http.routers.api.entrypoints=https"
      - "traefik.http.routers.api.tls=true"
      - "traefik.http.routers.api.tls.certresolver=letsencrypt"
      - "traefik.http.services.api.loadbalancer.server.port=8000"
```

### Escenario B: Microservicios en subdominio.ejemplo.com

```yaml
services:
  service1:
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.svc1.rule=Host(`service1.ejemplo.com`)"
      - "traefik.http.services.svc1.loadbalancer.server.port=3000"

  service2:
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.svc2.rule=Host(`service2.ejemplo.com`)"
      - "traefik.http.services.svc2.loadbalancer.server.port=3000"
```

### Escenario C: Servicio interno + Admin Panel accesible

```yaml
services:
  worker:
    # ❌ NO LABELS: solo acceso interno desde app
    # Accesible como "worker:8000" desde otros contenedores
    labels: []  # O simplemente omitir la sección

  admin:
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.admin.rule=Host(`admin.ejemplo.com`)"
      - "traefik.http.routers.admin.entrypoints=https"
      - "traefik.http.routers.admin.tls=true"
      - "traefik.http.routers.admin.tls.certresolver=letsencrypt"
      - "traefik.http.services.admin.loadbalancer.server.port=8080"
      # ⚠️ Recomendación: añadir autenticación (BasicAuth, OAuth2, etc.)
```

---

## 10. CUÁNDO INVOCAR ESTE SKILL

✅ **Usa este skill cuando:**
- Estés creando o modificando un `docker-compose.yml` para producción.
- Necesites decidir si un servicio requiere labels de proxy.
- Configures routing por host, path, o combinación.
- Falte conectividad y sospechas que es por falta de labels.
- Valides sintaxis y buenas prácticas antes de desplegar.

❌ **No necesitas este skill si:**
- Solo trabajas con desarrollo local (`docker compose` sin proxy).
- El proxy está configurado externamente (Kubernetes Ingress, etc.).

---

## 11. REFERENCIAS Y APUNTES FINALES

**Documentación oficial:**
- [Docker Compose Spec](https://github.com/compose-spec/compose-spec)
- [Traefik Docker Provider](https://docs.traefik.io/providers/docker/)
- [Docker Labels Best Practices](https://docs.docker.com/config/labels-custom-metadata/)

**Aprendizaje clave:**
> "Sin labels, el proxy inverso no sabe que tu servicio existe. Es la conexión entre orquestación de contenedores y enrutamiento de tráfico. No son opcionales en producción."

**Próximos pasos:**
- Revisar AGENTS.md del proyecto para contexto específico.
- Validar labels con `docker compose config`.
- Testear accesibilidad con `curl` desde fuera del contenedor.
```

Ahora voy a crear un **AGENTS.md** agnóstico que se pueda usar como plantilla para nuevos proyectos: