#!/usr/bin/env sh
set -eu

mkdir -p /data
chown -R app:app /data || true

exec su-exec app:app \
  python -m uvicorn main:app --host 0.0.0.0 --port 8000
