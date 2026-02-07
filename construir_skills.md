Para crear **Skills** en el entorno de **Oh My OpenCode (OMO)** —el framework de orquestación para OpenCode.ai— necesitas comprender tanto la estructura de archivos obligatoria como las herramientas de metaprogramación que ofrece el sistema.

Basado en la documentación técnica de OMO y OpenCode, aquí tienes los requisitos y pasos exactos para desarrollar y operar skills.

### 1. El Requisito Fundamental: El Archivo `SKILL.md`

A diferencia de las herramientas ejecutables ("Tools" en TypeScript), un **Skill** es una unidad de conocimiento procedimental encapsulada en un archivo Markdown. Para crear uno, necesitas crear un archivo `SKILL.md` que contenga obligatoriamente dos secciones:

*   **Frontmatter YAML:** Metadatos al inicio del archivo para que el agente sepa cómo y cuándo usarlo.
*   **Cuerpo Markdown:** Las instrucciones en lenguaje natural.

**Estructura de ejemplo:**
```markdown
---
name: refactor-solid
description: Aplica principios SOLID para refactorizar clases.
license: MIT
---

# Guía de Refactorización
...instrucciones paso a paso...
```
,

### 2. Ubicación y "Routing" (Dónde guardarlos)

Para que OMO reconozca tu skill, debes colocarlo en una estructura de directorios específica. El sistema usa un algoritmo de "Walk-Up" (escaneo jerárquico), buscando en las siguientes rutas (de mayor a menor prioridad):

1.  **Nivel Proyecto (Local):** En la raíz de tu repositorio actual:
    *   `.opencode/skills/<nombre-del-skill>/SKILL.md`
    *   `.agents/skills/<nombre-del-skill>/SKILL.md`
2.  **Nivel Usuario (Global):** En tu carpeta de usuario:
    *   `~/.config/opencode/skills/<nombre-del-skill>/SKILL.md`
    *   `~/.agents/skills/<nombre-del-skill>/SKILL.md`

**Nota Importante:** OMO es compatible con el ecosistema de Anthropic, por lo que también detectará skills guardados en carpetas `.claude/skills`,.

### 3. Reglas Críticas de Validación

Para que el skill funcione y no sea ignorado silenciosamente por el sistema, debes cumplir estas reglas estrictas:

*   **Coincidencia de Nombre:** El campo `name` en el YAML debe ser **idéntico** al nombre de la carpeta que contiene el archivo.
*   **Sintaxis del Nombre:** Solo se permiten letras minúsculas, números y guiones simples. Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`. Nombres como `RefactorCode` (con mayúsculas) o `refactor_code` (guion bajo) fallarán.
*   **Descripción Semántica:** La `description` en el YAML es vital. El agente no carga todo el skill en su memoria; solo lee la descripción. Si es vaga ("ayuda con código"), el agente nunca invocará el skill. Debe ser específica (ej. "Genera mensajes de commit siguiendo la convención Angular"),.

### 4. ¿Puedo construir un Skill usando otro Skill? (Metaprogramación)

**Sí, absolutamente.** Esta es una de las características más potentes de OMO.

Respondiendo a tu consulta sobre si *"con un skill puedo construir otra skills en omo"*: OMO está diseñado para la **metaprogramación**. El sistema posee flujos de trabajo nativos para que el agente escriba sus propias habilidades:

*   **Herramienta `question`:** OMO utiliza una herramienta llamada `question` para "entrevistarte". Si el agente detecta que haces una tarea repetitiva, puede proponerte crear un skill. Te hará preguntas para definir los requisitos y luego usará la herramienta `write` para generar automáticamente el directorio y el archivo `SKILL.md` con la metadata correcta.
*   **Modo Ultrawork (ulw):** Puedes usar el modo de paralelismo cognitivo. Mientras el agente principal (Sisyphus) trabaja en código, un agente en segundo plano puede leer documentación nueva y generar un skill resumen para que el agente principal lo use más tarde.
*   **Comando `/init`:** Al ejecutar este comando en un proyecto nuevo, el agente analiza la estructura y genera un archivo `AGENTS.md`, que actúa como memoria a largo plazo y base para futuros skills del proyecto.

### 5. Activación y Uso

Una vez creado el archivo, no necesitas un comando de importación. El sistema usa "carga bajo demanda" (lazy loading):
1.  El sistema inyecta la descripción del skill en el prompt del sistema.
2.  Cuando pides algo relacionado (ej. "Refactoriza esto"), el agente decide autónomamente invocar `skill({ name: "tu-skill" })`.
3.  También puedes forzarlo explícitamente diciendo: "Usa el skill de refactorización".

### Resumen de lo que necesitas:
1.  **Editor de texto** o terminal.
2.  Crear la carpeta `.opencode/skills/nombre-skill/`.
3.  Crear `SKILL.md` con **Frontmatter YAML** válido.
4.  *(Opcional pero recomendado)* Usar el propio agente de OMO para que escriba el skill por ti mediante el flujo de "entrevista".
