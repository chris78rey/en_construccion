# 🚀 Kit Completo: Docker-Compose en Producción con Labels Obligatorios

**Versión:** 1.0  
**Creado:** 2026-02-07  
**Basado en:** Lecciones reales del proyecto `da-tica` en Coolify  
**Aplicable a:** Cualquier proyecto con proxy inverso gestionado

---

## 📦 ¿QUÉ CONTIENE ESTE KIT?

Este kit te proporciona **todo lo necesario** para desplegar correctamente cualquier proyecto en producción usando docker-compose con proxy inverso (Traefik en Coolify, Kubernetes, etc.).

### Archivos Incluidos

```
en_construccion/
├── 📄 PROMPT_CONSOLIDADO.md              # ⭐ PUNTO DE ENTRADA (léelo primero)
├── 📄 KIT_README.md                      # Este archivo
├── .opencode/
│   └── skills/
│       └── docker-compose-production/
│           └── 📘 SKILL.md               # Skill OMO: plantilla + validación
├── templates/
│   └── 📋 AGENTS.md.template             # Plantilla para nuevos proyectos
├── docker-compose.yml                    # Ejemplo real (proyecto da-tica)
└── AGENTS.md                             # AGENTS.md del proyecto actual
```

---

## 🎯 POR DÓNDE EMPEZAR

### Opción A: Aprender Primero (Recomendado)

1. **Lee `PROMPT_CONSOLIDADO.md`** (5-10 minutos)
   - Entiende el "triángulo crítico" (Internet → Proxy → Contenedores)
   - Comprende POR QUÉ los labels son obligatorios
   - Ve ejemplo completo con estructura

2. **Consulta el Skill `SKILL.md`** en `.opencode/skills/docker-compose-production/`
   - Plantilla detallada con múltiples escenarios
   - Tabla de anti-patrones y soluciones
   - Checklist pre-despliegue
   - Debugging step-by-step

3. **Copia la plantilla `AGENTS.md.template`** para tu nuevo proyecto
   - Personaliza con tus datos
   - Úsalo como "manual ejecutivo" del proyecto

### Opción B: Empezar Rápido (Para Impacienes)

1. Copia `templates/AGENTS.md.template` → tu proyecto
2. Copia el ejemplo de `docker-compose.yml` del actual
3. Reemplaza placeholders
4. Ejecuta checklist (sección "CHECKLIST: ANTES DE DESPLEGAR" en `PROMPT_CONSOLIDADO.md`)

---

## 📚 GUÍA DE LECTURA

### Para Arquitectos / Líderes Técnicos
- **AGENTS.md** (este proyecto): Visión general, estructura, convenciones
- **PROMPT_CONSOLIDADO.md**: Razones técnicas, anti-patrones, debugging

### Para Desarrolladores / DevOps
- **SKILL.md** (docker-compose-production): Plantillas, ejemplos prácticos
- **docker-compose.yml** (ejemplo): Referencia concreta
- **PROMPT_CONSOLIDADO.md** (sección VI): Debugging rápido

### Para Agentes IA / Automatización
- **AGENTS.md.template**: Instrucciones estructuradas
- **PROMPT_CONSOLIDADO.md**: Contexto completo
- **SKILL.md**: Validación y checklist

---

## 🔑 CONCEPTOS CLAVE

### El Problema Original
Tu docker-compose funcionaba localmente pero fallaba en producción (Coolify) con:
```
502 Bad Gateway
```

**Causa:** Labels de Traefik **faltaban** o estaban **malformados**.

### La Solución
Añadir **10-15 labels** por servicio público para que el proxy sepa:
- Qué dominio/host enruta aquí
- Qué puerto interno escucha
- Si usar HTTPS/TLS
- Cómo redirigir HTTP → HTTPS

### El Aprendizaje
> **En producción con proxy inverso gestionado, los labels SON tan importantes como los contenedores.**

Sin labels = proxy no sabe que existes  
Con labels = proxy te encuentra automáticamente

---

## 📋 CHECKLIST RÁPIDO (Antes de Desplegar)

```bash
# 1. Validar sintaxis
docker compose config                          # ✅ Sin errores

# 2. Verificar labels
docker inspect {container} | grep -A 20 Labels # ✅ Presentes

# 3. Probar conectividad local
docker exec {container} wget -qO- http://127.0.0.1:{puerto}/
                                               # ✅ Responde

# 4. Revisar estructura en compose
# ✅ Servicios públicos: tienen labels
# ✅ Servicios internos: SIN labels
# ✅ Todos en la misma red
# ✅ Imágenes con versión fija (no latest)
# ✅ Credenciales en .env (no en compose)
```

---

## 🚨 PROHIBICIONES ABSOLUTAS

**NUNCA HAGAS ESTO EN PRODUCCIÓN:**

1. ❌ `ports: ["8080:8080"]` → ✅ Usa `expose: ["8080"]`
2. ❌ `image: nginx:latest` → ✅ `image: nginx:1.26-alpine`
3. ❌ Credenciales hardcodeadas → ✅ Variables `${VAR}`
4. ❌ Omitir labels en servicios públicos → ✅ 10-15 labels
5. ❌ `network_mode: host` → ✅ Red bridge/overlay nombrada
6. ❌ Healthcheck omitido → ✅ Incluir en servicios críticos

---

## 📁 ESTRUCTURA DE ARCHIVOS EXPLICADA

### `PROMPT_CONSOLIDADO.md`
**¿Qué es?** El "diccionario ejecutivo" de docker-compose en producción  
**Cuándo leerlo?** Primero (5-10 minutos)  
**Contiene:**
- Triángulo crítico (Internet → Proxy → Contenedores)
- Estructura obligatoria (servicios, redes, volúmenes, labels)
- 4 grupos de labels (activación, router, servicio, middleware)
- Prohibiciones absolutas
- Checklist pre-despliegue
- Debugging rápido (502, Connection Refused, DNS)
- Template reutilizable
- Variables de entorno
- Anti-patrones comunes

### `.opencode/skills/docker-compose-production/SKILL.md`
**¿Qué es?** Skill ejecutable en OMO (Oh My OpenCode)  
**Cuándo usarlo?** Cuando trabajes con docker-compose  
**Contiene:**
- 11 secciones con detalles profundos
- Arquitectura conceptual visual
- Estructura nivel-por-nivel (servicios, redes, volúmenes)
- Labels con ejemplos prácticos
- Variantes de reglas (Host, PathPrefix, combinados)
- Ejemplo completo paso-a-paso
- 5 escenarios reales (Frontend + API, Microservicios, Interno+Admin)
- Flujo de diagnóstico (7 pasos)
- Template reutilizable
- Checklist completo de validación
- Referencias documentadas

### `templates/AGENTS.md.template`
**¿Qué es?** Plantilla para AGENTS.md de nuevos proyectos  
**Cuándo usarlo?** Al crear un nuevo proyecto  
**Cómo:**
```bash
cp templates/AGENTS.md.template ./nuevo-proyecto/AGENTS.md
# Edita y personaliza:
# - {FECHA}, {COMMIT_HASH}
# - Nombres de servicios
# - Dominios
# - Variables de entorno
```

**Contiene:**
- Structure del proyecto
- WHERE TO LOOK (tabla de referencias rápidas)
- Convenciones obligatorias
- Anti-patterns reales
- Deployment checklist
- Common issues & solutions
- Skills disponibles
- Variables de entorno por categoría
- Notes for AI Agents

### `docker-compose.yml` (Proyecto da-tica)
**¿Qué es?** Ejemplo real, funcional, en producción  
**Cuándo consultarlo?** Como referencia concreta  
**Contiene:**
- 2 servicios: `web` (nginx) + `api` (python/node)
- Labels completos (15+ por servicio)
- Healthchecks configurados
- Variables de entorno
- Red privada `coolify`
- Volúmenes persistentes
- Redirección HTTP → HTTPS

---

## 🛠️ CÓMO USAR ESTE KIT EN TU PROYECTO

### Paso 1: Inicializa el Proyecto

```bash
mkdir mi-proyecto
cd mi-proyecto
git init
```

### Paso 2: Copia la Plantilla AGENTS.md

```bash
cp ../templates/AGENTS.md.template ./AGENTS.md
# Edita con tu información:
# - Nombre del proyecto
# - Servicios específicos
# - Dominios
# - Fechas
```

### Paso 3: Copia el Skill

```bash
mkdir -p .opencode/skills
cp -r ../en_construccion/.opencode/skills/docker-compose-production \
      .opencode/skills/
```

### Paso 4: Crea tu docker-compose.yml

Basándote en:
- `PROMPT_CONSOLIDADO.md` (sección VII: Template Reutilizable)
- `SKILL.md` (sección 8 o 9: escenarios específicos)
- `docker-compose.yml` actual como referencia

**Estructura mínima:**

```yaml
version: "3.9"

services:
  # Servicio público con labels
  web:
    image: nginx:1.26-alpine
    restart: unless-stopped
    networks: [app]
    expose: ["8080"]
    labels:
      - "traefik.enable=true"
      - "traefik.docker.network=app"
      # ... 10 labels más (ver template)

  # Servicio interno SIN labels
  db:
    image: postgres:16-alpine
    restart: unless-stopped
    networks: [app]
    expose: ["5432"]
    # ❌ Sin labels

networks:
  app:
    external: false
```

### Paso 5: Valida Antes de Desplegar

```bash
# Sintaxis
docker compose config

# Labels
docker inspect {container} | grep Labels

# Conectividad
docker exec {container} wget -qO- http://127.0.0.1:PUERTO

# Checklist completo
# (Ver PROMPT_CONSOLIDADO.md, sección V)
```

---

## 💡 PREGUNTAS FRECUENTES

**P: ¿Realmente necesito labels en producción?**  
R: Sí. Sin ellos, el proxy no sabe cómo rutear. Es obligatorio.

**P: ¿Qué pasa si me olvido un label?**  
R: El proxy no sabrá qué hacer con ese servicio. Verás `502 Bad Gateway`.

**P: ¿Puedo usar esto con Kubernetes?**  
R: El concepto es el mismo (Ingress rules), pero la sintaxis cambia. Este kit es específico de Docker Compose + Traefik.

**P: ¿Los labels van en compose o en archivo aparte?**  
R: En el compose, en la sección `labels:` de cada servicio.

**P: ¿Necesito recargar el proxy después de cambiar labels?**  
R: No. Traefik en Docker lee labels continuamente. Solo reinicia el contenedor.

**P: ¿Qué significa "502 Bad Gateway"?**  
R: El proxy no puede alcanzar el contenedor. Causas probables: labels ausentes, puerto incorrecto, red incorrecta.

---

## 🔗 REFERENCIAS RÁPIDAS

### Dentro de Este Kit
- **Aprende:** `PROMPT_CONSOLIDADO.md`
- **Implementa:** `SKILL.md` (en `.opencode/skills/`)
- **Plantilla:** `templates/AGENTS.md.template`
- **Ejemplo Real:** `docker-compose.yml`
- **Documentación:** Este archivo (`KIT_README.md`)

### Documentación Externa
- [Docker Compose Spec](https://github.com/compose-spec/compose-spec)
- [Traefik Docker Provider](https://docs.traefik.io/providers/docker/)
- [Docker Labels Best Practices](https://docs.docker.com/config/labels-custom-metadata/)

### Comandos Útiles
```bash
# Validar sintaxis
docker compose config

# Revisar labels
docker inspect {container} | jq '.Config.Labels'

# Probar conectividad
docker exec {container} wget -qO- http://127.0.0.1:{puerto}/health

# Ver logs del proxy
docker logs traefik

# Reiniciar todo
docker compose down && docker compose up -d
```

---

## 📊 DIAGRAMA DEL KIT

```
┌─────────────────────────────────────────────────────┐
│         KIT DOCKER-COMPOSE EN PRODUCCIÓN            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. PROMPT_CONSOLIDADO.md  ← LÉELO PRIMERO        │
│     • Conceptos fundamentales                       │
│     • Estructura obligatoria                        │
│     • Labels: 4 grupos                              │
│     • Checklist pre-deploy                          │
│     • Debugging rápido                              │
│                                                     │
│  2. SKILL.md  ← CONSULTA CUANDO TRABAJES           │
│     • Plantilla agnóstica                           │
│     • 5 escenarios reales                           │
│     • Anti-patrones detallados                      │
│     • Ejemplos paso-a-paso                          │
│                                                     │
│  3. AGENTS.md.template  ← COPIA A TU PROYECTO      │
│     • Personaliza con tus datos                     │
│     • Convenciones y reglas                         │
│     • WHERE TO LOOK (referencias rápidas)           │
│                                                     │
│  4. docker-compose.yml  ← USA COMO REFERENCIA      │
│     • Ejemplo real en producción                    │
│     • 2 servicios (web + api)                       │
│     • Labels completos                              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 HOJA DE RUTA

### Semana 1: Aprender
- [ ] Lee `PROMPT_CONSOLIDADO.md` (1 hora)
- [ ] Estudia `SKILL.md` secciones 1-5 (2 horas)
- [ ] Revisa ejemplos en `docker-compose.yml` (1 hora)

### Semana 2: Implementar
- [ ] Copia `AGENTS.md.template` a tu proyecto
- [ ] Crea `docker-compose.yml` basado en template
- [ ] Copia el skill a `.opencode/skills/`
- [ ] Ejecuta checklist pre-deploy

### Semana 3: Validar
- [ ] `docker compose config` → sin errores
- [ ] `docker inspect` → labels presentes
- [ ] Pruebas de conectividad
- [ ] Deploy a staging
- [ ] Monitoreo en producción

---

## 📞 SOPORTE Y CONTRIBUCIONES

Si encuentras:
- **Un nuevo anti-patrón:** Documéntalo en `PROMPT_CONSOLIDADO.md`
- **Un bug o ambigüedad:** Clarifica en `SKILL.md`
- **Una mejora:** Actualiza `AGENTS.md.template`

Este kit es **vivo**. Evoluciona con tus aprendizajes.

---

## 📈 CHANGELOG

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2026-02-07 | Kit completo agnóstico; énfasis en labels obligatorios |

---

## 🏆 LECCIONES APRENDIDAS (Resumen)

### ¿Por Qué Existe Este Kit?

El proyecto `da-tica` en Coolify enseñó que:

1. **Los labels NO son opcionales** en producción con proxy gestionado
2. **502 Bad Gateway** usualmente significa: labels ausentes o malformados
3. **La validación temprana** (checklist) previene despliegues fallidos
4. **La documentación clara** (AGENTS.md) evita errores futuros
5. **Los ejemplos concretos** (docker-compose.yml) aceleran implementación

### Impacto

- **Antes:** "¿Por qué no funciona en producción?" (debugging ciego)
- **Después:** Checklist → validación → deployment seguro

---

## 🚀 NEXT STEPS

1. **Ahora:** Lee `PROMPT_CONSOLIDADO.md` (5 minutos)
2. **Luego:** Consulta `SKILL.md` para tu caso específico (10 minutos)
3. **Después:** Copia plantilla + crea tu `docker-compose.yml`
4. **Finalmente:** Ejecuta checklist + deploy

---

**¡Felicidades!** Tienes todo lo necesario para desplegar correctamente. 🎉

*Generado a partir de lecciones reales. Última actualización: 2026-02-07*