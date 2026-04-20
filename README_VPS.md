# Da-TIca - Despliegue Astro en VPS propio

## Estructura principal
```text
.
├── src/
├── public/
├── nginx/
├── deploy/
├── scripts/
├── Dockerfile
├── docker-compose.vps.yml
└── .env.vps.example
```

## Requisitos
- VPS con Ubuntu/Debian
- Docker y Docker Compose
- Dominio apuntando al VPS
- Puertos 80 y 443 abiertos

## Preparación
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker

sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 443/udp
```

## Variables de entorno
```bash
cp .env.vps.example .env
nano .env
```

## Primer despliegue
```bash
bash scripts/first_deploy.sh
```

## Actualización
```bash
bash scripts/update_deploy.sh
```

## Validaciones
```bash
docker compose -f docker-compose.vps.yml ps
docker compose -f docker-compose.vps.yml logs -f
curl -I https://da-tica.com
```
