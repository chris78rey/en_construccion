# Da-TIca - Despliegue en Coolify

## Configuración en Coolify

### Dominios

En **Configuration → General → Domains for web**, configurar:

```
https://portal.da-tica.com:8080,https://www.portal.da-tica.com:8080
```

⚠️ **Importante:** El puerto `:8080` es obligatorio porque el contenedor escucha internamente en ese puerto. La variable `DOMAIN` en el compose **NO controla** el proxy de Coolify.

### Variables de Entorno

Para este sitio estático, **no son necesarias**. Se pueden eliminar:

- `CLIENT_ID`
- `DOMAIN`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`

El campo **Domains** en Coolify es el que controla el routing.

## docker-compose.yml

```yaml
services:
  web:
    build:
      context: ./web
      dockerfile: Dockerfile
    image: da-tica_portal_web:1.0.0
    restart: unless-stopped
    expose:
      - '8080'
    healthcheck:
      test:
        - CMD
        - wget
        - '-qO-'
        - 'http://127.0.0.1:8080/'
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 20s
```

## Estructura del Proyecto

```
web/
├── index.html
├── sitios-web.html
├── data-mining.html
├── cursos.html
├── styles.css
├── Dockerfile          # Build nginx :8080
├── robots.txt
└── img/                # Imágenes (vacío si no se usa)
```

## Solución de Problemas

### "No Available Server (503)"

1. Verificar que el contenedor esté **Running (healthy)**
2. Configurar dominio en **Domains for web** con `:8080`
3. Verificar DNS:
   ```bash
   nslookup portal.da-tica.com
   ```

### Contenedor no levanta

```bash
# Ver logs del contenedor en Coolify
docker logs <container_name>

# Test interno
docker exec <container_name> wget -qO- http://127.0.0.1:8080/
```

## Flujo de Despliegue

1. Crear aplicación en Coolify
2. Vincular repositorio GitHub (rama DESARROLLO)
3. Configurar **Build Pack** → Docker Compose
4. En **Domains for web**: `https://portal.da-tica.com:8080`
5. Deploy
6. Verificar: `https://portal.da-tica.com`

## DNS Requerido

| Tipo | Host | Valor |
|------|------|-------|
| A | portal.da-tica.com | IP_DEL_VPS |
| A | www.portal.da-tica.com | IP_DEL_VPS |