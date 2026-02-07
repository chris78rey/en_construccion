# Production Dockerfile for static site (nginx)
# Builds an image that serves the contents of the ./web directory via nginx on internal port 8080.
# - Exposes 8080 (internal only; do NOT map host ports in production compose)
# - Provides a simple nginx config with SPA-friendly routing (fallback to index.html)
# - Adds caching headers for static assets and some basic security headers
# - Healthcheck is included for container orchestration

FROM nginx:1.26.3-alpine

LABEL maintainer="da-tica <ops@da-tica.example>"
LABEL description="Static site served by nginx on port 8080 (production image for Coolify)"

# Remove default nginx config
RUN rm -f /etc/nginx/conf.d/default.conf

# Create nginx conf that listens on 8080
RUN mkdir -p /etc/nginx/conf.d && \
    cat > /etc/nginx/conf.d/default.conf <<'NGINX_CONF'
server {
  listen 8080;
  server_name _;

  root /usr/share/nginx/html;
  index index.html;

  # SPA fallback: if asset not found, serve index.html
  location / {
    try_files $uri $uri/ /index.html;
  }

  # Static assets: long cache, public
  location ~* \.(?:css|js|json|png|jpg|jpeg|svg|gif|ico|webp|woff2?)$ {
    try_files $uri =404;
    access_log off;
    add_header Cache-Control "public, max-age=604800, immutable";
  }

  # Minimal security headers
  add_header X-Content-Type-Options nosniff;
  add_header X-Frame-Options DENY;

  # Optional: disable .htaccess style files
  location ~ /\.ht {
    deny all;
  }
}
NGINX_CONF

# Copy static site into nginx html folder
# Expectation: build context contains the final static files (index.html, app.js, styles.css, assets...)
COPY . /usr/share/nginx/html

# Ensure ownership/permissions are ok for nginx user
RUN chown -R nginx:nginx /usr/share/nginx/html || true

# Expose the internal port that Traefik/Coolify will route to (do not map host ports in compose)
EXPOSE 8080

# Healthcheck to allow orchestrators (and compose healthcheck override) to see readiness
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget -qO- --timeout=2 http://127.0.0.1:8080/ >/dev/null 2>&1 || exit 1

# Run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]