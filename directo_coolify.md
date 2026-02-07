Actúa como **Arquitecto de Plataforma y Consultor Senior en DevOps (Coolify/Docker)**. Se requiere producir una guía técnica y operativa, de nivel empresarial, orientada a estandarizar despliegues reproducibles y “cero fricción” en un VPS gestionado con **Coolify**, partiendo de desarrollos locales basados en **Docker Compose** y un flujo de versionado en **GitHub**.

### 1) Contexto, problema y objetivo central

Se debe analizar por qué stacks que “funcionan en local” con `docker-compose` fallan al desplegarse en un VPS con Coolify, identificando **errores comunes**, **patrones de fallo** y **factores que complican el despliegue**. El objetivo es construir un enfoque que permita **subir cambios a GitHub** y que **Coolify construya y ejecute automáticamente** la aplicación **sin ajustes manuales posteriores**, salvo escenarios excepcionales debidamente tipificados.

### 2) Alcance del sistema a estandarizar

El sistema objetivo contempla **aplicaciones completas** empaquetadas como stacks multi-servicio (por ejemplo: `web`, `api`, `db`, `worker`, `cache`), con los siguientes principios obligatorios:

* **Unidad mínima de despliegue:** *una imagen Docker por servicio*, coordinadas mediante `docker-compose` (no una sola imagen monolítica con múltiples servicios internos).
* **Consistencia entre entornos:** *un único `docker-compose.yml` base*, diseñado desde el inicio para ejecutarse correctamente en Coolify **sin overrides locales** y sin depender de configuraciones específicas del host.
* **Persistencia y seguridad de datos:** *volúmenes nombrados* para servicios con estado (DB, storage, uploads), desacoplados del ciclo de vida de los contenedores, garantizando que cambios de UI o de servicios “stateless” no afecten los datos.
* **Operación “push-to-deploy”:** cambios versionados en GitHub deben disparar la construcción y despliegue en Coolify de forma automática, minimizando intervención manual.

### 3) Requerimientos de salida (entregables)

La respuesta debe estar estructurada y ser accionable, incluyendo como mínimo:

#### A. Modelo de referencia para Coolify + Compose

* Arquitectura objetivo (capas y responsabilidades) y cómo Coolify/Traefik gestiona el enrutamiento y TLS.
* Reglas de diseño para `docker-compose.yml` orientadas a Coolify (puertos internos, exposición, redes, healthchecks, dependencias, variables de entorno, secretos).

#### B. Catálogo priorizado de errores comunes (mínimo 15)

Para cada error, incluir obligatoriamente:

* Síntomas observables (logs, estado “restarting/unhealthy”, inaccesibilidad pública, fallos de build).
* Causa raíz típica en la transición local → Coolify.
* Pasos de diagnóstico rápido en Coolify.
* Corrección inmediata y medida preventiva permanente.

Ejemplos de familias de errores a cubrir (no limitativo):

* Puertos mal declarados o servicios escuchando en interfaz incorrecta.
* Uso indebido de `ports:` vs `expose:`.
* Healthchecks que fallan por herramientas inexistentes en la imagen final.
* Dependencias ocultas del host (rutas locales, permisos, uid/gid).
* Persistencia incorrecta (volúmenes ausentes, bind mounts frágiles, recreación de DB).
* Variables de entorno faltantes/secretos mal gestionados.
* Orden de arranque y readiness (db no lista, migraciones, workers).
* Problemas de build remoto (contextos incorrectos, Dockerfile multi-stage incompleto).

#### C. Estrategia de persistencia sin pérdida de datos

* Patrón recomendado de volúmenes nombrados por servicio.
* Lineamientos para actualizaciones seguras (incluyendo migraciones cuando aplique).
* Recomendación mínima de backups y verificación post-deploy.

#### D. Flujo operativo GitHub → Coolify “sin tocar Coolify”

* Proceso paso a paso desde commit hasta despliegue.
* Reglas para versionado y releases (tags, inmutabilidad, reproducibilidad).
* Checklist previo al push (mínimo 12 validaciones) y checklist post-deploy (mínimo 8 validaciones).

#### E. Criterios verificables de éxito

Definir condiciones medibles que demuestren que el despliegue “funciona para el mundo”, incluyendo:

* Disponibilidad pública por dominio.
* TLS activo y correcto (si aplica).
* Servicios en estado estable (sin reinicios).
* Persistencia confirmada tras redeploy y restart.
* Trazabilidad de versión desplegada.

### 4) Restricciones y principios de calidad

* Priorizar soluciones **simples, mantenibles y repetibles**.
* Evitar propuestas que requieran reconfiguración manual recurrente en Coolify.
* Mantener lenguaje formal, técnico y preciso.
* Entregar contenido conciso pero completo, sin redundancias, con estructura clara y progresión lógica.
* Asumir que el objetivo final es que el usuario pueda empaquetar aplicaciones completas en Docker Compose, versionarlas en GitHub y lograr despliegues consistentes en Coolify con mínima intervención.

### 5) Orientación final

El resultado debe servir como base para una metodología/estándar de despliegue que reduzca fallos, acelere entregas y preserve datos, permitiendo operar bajo el principio: **“push a GitHub y despliegue automático en Coolify a la primera”**, con causas de excepción claramente definidas y tratables.
