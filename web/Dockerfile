# Production Dockerfile for static site (nginx)
FROM nginx:1.26.3-alpine

LABEL maintainer="da-tica <ops@da-tica.example>"
LABEL description="Static site served by nginx on port 8080 (multi-page ready)"

RUN rm -f /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/conf.d &&     cat > /etc/nginx/conf.d/default.conf <<'NGINX_CONF'
server {
  listen 8080;
  server_name _;

  root /usr/share/nginx/html;
  index index.html;

  # Serve static files directly (multi-page support)
  location / {
    try_files $uri $uri/ =404;
  }

  # Static assets: long cache
  location ~* \.(?:css|js|json|png|jpg|jpeg|svg|gif|ico|webp|woff2?)$ {
    try_files $uri =404;
    access_log off;
    add_header Cache-Control "public, max-age=604800, immutable";
  }

  # HTML files: no cache for updates
  location ~* \.html?$ {
    add_header Cache-Control "no-cache, must-revalidate";
  }

  # Security headers
  add_header X-Content-Type-Options nosniff;
  add_header X-Frame-Options DENY;

  location ~ /\. {
    deny all;
  }
}
NGINX_CONF

COPY . /usr/share/nginx/html

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3   CMD wget -qO- --timeout=2 http://127.0.0.1:8080/ >/dev/null 2>&1 || exit 1

CMD ["nginx", "-g", "daemon off;"]
