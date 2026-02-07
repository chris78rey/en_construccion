---
name: professional-ui-guidelines
description: Proporciona guías de UI/UX profesionales listas para aplicar inmediatamente, incluyendo paletas de color, tipografía, espaciado y componentes estándar sin necesidad de explicaciones detalladas.
license: MIT
---

# Skill: Guías Profesionales de UI/UX

## Propósito

Proporcionar **directrices listas para aplicar** sin explicaciones extensas. Cuando pidas "UI profesional", obtienes configuración completa lista para copiar y pegar.

---

## 1. PALETAS DE COLOR (Pre-diseñadas)

### Paleta Corporativa Minimalista (Recomendada)
```
Primary: #0f172a (Azul oscuro profesional)
Secondary: #1e293b (Gris azulado)
Accent: #3b82f6 (Azul brillante)
Success: #10b981 (Verde esmeralda)
Warning: #f59e0b (Ámbar)
Error: #ef4444 (Rojo claro)
Background: #ffffff (Blanco)
Surface: #f8fafc (Gris muy claro)
Text: #0f172a (Azul oscuro)
TextSecondary: #64748b (Gris azulado)
Border: #e2e8f0 (Gris claro)
```

### Paleta Moderna Tech
```
Primary: #1f2937 (Gris oscuro)
Secondary: #374151 (Gris medio)
Accent: #06b6d4 (Cyan)
Success: #14b8a6 (Teal)
Warning: #eab308 (Amarillo)
Error: #f43f5e (Rosa)
Background: #0f172a (Azul oscuro)
Surface: #1e293b (Azul gris)
Text: #f1f5f9 (Blanco gris)
TextSecondary: #cbd5e1 (Gris claro)
Border: #334155 (Gris oscuro)
```

### Paleta Creative/Startup
```
Primary: #7c3aed (Púrpura)
Secondary: #ec4899 (Rosa)
Accent: #f59e0b (Ámbar)
Success: #8b5cf6 (Púrpura claro)
Warning: #fb923c (Naranja)
Error: #f87171 (Rojo claro)
Background: #ffffff (Blanco)
Surface: #fafafa (Gris muy claro)
Text: #1f2937 (Gris oscuro)
TextSecondary: #6b7280 (Gris)
Border: #e5e7eb (Gris claro)
```

---

## 2. TIPOGRAFÍA PROFESIONAL

### Stack Tipográfico
```
Fuentes recomendadas:
- Headings: "Inter", "Helvetica Neue", sans-serif
- Body: "Segoe UI", "Roboto", sans-serif
- Mono: "Monaco", "Courier New", monospace

Tamaños y pesos:
H1: 36px / 700 / 1.2 line-height
H2: 28px / 700 / 1.3 line-height
H3: 24px / 600 / 1.4 line-height
H4: 20px / 600 / 1.5 line-height
Body: 16px / 400 / 1.6 line-height
Small: 14px / 400 / 1.5 line-height
Caption: 12px / 400 / 1.4 line-height
```

---

## 3. ESPACIADO Y GEOMETRÍA

### Escala de Espaciado
```
xs: 4px
sm: 8px
md: 16px
lg: 24px
xl: 32px
2xl: 48px
3xl: 64px

Border Radius:
sm: 4px
md: 8px
lg: 12px
xl: 16px
full: 9999px

Elevación (Shadows):
sm: 0 1px 2px 0 rgba(0,0,0,0.05)
md: 0 4px 6px -1px rgba(0,0,0,0.1)
lg: 0 10px 15px -3px rgba(0,0,0,0.1)
xl: 0 20px 25px -5px rgba(0,0,0,0.1)
```

---

## 4. COMPONENTES ESTÁNDAR (Definiciones Rápidas)

### Botones
```
Primary Button:
- bg: #3b82f6
- text: white
- padding: 10px 16px
- border-radius: 8px
- font-weight: 600
- min-width: 120px
- hover: brightness(1.1)

Secondary Button:
- bg: #e2e8f0
- text: #0f172a
- padding: 10px 16px
- border: 1px solid #cbd5e1
- border-radius: 8px
- font-weight: 600
- hover: bg-#f1f5f9

Outline Button:
- bg: transparent
- border: 2px solid #3b82f6
- text: #3b82f6
- padding: 8px 16px
- border-radius: 8px
- hover: bg: rgba(59,130,246,0.1)
```

### Inputs
```
Text Input:
- width: 100%
- padding: 10px 12px
- border: 1px solid #cbd5e1
- border-radius: 6px
- font: 16px / 400
- transition: border 0.2s
- focus: border #3b82f6 + outline-none + box-shadow
- placeholder: #94a3b8

Textarea:
- same as input
- min-height: 120px
- resize: vertical
- font-family: inherit

Select/Dropdown:
- same as input
- appearance: none
- padding-right: 32px (para arrow icon)
- cursor: pointer
```

### Cards
```
Card:
- bg: white
- border: 1px solid #e2e8f0
- border-radius: 12px
- padding: 24px
- box-shadow: sm (0 1px 2px)
- hover: shadow-md + border-#cbd5e1

Card Header:
- padding: 0 0 16px 0
- border-bottom: 1px solid #f1f5f9
- font-size: 20px
- font-weight: 600

Card Content:
- padding: 16px 0

Card Footer:
- padding: 16px 0 0 0
- border-top: 1px solid #f1f5f9
- text-align: right
```

### Navigation
```
Navbar:
- bg: white
- border-bottom: 1px solid #e2e8f0
- height: 64px
- padding: 0 24px
- position: sticky / fixed
- z-index: 1000
- box-shadow: sm

NavItem:
- padding: 8px 16px
- color: #64748b
- font-weight: 500
- border-bottom: 3px solid transparent
- cursor: pointer
- hover: color #0f172a + border-bottom #3b82f6
- active: color #0f172a + border-bottom #3b82f6
```

### Badges
```
Badge:
- display: inline-flex
- padding: 4px 12px
- border-radius: 12px
- font-size: 12px
- font-weight: 600

Variants:
Success: bg-#d1fae5 text-#065f46
Warning: bg-#fef3c7 text-#92400e
Error: bg-#fee2e2 text--#991b1b
Info: bg-#dbeafe text--#0c2340
```

### Modals/Dialogs
```
Modal Overlay:
- position: fixed
- inset: 0
- bg: rgba(0,0,0,0.5)
- z-index: 2000

Modal Container:
- position: fixed
- top: 50%
- left: 50%
- transform: translate(-50%, -50%)
- bg: white
- border-radius: 12px
- max-width: 500px
- width: 90%
- z-index: 2001
- box-shadow: xl
- animation: fadeIn 0.2s

Modal Header:
- padding: 24px
- border-bottom: 1px solid #e2e8f0
- font-size: 20px
- font-weight: 600
- display: flex
- justify-content: space-between

Modal Body:
- padding: 24px
- max-height: 60vh
- overflow-y: auto

Modal Footer:
- padding: 24px
- border-top: 1px solid #e2e8f0
- text-align: right
- gap: 12px
```

---

## 5. PATRONES DE LAYOUT

### Container Responsivo
```
Max-width breakpoints:
- sm: 640px (mobile)
- md: 768px (tablet)
- lg: 1024px (laptop)
- xl: 1280px (desktop)
- 2xl: 1536px (ultra-wide)

Padding by breakpoint:
- mobile: 16px horizontal
- tablet: 20px horizontal
- desktop: 24px horizontal
```

### Grid Profesional
```
12-column grid:
- mobile: 1 column
- tablet: 2 columns
- desktop: 3-4 columns

Gutter: 16px-24px (responde a tamaño)

Card grid:
- max-width: 1200px
- auto-fit columns
- min-width: 300px (cards)
- gap: 24px
```

### Hero Section
```
Min-height: 60vh-100vh
Padding: 80px 24px (vertical)
Background: gradient o imagen
Text align: center
Headline: H1 + bold
Subheadline: Body + secondary color
CTA: Primary button centered
```

---

## 6. EFECTOS Y MICRO-INTERACCIONES

### Transitions Estándar
```
Button/Link hover: 0.2s ease
Color change: 0.15s ease
Width/Height: 0.3s ease-out
Opacity: 0.2s ease
Transform: 0.2s ease-out
All: 0.2s ease (default)
```

### Loading States
```
Skeleton: bg: #f1f5f9 + animate-pulse
Spinner: 24px circle / border 2px / animated
Progress bar: height 4px / bg-gradient / animated

Loading animation:
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

### Hover States
```
Button: brightness(1.1) / shadow-md / scale(1.02)
Link: color change + underline
Card: shadow-lg / border-primary / scale(1.02)
Form: border-primary + shadow-sm
```

---

## 7. MODO OSCURO (Dark Mode)

### Mapeo de Colores
```
Light → Dark:
White (#fff) → #0f172a (azul oscuro)
#f8fafc → #1e293b (azul gris)
#e2e8f0 → #334155 (gris oscuro)
#0f172a → #f1f5f9 (blanco gris)
#64748b → #cbd5e1 (gris claro)

Aplicar con:
@media (prefers-color-scheme: dark)
o clase .dark-mode en root
o CSS variables
```

---

## 8. ACCESIBILIDAD MÍNIMA

### Contraste
```
Normal text: 4.5:1
Large text: 3:1
UI components: 3:1

Verificar en: webaim.org/resources/contrastchecker
```

### Focus States
```
a, button, input:focus {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}
```

### Keyboard Navigation
```
Tab order: natural / logical
Focus visible: siempre visible
Hover = Focus: mismos estilos
```

---

## CÓMO USAR ESTE SKILL

### Opción 1: Copiar Paleta Completa
```
Tú: "Dame una paleta profesional"
Yo: Copias "Paleta Corporativa Minimalista" y usas en proyecto
Tokens: ~100 (muy eficiente)
```

### Opción 2: Pedir Componente Específico
```
Tú: "Dame definición de botón primario profesional"
Yo: Copias especificación de "Buttons → Primary Button"
Tokens: ~50
```

### Opción 3: Aplicar a Framework Específico
```
Tú: "Aplica estas guías a Tailwind"
Yo: Convierto a clases Tailwind (tema aparte)
Tokens: ~200
```

---

## INTEGRACIÓN RÁPIDA

### Con CSS Variables
```css
:root {
  --primary: #0f172a;
  --secondary: #1e293b;
  --accent: #3b82f6;
  --success: #10b981;
  --warning: #f59e0b;
  --error: #ef4444;
  --bg: #ffffff;
  --surface: #f8fafc;
  --text: #0f172a;
  --text-secondary: #64748b;
  --border: #e2e8f0;
  
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  --shadow-sm: 0 1px 2px 0 rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
}
```

### Con Tailwind Config
```js
module.exports = {
  theme: {
    colors: {
      primary: '#0f172a',
      secondary: '#1e293b',
      accent: '#3b82f6',
      success: '#10b981',
      warning: '#f59e0b',
      error: '#ef4444',
    },
    spacing: {
      xs: '4px',
      sm: '8px',
      md: '16px',
      lg: '24px',
      xl: '32px',
    },
    borderRadius: {
      sm: '4px',
      md: '8px',
      lg: '12px',
    }
  }
}
```

---

## CHECKLIST PROFESIONAL

Antes de considerar UI "lista":
- [ ] Paleta de 6-8 colores consistente
- [ ] Tipografía: máximo 2 familias
- [ ] Espaciado: basado en escala
- [ ] Contraste: 4.5:1 mínimo
- [ ] Radios: consistentes por tipo
- [ ] Sombras: sutiles y profesionales
- [ ] Transiciones: suaves 0.2s-0.3s
- [ ] Hover/Focus: visibles y consistentes
- [ ] Responsivo: testeado en 3 breakpoints
- [ ] Dark mode: (opcional pero recomendado)

---

## TOKENS AHORRADOS

Este skill está diseñado para **minimizar explicaciones verbosas**:
- ❌ NO describo por qué cada color
- ❌ NO explico teoría de diseño
- ❌ NO repito definiciones
- ✅ SOLO copiar y pegar
- ✅ SOLO números y valores
- ✅ SOLO aplicar

**Cada consulta: ~50-150 tokens (vs 500-1000 sin este skill)**