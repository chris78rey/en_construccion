# 📑 INDEX: Guía de Navegación del Kit Docker-Compose + Labels

**Versión:** 1.0  
**Fecha:** 2026-02-07  
**Propósito:** Mapa rápido de todos los recursos en el kit

---

## 🎯 ¿POR DÓNDE EMPIEZO?

### Opción 1: Entender Primero (Recomendado)
```
1. LEE: PROMPT_CONSOLIDADO.md         (5-10 min)
   → Entiende el concepto
   
2. ESTUDIA: SKILL.md                   (15-20 min)
   → Ve ejemplos prácticos
   
3. COPIA: AGENTS.md.template           (personalizar)
   → Adapta a tu proyecto
   
4. CREA: docker-compose.yml            (basado en template)
   → Implementa
   
5. VALIDA: Checklist pre-deploy        (10 min)
   → Asegura calidad
```

### Opción 2: Implementar Rápido
```
1. COPIA: templates/AGENTS.md.template → tu proyecto
2. COPIA: docker-compose.yml ejemplo → tu proyecto
3. MODIFICA: placeholders
4. EJECUTA: docker compose config
5. VALIDA: Checklist
```

---

## 📚 ESTRUCTURA DEL KIT

```
en_construccion/
│
├── 🎯 PUNTO DE ENTRADA
│   ├── PROMPT_CONSOLIDADO.md          ⭐ Léelo primero (maestro)
│   ├── KIT_README.md                  📖 Guía de uso del kit
│   └── INDEX.md                       📑 Este archivo (navegación)
│
├── 📟 ARCHIVOS EJECUTABLES
│   ├── docker-compose.yml             ✅ Ejemplo real (2 servicios)
│   ├── docker-compose.dev.yml         💻 Versión desarrollo
│   └── docker-compose.yml.api         (adicional)
│
├── 🔧 SKILLS (OMO - Oh My OpenCode)
│   ├── .opencode/skills/docker-compose-production/SKILL.md
│   │   └── Skill agnóstico: plantilla + validación
│   ├── .opencode/skills/validate-traefik-labels/SKILL.md
│   │   └── Validación específica de labels Traefik
│   ├── .opencode/skills/generate-compose-with-labels/SKILL.md
│   │   └── Generador de docker-compose
│   └── [10+ skills adicionales para Coolify]
│
├── 📋 PLANTILLAS
│   ├── templates/AGENTS.md.template    🔄 Copia para nuevos proyectos
│   └── (más plantillas aquí)
│
└── 📄 DOCUMENTACIÓN
    ├── AGENTS.md                      📍 Documentación del proyecto actual
    ├── instr.md                       📌 Instrucciones consolidadas
    └── construir_skills.md            🛠️ Guía para crear skills
```

---

## 🔍 BÚSQUEDA RÁPIDA POR NECESIDAD

### Necesito... → Consulta...

| Necesito | Archivo | Sección |
|----------|---------|---------|
| **Entender conceptos** | PROMPT_CONSOLIDADO.md | I-II (Triángulo + Estructura) |
| **Ver ejemplo completo** | docker-compose.yml | Todo el archivo |
| **Labels específicamente** | PROMPT_CONSOLIDADO.md | III (Labels: 4 grupos) |
| **Checklist antes de deploy** | PROMPT_CONSOLIDADO.md | V (Checklist Pre-Deploy) |
| **Debugging (502, etc.)** | PROMPT_CONSOLIDADO.md | VI (Diagnóstico Rápido) |
| **Template para nuevo proyecto** | templates/AGENTS.md.template | Todo |
| **Skill de referencia** | .opencode/skills/docker-compose-production/SKILL.md | Todo |
| **Anti-patrones** | PROMPT_CONSOLIDADO.md | IX (Anti-patterns) |
| **Variables .env** | PROMPT_CONSOLIDADO.md | VIII (Environment Variables) |
| **Prohibiciones** | PROMPT_CONSOLIDADO.md | IV (Prohibiciones Absolutas) |
| **Estructura YAML mínima** | PROMPT_CONSOLIDADO.md | VII (Template Reutilizable) |
| **Flujo de uso paso-a-paso** | KIT_README.md | "Cómo usar este kit en tu proyecto" |
| **Validación de labels** | .opencode/skills/validate-traefik-labels/SKILL.md | Todo |
| **Generar compose automáticamente** | .opencode/skills/generate-compose-with-labels/SKILL.md | Todo |

---

## 📖 CONTENIDO POR ARCHIVO

### PROMPT_CONSOLIDADO.md
**Descripción:** Documento maestro agnóstico  
**Largo:** ~470 líneas  
**Tiempo lectura:** 10-15 minutos  

| Sección | Contenido |
|---------|-----------|
| I | El triángulo crítico (conceptual) |
| II | Estructura obligatoria (YAML) |
| III | **Labels (lo más crítico)** - 4 grupos, variantes |
| IV | Prohibiciones absolutas |
| V | Checklist pre-deploy |
| VI | Diagnóstico rápido (502, Connection Refused, DNS) |
| VII | Template reutilizable (copia y adapta) |
| VIII | Variables de entorno (.env) |
| IX | Anti-patrones comunes |
| X | Notas para agentes IA |
| XI | Referencias |
| XII | Cómo usar este prompt |

**↓ Léelo primero ↓**

---

### SKILL.md (docker-compose-production)
**Ubicación:** `.opencode/skills/docker-compose-production/SKILL.md`  
**Descripción:** Skill ejecutable en OMO  
**Largo:** ~540 líneas  
**Tiempo lectura:** 20-30 minutos  

| Sección | Contenido |
|---------|-----------|
| 1 | Introducción: por qué existe este skill |
| 2 | Arquitectura conceptual (diagrama) |
| 3 | Estructura obligatoria (3 niveles) |
| 4 | Labels para proxy inverso ⭐ |
| 5 | Anti-patrones críticos |
| 6 | Validación pre-deploy (checklist) |
| 7 | Flujo de diagnóstico (7 pasos) |
| 8 | Template reutilizable |
| 9 | Mejores prácticas por escenario (3 casos) |
| 10 | Cuándo invocar este skill |
| 11 | Referencias |

**↓ Úsalo cuando trabajes con docker-compose ↓**

---

### KIT_README.md
**Descripción:** Guía de uso del kit completo  
**Largo:** ~455 líneas  
**Tiempo lectura:** 5-10 minutos  

**Secciones principales:**
- Por dónde empezar (Opción A y B)
- Guía de lectura por rol
- Conceptos clave
- Checklist rápido
- Prohibiciones absolutas
- Estructura de archivos explicada
- Cómo usar este kit en tu proyecto (5 pasos)
- Preguntas frecuentes
- Hoja de ruta (3 semanas)

**↓ Lee esto si no sabes qué consultar ↓**

---

### templates/AGENTS.md.template
**Descripción:** Plantilla para AGENTS.md de nuevos proyectos  
**Largo:** ~274 líneas  
**Tiempo creación:** 10-15 minutos (copiar + personalizar)  

**Cómo usar:**
```bash
cp templates/AGENTS.md.template ./nuevo-proyecto/AGENTS.md
# Edita: {FECHA}, {COMMIT_HASH}, nombres servicios, variables
```

**Contiene:**
- Overview agnóstico
- WHERE TO LOOK (referencias rápidas)
- Convenciones y reglas obligatorias
- Anti-patterns
- Deployment checklist
- Common issues & solutions
- Skills disponibles
- Variables de entorno
- Notes for AI Agents

**↓ Copia a tu proyecto ↓**

---

### docker-compose.yml
**Descripción:** Ejemplo real, funcional, en producción  
**Aplicación:** Proyecto da-tica  
**Servicios:** 2 (web + api) + postgres  

**Incluye:**
- Labels completos para web y api
- Healthchecks configurados
- Variables de entorno
- Red privada (coolify)
- Volúmenes persistentes
- Redirección HTTP → HTTPS
- Comentarios explicativos

**↓ Usa como referencia concreta ↓**

---

## 🎓 FLUJO RECOMENDADO PARA NUEVOS USUARIOS

### Paso 1: Aprender (30 minutos)
```
1. Lee PROMPT_CONSOLIDADO.md              (10 min)
   Entiende: triángulo, estructura, labels
   
2. Lee KIT_README.md                      (5 min)
   Visión general del kit
   
3. Estudia secciones 1-5 de SKILL.md      (15 min)
   Estructura, labels, ejemplos
```

### Paso 2: Prepararse (20 minutos)
```
1. Abre docker-compose.yml actual         (reference)
   Compara con template
   
2. Abre SKILL.md sección 8 o 9           (template)
   Escoge tu escenario
   
3. Copia AGENTS.md.template              (personalizar)
   Edita con tus datos
```

### Paso 3: Implementar (30 minutos)
```
1. Crea docker-compose.yml               (basado en template)
   Usa PROMPT_CONSOLIDADO.md sección VII
   
2. Añade labels usando SKILL.md           (4 grupos)
   Estructura: activación → router → servicio → middleware
   
3. Organiza variables en .env.example
   Basado en AGENTS.md.template sección "ENVIRONMENT VARIABLES"
```

### Paso 4: Validar (20 minutos)
```
1. docker compose config                  (sintaxis)
2. docker inspect {container}             (labels)
3. docker exec {container} wget           (conectividad)
4. Checklist pre-deploy                   (completar)
5. Revisar PROMPT_CONSOLIDADO.md sec VI   (debugging)
```

### Paso 5: Desplegar
```
1. Ejecuta checklist completo
2. Deploy a staging
3. Pruebas de conectividad
4. Deploy a producción
5. Monitoreo
```

---

## 🔗 REFERENCIAS CRUZADAS

### Labels (Lo Más Crítico)
- **Aprende:** PROMPT_CONSOLIDADO.md sección III
- **Implementa:** SKILL.md sección 4
- **Valida:** .opencode/skills/validate-traefik-labels/SKILL.md
- **Genera:** .opencode/skills/generate-compose-with-labels/SKILL.md
- **Ejemplo:** docker-compose.yml (15+ labels por servicio)

### Anti-patrones
- **Lista:** PROMPT_CONSOLIDADO.md sección IV y IX
- **Detallado:** SKILL.md sección 5
- **Tabla:** KIT_README.md (sección "PROHIBICIONES ABSOLUTAS")

### Debugging
- **Rápido:** PROMPT_CONSOLIDADO.md sección VI
- **Detallado:** SKILL.md sección 7
- **Soluciones:** AGENTS.md.template sección "COMMON ISSUES & SOLUTIONS"

### Checklists
- **Pre-deploy:** PROMPT_CONSOLIDADO.md sección V
- **Validación:** SKILL.md sección 6
- **Deployment:** AGENTS.md.template (al final)

---

## 📊 ESTADÍSTICAS DEL KIT

| Métrica | Valor |
|---------|-------|
| Documentos principales | 3 |
| Skills (Traefik/Docker) | 8+ |
| Líneas de documentación | ~1,700 |
| Ejemplo completo (docker-compose) | 1 |
| Plantillas | 1 |
| Tiempo lectura total | 30-40 min |
| Tiempo implementación | 1-2 horas |
| Tiempo validación | 20-30 min |

---

## ✅ CHECKLIST RÁPIDO

Antes de desplegar, verifica:

- [ ] Leíste PROMPT_CONSOLIDADO.md sección III (Labels)
- [ ] Copiaste docker-compose.yml template (SKILL.md sección 8)
- [ ] Ejecutaste `docker compose config` (sin errores)
- [ ] Verificaste `docker inspect {container}` (labels presentes)
- [ ] Probaste `docker exec wget` (conectividad)
- [ ] Completaste checklist pre-deploy (PROMPT_CONSOLIDADO.md sección V)
- [ ] Revistas anti-patrones (PROMPT_CONSOLIDADO.md sección IV)
- [ ] Documentaste variables en `.env.example`
- [ ] Creaste/personalizaste `AGENTS.md` (basado en template)
- [ ] Alguien verificó tu `docker-compose.yml` (peer review)

---

## 🎯 MAPA DE NAVEGACIÓN VISUAL

```
┌─────────────────────────────────────────────────────────────┐
│                    INICIO DEL KIT                           │
│                                                             │
│  ¿Primera vez?              ¿Tengo experiencia?            │
│       ↓                              ↓                      │
│  Lee KIT_README.md          Lee PROMPT_CONSOLIDADO.md      │
│       ↓                              ↓                      │
│  Lee PROMPT_CONSOLIDADO.md  Consulta SKILL.md             │
│       ↓                              ↓                      │
│  Estudia SKILL.md           Copia docker-compose.yml       │
│       ↓                              ↓                      │
│  Copia AGENTS.md.template   Adapta a tu proyecto          │
│       ↓                              ↓                      │
│  Copia docker-compose.yml   Valida con checklist          │
│       ↓                              ↓                      │
│  Personaliza todo      →  Implementa → Valida → Deploy    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 TIPS RÁPIDOS

1. **Siempre valida ANTES de desplegar:** `docker compose config`
2. **502 Bad Gateway = labels problem:** Verifica `docker inspect`
3. **Los labels son obligatorios en producción:** No son opcionales
4. **El Skill es tu amigo:** Consulta cuando trabajes con compose
5. **El checklist salva vidas:** Úsalo siempre
6. **La plantilla AGENTS.md evoluciona:** Actualiza cuando aprendas algo nuevo

---

## 🚀 NEXT STEPS

**Ahora:**
1. Abre `PROMPT_CONSOLIDADO.md`
2. Lee secciones I-III
3. Ve el ejemplo en `docker-compose.yml`

**Después:**
1. Abre `.opencode/skills/docker-compose-production/SKILL.md`
2. Estudia tu caso específico (sección 9)
3. Copia template (sección 8)

**Luego:**
1. Personaliza para tu proyecto
2. Ejecuta checklist
3. Deploy

---

## 📞 SOPORTE

**Si tienes dudas:**
- Busca en PROMPT_CONSOLIDADO.md (Ctrl+F)
- Consulta tabla "Búsqueda Rápida por Necesidad" (arriba)
- Lee sección relevante del SKILL.md
- Revisa docker-compose.yml para ejemplo concreto

**Si encuentras un bug:**
- Documenta en issue
- Actualiza los archivos
- Comparte con el equipo

---

## 📈 EVOLUCIÓN DEL KIT

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0 | 2026-02-07 | Kit completo agnóstico inicial |

Próximas mejoras:
- [ ] Video tutorials
- [ ] Herramientas de validación automática
- [ ] Integración con CI/CD
- [ ] Casos de uso adicionales

---

## 🏁 RESUMEN EN UNA ORACIÓN

> **Lee PROMPT_CONSOLIDADO.md, copia AGENTS.md.template, crea docker-compose.yml con labels, valida con checklist, despliega.**

---

*Mapa de navegación del Kit Docker-Compose en Producción*  
*Generado: 2026-02-07*  
*Última actualización: 2026-02-07*