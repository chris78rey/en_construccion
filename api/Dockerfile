FROM python:3.12.8-alpine3.20

WORKDIR /app

RUN apk add --no-cache su-exec

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY main.py /app/main.py
COPY entrypoint.sh /app/entrypoint.sh

RUN adduser -D -u 10001 app \
  && chmod +x /app/entrypoint.sh

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=10s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/api/health', timeout=3).read()"

ENTRYPOINT ["/app/entrypoint.sh"]
