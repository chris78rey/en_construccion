---
name: validate-common-coolify-errors
description: Identifica y resuelve los 15+ errores más comunes en despliegues Coolify (puertos mal declarados, healthchecks fallidos, persistencia incorrecta, variables ausentes, problemas de build, orden de arranque).
license: MIT
---

# Skill: Validación de Errores Comunes en Coolify

## Propósito

Este skill identifica, diagnostica y resuelve los **15+ errores más comunes** que causan fallos en despliegues Coolify. Cada error incluye síntomas, causa raíz, diagnóstico rápido y corrección inmediata.

---

## Catálogo Priorizado de Errores Comunes

### ERROR #1: Puertos Mal Declarados (servicios web con `ports:`)

**Síntomas:**
- Servicio inaccesible públicamente
- Traefik/Coolify no enruta hacia el servicio
- Logs: "connection refused" o timeout

**Causa Raíz:**
- `ports: "8080:8080"` en servicios web → Coolify no puede gestionar el enrutamiento
- El servicio está expuesto en `localhost:8080` del VPS, no accesible vía Traefik

**Diagnóstico Rápido:**
```bash
# En Coolify, revisar logs del servicio
docker logs <container_name>

# Verificar qué puertos está exponiendo
docker port <container_name>

# Buscar en compose si hay ports: en servicios web
grep -A 5 "services:" docker-compose.yml | grep -B 3 "ports:"
```

**Corrección Inmediata:**
```yaml
# ❌ INCORRECTO
services:
  web:
    image: node:18-alpine
    ports:
      - "8080:8080"

# ✅ CORRECTO
services:
  web:
    image: node:18-alpine
    expose:
      - "8080"
```

**Medida Preventiva:**
- Usar siempre `expose:` en servicios web, nunca `ports:`
- Documentar puerto interno en comentarios
- Coolify detectará automáticamente el puerto si está en `expose:`

---

### ERROR #2: Servicios Escuchando en `localhost` en lugar de `0.0.0.0`

**Síntomas:**
- Servicio "funciona" en local pero no responde en Coolify
- Traefik ve el contenedor pero no puede conectar
- Logs: "connection refused" desde Traefik

**Causa Raíz:**
- App configurada para escuchar solo en `127.0.0.1` o `localhost`
- Traefik intenta conectar desde la red Docker, no desde localhost
- Ej: `node app.js --host localhost` o `app.listen('localhost', 8080)`

**Diagnóstico Rápido:**
```bash
# Verificar qué interfaz escucha el servicio
docker exec <container_name> netstat -tlnp | grep LISTEN
# o con ss (más moderno)
docker exec <container_name> ss -tlnp | grep LISTEN

# Debería mostrar 0.0.0.0:8080, no 127.0.0.1:8080
```

**Corrección Inmediata:**
```dockerfile
# Dockerfile - Modificar comando de inicio
# ❌ Incorrecto
CMD ["node", "server.js", "--host", "localhost"]

# ✅ Correcto
CMD ["node", "server.js", "--host", "0.0.0.0"]

# O en environment variable
ENV HOST=0.0.0.0
```

```yaml
# O en docker-compose
services:
  app:
    environment:
      - HOST=0.0.0.0
      - PORT=8080
```

**Medida Preventiva:**
- Revisar configuración de la app (framework settings, env vars)
- Frameworks modernos por defecto escuchan en `0.0.0.0` (Express, FastAPI, etc.)
- Documentar en README: "Asegúrate de que la app escucha en 0.0.0.0"

---

### ERROR #3: Healthchecks Fallidos por Herramientas Ausentes

**Síntomas:**
- Contenedor en estado "unhealthy" o "restarting"
- Logs: `exec: "wget": executable file not found` o similar
- Servicio nunca llega a "healthy"

**Causa Raíz:**
- Healthcheck usa `wget`, `curl` u otra herramienta no presente en la imagen
- Imagen alpine o slim no incluye estas herramientas por defecto
- Ej: intentar usar `wget` en image `node:18-alpine`

**Diagnóstico Rápido:**
```bash
# Ver estado del healthcheck
docker inspect <container_name> | grep -A 10 "State"

# Revisar logs específicos del healthcheck
docker inspect <container_name> | grep -A 5 "Health"

# Ejecutar manualmente el test del healthcheck
docker exec <container_name> wget -qO- http://127.0.0.1:8080/health
```

**Corrección Inmediata:**

**Opción A: Usar herramientas disponibles en la imagen**
```yaml
# Node.js alpine tiene sh y node, usar node para healthcheck
services:
  app:
    image: node:18-alpine
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://127.0.0.1:8080',res=>process.exit(res.statusCode===200?0:1)).on('error',()=>process.exit(1))"]
      interval: 30s
      timeout: 5s
      retries: 3
```

**Opción B: Instalar herramientas necesarias en Dockerfile**
```dockerfile
FROM node:18-alpine
RUN apk add --no-cache curl
COPY . .
RUN npm install
CMD ["npm", "start"]
```

**Opción C: Usar `/bin/sh` con comando directo**
```yaml
healthcheck:
  test: ["CMD-SHELL", "wget --quiet --tries=1 --spider http://127.0.0.1:8080/health || exit 1"]
  interval: 30s
  timeout: 5s
  retries: 3
```

**Medida Preventiva:**
- Documentar qué herramientas necesita el healthcheck
- Preferir `curl` (más portable) o comandos nativos del runtime
- Exponer endpoint `/health` en la aplicación
- Validar localmente que el healthcheck funciona antes de deployar

---

### ERROR #4: Dependencias Incorrectas (`depends_on` sin `service_healthy`)

**Síntomas:**
- App intenta conectar a DB antes de que DB esté lista
- Logs: "FATAL: remaining connection slots are reserved" o "connection refused"
- Restart loop: app cae, reinicia, intenta conectar antes de DB, cae nuevamente

**Causa Raíz:**
- `depends_on: [db]` solo espera que el contenedor exista, no que esté *listo*
- DB puede estar levantando mientras app ya intenta conectar
- Sin `condition: service_healthy`, no hay sincronización real

**Diagnóstico Rápido:**
```bash
# Revisar logs de la app y DB simultáneamente
docker logs <app_container> --follow
docker logs <db_container> --follow

# Verificar si DB tiene healthcheck
docker inspect <db_container> | grep -A 10 "Health"

# Ver si app reinicia constantemente
docker ps --no-trunc | grep <app_container>
```

**Corrección Inmediata:**
```yaml
# ❌ INCORRECTO - Solo ordena contenedores
services:
  app:
    depends_on:
      - db
  db:
    image: postgres:16-alpine

# ✅ CORRECTO - Espera a que DB sea healthy
services:
  app:
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

**Medida Preventiva:**
- SIEMPRE usar `condition: service_healthy` en dependencias críticas
- SIEMPRE incluir healthcheck en servicios con estado (DB, Redis, etc.)
- Implementar reintentos en la app (ej: exponential backoff al conectar a DB)
- Documentar orden de arranque esperado

---

### ERROR #5: Volúmenes Ausentes o Persistencia Incorrecta

**Síntomas:**
- Datos de DB desaparecen tras redeploy
- Archivos subidos se pierden
- "volume not found" en logs de Coolify

**Causa Raíz:**
- Bind mounts a rutas locales que no existen en producción
- Sin `volumes:` definidos en compose → contenedor stateful sin persistencia
- Usar `volumes:` con nombres cortos sin definir en sección `volumes:`

**Diagnóstico Rápido:**
```bash
# Listar volúmenes del stack
docker volume ls | grep <stack_name>

# Inspeccionar volumen específico
docker volume inspect <stack_name>_db_data

# Ver qué volúmenes usa un contenedor
docker inspect <db_container> | grep -A 20 "Mounts"
```

**Corrección Inmediata:**
```yaml
# ❌ INCORRECTO - Bind mount frágil
services:
  db:
    image: postgres:16-alpine
    volumes:
      - /home/user/data:/var/lib/postgresql/data  # Ruta local específica

# ✅ CORRECTO - Volumen nombrado
services:
  db:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:  # Definido explícitamente
```

**Patrón completo:**
```yaml
version: "3.8"
services:
  db:
    image: postgres:16-alpine
    restart: unless-stopped
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  app:
    image: myapp:1.0.0
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - app_uploads:/app/uploads  # Si la app sube archivos
    environment:
      DATABASE_URL: postgres://postgres:${DB_PASSWORD}@db:5432/mydb

volumes:
  postgres_data:
  app_uploads:
```

**Medida Preventiva:**
- NUNCA usar bind mounts a rutas locales en producción
- Usar volúmenes nombrados por servicio
- Documentar qué rutas internas necesitan persistencia
- Hacer backup del volumen antes de grandes cambios
- Verificar post-deploy que datos persisten tras `docker-compose down && up`

---

### ERROR #6: Variables de Entorno Faltantes o Secretos Hardcodeados

**Síntomas:**
- "undefined environment variable" en logs
- Servicio no inicia
- Credenciales visibles en Git o logs públicos

**Causa Raíz:**
- Variables `${VAR}` en compose pero no definidas en Coolify
- Secretos hardcodeados en compose/Dockerfile en lugar de variables
- `.env` local nunca fue transferido a Coolify

**Diagnóstico Rápido:**
```bash
# Ver variables del contenedor
docker inspect <container_name> | grep -A 20 "Env"

# Revisar si variable fue resuelto
docker exec <container_name> env | grep DATABASE_URL

# Buscar hardcodes sospechosos en compose
grep -i "password\|secret\|api_key\|token" docker-compose.yml
```

**Corrección Inmediata:**
```yaml
# ❌ INCORRECTO
services:
  app:
    environment:
      - DATABASE_URL=postgres://user:password123@db:5432/mydb
      - API_KEY=sk-123456789

# ✅ CORRECTO
services:
  app:
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - API_KEY=${API_KEY}
      - NODE_ENV=${NODE_ENV:-production}
```

**Crear `.env.example` en Git (SIN valores reales):**
```bash
# .env.example
DATABASE_URL=postgres://user:${DB_PASSWORD}@db:5432/mydb
API_KEY=
NODE_ENV=production
DB_PASSWORD=
REDIS_URL=redis://redis:6379
```

**En Coolify:**
- Copiar `.env.example`
- Renombrar a `.env`
- Llenar valores reales
- NO subir a Git

**Medida Preventiva:**
- Checklist: "¿Ningún valor secreto en compose visible?"
- Usar `${VAR}` para TODAS las credenciales y configs sensibles
- Documentar variables obligatorias vs opcionales
- En CI/CD, inyectar variables desde secretos, no desde archivos

---

### ERROR #7: Orden de Arranque - Migraciones y Seeds Fallidos

**Síntomas:**
- App inicia pero DB no tiene schema
- "relation does not exist" en logs
- Datos de seed faltantes

**Causa Raíz:**
- App intenta usar DB antes de que migraciones ejecuten
- Migraciones no se ejecutan automáticamente
- Workers inician antes de que DB sea accesible

**Diagnóstico Rápido:**
```bash
# Revisar logs de app y db
docker logs <app_container>
docker logs <db_container>

# Conectar a DB y verificar schema
docker exec <db_container> psql -U postgres -d mydb -c "\dt"
```

**Corrección Inmediata:**

**Opción A: Migraciones en entrypoint (recomendado)**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Script wrapper que ejecuta migraciones
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["npm", "start"]
```

```bash
# docker-entrypoint.sh
#!/bin/sh
set -e

echo "Esperando DB..."
until nc -z db 5432; do
  sleep 1
done

echo "Ejecutando migraciones..."
npm run migrate

echo "Iniciando app..."
exec npm start
```

**Opción B: Job de migración separado**
```yaml
services:
  db:
    image: postgres:16-alpine
    # ... config ...

  migrate:
    image: myapp:1.0.0
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DATABASE_URL=${DATABASE_URL}
    command: npm run migrate
    restart: "no"  # Se ejecuta una sola vez

  app:
    image: myapp:1.0.0
    depends_on:
      - migrate  # Espera a que migrate termine
    # ... config ...
```

**Opción C: Init container pattern**
```yaml
services:
  app:
    image: myapp:1.0.0
    init_containers:
      - name: migrate
        image: myapp:1.0.0
        command: npm run migrate
        environment:
          - DATABASE_URL=${DATABASE_URL}
```

**Medida Preventiva:**
- Ejecutar migraciones como paso previo a app start
- Documentar orden de inicialización
- Usar healthchecks para sincronización
- Testear localmente: `docker-compose down && docker-compose up` debería "funcionar de cero"

---

### ERROR #8: Problemas de Build Remoto - Contexto Incorrecto

**Síntomas:**
- "COPY failed: file not found" en Coolify build
- "build context not found"
- Funciona localmente pero falla en Coolify

**Causa Raíz:**
- Dockerfile usa rutas relativas que no existen en contexto de build
- `.dockerignore` incluye archivos necesarios por error
- Contexto de build incorrecto en Coolify

**Diagnóstico Rápido:**
```bash
# Simular build de Coolify localmente
docker build -t test:latest .

# Ver qué está en el contexto
docker build --progress=plain -t test:latest . 2>&1 | head -20

# Revisar .dockerignore
cat .dockerignore
```

**Corrección Inmediata:**
```dockerfile
# ❌ INCORRECTO - Ruta que no existe
COPY ./src/app /app/src
WORKDIR /app/src

# ✅ CORRECTO - Estructura clara
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --only=production
COPY src ./src
COPY public ./public
CMD ["npm", "start"]
```

**`.dockerignore` completo:**
```
.git
.gitignore
node_modules
npm-debug.log
.env
.env.local
.DS_Store
dist
build
.next
.nuxt
coverage
```

**Medida Preventiva:**
- Testear `docker build` antes de pushear
- Revisar que `COPY` coincida con estructura real
- Documentar estructura esperada del proyecto
- En Coolify, verificar que contexto es raíz del repo

---

### ERROR #9: Red Bridge Incorrecta - Servicios no se comunican

**Síntomas:**
- "connection refused" entre contenedores
- Services cannot reach each other
- Cada servicio aislado en su red

**Causa Raíz:**
- Servicios sin `networks:` definido
- Cada servicio en red diferente
- Sin definición explícita de red bridge

**Diagnóstico Rápido:**
```bash
# Ver redes del stack
docker network ls | grep <stack_name>

# Inspeccionar contenedores conectados a red
docker network inspect <stack_name>_default | grep -A 20 "Containers"

# Probar conectividad entre contenedores
docker exec <app_container> ping db
```

**Corrección Inmediata:**
```yaml
version: "3.8"

services:
  app:
    image: node:18-alpine
    networks:
      - backend
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    networks:
      - backend

networks:
  backend:
    driver: bridge
```

**Medida Preventiva:**
- Siempre definir `networks:` explícitamente
- Usar nombre simple para la red principal (ej. `backend`)
- Si hay servicios que no deberían comunicarse, usar redes separadas

---

### ERROR #10: Reinicio Infinito - Crash Loop Backoff

**Síntomas:**
- Contenedor inicia, cae casi inmediatamente, reinicia
- `Restarting (1) 5 seconds ago` en `docker ps`
- Patrón repetitivo en logs

**Causa Raíz:**
- App no puede iniciar (error en código, dependencia faltante)
- Puerto ya está en uso
- Credenciales incorrectas causando crash

**Diagnóstico Rápido:**
```bash
# Ver historial de reinicio
docker ps -a | grep <container_name>

# Leer logs completos (incluyendo antes del crash)
docker logs <container_name> --tail 50

# Ver límite de reintentos
docker inspect <container_name> | grep -A 5 "RestartPolicy"
```

**Corrección Inmediata:**
1. Revisar logs más recientes
2. Verificar que todas las dependencias existen
3. Probar app localmente con mismo environment
4. Ejecutar healthcheck manualmente para ver error exacto

**Ejemplo fix común:**
```yaml
# Si app requiere variable, documentar como obligatoria
services:
  app:
    environment:
      - DATABASE_URL=${DATABASE_URL}  # OBLIGATORIA
      - NODE_ENV=production
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s  # Dar más tiempo antes de primeros healthchecks
```

**Medida Preventiva:**
- Siempre tener `start_period` en healthcheck (mínimo 5s)
- Logs informativos en inicio de app
- Testear con variables reales antes de deployar

---

### ERROR #11: Límites de Recursos - OOM (Out of Memory)

**Síntomas:**
- Proceso "Killed" sin razón aparente
- Otros servicios empiezan a fallar
- VPS se vuelve lento o inresponsivo

**Causa Raíz:**
- Contenedor consume toda la RAM disponible
- Sin límites de memoria definidos
- Memory leak en aplicación

**Diagnóstico Rápido:**
```bash
# Ver uso de memoria en tiempo real
docker stats <container_name>

# Ver límites configurados
docker inspect <container_name> | grep -A 10 "MemoryLimit"

# Revisar si fue killed por OOM
docker inspect <container_name> | grep "OOMKilled"
```

**Corrección Inmediata:**
```yaml
services:
  app:
    image: node:18-alpine
    deploy:
      resources:
        limits:
          memory: 512M  # Máximo que puede usar
        reservations:
          memory: 256M  # Memory garantizada
  
  db:
    image: postgres:16-alpine
    deploy:
      resources:
        limits:
          memory: 1G
        reservations:
          memory: 512M
```

**Medida Preventiva:**
- En VPS con 2GB RAM: limits conservadores (512M-1G máximo por servicio)
- Monitorear con `docker stats` regularmente
- Detectar memory leaks en development
- Usar Alpine/lean images

---

### ERROR #12: Certificados/TLS - HTTPS Fallando

**Síntomas:**
- "certificate not trusted" en navegador
- HTTPS no funciona pero HTTP sí
- Traefik no obtiene certificado

**Causa Raíz:**
- Dominio no apunta correctamente a VPS
- Traefik no puede validar dominio
- Certificado expirado
- En local con self-signed, no en producción

**Diagnóstico Rápido:**
```bash
# Verificar que dominio apunta a VPS
nslookup tu-dominio.com

# Revisar certificados en Traefik
docker exec traefik traefik info | grep certs

# Ver logs de certificado
docker logs traefik | grep -i "certificate\|tls\|acme"
```

**Corrección Inmediata:**
```yaml
# En producción con Traefik/Coolify, Coolify maneja certs automáticamente
# En local, acceptar self-signed es normal
services:
  web:
    labels:
      # Coolify/Traefik enrutará HTTP → HTTPS automáticamente
      - "traefik.http.routers.web.rule=Host(`tu-dominio.com`)"
      - "traefik.http.routers.web.entrypoints=web,websecure"
      - "traefik.http.services.web.loadbalancer.server.port=8080"
```

**Medida Preventiva:**
- En Coolify: dejar que gestione certificados (Let's Encrypt automático)
- Verificar que DNS propaga correctamente (esperar hasta 24h)
- No usar http en producción (solo https)

---

### ERROR #13: Logs Ausentes o Ilegibles

**Síntomas:**
- No hay información de qué falló
- Logs vacíos o sin timestamp
- Difícil debuggear problemas

**Causa Raíz:**
- App escribe a archivos en lugar de stdout
- Buffering de salida
- Logging mal configurado

**Diagnóstico Rápido:**
```bash
# Ver logs docker
docker logs <container_name>

# Ver logs en tiempo real
docker logs <container_name> -f

# Revisar si hay logs internos
docker exec <container_name> cat /app/logs/*.log
```

**Corrección Inmediata:**
```dockerfile
# Asegurar que logs van a stdout (Docker los captura)
ENV NODE_ENV=production
# Node: Express por defecto usa console.log que va a stdout ✅
# Python: usar logging.basicConfig(level=logging.INFO) ✅

# Si app escribe a archivo, redirigir:
RUN ln -sf /dev/stdout /app/logs/app.log
```

```yaml
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

**Medida Preventiva:**
- Todos los logs a stdout/stderr
- Incluir timestamps y niveles (INFO, ERROR, DEBUG)
- En Coolify, los logs se capturan automáticamente

---

### ERROR #14: Permisos de Archivo - UID/GID Mismatch

**Síntomas:**
- "Permission denied" en volúmenes
- Bind mounts inaccesibles
- App no puede escribir en directorio

**Causa Raíz:**
- UID del contenedor diferente al del host
- Archivo creado como root en contenedor
- Permisos demasiado restrictivos

**Diagnóstico Rápido:**
```bash
# Ver usuario del contenedor
docker inspect <container_name> | grep -i "user"

# Ver permisos en volumen
docker exec <container_name> ls -la /app
```

**Corrección Inmediata:**
```dockerfile
# Crear usuario no-root con ID explícito
FROM node:18-alpine
RUN addgroup -g 1000 app && adduser -D -u 1000 -G app app
WORKDIR /app
COPY --chown=app:app . .
USER app
CMD ["npm", "start"]
```

```yaml
services:
  app:
    image: myapp:1.0.0
    user: "1000:1000"  # UID:GID
    volumes:
      - app_data:/app/data
```

**Medida Preventiva:**
- Usar `user: non-root` en todas las imágenes
- Si bind mount necesario, asegurar permisos en host
- Preferir volúmenes nombrados (sin permisos del host)

---

### ERROR #15: Versionado de Imagen - "Rolling Tag" Problem

**Síntomas:**
- No se sabe qué versión está desplegada
- Redeploy tira la misma imagen (no hay cambios)
- Imposible rollback

**Causa Raíz:**
- Usar `:latest` o `:main` (tags flotantes)
- Imágenes sin versión inmutable
- No hay trazabilidad de qué fue desplegado

**Diagnóstico Rápido:**
```bash
# Ver qué digest tiene imagen actualmente
docker inspect <image>:<tag> | grep RepoDigests

# Comparar con build anterior
docker images | grep <image>
```

**Corrección Inmediata:**
```yaml
# ❌ INCORRECTO
services:
  app:
    image: myapp:latest  # Flotante, puede cambiar

# ✅ CORRECTO - Usar SemVer o SHA
services:
  app:
    image: myapp:1.2.3  # O myapp:abc123def456
```

**En CI/CD:**
```yaml
# Construir con versión de Git tag
- name: Build image
  run: |
    VERSION=$(git describe --tags)
    docker build -t myapp:$VERSION .
    docker push myapp:$VERSION
    
    # También pushear latest para referencias
    docker tag myapp:$VERSION myapp:latest
    docker push myapp:latest
```

**En docker-compose:**
```yaml
services:
  app:
    image: myapp:v1.2.3  # Imagen inmutable
    environment:
      - VERSION=v1.2.3  # Documentar versión en env
```

**Medida Preventiva:**
- NUNCA usar `:latest` en producción
- Usar SemVer o commit SHA para versionado
- Documentar versión desplegada en metadata o env var
- Usar Git tags para releases

---

## Matriz de Referencia Rápida

| Error | Síntoma | Causa | Fix Rápido |
|-------|---------|-------|-----------|
| Puertos | Inaccesible | `ports:` en web | Cambiar a `expose:` |
| Localhost | Traefik conn refused | `127.0.0.1` en app | `--host 0.0.0.0` |
| Healthcheck | Unhealthy/restarting | Herramienta ausente | Usar cmd nativo o instalar |
| Dependencias | App cae | No espera DB ready | Agregar `condition: service_healthy` |
| Volúmenes | Datos pierden | Sin volumes | Agregar volumen nombrado + sección `volumes:` |
| Variables | Undefined | Falta en Coolify | Copiar .env.example, llenar valores |
| Migraciones | Schema missing | No ejecutan auto | Entrypoint que ejecuta `migrate` |
| Build | COPY failed | Contexto incorrecto | Verificar `.dockerignore` y rutas |
| Red | Services no conectan | Sin `networks:` | Definir network bridge explícita |
| Restart | Crash loop | App no inicia | Revisar logs, verificar deps |
| RAM | Killed/OOM | Sin limits | Agregar `deploy.resources.limits.memory` |
| TLS | Cert error | DNS/Traefik issue | Verificar DNS, dejar Coolify manejar |
| Logs | No info | App escribe a archivo | Redirigir a stdout |
| Permisos | Perm denied | UID mismatch | Usar `user: non-root` |
| Versión | No trazabilidad | `:latest` tag | Usar SemVer inmutable |

---

## Cómo Usar Este Skill

Cuando encuentres un error en Coolify:

1. **Identifica el síntoma** en la tabla o en el catálogo
2. **Lee la "Causa Raíz"** para confirmar
3. **Ejecuta "Diagnóstico Rápido"** para verificar
4. **Aplica "Corrección Inmediata"**
5. **Implementa "Medida Preventiva"** para no repetir

---

## Integración con Otros Skills

- Después de resolver un error, usa `validate-coolify-compose` para asegurar que no hay otros
- Si necesitas diseñar desde cero, usa `coolify-architect-guidance`
- Antes de desplegar, usa `coolify-deploy-checklist`

```
