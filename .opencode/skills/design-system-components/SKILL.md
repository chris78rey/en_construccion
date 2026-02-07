---
name: design-system-components
description: Proporciona librería de componentes UI profesionales reutilizables con variables de diseño, paletas de colores, tipografía y patrones de componentes predefinidos para acelerar desarrollo sin escribir CSS desde cero.
license: MIT
---

# Skill: Design System & Componentes Reutilizables

## Propósito

Acelerar desarrollo UI/UX proporcionando:
- ✅ Sistema de diseño consistente (colores, tipografía, espaciado)
- ✅ Componentes HTML/Tailwind predefinidos profesionales
- ✅ Variables CSS y Tailwind config listos para usar
- ✅ Patrones de layout comunes
- ✅ Token-efficient (minimiza prompt engineering)

---

## Sección 1: Variables de Diseño (CSS Custom Properties)

### Paleta de Colores Primaria

```css
:root {
  /* Primarios - Da-Tica Brand */
  --color-primary: #0066cc;
  --color-primary-dark: #0052a3;
  --color-primary-light: #4d94ff;
  
  /* Secundarios */
  --color-secondary: #00d4aa;
  --color-secondary-dark: #00a88a;
  --color-secondary-light: #4dede8;
  
  /* Neutros */
  --color-neutral-50: #f9fafb;
  --color-neutral-100: #f3f4f6;
  --color-neutral-200: #e5e7eb;
  --color-neutral-300: #d1d5db;
  --color-neutral-400: #9ca3af;
  --color-neutral-500: #6b7280;
  --color-neutral-600: #4b5563;
  --color-neutral-700: #374151;
  --color-neutral-800: #1f2937;
  --color-neutral-900: #111827;
  
  /* Estados */
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
  --color-info: #3b82f6;
  
  /* Sombras */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  
  /* Espaciado */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 3rem;
  --spacing-3xl: 4rem;
  
  /* Tipografía */
  --font-family-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-mono: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
  
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;
  
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
  
  /* Border Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-2xl: 1rem;
  --radius-full: 9999px;
  
  /* Transiciones */
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-base: 200ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## Sección 2: Componentes HTML + Tailwind

### Botón Primario
```html
<button class="px-4 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 active:bg-blue-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
  Botón Primario
</button>
```

### Botón Secundario
```html
<button class="px-4 py-2 border-2 border-blue-600 text-blue-600 font-medium rounded-lg hover:bg-blue-50 active:bg-blue-100 transition-colors">
  Botón Secundario
</button>
```

### Botón Tertiary (Ghost)
```html
<button class="px-4 py-2 text-blue-600 font-medium rounded-lg hover:bg-blue-50 active:bg-blue-100 transition-colors">
  Botón Tertiary
</button>
```

### Input Text
```html
<input 
  type="text"
  class="w-full px-3 py-2 border border-neutral-300 rounded-lg font-base text-neutral-900 placeholder-neutral-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
  placeholder="Escribe aquí..."
/>
```

### Textarea
```html
<textarea
  class="w-full px-3 py-2 border border-neutral-300 rounded-lg font-base text-neutral-900 placeholder-neutral-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors resize-none"
  rows="4"
  placeholder="Escribe tu mensaje..."></textarea>
```

### Checkbox
```html
<label class="flex items-center gap-2 cursor-pointer">
  <input type="checkbox" class="w-4 h-4 accent-blue-600 rounded cursor-pointer" />
  <span class="text-neutral-900 font-medium">Aceptar términos</span>
</label>
```

### Radio Button
```html
<label class="flex items-center gap-2 cursor-pointer">
  <input type="radio" name="option" class="w-4 h-4 accent-blue-600 cursor-pointer" />
  <span class="text-neutral-900 font-medium">Opción 1</span>
</label>
```

### Select/Dropdown
```html
<select class="w-full px-3 py-2 border border-neutral-300 rounded-lg font-base text-neutral-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent">
  <option value="">Selecciona una opción</option>
  <option value="1">Opción 1</option>
  <option value="2">Opción 2</option>
</select>
```

### Tarjeta (Card)
```html
<div class="bg-white border border-neutral-200 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
  <h3 class="text-lg font-semibold text-neutral-900 mb-2">Título de Tarjeta</h3>
  <p class="text-neutral-600 text-sm mb-4">Descripción breve del contenido.</p>
  <button class="text-blue-600 font-medium text-sm hover:text-blue-700">Leer más →</button>
</div>
```

### Alert - Success
```html
<div class="bg-green-50 border-l-4 border-green-500 p-4 rounded">
  <div class="flex items-start gap-3">
    <svg class="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
    </svg>
    <div>
      <h3 class="text-green-900 font-semibold text-sm">¡Éxito!</h3>
      <p class="text-green-800 text-sm mt-1">Tu acción se completó correctamente.</p>
    </div>
  </div>
</div>
```

### Alert - Error
```html
<div class="bg-red-50 border-l-4 border-red-500 p-4 rounded">
  <div class="flex items-start gap-3">
    <svg class="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"/>
    </svg>
    <div>
      <h3 class="text-red-900 font-semibold text-sm">Error</h3>
      <p class="text-red-800 text-sm mt-1">Algo salió mal. Intenta nuevamente.</p>
    </div>
  </div>
</div>
```

### Badge
```html
<span class="inline-block px-3 py-1 bg-blue-100 text-blue-700 text-xs font-semibold rounded-full">
  Nuevo
</span>
```

### Spinner/Loading
```html
<div class="flex justify-center items-center">
  <div class="w-8 h-8 border-4 border-neutral-200 border-t-blue-600 rounded-full animate-spin"></div>
</div>
```

### Modal/Dialog
```html
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
  <div class="bg-white rounded-lg shadow-xl p-6 max-w-md w-full mx-4">
    <h2 class="text-xl font-bold text-neutral-900 mb-2">Título del Modal</h2>
    <p class="text-neutral-600 text-sm mb-6">Contenido descriptivo del modal.</p>
    <div class="flex gap-3">
      <button class="flex-1 px-4 py-2 border border-neutral-300 text-neutral-900 font-medium rounded-lg hover:bg-neutral-50">
        Cancelar
      </button>
      <button class="flex-1 px-4 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700">
        Confirmar
      </button>
    </div>
  </div>
</div>
```

### Tooltip
```html
<div class="relative group">
  <button class="text-neutral-500 hover:text-neutral-700">?</button>
  <div class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-3 py-2 bg-neutral-900 text-white text-xs rounded-md opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap">
    Texto del tooltip
  </div>
</div>
```

### Pagination
```html
<div class="flex items-center justify-center gap-1">
  <button class="px-3 py-2 border border-neutral-300 rounded-lg text-neutral-600 hover:bg-neutral-50">←</button>
  <button class="px-3 py-2 bg-blue-600 text-white rounded-lg font-medium">1</button>
  <button class="px-3 py-2 border border-neutral-300 rounded-lg text-neutral-600 hover:bg-neutral-50">2</button>
  <button class="px-3 py-2 border border-neutral-300 rounded-lg text-neutral-600 hover:bg-neutral-50">3</button>
  <button class="px-3 py-2 border border-neutral-300 rounded-lg text-neutral-600 hover:bg-neutral-50">→</button>
</div>
```

---

## Sección 3: Tailwind Config Recomendado

```javascript
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx,html}'],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f6ff',
          100: '#e0edff',
          500: '#0066cc',
          600: '#0052a3',
          700: '#003d7a',
        },
        secondary: {
          500: '#00d4aa',
          600: '#00a88a',
        },
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto'],
        mono: ['SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono'],
      },
      boxShadow: {
        sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        md: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
        lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
        xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1)',
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in',
        'slide-in': 'slideIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: { '0%': { opacity: '0' }, '100%': { opacity: '1' } },
        slideIn: { '0%': { transform: 'translateY(-10px)', opacity: '0' }, '100%': { transform: 'translateY(0)', opacity: '1' } },
      },
    },
  },
  plugins: [],
};
```

---

## Sección 4: Cómo Usar Este Skill

### Opción A: Pedir componente específico
**Tú:** "Dame el código HTML de un botón primario profesional."
**Yo:** Te doy el código del componente directamente (sin explicación larga).

### Opción B: Pedir paleta completa
**Tú:** "Necesito una paleta de colores profesional para mi proyecto."
**Yo:** Te doy las variables CSS Custom Properties listas para copiar/pegar.

### Opción C: Generar página completa con componentes
**Tú:** "Crea una página de login con email, password, recordar, y botón."
**Yo:** Automáticamente uso este skill para armar la página con componentes predefinidos.

---

## Sección 5: Checklist de Profesionalismo

Cada componente que proporcionó cumple:
- ✅ Focus states (accesibilidad)
- ✅ Hover/active states
- ✅ Transiciones suaves
- ✅ Responsive (mobile-first)
- ✅ Colores profesionales
- ✅ Espaciado consistente
- ✅ Tipografía legible

---

## Integración con Otros Skills

- Usa este skill cuando necesites componentes profesionales rápido
- No requiere explicación larga (token-efficient)
- Combina con `responsive-layout-snippets` para layouts completos
- Combina con `accessible-ui-patterns` para accesibilidad avanzada
