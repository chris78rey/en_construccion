[root@vmi3064761:~#
root@vmi3064761:~# ./
.cache/                .docker/               .ssh/                  diagnostico-portal.sh  fix-portal.sh
root@vmi3064761:~# ./fix-portal.sh
WEB=web-w40ssgg408swss4088ok8cck-024409871679

== Containers ==
web-w40ssgg408swss4088ok8cck-024409871679   da-tica_portal_web:1.0.0                     Up 18 minutes (healthy)
coolify-proxy                               traefik:v3.6                                 Up 38 hours (healthy)

== Networks ==
WEB networks:   w40ssgg408swss4088ok8cck
PROXY networks: coolify, w40ssgg408swss4088ok8cck

Selected WEB_NET=w40ssgg408swss4088ok8cck

== Test from proxy namespace -> WEB:8080 ==
* Host web-w40ssgg408swss4088ok8cck-024409871679:8080 was resolved.
* IPv6: (none)
* IPv4: 10.0.2.3
*   Trying 10.0.2.3:8080...
* Connected to web-w40ssgg408swss4088ok8cck-024409871679 (10.0.2.3) port 8080
> GET / HTTP/1.1
> Host: web-w40ssgg408swss4088ok8cck-024409871679:8080
> User-Agent: curl/8.6.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.26.3
< Date: Sat, 07 Feb 2026 03:02:33 GMT
< Content-Type: text/html
< Content-Length: 16657
< Last-Modified: Sat, 07 Feb 2026 02:44:05 GMT
< Connection: keep-alive
< ETag: "6986a6f5-4111"
< X-Content-Type-Options: nosniff
< X-Frame-Options: DENY
< Accept-Ranges: bytes
<
{ [14480 bytes data]
* Connection #0 to host web-w40ssgg408swss4088ok8cck-024409871679 left intact

== Connect coolify-proxy to WEB_NET if missing ==
Already connected: coolify-proxy -> w40ssgg408swss4088ok8cck

== Re-test from proxy namespace -> WEB:8080 ==
* Host web-w40ssgg408swss4088ok8cck-024409871679:8080 was resolved.
* IPv6: (none)
* IPv4: 10.0.2.3
*   Trying 10.0.2.3:8080...
* Connected to web-w40ssgg408swss4088ok8cck-024409871679 (10.0.2.3) port 8080
> GET / HTTP/1.1
> Host: web-w40ssgg408swss4088ok8cck-024409871679:8080
> User-Agent: curl/8.6.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.26.3
< Date: Sat, 07 Feb 2026 03:02:33 GMT
< Content-Type: text/html
< Content-Length: 16657
< Last-Modified: Sat, 07 Feb 2026 02:44:05 GMT
< Connection: keep-alive
< ETag: "6986a6f5-4111"
< X-Content-Type-Options: nosniff
< X-Frame-Options: DENY
< Accept-Ranges: bytes
<
{ [16657 bytes data]
* Connection #0 to host web-w40ssgg408swss4088ok8cck-024409871679 left intact

== HTTPS direct to origin (expect 200) ==
503
root@vmi3064761:~#
](Logs
Server: localhost
Lines:
100
Find in logs








INFO:     127.0.0.1:35908 - "GET /api/health HTTP/1.1" 200 OK
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
Lines:
100
Find in logs








/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
127.0.0.1 - - [07/Feb/2026:04:01:39 +0000] "GET / HTTP/1.1" 200 29450 "-" "Wget" "-"
10.0.1.6 - - [07/Feb/2026:04:01:42 +0000] "GET / HTTP/1.1" 200 29450 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36" "104.23.245.196"
2026/02/07 04:01:34 [notice] 1#1: using the "epoll" event method
2026/02/07 04:01:34 [notice] 1#1: nginx/1.26.3
2026/02/07 04:01:34 [notice] 1#1: built by gcc 13.2.1 20240309 (Alpine 13.2.1_git20240309) 
2026/02/07 04:01:34 [notice] 1#1: OS: Linux 6.8.0-90-generic
2026/02/07 04:01:34 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
2026/02/07 04:01:34 [notice] 1#1: start worker processes
2026/02/07 04:01:34 [notice] 1#1: start worker process 29
2026/02/07 04:01:34 [notice] 1#1: start worker process 30
2026/02/07 04:01:34 [notice] 1#1: start worker process 31
2026/02/07 04:01:34 [notice] 1#1: start worker process 32
2026/02/07 04:01:34 [notice] 1#1: start worker process 33
2026/02/07 04:01:34 [notice] 1#1: start worker process 34)
