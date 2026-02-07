# 🎯 RESUMEN EJECUTIVO: Docker-Compose + Labels Agnóstico

**Versión:** 2.0  
**Fecha:** 2026-02-07  
**Audiencia:** Arquitectos, DevOps, Desarrolladores, Agentes IA  
**Tiempo lectura:** 5 minutos

---

## ⚡ EL PROBLEMA Y LA SOLUCIÓN

### El Problema Original
Tu docker-compose funcionaba localmente pero fallaba en Coolify (producción):
```
ERROR: 502 Bad Gateway
```

El contenedor estaba **corriendo perfectamente**, pero **no era alcanzable** desde internet.

### La Causa Raíz
**Faltaban los labels de Traefik.** El proxy inverso no tenía instrucciones sobre cómo rutear el tráfico.

### La Solución
Añadir **10-15 labels** por servicio público para que el proxy sepa:
- Qué dominio enruta aquí
- Qué puerto escucha
- Si usar HTTPS/TLS
- Cómo redirigir HTTP → HTTPS

### El Aprendizaje Clave
> **En producción con proxy inverso gestionado, los labels SON tan críticos como los contenedores.**
>
> **Sin labels** = proxy no sabe que existes  
> **Con labels** = proxy te encuentra automáticamente  

---

## 📦 QUÉ CONTIENE ESTE KIT

Un **conjunto completo agnóstico** (aplica a cualquier proyecto) basado en lecciones reales:

| Componente | Archivo | Propósito |
|-----------|---------|-----------|
| 📘 **Documento Maestro** | `PROMPT_CONSOLIDADO.md` | Referencia completa de docker-compose en producción |
| 🛠️ **Skill Ejecutable** | `.opencode/skills/docker-compose-production/SKILL.md` | Plantilla detallada + validación para OMO |
| 📋 **Plantilla Agnóstica** | `templates/AGENTS.md.template` | Copia a nuevos proyectos |
| 💎 **Ejemplo Real** | `docker-compose.yml` | Código funcional en producción (2 servicios + DB) |
| 📖 **Guía de Uso** | `KIT_README.md` | Cómo usar el kit completo |
| 📑 **Índice** | `INDEX.md` | Navegación rápida |

---

## 🚀 INICIO RÁPIDO (5 PASOS)

### Paso 1: Aprende los Conceptos (10 minutos)
```
Lee: PROMPT_CONSOLIDADO.md secciones I-III
Qué: El triángulo (Internet → Proxy → Contenedores)
      + Estructura obligatoria (servicios, redes, volúmenes, labels)
      + Los 4 grupos de labels
```

### Paso 2: Ve un Ejemplo Real (5 minutos)
```
Abre: docker-compose.yml
Qué:  Proyecto da-tica: 2 servicios + DB + labels completos
```

### Paso 3: Copia la Plantilla (5 minutos)
```
Copia: templates/AGENTS.md.template → tu-proyecto/AGENTS.md
Personaliza: nombres, dominio, variables
```

### Paso 4: Crea tu docker-compose.yml (30 minutos)
```
Basándote en:
- PROMPT_CONSOLIDADO.md sección VII (template)
- SKILL.md secciones 8-9 (escenarios específicos)
- docker-compose.yml (referencia concreta)

Incluye:
✅ Servicios con estructura correcta
✅ 10-15 labels por servicio público
✅ Healthchecks en servicios críticos
✅ Variables en .env.example
✅ Red privada interna
✅ Volúmenes persistentes
```

### Paso 5: Valida Antes de Desplegar (20 minutos)
```
1. docker compose config              # Sintaxis OK?
2. docker inspect {container}         # Labels presentes?
3. docker exec {c} wget http://...    # Responde?
4. Checklist pre-deploy               # Todo ✅?
5. Peer review                        # Alguien revisó?
```

**Tiempo total:** ~1.5 horas (primera vez)

---

## 🎓 LOS 4 GRUPOS DE LABELS (CRÍTICO)

Cada servicio **público** necesita estos labels:

### Grupo 1: ACTIVACIÓN (2 labels)
```yaml
- "traefik.enable=true"                    # Activar exposición
- "traefik.docker.network=app"             # Red donde está
```

### Grupo 2: ENRUTADOR (4 labels)
```yaml
- "traefik.http.routers.web-https.rule=Host(`ejemplo.com`)"
- "traefik.http.routers.web-https.entrypoints=https"
- "traefik.http.routers.web-https.tls=true"
- "traefik.http.routers.web-https.tls.certresolver=letsencrypt"
```

### Grupo 3: SERVICIO (1 label)
```yaml
- "traefik.http.services.web.loadbalancer.server.port=8080"
```

### Grupo 4: MIDDLEWARE (3 labels - redirección HTTP→HTTPS)
```yaml
- "traefik.http.routers.web-http.rule=Host(`ejemplo.com`)"
- "traefik.http.routers.web-http.entrypoints=http"
- "traefik.http.routers.web-http.middlewares=web-redirect"
- "traefik.http.middlewares.web-redirect.redirectscheme.scheme=https"
- "traefik.http.middlewares.web-redirect.redirectscheme.permanent=true"
```

**Total:** ~12-15 labels por servicio público

---

## ✅ CHECKLIST PRE-DESPLIEGUE (5 minutos)

```bash
# 1. SINTAXIS
docker compose config                    # ✅ Sin errores

# 2. LABELS
docker inspect {container}               # ✅ traefik.enable=true presente
                                        # ✅ Router definido
                                        # ✅ Servicio con puerto

# 3. CONECTIVIDAD
docker exec {container} wget -qO- http://127.0.0.1:PUERTO
                                        # ✅ Responde (no timeout)

# 4. ESTRUCTURA YAML
# ✅ Imágenes con versión fija (no latest)
# ✅ restart: unless-stopped en producción
# ✅ Credenciales en .env (no en compose)
# ✅ Servicios internos SIN labels
# ✅ Todos en la misma red
# ✅ Volúmenes nombrados para datos
```

**Si todo está ✅, puedes desplegar.**

---

## 🚫 PROHIBICIONES ABSOLUTAS

| Prohibición | Consecuencia | Solución |
|------------|--------------|----------|
| `ports: ["8080:8080"]` | Inseguro; proxy no lo usa | Usar solo `expose: ["8080"]` |
| `image: nginx:latest` | Cambios inesperados | Versión fija: `nginx:1.26-alpine` |
| Credenciales en compose | Security breach | Variables desde `.env` |
| Omitir labels en público | 502 Bad Gateway | Incluir 10-15 labels |
| Sin healthcheck | Servicios "zombis" | Incluir siempre en DB/API |
| `network_mode: host` | Sin service discovery | Red bridge/overlay nombrada |

---

## 🔧 ESTRUCTURA MÍNIMA OBLIGATORIA

```yaml
version: "3.9"

services:
  # SERVICIO PÚBLICO (con labels)
  web:
    image: nginx:1.26-alpine              # ✅ Versión fija
    restart: unless-stopped                # ✅ Recuperación automática
    networks:
      - app                               # ✅ Red privada
    expose:
      - "8080"                            # ✅ Puerto interno (no ports!)
    environment:
      - VAR=${VAR}                        # ✅ Variables, no hardcoded
    healthcheck:                          # ✅ Obligatorio
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:8080/"]
      interval: 30s
      timeout: 5s
      retries: 3
    labels:                               # ⚠️ CRÍTICO (10-15 labels)
      - "traefik.enable=true"
      - "traefik.docker.network=app"
      # ... 10-13 labels más (ver PROMPT_CONSOLIDADO.md sección VII)

  # SERVICIO INTERNO (SIN labels)
  db:
    image: postgres:16-alpine              # ✅ Versión fija
    restart: unless-stopped                # ✅ Recuperación automática
    networks:
      - app                               # ✅ Misma red que web
    expose:
      - "5432"                            # ✅ Documentación (no exponer)
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}  # ✅ Variables
    volumes:
      - db_data:/var/lib/postgresql/data  # ✅ Persistencia
    healthcheck:                          # ✅ Obligatorio
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    # ❌ SIN LABELS - acceso solo interno

volumes:
  db_data:                                # ✅ Volumen nombrado

networks:
  app:                                    # ✅ Red privada
    external: false                       # false: docker-compose crea
                                          # true: orquestador crea
```

---

## 🐛 DEBUGGING: "502 Bad Gateway"

**Si ves este error, sigue este flujo:**

```
Paso 1: ¿Tiene labels?
        → docker inspect {container} | grep -A 20 '"Labels"'
        
Paso 2: ¿Labels correctos?
        → Busca: traefik.enable, routers, services
        
Paso 3: ¿Sintaxis YAML válida?
        → docker compose config
        
Paso 4: ¿Puerto interno correcto?
        → ¿expose: ["8080"] coincide con app?
        
Paso 5: ¿Red correcta?
        → ¿traefik.docker.network coincide con networks:?
        
Paso 6: ¿Contenedor responde localmente?
        → docker exec {c} wget -qO- http://127.0.0.1:PUERTO
        
Paso 7: ¿Logs del proxy?
        → docker logs traefik
```

**90% de probabilidad:** Falta un label o está malformado.

---

## 📚 DOCUMENTOS PRINCIPALES

### 1. PROMPT_CONSOLIDADO.md (470 líneas)
**¿Qué es?** El documento maestro  
**Tiempo:** 15 minutos lectura  
**Contiene:**
- Triángulo crítico (conceptual)
- Estructura obligatoria (YAML)
- Labels: 4 grupos + variantes
- Prohibiciones + anti-patrones
- Checklist pre-deploy
- Debugging rápido
- Template reutilizable

**👉 Léelo primero**

---

### 2. SKILL.md (540 líneas)
**¿Qué es?** Skill ejecutable en OMO (Oh My OpenCode)  
**Tiempo:** 20 minutos lectura  
**Contiene:**
- Plantilla agnóstica detallada
- Ejemplos paso-a-paso
- 5 escenarios reales
- Validación completa
- Diagnóstico 7-pasos

**👉 Consulta cuando trabajes**

---

### 3. AGENTS.md.template (274 líneas)
**¿Qué es?** Plantilla para nuevos proyectos  
**Cómo usar:**
```bash
cp templates/AGENTS.md.template ./nuevo-proyecto/AGENTS.md
# Personaliza: fecha, nombre, servicios, variables
```

**👉 Copia a tu proyecto**

---

### 4. docker-compose.yml
**¿Qué es?** Ejemplo real, funcional, en producción  
**Contiene:** 2 servicios (web + api) + postgres + labels completos  

**👉 Usa como referencia**

---

## 🎯 ¿CUÁL ERES TÚ?

### Arquitecto / Líder Técnico
```
1. Lee PROMPT_CONSOLIDADO.md secciones I-II      (5 min)
2. Revisa AGENTS.md.template                      (5 min)
3. Examina docker-compose.yml                     (5 min)
→ Listo para tomar decisiones arquitectónicas
```

### Desarrollador / DevOps
```
1. Lee PROMPT_CONSOLIDADO.md secciones II-III    (10 min)
2. Estudia SKILL.md secciones 8-9                (15 min)
3. Copia template y personaliza                   (20 min)
→ Listo para implementar
```

### Agente IA / Automatización
```
1. Carga AGENTS.md (plantilla personalizada)
2. Consulta SKILL.md según tarea
3. Ejecuta checklist pre-deploy
→ Listo para validar y desplegar
```

---

## 💡 IDEAS CLAVE A RECORDAR

1. **Labels no son opcionales.** Sin ellos, proxy no sabe routear.

2. **El checklist es tu mejor amigo.** Úsalo siempre antes de desplegar.

3. **502 Bad Gateway = problema de labels.** Verifica primero eso.

4. **Desarrollo ≠ Producción.** En local puedes ignorar labels. En prod, son obligatorios.

5. **Valida ANTES de desplegar.** `docker compose config` es tu primera línea de defensa.

6. **Las variables van en .env, no en compose.** Nunca hardcodees credenciales.

7. **Red privada interna.** Los servicios hablan por nombre, no IP.

8. **Imágenes con versión fija.** Nunca uses `latest`.

---

## 📊 MÉTRICAS DEL KIT

| Métrica | Valor |
|---------|-------|
| Documentación | ~1,700 líneas |
| Skills | 8+ específicos para Traefik/Docker |
| Ejemplos | 1 real + templates |
| Tiempo aprendizaje | 30-40 minutos |
| Tiempo implementación | 1-2 horas |
| Aplicable a | Cualquier proyecto con proxy |
| ROI | Evita 502 errors en producción |

---

## 🚀 PRÓXIMOS PASOS

### Ahora (5 minutos)
1. Abre `PROMPT_CONSOLIDADO.md`
2. Lee secciones I-III
3. Ve el ejemplo en `docker-compose.yml`

### Luego (1 hora)
1. Abre `.opencode/skills/docker-compose-production/SKILL.md`
2. Estudia tu caso específico
3. Copia template para tu proyecto

### Después (1-2 horas)
1. Crea tu `docker-compose.yml`
2. Personaliza `AGENTS.md`
3. Ejecuta checklist

### Finalmente
1. Valida con comandos
2. Deploy a staging
3. Monitorea
4. Deploy a producción

---

## 🎁 BONUS: REFERENCIAS RÁPIDAS

**Archivo más importante:** `PROMPT_CONSOLIDADO.md` (sección III: Labels)  
**Skill más útil:** `.opencode/skills/docker-compose-production/SKILL.md`  
**Ejemplo más claro:** `docker-compose.yml`  
**Plantilla más fácil:** `templates/AGENTS.md.template`  

**Comando más importante:** `docker compose config`  
**Comando más revelador:** `docker inspect {container} | grep Labels`  

---

## ⏱️ TIEMPO TOTAL

- **Aprender:** 30-40 minutos
- **Implementar:** 1-2 horas
- **Validar:** 20-30 minutos
- **Total primera vez:** ~2-3 horas
- **Proyectos futuros:** 30-60 minutos (reutilizar templates)

---

## 🏆 CUANDO TERMINES

Habrás aprendido a:
- ✅ Crear docker-compose.yml correcto en producción
- ✅ Entender POR QUÉ los labels son críticos
- ✅ Configurar 4 grupos de labels correctamente
- ✅ Evitar prohibiciones que rompen despliegues
- ✅ Validar antes de desplegar
- ✅ Debuggear problemas comunes (502, etc.)
- ✅ Usar templates reutilizables
- ✅ Documentar con AGENTS.md

---

## 📞 ¿AYUDA?

- **¿Por dónde empiezo?** → Lee este resumen + PROMPT_CONSOLIDADO.md
- **¿Cómo creo labels?** → Ve SKILL.md secciones 3-4
- **¿Cómo debuggeo?** → PROMPT_CONSOLIDADO.md sección VI
- **¿Tengo dudas?** → Busca en KIT_README.md (FAQ)
- **¿Necesito ejemplo?** → Abre docker-compose.yml

---

## 🎯 RESUMEN EN UNA FRASE

> **Lee PROMPT_CONSOLIDADO.md, entiende los labels, copia templates, crea docker-compose.yml, valida con checklist, despliega confiadamente.**

---

## 📈 CHANGELOG

| Versión | Cambio |
|---------|--------|
| 2.0 | Resumen ejecutivo de kit agnóstico |
| 1.0 | Kit inicial basado en proyecto da-tica |

---

**¡Felicidades!** Ya tienes todo lo necesario para desplegar correctamente en producción. 🚀

*Resumen Ejecutivo del Kit Docker-Compose en Producción*  
*Generado: 2026-02-07*  
*Listo para usar*