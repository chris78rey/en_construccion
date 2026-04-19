# Da-TIca - Despliegue en VPS Propio

Guía para desplegar el sitio en un VPS propio usando Docker Compose + Caddy.

## Prerrequisitos

- VPS con Ubuntu/Debian
- Docker y Docker Compose instalados
- Dominio apuntando al VPS (registros A)
- Puertos 80 y 443 abiertos

## Estructura de Archivos

```
├── web/                    # Contenido estático del sitio
│   ├── index.html
│   ├── styles.css
│   ├── sitios-web.html
│   ├── data-mining.html
│   ├── cursos.html
│   └── Dockerfile          # Build de imagen nginx
├── deploy/
│   └── Caddyfile           # Configuración del proxy HTTPS
├── scripts/
│   ├── first_deploy.sh     # Script para primer despliegue
│   └── update_deploy.sh    # Script para actualizaciones
├── docker-compose.vps.yml  # Compose para VPS propio
├── .env.vps.example        # Variables de entorno ejemplo
└── .dockerignore           # Archivos excluidos del build
```

## Pasos de Instalación

### 1. Preparar el VPS

```bash
# Instalar Docker
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker

# Abrir firewall
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 443/udp
sudo ufw enable
```

### 2. Verificar que los puertos no estén ocupados

```bash
sudo ss -tulpn | grep -E ':80|:443'
```

Si hay nginx o apache2, detenerlos:

```bash
sudo systemctl stop nginx apache2
sudo systemctl disable nginx apache2
```

### 3. Subir los archivos al VPS

```bash
# Desde tu máquina local
scp -r . user@tu-vps:/opt/datica/
```

### 4. Configurar variables de entorno

```bash
cd /opt/datica
cp .env.vps.example .env
nano .env  # Editar DOMAIN y LETSENCRYPT_EMAIL
```

### 5. Primer despliegue

```bash
cd /opt/datica
bash scripts/first_deploy.sh
```

### 6. Verificar funcionamiento

```bash
# Ver estado de contenedores
docker compose -f docker-compose.vps.yml ps

# Ver logs
docker compose -f docker-compose.vps.yml logs -f

# Probar desde el navegador
# https://tu-dominio.com
```

## Actualizaciones

Cuando modifiques el código del sitio:

```bash
cd /opt/datica
bash scripts/update_deploy.sh
```

## Comandos Útiles

```bash
# Ver estado
docker compose -f docker-compose.vps.yml ps

# Ver logs en vivo
docker compose -f docker-compose.vps.yml logs -f

# Reiniciar servicios
docker compose -f docker-compose.vps.yml restart

# Detener todo
docker compose -f docker-compose.vps.yml down

# Ver contenedores en ejecución
docker ps

# Limpiar volúmenes (⚠️ borra certificados)
docker compose -f docker-compose.vps.yml down -v
```

## DNS Requerido

En tu proveedor de dominio, crear:

| Tipo | Nombre | Valor |
|------|--------|-------|
| A | da-tica.com | IP_DEL_VPS |
| A | www.da-tica.com | IP_DEL_VPS |

## Solución de Problemas

### Caddy no obtiene certificado

1. Verificar que el dominio apunta correctamente:
   ```bash
   dig da-tica.com
   ```

2. Verificar que los puertos están abiertos:
   ```bash
   curl -I http://tu-vps-ip
   ```

3. Revisar logs de Caddy:
   ```bash
   docker compose -f docker-compose.vps.yml logs caddy
   ```

### Error 502 Bad Gateway

1. Verificar que el contenedor web está corriendo:
   ```bash
   docker compose -f docker-compose.vps.yml ps
   ```

2. Verificar que nginx responde:
   ```bash
   docker exec datica-web wget -qO- http://localhost:8080/
   ```

### Contenedor no inicia

```bash
# Ver logs detallados
docker compose -f docker-compose.vps.yml logs web

# Rebuild sin caché
docker compose -f docker-compose.vps.yml build --no-cache web
docker compose -f docker-compose.vps.yml up -d
```