---
name: coolify-puerto-80-ocupado
description: Diagnóstico y corrección de despliegue fallido en Coolify/VPS por conflicto de puerto 80. Usa esta skill cuando el despliegue construye, crea el contenedor principal, pero falla al iniciar un proxy interno (caddy, nginx, traefik) con error "Bind for 0.0.0.0:80 failed: port is already allocated" o "driver failed programming external connectivity". No es un problema de Astro, ni de código frontend, ni de textos — es un conflicto de puertos en el host. Activa especialmente si el usuario menciona despliegue fallido, puerto ocupado, o está perdiendo tiempo revisando código que no tiene error.
---

# Skill: Despliegue fallido en Coolify — Puerto 80 ocupado

Diagnostica y corrige el despliegue que falla en Coolify/VPS cuando el proxy interno del proyecto intenta publicar el puerto 80 del host, pero ya está ocupado.

## Cuándo activar esta skill

Esta skill debe activar cuando reconozcas estas señales:

**Errores en logs:**
- `Bind for 0.0.0.0:80 failed: port is already allocated`
- `Error response from daemon: driver failed programming external connectivity`

**Contexto del fallo:**
- El build sí avanzó
- El contenedor `web` sí fue creado e iniciado
- El fallo ocurrió al arrancar un contenedor proxy (`caddy`, `nginx`, `traefik`)

**Patrón de diagnóstico errado:**
- El usuario está revisando Astro, componentes Vue, textos, o código frontend
- Pero la aplicación está técnicamente correcta
- El problema real es de infraestructura, no de código

## Síntoma observado

```
✓ Build del proyecto avanzó
✓ Contenedor web creado e iniciado
✗ Fallo al iniciar contenedor proxy (caddy/nginx/traefik)
   → Bind for 0.0.0.0:80 failed: port is already allocated
```

## Causa raíz

La causa **no** es Astro, ni Vue, ni textos, ni el contenido de las páginas.

La causa real es un **conflicto de puertos en el host**:
- El servicio `caddy` del proyecto intenta publicar `80:80`
- El **puerto 80 del VPS ya está en uso** por otro servicio o contenedor
- Docker no puede enlazar ese puerto → fallo en despliegue

### Por qué puede pasar

1. **Ya existe otro proxy en el VPS**
   - Otro Caddy, Nginx, Apache, Traefik, o el proxy global de Coolify

2. **Quedó un contenedor viejo ocupando el puerto 80**
   - Un despliegue anterior dejó un contenedor activo con `80:80`

3. **El proyecto está duplicando el rol de proxy**
   - Si Coolify ya enruta el dominio, agregar un `caddy` interno genera conflicto

## Diagnóstico rápido

Ejecutar en el VPS:

```bash
# Ver qué proceso escucha en puerto 80
sudo ss -ltnp | grep ':80'

# Ver todos los contenedores con puertos publicados
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}"

# Ver específicamente qué contenedor publica el 80
docker ps --filter publish=80
```

## Revisión del proyecto

Revisar `docker-compose.vps.yml` — buscar algo como:

```yaml
services:
  caddy:
    ports:
      - "80:80"    # ← esto causa el conflicto
      - "443:443"
```

## Soluciones según el escenario

### Opción A: Eliminar el proxy interno (recomendado)

Cuando Coolify ya actúa como proxy y enruta al contenedor `web`.

```yaml
services:
  web:
    build:
      context: ./web
      dockerfile: Dockerfile
    image: da-tica_portal_web:1.0.0
    restart: unless-stopped
    expose:
      - "8080"
    # caddy eliminado — Coolify maneja la exposición
```

### Opción B: Cambiar temporalmente el puerto

Solo para pruebas o cuando sí se necesita el proxy interno.

```yaml
ports:
  - "8081:80"
```

### Opción C: Detener el contenedor viejo

Solo si se confirma que el contenedor anterior ya no debe seguir activo.

```bash
docker ps --filter publish=80
docker stop NOMBRE_O_ID
docker rm NOMBRE_O_ID
```

## Comando rápido de diagnóstico

```bash
sudo ss -ltnp | grep ':80' && docker ps --filter publish=80
```

## Resultado esperado tras la corrección

- Contenedor `web` queda `Up`
- Despliegue no falla por `port is already allocated`
- Acceso por dominio controlado por el componente correcto

## Lección aprendida

La falla ocurrió por una **colisión del puerto 80 en el VPS**.
El problema fue de **infraestructura de despliegue**, no de código fuente.

Cuando Coolify ya administra la exposición o proxy, agregar otro servicio que publique `80:80` dentro del proyecto puede romper el despliegue aunque la aplicación esté técnicamente correcta.

## Prevención

1. **No duplicar proxies** — si Coolify publica el dominio, no agregar otro `caddy` o `nginx` en `80:80`
2. **Revisar puertos antes de desplegar** — ejecutar `sudo ss -ltnp | grep ':80'` antes del despliegue
3. **Documentar la arquitectura** — dejar claro si Coolify o el proyecto manejan el proxy
4. **Leer el log exacto** — un error de infraestructura puede parecer error de aplicación
