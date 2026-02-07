# 🗺️ MAPA DE UBICACIÓN DE CARACTERÍSTICAS

**Archivo:** `web/index.html`  
**Total líneas:** 1,138  
**Framework:** Alpine.js 3.x (CDN)

---

## 📍 UBICACIÓN DE CARACTERÍSTICAS

### 1. Alpine.js CDN
**Líneas: 9-10**
```html
<!-- Alpine.js CDN -->
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
```
📌 **Ubicación:** En `<head>`, después del `<title>`  
✨ **Propósito:** Carga framework para componentes reactivos

---

### 2. ACORDEONES - Pain Points
**HTML: Líneas 594-653**  
**JavaScript: Líneas 1027-1031**  
**CSS: Líneas 346-391**

#### En HTML:
```html
<!-- Línea 594: Contenedor con x-data -->
<div class="pain-grid" x-data="painPointsAccordion()" 
     style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-md);">

  <!-- Línea 595: Primer acordeón (Fragmentación) -->
  <article class="card pain-card accordion-item" x-bind:class="{ 'active': openAccordion === 0 }">
    <div class="accordion-header" @click="openAccordion = openAccordion === 0 ? null : 0">
      <!-- Contenido de header -->
    </div>
    <div class="accordion-body">
      <!-- Contenido expandible -->
    </div>
  </article>

  <!-- Línea 615: Segundo acordeón (Costos) -->
  <!-- Línea 635: Tercer acordeón (Riesgo Regulatorio) -->
```

#### En JavaScript:
```javascript
// Línea 1027-1031
function painPointsAccordion() {
    return {
        openAccordion: 0,
    };
}
```

#### En CSS:
```css
/* Línea 346-391: Estilos acordeón */
.accordion-item { }
.accordion-header { }
.accordion-toggle { }
.accordion-body { }
.accordion-item.active { }
```

---

### 3. MODALES - Servicios
**HTML: Líneas 766-900**  
**JavaScript: Líneas 1034-1044**  
**CSS: Líneas 291-343**

#### En HTML:
```html
<!-- Línea 766: Section con x-data -->
<section id="servicios" class="container mt-xl" x-data="servicesModals()">
  <h2 class="text-4xl text-center mb-lg">Soluciones Productized</h2>
  
  <!-- Línea 769-805: 4 tarjetas de servicios -->
  <div class="services-grid">
    <article class="card fade-in-up">
      <!-- Botón que abre modal -->
      <button class="btn btn-outline" style="width: 100%" 
              @click="openModal('modernization')">
        Ver Detalles
      </button>
    </article>
    <!-- ... 3 servicios más ... -->
  </div>

  <!-- Línea 808-829: MODAL 1 - Modernización Legacy -->
  <div class="modal-overlay" x-show="activeModal === 'modernization'" 
       @click.self="activeModal = null" :hidden="activeModal !== 'modernization'">
    <div class="modal">
      <div class="modal-header">
        <h3 class="text-2xl">Modernización Legacy</h3>
        <button class="modal-close" @click="activeModal = null">×</button>
      </div>
      <!-- Contenido del modal -->
    </div>
  </div>

  <!-- Línea 831-852: MODAL 2 - Ultra-Baja Latencia -->
  <!-- Línea 854-875: MODAL 3 - IA Soberana -->
  <!-- Línea 877-899: MODAL 4 - Auditoría Proactiva -->
```

#### En JavaScript:
```javascript
// Línea 1034-1044
function servicesModals() {
    return {
        activeModal: null,
        openModal(service) {
            this.activeModal = service;
        },
        closeModal() {
            this.activeModal = null;
        }
    };
}
```

#### En CSS:
```css
/* Línea 291-343: Estilos modales */
.modal-overlay { }
.modal { }
.modal-header { }
.modal-close { }
```

---

### 4. CALCULADORA ROI
**HTML: Líneas 704-760**  
**JavaScript: Líneas 1047-1076**  
**CSS: Líneas 406-494**

#### En HTML:
```html
<!-- Línea 697-760: Contenedor CFO con calculadora -->
<div id="cfo-content" class="icp-content" x-data="roiCalculator()" x-init="init()">
  <div class="card" style="background: var(--bg-surface-2); border: none;">
    
    <!-- Línea 704-707: Botón para abrir calculadora -->
    <button class="btn btn-primary mt-md" @click="showCalculator = !showCalculator">
      <span x-show="!showCalculator">Abrir Calculadora ROI</span>
      <span x-show="showCalculator">Cerrar Calculadora</span>
    </button>

    <!-- Línea 727-760: Calculadora expandible -->
    <div class="calculator-container" x-show="showCalculator">
      <h4 class="text-xl mb-md">Calculadora ROI Interactiva</h4>
      
      <!-- Slider 1: Costo Cloud Actual -->
      <div class="input-group">
        <label class="input-label">
          Costo Cloud Actual: <span class="input-value" x-text="formatCurrency(currentCost)">$2.5M</span>
        </label>
        <input type="range" class="input-range" x-model.number="currentCost" 
               min="500000" max="10000000" step="100000" @input="recalculate()">
      </div>

      <!-- Slider 2: Reducción Esperada -->
      <div class="input-group">
        <label class="input-label">
          Reducción Esperada: <span class="input-value" x-text="reductionPercent + '%'">40%</span>
        </label>
        <input type="range" class="input-range" x-model.number="reductionPercent" 
               min="20" max="80" step="5" @input="recalculate()">
      </div>

      <!-- Slider 3: Período de Amortización -->
      <div class="input-group">
        <label class="input-label">
          Período de Amortización: <span class="input-value" x-text="paybackPeriod + ' años'">2</span>
        </label>
        <input type="range" class="input-range" x-model.number="paybackPeriod" 
               min="1" max="5" step="0.5" @input="recalculate()">
      </div>

      <!-- Resultado -->
      <div class="calculator-result">
        <div class="calculator-result-label">Ahorro Anual Proyectado</div>
        <div class="calculator-result-value" x-text="formatCurrency(savings)">$1.0M</div>
        <div class="calculator-result-label mt-md">ROI Total (5 años)</div>
        <div class="calculator-result-value" x-text="formatCurrency(totalROI)">$5.0M</div>
      </div>
    </div>
  </div>
</div>
```

#### En JavaScript:
```javascript
// Línea 1047-1076
function roiCalculator() {
    return {
        showCalculator: false,
        currentCost: 2500000,
        reductionPercent: 40,
        paybackPeriod: 2,
        optimizedCost: 1500000,
        savings: 1000000,
        totalROI: 5000000,

        formatCurrency(value) {
            return new Intl.NumberFormat('es-ES', {
                style: 'currency',
                currency: 'USD',
                minimumFractionDigits: 0,
                maximumFractionDigits: 0,
            }).format(value);
        },

        recalculate() {
            this.optimizedCost = this.currentCost * (1 - this.reductionPercent / 100);
            this.savings = this.currentCost - this.optimizedCost;
            this.totalROI = this.savings * 5;
        },

        init() {
            this.recalculate();
        }
    };
}
```

#### En CSS:
```css
/* Línea 406-494: Estilos calculadora */
.calculator-container { }
.input-group { }
.input-label { }
.input-range { }
.input-range::-webkit-slider-thumb { }
.input-value { }
.calculator-result { }
.calculator-result-label { }
.calculator-result-value { }
```

---

### 5. ANIMACIONES DE SCROLL - Servicios
**HTML: Línea 771 (clase `fade-in-up`)**  
**JavaScript: Líneas 1080-1105**  
**CSS: Líneas 394-403**

#### En HTML:
```html
<!-- Línea 769-805: Tarjetas de servicios con clase fade-in-up -->
<div class="services-grid">
  <article class="card fade-in-up">  <!-- ← Clase para animación -->
    <div class="service-icon">🏛️</div>
    <h3 class="text-xl mb-xs">Modernización Legacy</h3>
    <!-- ... -->
  </article>

  <article class="card fade-in-up">  <!-- ← Clase para animación -->
    <div class="service-icon">⚡</div>
    <h3 class="text-xl mb-xs">Ultra-Baja Latencia</h3>
    <!-- ... -->
  </article>

  <!-- ... 2 tarjetas más con fade-in-up ... -->
</div>
```

#### En JavaScript:
```javascript
// Línea 1080-1090: Observer para fade-in-up
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-in-up').forEach(el => {
        observer.observe(el);
    });
```

#### En CSS:
```css
/* Línea 394-403 */
.fade-in-up {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}

.fade-in-up.visible {
    opacity: 1;
    transform: translateY(0);
}
```

---

### 6. CONTADORES ANIMADOS - Métricas
**HTML: Línea 568-571 (elementos `.metric-item strong`)**  
**JavaScript: Líneas 1093-1135**  
**CSS: Líneas 221-222**

#### En HTML:
```html
<!-- Línea 566-585: Sección de métricas -->
<section id="autoridad" class="container">
  <div class="metrics-grid">
    <div class="metric-item text-center">
      <strong>325K</strong>  <!-- ← Será animado -->
      <span>Transacciones / 40s</span>
    </div>
    <div class="metric-item text-center">
      <strong>1.2M</strong>  <!-- ← Será animado -->
      <span>Usuarios Simultáneos</span>
    </div>
    <div class="metric-item text-center">
      <strong>&lt;50ms</strong>  <!-- ← Será animado -->
      <span>Latencia Determinística</span>
    </div>
    <div class="metric-item text-center">
      <strong>20+</strong>  <!-- ← Será animado -->
      <span>Años en Defensa/Banca</span>
    </div>
  </div>
</section>
```

#### En JavaScript:
```javascript
// Línea 1093-1135: Observer para contadores
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            entry.target.dataset.animated = 'true';
            animateCounter(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.metric-item strong').forEach(el => {
    counterObserver.observe(el);
});

function animateCounter(element) {
    const text = element.textContent;
    const isNumber = /\d+/.test(text);
    if (!isNumber) return;

    const match = text.match(/(\d+)/);
    const target = parseInt(match[1]);
    const suffix = text.replace(match[0], '');
    
    let current = 0;
    const duration = 1500;
    const start = Date.now();

    const animate = () => {
        const elapsed = Date.now() - start;
        const progress = Math.min(elapsed / duration, 1);
        current = Math.floor(target * progress);
        element.textContent = current + suffix;

        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            element.textContent = target + suffix;
        }
    };

    animate();
}
```

#### En CSS:
```css
/* Línea 221-222: Solo estilos base */
.metric-item strong { display: block; font-size: 2.5rem; font-weight: 800; }
.metric-item span { font-size: 0.875rem; color: var(--text-muted); }
```

---

## 🎯 Resumen Rápido

| Característica | HTML | CSS | JS | Alpine |
|---|---|---|---|---|
| **Acordeones** | 594-653 | 346-391 | 1027-1031 | ✅ |
| **Modales** | 766-900 | 291-343 | 1034-1044 | ✅ |
| **Calculadora ROI** | 704-760 | 406-494 | 1047-1076 | ✅ |
| **Fade-in Scroll** | 771 (clase) | 394-403 | 1080-1090 | ❌ |
| **Contadores** | 568-571 | 221-222 | 1093-1135 | ❌ |

---

## 🔍 Cómo Navegar el Código

### Para entender acordeones:
1. Abre línea 594 → Ve `x-data="painPointsAccordion()"`
2. Busca la función en línea 1027 → Lee la lógica
3. Busca estilos en línea 346 → Entiende la animación

### Para entender modales:
1. Abre línea 766 → Ve `x-data="servicesModals()"`
2. Busca botones en línea 776, 785, 794, 803 → Ve `@click="openModal('...')"`
3. Busca modales en línea 808-899 → Ve `x-show="activeModal === '...'"`
4. Busca función en línea 1034 → Lee la lógica

### Para entender calculadora:
1. Abre línea 697 → Ve `x-data="roiCalculator()"`
2. Busca botón en línea 704 → Ve `@click="showCalculator = !showCalculator"`
3. Busca sliders en línea 730-751 → Ve `x-model.number` y `@input="recalculate()"`
4. Busca función en línea 1047 → Lee la lógica

### Para entender animaciones:
1. Abre línea 771 → Ve clase `fade-in-up` en tarjetas
2. Busca CSS en línea 394 → Entiende transición
3. Busca JS en línea 1080 → Entiende observer

### Para entender contadores:
1. Abre línea 568 → Ve elementos `<strong>`
2. Busca JS en línea 1093 → Entiende observer
3. Busca función en línea 1108 → Entiende animación

---

## 📊 Estadísticas

```
Total líneas HTML:     1,138
├── HTML componentes:  +100 líneas
├── CSS componentes:   +230 líneas
└── JS componentes:    +155 líneas

Archivo original:      619 líneas
Archivo modificado:    1,138 líneas (+519 líneas)

Cambios no-invasivos:
✓ Sin eliminar nada
✓ Solo agregar atributos y etiquetas
✓ Estructura intacta
```

---

## ✅ Checklist de Validación

```
□ Alpine.js CDN cargado (línea 9-10)
□ Componentes x-data presentes (4 ubicaciones)
□ Acordeones con x-bind:class (línea 595, 615, 635)
□ Modales con x-show (línea 808-899)
□ Calculadora con x-model.number (línea 734, 742, 750)
□ Botones con @click (línea 665, 704, 776, 785, 794, 803)
□ Clases fade-in-up presentes (línea 771, 780, 789, 798)
□ IntersectionObserver para scroll (línea 1080-1090)
□ IntersectionObserver para contadores (línea 1093-1135)
□ Funciones de componentes definidas (línea 1027-1076)
□ CSS de modales presente (línea 291-343)
□ CSS de acordeones presente (línea 346-391)
□ CSS de animaciones presente (línea 394-403)
□ CSS de calculadora presente (línea 406-494)
```

---

Este mapa te permite:
- ✅ Encontrar rápidamente cualquier característica
- ✅ Entender cómo se conectan HTML, CSS y JS
- ✅ Modificar valores (números, textos, estilos)
- ✅ Debuggear problemas específicos