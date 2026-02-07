---
name: validate-coolify-rules
description: Valida que el código y configuraciones cumplan con las reglas obligatorias de Coolify (prohibiciones de ports, network_mode, credenciales hardcodeadas, etc.).
license: MIT
---

# Skill: Validación de Reglas Coolify

## Propósito

Garantizar que cualquier artefacto (docker-compose, configuración, código) cumpla con las **prohibiciones absolutas** y **requisitos obligatorios** del entorno Coolify de producción (Contabo + Cloudflare).

---

## Reglas Obligatorias a Validar

### 🚫 PROHIBICIONES ABSOLUTAS (VÍA NEGATIVA)

Cuando revises código o configuración, **rechaza explícitamente** cualquiera de estos patrones:

1. **Mapeo de puertos en servicios web**
   - ❌ `ports: "80:80"`, `ports: "443:443"`, `ports: "8080:8080"`
   - ❌ `ports: ["80:80", "443:443"]`
   - ✅ Usar solo `expose:` en servicios web

2. **Exposición de puertos internos al exterior**
   - ❌ Bases de datos con `ports: "5432:5432"` (PostgreSQL, MySQL, Redis, MongoDB, etc.)
   - ❌ Servicios internos con puertos públicos
   - ✅ Comunicación interna por nombre de servicio (ej. `postgres:5432`)

3. **Network mode host**
   - ❌ `network_mode: host`
   - ✅ Usar redes Docker estándar (`networks:`)

4. **Credenciales hardcodeadas**
   - ❌ `POSTGRES_PASSWORD: "mi_password_123"`
   - ❌ `API_KEY: "secret-key-xyz"`
   - ❌ URLs con contraseña: `postgres://user:pass@host`
   - ✅ Usar variables `${VARIABLE}` referenciadas en `.env`

5. **Imágenes sin versión fija**
   - ❌ `image: postgres:latest`
   - ❌ `image: node:latest`
   - ✅ `image: postgres:16-alpine`, `image: node:18.20.1-alpine3.18`

6. **Falta de restart policy**
   - ❌ Omitir `restart:` en servicios de producción
   - ✅ `restart: unless-stopped`

---

### ✅ REQUISITOS OBLIGATORIOS (VÍA POSITIVA)

1. **Apps escuchan en 0.0.0.0**
   - ✅ La aplicación debe escuchar en `0.0.0.0` (no solo `localhost` o `127.0.0.1`)
   - ✅ Documentar el puerto interno

2. **Persistencia de datos**
   - ✅ Servicios de BD deben tener `volumes:` definidos
   - ✅ Rutas explícitas: `/var/lib/postgresql`, `/data`, `/etc/config`, etc.

3. **Healthchecks en servicios críticos**
   - ✅ BD (PostgreSQL, MySQL, MongoDB, Redis)
   - ✅ APIs y servicios web
   - ✅ Formato: `healthcheck:` con `test`, `interval`, `timeout`, `retries`

4. **Dependencias correctamente declaradas**
   - ✅ `depends_on:` listando servicios dependientes
   - ✅ Si es crítico: `condition: service_healthy`

5. **Preferir imágenes alpine**
   - ✅ `postgres:16-alpine` en lugar de `postgres:16`
   - ✅ `node:18-alpine` en lugar de `node:18`

6. **User no-root cuando sea posible**
   - ✅ `user: non-root`, `user: node`, `user: postgres` (según la imagen)
   - ⚠️ Si no es soportado por la imagen, documentar por qué

7. **Límites de recursos en VPS con poco RAM**
   - ✅ Servicios pesados deben tener `deploy.resources.limits.memory`
   - ✅ Evitar que un servicio consuma toda la RAM y mate otros

---

## Proceso de Validación

Cuando se te pida validar un artefacto Coolify, sigue estos pasos:

### Paso 1: Análisis Inicial
- Identifica el tipo de artefacto (docker-compose.yml, Dockerfile, script, código, etc.)
- Extrae la sección relevante (servicios, variables, puerto)

### Paso 2: Validar Prohibiciones
Para cada prohibición, busca patrones:
- **ports:** en servicios → Rechaza a menos que se justifique explícitamente
- **network_mode: host** → Rechaza
- **Credenciales hardcodeadas** → Busca `PASSWORD`, `API_KEY`, `SECRET`, URLs con auth
- **latest tag** → Busca `:latest` o sin versión
- **restart ausente** → Busca línea `restart:`

### Paso 3: Validar Requisitos
- **expose:** está presente en servicios web
- **volumes:** está presente en servicios stateful
- **healthcheck:** está presente en servicios críticos
- **user:** está presente o documentado
- **0.0.0.0:** verifica que la app no escuche solo en localhost

### Paso 4: Emitir Reporte
**Formato de salida obligatorio:**

```
## ✅ VALIDACIÓN COOLIFY: [ARCHIVO O SECCIÓN]

### 🔴 ERRORES CRÍTICOS (Bloquean despliegue)
- [ ] Error 1: Descripción
- [ ] Error 2: Descripción

### 🟡 ADVERTENCIAS (Revisar antes de producción)
- [ ] Advertencia 1: Descripción
- [ ] Advertencia 2: Descripción

### 🟢 APROBADOS
- ✅ Reinicio policy correcta
- ✅ Imágenes con versiones fijas
- ✅ Variables externalizadas

### 📝 RECOMENDACIONES
- Acción 1
- Acción 2

### ⚡ RESUMEN FINAL
**ESTADO:** [APROBADO | REQUIERE CAMBIOS | BLOQUEADO]
**Línea de acción:** [Próximos pasos]
```

---

## Ejemplos de Validación

### Ejemplo 1: ❌ RECHAZAR
```yaml
services:
  postgres:
    image: postgres:latest
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: "mi_pass_123"
```
**Problemas:**
- ❌ `ports: "5432:5432"` → Expone DB al exterior
- ❌ `latest` tag → Sin versión fija
- ❌ Credencial hardcodeada → `POSTGRES_PASSWORD`

### Ejemplo 2: ✅ APROBAR
```yaml
services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    expose:
      - "5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 3
```
**Aprobado:**
- ✅ Versión fija `16-alpine`
- ✅ `expose:` en lugar de `ports:`
- ✅ Variable `${DB_PASSWORD}`
- ✅ Volumen persistente
- ✅ Healthcheck

---

## Regla de Oro

> **Si la configuración cumple TODAS las prohibiciones negativas y TODOS los requisitos positivos, está lista para Coolify.**

---

## Notas Operativas

- **Modo LOCAL vs PRODUCCIÓN:** Este skill valida reglas que aplican en **producción**. Modo local puede ser más permisivo (ej. `ports:` para debugging), pero debe estar explícitamente marcado como LOCAL.
- **Excepciones documentadas:** Si hay un caso excepcional (ej. servicio SMTP que realmente necesita un puerto), docméntalo con `# ⚠️ Puerto expuesto intencionalmente — revisar con arquitecto`.
- **Reevaluar ante cambios:** Si el proyecto cambia de infraestructura (ej. de Coolify a Kubernetes), estas reglas pueden cambiar.
