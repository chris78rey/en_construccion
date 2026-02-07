---
name: responsive-layout-snippets
description: Proporciona snippets de layout responsive profesionales (grid, flexbox, mobile-first) listos para copiar y pegar, sin necesidad de escribir CSS desde cero.
license: MIT
---

# Skill: Snippets de Layout Responsive

## Propósito

Ofrecer **patrones de layout profesionales y probados** que puedes copiar directamente sin escribir CSS custom. Utiliza Tailwind CSS para máxima velocidad y consistencia.

---

## 1. Hero Section (Banner Principal)

### Versión Simple
```html
<!-- Hero con texto + CTA -->
<section class="min-h-screen bg-gradient-to-br from-slate-900 to-slate-800 flex items-center justify-center text-center px-4">
  <div class="max-w-2xl mx-auto">
    <h1 class="text-5xl md:text-7xl font-bold text-white mb-4">
      Tu Título Aquí
    </h1>
    <p class="text-xl md:text-2xl text-slate-300 mb-8">
      Descripción breve y atractiva
    </p>
    <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg transition duration-200">
      Call to Action
    </button>
  </div>
</section>
```

### Versión con Imagen
```html
<section class="min-h-screen grid grid-cols-1 md:grid-cols-2 gap-8 items-center px-4 md:px-8 max-w-6xl mx-auto">
  <!-- Texto -->
  <div>
    <h1 class="text-5xl md:text-6xl font-bold text-slate-900 mb-4">
      Solución Profesional
    </h1>
    <p class="text-lg text-slate-600 mb-6">
      Descripción detallada de beneficios
    </p>
    <button class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg">
      Comenzar Ahora
    </button>
  </div>
  <!-- Imagen -->
  <div class="hidden md:block">
    <img src="hero-image.png" alt="Hero" class="w-full rounded-lg shadow-lg" />
  </div>
</section>
```

---

## 2. Navbar (Navegación)

### Navbar Sticky Simple
```html
<nav class="sticky top-0 z-50 bg-white shadow-md">
  <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
    <!-- Logo -->
    <div class="text-2xl font-bold text-blue-600">
      Logo
    </div>
    
    <!-- Menu -->
    <div class="hidden md:flex gap-8">
      <a href="#" class="text-slate-700 hover:text-blue-600 transition">Inicio</a>
      <a href="#" class="text-slate-700 hover:text-blue-600 transition">Servicios</a>
      <a href="#" class="text-slate-700 hover:text-blue-600 transition">Contacto</a>
    </div>
    
    <!-- Mobile Menu Icon -->
    <button class="md:hidden text-slate-700">
      ☰
    </button>
  </div>
</nav>
```

---

## 3. Card Grid (Tarjetas en Grid)

### 3 Columnas Responsive
```html
<section class="max-w-6xl mx-auto px-4 py-12">
  <h2 class="text-4xl font-bold text-center mb-12">Nuestros Servicios</h2>
  
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Card -->
    <div class="bg-white rounded-lg shadow-md hover:shadow-lg transition p-6">
      <div class="text-4xl mb-4">🚀</div>
      <h3 class="text-xl font-bold text-slate-900 mb-2">Titulo Servicio</h3>
      <p class="text-slate-600 mb-4">
        Descripción breve del servicio
      </p>
      <a href="#" class="text-blue-600 font-semibold hover:underline">
        Más info →
      </a>
    </div>
    
    <!-- Repetir para más cards -->
  </div>
</section>
```

---

## 4. Dos Columnas (50/50)

### Layout Equilibrado
```html
<section class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-6xl mx-auto px-4 py-12">
  <!-- Columna 1 -->
  <div>
    <h2 class="text-3xl font-bold text-slate-900 mb-4">Título Columna 1</h2>
    <p class="text-slate-600 mb-4">Contenido aquí</p>
  </div>
  
  <!-- Columna 2 -->
  <div>
    <h2 class="text-3xl font-bold text-slate-900 mb-4">Título Columna 2</h2>
    <p class="text-slate-600 mb-4">Contenido aquí</p>
  </div>
</section>
```

---

## 5. Feature List (Lista de Características)

### Con Checkmarks
```html
<section class="max-w-4xl mx-auto px-4 py-12">
  <h2 class="text-4xl font-bold text-center mb-12">Características</h2>
  
  <ul class="space-y-4">
    <li class="flex items-start gap-3">
      <span class="text-green-600 font-bold text-lg mt-1">✓</span>
      <div>
        <h4 class="font-bold text-slate-900">Característica 1</h4>
        <p class="text-slate-600 text-sm">Descripción breve</p>
      </div>
    </li>
    <!-- Repetir -->
  </ul>
</section>
```

---

## 6. Testimonios (Carrusel Simple)

### Cards Estáticas (sin JS)
```html
<section class="bg-slate-50 py-12 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-4xl font-bold text-center mb-12">Testimonios</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <!-- Testimonio -->
      <div class="bg-white rounded-lg p-6 shadow-md">
        <div class="flex gap-1 mb-4">
          <span class="text-yellow-400">★</span>
          <span class="text-yellow-400">★</span>
          <span class="text-yellow-400">★</span>
          <span class="text-yellow-400">★</span>
          <span class="text-yellow-400">★</span>
        </div>
        <p class="text-slate-600 italic mb-4">
          "Testimonio del cliente aquí"
        </p>
        <p class="font-bold text-slate-900">Nombre Cliente</p>
        <p class="text-sm text-slate-500">Cargo/Empresa</p>
      </div>
      <!-- Repetir -->
    </div>
  </div>
</section>
```

---

## 7. Contact Form (Formulario)

### Formulario Limpio
```html
<section class="max-w-2xl mx-auto px-4 py-12">
  <h2 class="text-4xl font-bold text-center mb-8">Contacto</h2>
  
  <form class="space-y-6">
    <!-- Nombre -->
    <div>
      <label class="block text-sm font-semibold text-slate-900 mb-2">
        Nombre Completo
      </label>
      <input 
        type="text" 
        placeholder="Tu nombre" 
        class="w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
      />
    </div>
    
    <!-- Email -->
    <div>
      <label class="block text-sm font-semibold text-slate-900 mb-2">
        Email
      </label>
      <input 
        type="email" 
        placeholder="tu@email.com" 
        class="w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
      />
    </div>
    
    <!-- Mensaje -->
    <div>
      <label class="block text-sm font-semibold text-slate-900 mb-2">
        Mensaje
      </label>
      <textarea 
        placeholder="Tu mensaje..." 
        rows="5"
        class="w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
      ></textarea>
    </div>
    
    <!-- Botón -->
    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition">
      Enviar
    </button>
  </form>
</section>
```

---

## 8. Footer (Pie de Página)

### Footer Profesional
```html
<footer class="bg-slate-900 text-white py-12 px-4">
  <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
    <!-- Logo -->
    <div>
      <h3 class="text-2xl font-bold mb-4">Logo</h3>
      <p class="text-slate-400">Descripción breve de la empresa</p>
    </div>
    
    <!-- Links 1 -->
    <div>
      <h4 class="font-bold mb-4">Producto</h4>
      <ul class="space-y-2 text-slate-400">
        <li><a href="#" class="hover:text-white">Características</a></li>
        <li><a href="#" class="hover:text-white">Precios</a></li>
        <li><a href="#" class="hover:text-white">Seguridad</a></li>
      </ul>
    </div>
    
    <!-- Links 2 -->
    <div>
      <h4 class="font-bold mb-4">Empresa</h4>
      <ul class="space-y-2 text-slate-400">
        <li><a href="#" class="hover:text-white">Nosotros</a></li>
        <li><a href="#" class="hover:text-white">Blog</a></li>
        <li><a href="#" class="hover:text-white">Contacto</a></li>
      </ul>
    </div>
    
    <!-- Links 3 -->
    <div>
      <h4 class="font-bold mb-4">Legal</h4>
      <ul class="space-y-2 text-slate-400">
        <li><a href="#" class="hover:text-white">Privacidad</a></li>
        <li><a href="#" class="hover:text-white">Términos</a></li>
        <li><a href="#" class="hover:text-white">Cookies</a></li>
      </ul>
    </div>
  </div>
  
  <!-- Copyright -->
  <div class="border-t border-slate-700 pt-8 text-center text-slate-400">
    <p>&copy; 2024 Tu Empresa. Todos los derechos reservados.</p>
  </div>
</footer>
```

---

## 9. Pricing Table (Tabla de Precios)

### 3 Planes
```html
<section class="max-w-6xl mx-auto px-4 py-12">
  <h2 class="text-4xl font-bold text-center mb-12">Planes de Precios</h2>
  
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    <!-- Plan 1 -->
    <div class="border border-slate-200 rounded-lg p-8 text-center">
      <h3 class="text-2xl font-bold mb-2">Básico</h3>
      <p class="text-4xl font-bold text-blue-600 mb-6">$9<span class="text-lg text-slate-600">/mes</span></p>
      <ul class="space-y-3 text-slate-600 mb-8 text-left">
        <li>✓ Característica 1</li>
        <li>✓ Característica 2</li>
        <li>✓ Característica 3</li>
      </ul>
      <button class="w-full border-2 border-blue-600 text-blue-600 font-bold py-3 rounded-lg hover:bg-blue-50">
        Comenzar
      </button>
    </div>
    
    <!-- Plan 2 (Destacado) -->
    <div class="border-2 border-blue-600 rounded-lg p-8 text-center bg-blue-50">
      <div class="bg-blue-600 text-white px-4 py-1 rounded-full inline-block mb-4 text-sm font-bold">
        POPULAR
      </div>
      <h3 class="text-2xl font-bold mb-2">Profesional</h3>
      <p class="text-4xl font-bold text-blue-600 mb-6">$29<span class="text-lg text-slate-600">/mes</span></p>
      <ul class="space-y-3 text-slate-600 mb-8 text-left">
        <li>✓ Todo en Básico</li>
        <li>✓ Característica 4</li>
        <li>✓ Característica 5</li>
      </ul>
      <button class="w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700">
        Comenzar
      </button>
    </div>
    
    <!-- Plan 3 -->
    <div class="border border-slate-200 rounded-lg p-8 text-center">
      <h3 class="text-2xl font-bold mb-2">Empresarial</h3>
      <p class="text-4xl font-bold text-blue-600 mb-6">Personalizado</p>
      <ul class="space-y-3 text-slate-600 mb-8 text-left">
        <li>✓ Todo en Profesional</li>
        <li>✓ Soporte dedicado</li>
        <li>✓ SLA Garantizado</li>
      </ul>
      <button class="w-full border-2 border-blue-600 text-blue-600 font-bold py-3 rounded-lg hover:bg-blue-50">
        Contactar
      </button>
    </div>
  </div>
</section>
```

---

## 10. Stats Section (Números/Métricas)

### 4 Columnas
```html
<section class="bg-blue-600 text-white py-12 px-4">
  <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 text-center">
    <div>
      <p class="text-5xl font-bold mb-2">10K+</p>
      <p class="text-blue-100">Usuarios Activos</p>
    </div>
    <div>
      <p class="text-5xl font-bold mb-2">99%</p>
      <p class="text-blue-100">Uptime</p>
    </div>
    <div>
      <p class="text-5xl font-bold mb-2">24/7</p>
      <p class="text-blue-100">Soporte</p>
    </div>
    <div>
      <p class="text-5xl font-bold mb-2">150+</p>
      <p class="text-blue-100">Integraciones</p>
    </div>
  </div>
</section>
```

---

## 11. Modal / Dialog

### Modal Simple
```html
<!-- Backdrop -->
<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
  <!-- Modal -->
  <div class="bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
    <!-- Header -->
    <div class="border-b border-slate-200 px-6 py-4 flex justify-between items-center">
      <h2 class="text-xl font-bold text-slate-900">Título Modal</h2>
      <button class="text-slate-500 hover:text-slate-700">✕</button>
    </div>
    
    <!-- Body -->
    <div class="px-6 py-4">
      <p class="text-slate-600">
        Contenido del modal aquí
      </p>
    </div>
    
    <!-- Footer -->
    <div class="border-t border-slate-200 px-6 py-4 flex gap-3 justify-end">
      <button class="px-4 py-2 border border-slate-300 rounded-lg hover:bg-slate-50">
        Cancelar
      </button>
      <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
        Aceptar
      </button>
    </div>
  </div>
</div>
```

---

## 12. Accordion (Acordeón)

### Lista Expandible
```html
<section class="max-w-2xl mx-auto px-4 py-12">
  <h2 class="text-3xl font-bold mb-8">Preguntas Frecuentes</h2>
  
  <div class="space-y-4">
    <!-- Item -->
    <details class="border border-slate-200 rounded-lg">
      <summary class="px-6 py-4 font-semibold text-slate-900 cursor-pointer hover:bg-slate-50">
        ¿Cómo funciona?
      </summary>
      <div class="px-6 py-4 border-t border-slate-200 text-slate-600">
        Respuesta aquí
      </div>
    </details>
    
    <!-- Item -->
    <details class="border border-slate-200 rounded-lg">
      <summary class="px-6 py-4 font-semibold text-slate-900 cursor-pointer hover:bg-slate-50">
        ¿Cuál es el precio?
      </summary>
      <div class="px-6 py-4 border-t border-slate-200 text-slate-600">
        Respuesta aquí
      </div>
    </details>
  </div>
</section>
```

---

## Cómo Usar Este Skill

### Opción 1: Copiar y Pegar
```
Tú: "Necesito una tarjeta de servicio con descripción y enlace"

Yo: [Te doy el snippet #3 - Card Grid]
    Solo copias, cambias texto, ¡listo!
```

### Opción 2: Combinador
```
Tú: "Crea una página de landing con hero + features + footer"

Yo: [Combino snippets #1 + #5 + #8 en un HTML completo]
```

### Opción 3: Adaptación Rápida
```
Tú: "Necesito 4 columnas en lugar de 3"

Yo: [Cambio "lg:grid-cols-3" a "lg:grid-cols-4" automáticamente]
```

---

## Ventajas de Este Skill

✅ **Sin escribir CSS custom** - Todo es Tailwind  
✅ **Mobile-first** - Responsive automático  
✅ **Token eficiente** - Copiar/pegar, sin explicaciones largas  
✅ **Profesional** - Diseños ya validados  
✅ **Rápido** - Segundos en lugar de horas  
✅ **Combinable** - Mezcla snippets fácilmente  

---

## Colores Profesionales Usados

```css
Fondos: slate-50, white, slate-900, blue-600
Texto: slate-900, slate-600, slate-400
Acentos: blue-600, green-600, yellow-400
Bordes: slate-200, slate-300
Sombras: shadow-md, shadow-lg (naturales)
```

---

## Checklist Rápido

- [ ] ¿El layout es responsive? (grid + md/lg breakpoints)
- [ ] ¿Funciona en mobile? (prueba con 375px)
- [ ] ¿Tiene buena accesibilidad? (semántico HTML)
- [ ] ¿Los colores contrastan? (WCAG AA mínimo)
- [ ] ¿Las tipografías son legibles? (16px+ base)
