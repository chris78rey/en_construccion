# Da-TIca - Despliegue Astro en Coolify

## Build Pack
Usar **Docker Compose**.

## Base Directory
```text
/
```

## Docker Compose Location
```text
/docker-compose.yml
```

## Dominio
En **Domains for web**, configurar el dominio del servicio `web`.

Si el contenedor escucha en `8080`, colocar el puerto al final del dominio.

Ejemplo:
```text
https://da-tica.com:8080,https://www.da-tica.com:8080
```

## Qué cambió
- Ya no se construye `./web`
- Ahora se construye la raíz del proyecto
- El build final sale de `dist/`
- Nginx sirve la salida generada por Astro

## Validación rápida
- El recurso `web` debe quedar en **Running (healthy)**
- El dominio debe abrir sin error 503
- Si cambia código, hacer redeploy
