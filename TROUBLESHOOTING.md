# 🔧 TROUBLESHOOTING GUIDE

**Fecha:** 2026-02-07  
**Framework:** Alpine.js 3.x (CDN)  
**Archivo:** `web/index.html`

---

## ❌ PROBLEMA: Acordeones no funcionan

### Síntomas:
- Click en tarjeta "El Triángulo de la Crisis" no expande
- Las tarjetas no responden a clicks
- No hay animación

### Diagnóstico:

**1. Verifica que Alpine.js esté cargado:**
```javascript
// En Browser Console (F12):
typeof Alpine
// Debería retornar: "object"
// Si retorna "undefined" → Alpine no cargó
```

**2. Verifica atributo x-data:**
```bash
cd en_construccion
grep -n 'x-data="painPointsAccordion' web/index.html
# Debería retornar: una línea con el contenedor
```

**3. Verifica estructura HTML:**
```bash
grep -A 5 'pain-grid' web/index.html
# Debería mostrar: x-data y acordeones
```

### Soluciones:

**Si Alpine.js no cargó:**
```html
<!-- Línea 9-10 debería ser: -->
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
<!-- Verifica que NO hay errores de CORS -->
```

**Si hay error de CORS en Console:**
- El CDN está bloqueado
- Solución: Descarga Alpine.js localmente
```bash
# Descarga en web/ directory
wget https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js -O web/alpine.min.js

# Modifica referencia en HTML:
<script defer src="./alpine.min.js"></script>
```

**Si la estructura HTML está mal:**
- Revisa línea 594: debe tener `x-data="painPointsAccordion()"`
- Revisa línea 595-653: debe tener `x-bind:class="{ 'active': openAccordion === N }"`
- Si faltan atributos, agregalos manualmente

**Si hay error en Console:**
```
Uncaught ReferenceError: painPointsAccordion is not defined
```
- Solución: Verifica que función existe en línea 1027
- Si no existe, agrega:
```javascript
function painPointsAccordion() {
    return {
        openAccordion: 0,
    };
}
```

---

## ❌ PROBLEMA: Modales no abren

### Síntomas:
- Click en "Ver Detalles" no abre modal
- Modal abre pero no cierra
- Modal aparece off-screen

### Diagnóstico:

**1. Verifica atributo x-data en section:**
```bash
grep -n 'x-data="servicesModals' web/index.html
# Debe estar en línea ~766
```

**2. Verifica @click en botones:**
```bash
grep -n '@click="openModal' web/index.html
# Debe haber 4 coincidencias (uno por servicio)
```

**3. Verifica estructura modal:**
```bash
grep -n 'x-show="activeModal ===' web/index.html
# Debe haber 4 coincidencias (uno por modal)
```

### Soluciones:

**Si modales no abren:**
- Verifica que cada botón tiene `@click="openModal('X')"`
- Valores deben ser: 'modernization', 'latency', 'ai', 'audit'
- Verifica que cada modal tiene `x-show="activeModal === 'X'"`

**Si modales se abren pero no aparecen:**
- Revisa CSS en línea 291-315 (`.modal-overlay`, `.modal`)
- Verifica que no hay `display: none` en styles inline
- Abre DevTools (F12) → Elements → busca `.modal-overlay`
- Debe tener `position: fixed; inset: 0; z-index: 200`

**Si X para cerrar no funciona:**
- Verifica que existe botón `.modal-close` dentro del modal
- Verifica que tiene `@click="activeModal = null"`
- Ejemplo línea 812, 835, 858, 881

**Si click fuera del modal no cierra:**
- Verifica que `.modal-overlay` tiene `@click.self="activeModal = null"`
- `@click.self` es importante (solo cierra si click ES en overlay, no en modal)

---

## ❌ PROBLEMA: Calculadora ROI no funciona

### Síntomas:
- Sliders no responden
- Números no se actualizan
- Calculadora no aparece

### Diagnóstico:

**1. Verifica atributo x-data en CFO tab:**
```bash
grep -n 'x-data="roiCalculator' web/index.html
# Debe estar en línea ~697
```

**2. Verifica botón toggle:**
```bash
grep -n 'showCalculator = !showCalculator' web/index.html
# Debe haber 1 coincidencia
```

**3. Verifica sliders:**
```bash
grep -n 'x-model.number' web/index.html
# Debe haber 3 coincidencias (3 sliders)
```

### Soluciones:

**Si calculadora no aparece:**
- Tab CFO debe estar visible (click en "Soy CFO")
- Click en "Abrir Calculadora ROI" 
- Verifica que existe `<div class="calculator-container" x-show="showCalculator">`

**Si sliders no funcionan:**
```javascript
// Verifica en Console:
Alpine.store('roiCalculator')
// O busca valores manualmente
```
- Cada slider debe tener: `x-model.number="currentCost"` (etc)
- Cada slider debe tener: `@input="recalculate()"`
- min, max, step deben ser números válidos

**Si números no se actualizan:**
- Verifica que existen `x-text="formatCurrency(currentCost)"` (etc)
- Verifica que función `formatCurrency()` existe en línea 1059+
- Verifica que método `recalculate()` se llama al cambiar sliders

**Si hay error en formato de moneda:**
```javascript
// En Console:
new Intl.NumberFormat('es-ES', {
    style: 'currency',
    currency: 'USD',
}).format(2500000)
// Debe retornar: "2.500.000,00 US$" (formato español)
```

---

## ❌ PROBLEMA: Animaciones no funcionan

### Síntomas:
- Tarjetas servicios no animan al scroll
- Contadores de métricas no cuentan
- Animaciones saltan sin suavidad

### Diagnóstico:

**1. Verifica clase fade-in-up:**
```bash
grep -c 'class="card fade-in-up' web/index.html
# Debe retornar: 4 (uno por servicio)
```

**2. Verifica CSS de animación:**
```bash
grep -A 5 '.fade-in-up {' web/index.html
# Debe tener: opacity, transform, transition
```

**3. Verifica IntersectionObserver en Console:**
```javascript
// En Console:
typeof IntersectionObserver
// Debe retornar: "function"
// Si "undefined" → navegador no soporta (muy viejo)
```

### Soluciones:

**Si tarjetas no animan:**
- Verifica que clase `fade-in-up` está en HTML (línea 771, 780, 789, 798)
- Verifica que CSS existe (línea 394-403)
- Abre DevTools (F12) → busca elemento `.card.fade-in-up`
- Debe tener: `opacity: 0; transform: translateY(20px);`
- Al entrar en viewport, debe agregar clase `visible`

**Si animación muy rápida/lenta:**
- Modifica `transition` en CSS línea 394:
```css
.fade-in-up {
    transition: opacity 0.6s ease, transform 0.6s ease;  /* Cambiar 0.6s a 0.8s, etc */
}
```

**Si contadores no animan:**
- Verifica que función `animateCounter()` existe (línea 1108+)
- Verifica que `counterObserver` está inicializado (línea 1093+)
- Abre DevTools (F12) → Elements → busca `.metric-item strong`
- Debe haber `data-animated="true"` después de animar

**Si animaciones are jerky (no suave):**
```javascript
// En Console, abre DevTools:
// Performance tab → Record → Scroll → Stop
// Busca "Long task" (rojo) = problema de performance
// Solución: reduce cantidad de elementos animados simultáneamente
```

---

## ❌ PROBLEMA: Tema dark/light no funciona

### Síntomas:
- Toggle de tema no cambia colores
- Theme se resetea al recargar
- Botón sun/moon no aparece

### Diagnóstico:

**1. Verifica botón toggle:**
```bash
grep -n 'id="theme-toggle"' web/index.html
# Debe estar en línea ~535
```

**2. Verifica scripts de tema:**
```bash
grep -n 'const themeToggle' web/index.html
# Debe estar en línea ~985
```

**3. Verifica CSS de tema:**
```bash
grep -n '\[data-theme="dark"\]' web/index.html
# Debe estar en línea ~48
```

### Soluciones:

**Si tema no cambia:**
- Verifica que existe `addEventListener('click')` en script
- Verifica que modifica `document.documentElement.setAttribute('data-theme', ...)`
- Si no existe, el script de tema original se perdió
- Restaura líneas 985-1010 del archivo original

**Si tema no persiste:**
- Verifica que `localStorage.setItem('theme', ...)` se llama
- Si no, agrega:
```javascript
localStorage.setItem('theme', newTheme);
```

**Si colores son incorrectos:**
- Verifica variables CSS en línea 14-64
- Light theme (`:root`) y dark theme (`[data-theme="dark"]`)
- Asegúrate que valores son diferentes

---

## ❌ PROBLEMA: Página lenta/stuttering

### Síntomas:
- Scroll lag
- Modales tardan en abrir
- Animaciones interrumpidas

### Diagnóstico:

**1. Abre DevTools Performance:**
```
F12 → Performance tab → Record → Interact → Stop
Busca: Long tasks (rojo), dropped frames (amarillo)
```

**2. Verifica carga de Alpine.js:**
```
F12 → Network tab → Busca "alpine" o "cdn.jsdelivr.net"
Si tarda >1s → CDN lento o conexión lenta
```

**3. Verifica console errors:**
```
F12 → Console → Busca errores rojos
Si hay errores → Pueden causar lag
```

### Soluciones:

**Si Alpine.js carga lentamente:**
```html
<!-- Opción 1: Usa versión más pequeña (slim) -->
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.slim.min.js"></script>

<!-- Opción 2: Descarga localmente (recomendado para producción) -->
<script defer src="./alpine.min.js"></script>
```

**Si scroll stutters:**
- Reduce cantidad de elementos con observadores
- Modifica `threshold` en IntersectionObserver:
```javascript
const observer = new IntersectionObserver(callback, {
    threshold: 0.25  // Cambiar de 0.1 a 0.25 (menos triggers)
});
```

**Si modales abren lentamente:**
- Verifica que no hay animaciones conflictivas
- Verifica que CSS no tiene `transition` en elementos padres
- Simplifica contenido del modal (menos elementos)

---

## ❌ PROBLEMA: Cambios no se ven reflejados

### Síntomas:
- Modifiqué HTML pero cambios no aparecen
- Edité CSS pero no hay efecto
- Agregué JavaScript pero no funciona

### Soluciones:

**1. Hard refresh (limpia caché):**
```
Windows/Linux: Ctrl + Shift + R
Mac: Cmd + Shift + R
```

**2. Limpia caché local:**
```
F12 → Application → Cache Storage → Clear all
F12 → Application → Local Storage → Clear all
```

**3. Cierra todas las tabs del sitio:**
```
- Service Worker puede cachear
- Cierra todas las tabs del dominio
- Abre nueva tab e intenta nuevamente
```

**4. Si es Coolify:**
```bash
# Fuerza rebuild y redeploy:
docker compose -f docker-compose.yml down
docker compose -f docker-compose.yml up -d
# O en Coolify UI: Force Deploy
```

---

## ❌ PROBLEMA: Mobile no funciona bien

### Síntomas:
- Sliders no responden al touch
- Modales se ven mal en móvil
- Acordeones no funcionan en móvil

### Diagnóstico:

**1. Abre DevTools en modo móvil:**
```
F12 → Ctrl+Shift+M (mobile view)
O: Toggle device toolbar
```

**2. Prueba con diferentes tamaños:**
```
- iPhone SE (375px)
- iPhone 12 (390px)
- iPad (768px)
- Galaxy S21 (360px)
```

### Soluciones:

**Si sliders no responden:**
- Verifica que `input[type="range"]` tiene `width: 100%`
- Verifica que `.input-range` tiene height suficiente para touch
- Aumenta altura:
```css
.input-range {
    height: 10px;  /* Cambiar de 6px a 10px */
}
```

**Si modales se salen de pantalla:**
- Verifica que `.modal` tiene `max-width: 100%`
- Verifica que hay padding horizontal:
```css
.modal-overlay {
    padding: 1rem;  /* Crea espacio a los lados */
}
```

**Si botones son muy pequeños:**
- Aumenta padding en botones:
```css
.btn {
    padding: 1rem 2rem;  /* Fue 0.75rem 1.5rem */
    min-height: 44px;    /* Apple recomienda 44px para touch */
}
```

---

## ✅ CHECKLIST DE VALIDACIÓN

```
Hardware:
☐ Browser actualizado (Chrome 87+, Firefox 85+, Safari 14+)
☐ JavaScript habilitado (Settings → Privacidad)
☐ Conexión a internet estable
☐ Cookies habilitadas (para localStorage)

Software:
☐ Alpine.js cargando (typeof Alpine === 'object')
☐ Sin errores en Console (F12)
☐ Sin warnings de CORS
☐ Sin conflictos de JavaScript

HTML:
☐ Atributos x-data presentes
☐ Eventos @click correctos
☐ Clases CSS aplicadas
☐ IDs únicos en elementos

CSS:
☐ Estilos de modales presentes
☐ Estilos de acordeones presentes
☐ Transiciones configuradas
☐ Variables CSS definidas

JavaScript:
☐ Funciones Alpine definidas
☐ IntersectionObserver disponible
☐ localStorage disponible
☐ requestAnimationFrame disponible
```

---

## 🆘 ÚLTIMO RECURSO: Reset Completo

Si nada funciona, restaura el archivo a su versión original:

```bash
cd en_construccion

# Opción 1: Git (si usas git)
git checkout web/index.html

# Opción 2: Copia backup (si existe)
cp web/index.html.bak web/index.html

# Opción 3: Descarga nuevo
wget https://ejemplo.com/web/index.html -O web/index.html
```

Luego, reaplica cambios manualmente:

```bash
# 1. Agrega Alpine.js en <head> (línea ~9):
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

# 2. Copia CSS nuevo (línea ~291-494)
# 3. Copia componentes HTML (línea ~594-900)
# 4. Copia JavaScript (línea ~1027-1135)
```

---

## 📞 SOPORTE AVANZADO

Si aún no funciona, proporciona:

```
1. Navegador y versión:
   Chrome 120.0.6099.129 (ejemplo)

2. Error en Console (F12):
   Copy-paste el error exacto

3. URL del sitio:
   http://localhost:8000 o tu dominio

4. Pasos para reproducir:
   1. Abre el sitio
   2. Hago click en...
   3. Esperaba que sucediera X
   4. Pero sucedió Y

5. Screenshot o video:
   De preferencia del comportamiento incorrecto
```

---

**¡Con esta guía deberías poder resolver la mayoría de problemas! 🎉**