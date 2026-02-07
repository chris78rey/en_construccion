---
name: coolify-deploy-checklist
description: Valida un docker-compose antes de desplegar en Coolify verificando puertos, credenciales, healthchecks, volúmenes y reglas de seguridad obligatorias.
license: MIT
---

# Checklist de Despliegue Coolify

## Descripción
Este skill te ayuda a validar que tu `docker-compose.yml` cumple **todas las reglas obligatorias** antes de desplegarlo en Coolify. Previene errores comunes que causan fallos en producción.

## Reglas Obligatorias a Verificar

### 🚫 Prohibiciones Críticas (VÍA NEGATIVA)

1. **SIN puertos del host en servicios web**
   - ❌ `ports: "80:80"` en servicios HTTP/HTTPS
   - ❌ `ports: "8080:8080"` en APIs
   - ✅ Usar `expose:` en su lugar

2. **SIN puertos expuestos para bases de datos**
   - ❌ `ports: "5432:5432"` (PostgreSQL)
   - ❌ `ports: "3306:3306"` (MySQL)
   - ❌ `ports: "6379:6379"` (Redis)
   - ✅ Comunicación solo por nombre de servicio interno

3. **SIN network_mode: host**
   - ❌ `network_mode: host` causa conflictos con Traefik
   - ✅ Usar redes de Docker estándar

4. **SIN credenciales hardcodeadas**
   - ❌ `environment: DB_PASSWORD: "mi_password"`
   - ✅ `environment: DB_PASSWORD: ${DB_PASSWORD}`

5. **SIN imágenes con tag latest**
   - ❌ `image: postgres:latest`
   - ✅ `image: postgres:16-alpine`

6. **SIN omisión de restart policy**
   - ❌ Sin `restart:` o `restart: no`
   - ✅ `restart: unless-stopped`

### ✅ Requisitos Obligatorios (VÍA POSITIVA)

1. **Puerto interno documentado**
   - Cada servicio web debe tener `expose:` con su puerto
   - O documentado en comentarios

2. **Apps escuchando en 0.0.0.0**
   - No solo en `localhost` o `127.0.0.1`
   - Verificable en el Dockerfile o comando de inicio

3. **Volúmenes persistentes definidos**
   - Bases de datos: `volumes:` explícitos
   - Uploads/archivos: volúmenes nombrados o bind mounts

4. **Healthchecks en servicios críticos**
   - Base de datos: obligatorio
   - API/app principal: fuertemente recomendado
   - Formato: `healthcheck: test: ["CMD", ...]`

5. **Dependencias correctamente definidas**
   - Usar `depends_on` con `condition: service_healthy`
   - No solo `depends_on: [db]` sin condición

6. **Variables de entorno organizadas**
   - Agrupar por categoría (DB, APP, SECURITY)
   - Documentar qué es obligatorio vs opcional

7. **Preferir alpine en imágenes**
   - `node:18-alpine` en lugar de `node:18`
   - Reduce tamaño y superficie de ataque

8. **User no-root cuando sea posible**
   - `user: node` en Node
   - `user: www-data` en PHP
   - No ejecutar como root en producción

## Proceso de Validación

### Paso 1: Revisar Prohibiciones
Abre tu `docker-compose.yml` y busca:

```bash
# Busca puertos mapeados en servicios web
grep -n "ports:" docker-compose.yml

# Busca credenciales directas (excepto en .env)
grep -n "DB_PASSWORD\|API_KEY\|SECRET" docker-compose.yml

# Busca latest tags
grep -n ":latest" docker-compose.yml

# Busca network_mode: host
grep -n "network_mode: host" docker-compose.yml
```

**Acción:** Si encuentras algo, elimínalo antes de continuar.

### Paso 2: Verificar Requisitos
Para cada servicio en el compose:

- [ ] ¿Tiene `expose:` o documentación del puerto?
- [ ] ¿Tiene `restart: unless-stopped`?
- [ ] ¿Tiene volúmenes persistentes (si almacena datos)?
- [ ] ¿Es un servicio crítico? ¿Tiene healthcheck?
- [ ] ¿Las credenciales usan `${VAR}`?
- [ ] ¿Está en una red Docker (no host)?

### Paso 3: Validar Flujo de Datos
Para cada dependencia:

- [ ] Los servicios que dependen de otros usan `depends_on` con `condition: service_healthy`
- [ ] Las bases de datos NO tienen puertos expuestos
- [ ] Los servicios internos se comunican por nombre (ej. `db:5432`)

### Paso 4: Checklist de Seguridad
- [ ] ¿Ninguna credencial en el compose?
- [ ] ¿Imágenes con versiones fijas?
- [ ] ¿User no-root en aplicaciones críticas?
- [ ] ¿Healthchecks en DB y servicios principales?
- [ ] ¿Volúmenes persistentes para datos importantes?

## Ejemplo de Validación

### ❌ INCORRECTO
```yaml
services:
  app:
    image: node:latest
    ports:
      - "8080:8080"  # ❌ Puerto expuesto
    environment:
      DB_PASSWORD: "secret123"  # ❌ Credencial hardcodeada
    depends_on:
      - db  # ❌ Sin condición
  
  db:
    image: postgres:latest  # ❌ Sin versión
    ports:
      - "5432:5432"  # ❌ DB expuesta
    environment:
      POSTGRES_PASSWORD: "secret"  # ❌ Hardcodeada
```

### ✅ CORRECTO
```yaml
services:
  app:
    image: node:18-alpine
    expose:
      - "8080"  # ✅ Solo expose, no ports
    environment:
      DB_PASSWORD: ${DB_PASSWORD}  # ✅ Variable
      PORT: "8080"
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy  # ✅ Con condición
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:8080/health"]
      interval: 30s
      timeout: 5s
      retries: 3
  
  db:
    image: postgres:16-alpine  # ✅ Versión fija
    expose:
      - "5432"  # ✅ Solo expose
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}  # ✅ Variable
    volumes:
      - db_data:/var/lib/postgresql/data  # ✅ Volumen persistente
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  db_data:
```

## Pasos Finales Antes de Desplegar

1. **Crear `.env` con valores reales**
   - `DB_PASSWORD=...`
   - `API_KEY=...`
   - Nunca subir a Git (agregar a `.gitignore`)

2. **Testear localmente con Traefik**
   - Usar `docker-compose.coolify-local.yml` si existe
   - Verificar que funciona con ese setup

3. **Documentar puertos internos**
   - En Coolify, debes indicar qué puerto expone cada servicio
   - Usa `expose:` en el compose para claridad

4. **Revisar una última vez**
   - ¿Sin puertos públicos? ✅
   - ¿Sin credenciales visibles? ✅
   - ¿Con healthchecks? ✅
   - ¿Con volúmenes persistentes? ✅

5. **Desplegar**
   - Subir a Coolify y monitorear logs
   - Verificar que Traefik enruta correctamente

## Comandos Útiles

```bash
# Validar sintaxis YAML
docker-compose config

# Ver lo que se va a desplegar
docker-compose config | grep -A 20 "services:"

# Buscar violaciones de reglas
docker-compose config | grep -i "ports:"  # Debe estar vacío para webs
docker-compose config | grep -i ":latest"  # Debe estar vacío
```

## Referencia: Las 3 Reglas de Oro de Coolify

1. **Sin puertos expuestos en servicios web** → Usa `expose:` o documentación
2. **Sin credenciales hardcodeadas** → Variables `${VAR}` desde `.env`
3. **Si funciona localmente bajo Traefik, funcionará en Coolify sin sorpresas** → Usa `docker-compose.coolify-local.yml`

---

**Recuerda:** Este checklist previene el 95% de los problemas de despliegue. Si lo cumples, tu app funcionará en Coolify sin ajustes.