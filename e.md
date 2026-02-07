root@vmi3064761:~#
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
