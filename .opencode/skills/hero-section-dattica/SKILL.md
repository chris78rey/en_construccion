---
name: hero-section-dattica
description: Genera componente Hero Section con titulares de alto impacto para C-Suite. Incluye 3 opciones de messaging según ADN de marca da-tica (soberanía de datos, eliminación de latencia, modernización legacy + IA soberana).
license: MIT
---

# Skill: Hero Section da-tica con Titulares de Alto Impacto

## Contexto Estratégico

El Hero de da-tica.com debe reflejar **"Resonant Stark"**: minimalismo de alto impacto donde la velocidad de carga es el primer mensaje de autoridad. Dirigido a CTO/CFO que rechazan promesas genéricas.

## Opciones de Titulares (Elige una o rota)

### Opción 1: Soberanía de Datos (CTO Focus)
- **Titular:** "Recupere la Soberanía de sus Datos: Ingeniería de Alto Rendimiento para la Era de la IA Empresarial."
- **Subtítulo:** Garantizamos continuidad operativa 99.9% y control absoluto en infraestructuras críticas.
- **Métrica destacada:** +20 años protegiendo misión crítica en defensa, banca y salud pública.

### Opción 2: Eliminación de Latencia (Performance Focus)
- **Titular:** "Eliminamos la Latencia de su Crecimiento: Modernización de Sistemas de Misión Crítica con Precisión Quirúrgica."
- **Subtítulo:** Latencias <50ms en microservicios. 4x reducción en RAM/CPU vs Java tradicional.
- **Métrica destacada:** 325,000 transacciones en 40 segundos | 1.2M usuarios simultáneos.

### Opción 3: Legacy + IA Soberana (Strategic Transformation)
- **Titular:** "Transformamos Sistemas Legacy en Motores de IA Soberana: Rendimiento Extremo sin Perder el Control."
- **Subtítulo:** Oracle 26ai nativa + búsqueda vectorial bajo ACID + arquitectura RAG auditada.
- **Métrica destacada:** 85% reducción en tiempo de auditoría | Cumplimiento SPDP automático.

## Estructura HTML/Tailwind Recomendada

```html
<section class="hero min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-950 via-blue-950 to-slate-900 px-6 py-20">
  <div class="max-w-4xl mx-auto text-center">
    
    <!-- Titular Principal -->
    <h1 class="text-5xl md:text-7xl font-black text-white mb-6 leading-tight">
      Recupere la Soberanía de sus Datos
    </h1>
    
    <!-- Subtítulo -->
    <p class="text-xl md:text-2xl text-blue-200 mb-8 font-light max-w-3xl mx-auto">
      Ingeniería de Alto Rendimiento para la Era de la IA Empresarial
    </p>
    
    <!-- Puntos de Credibilidad Inmediatos -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12 py-8 border-y border-blue-800">
      <div>
        <p class="text-3xl font-bold text-cyan-400">99.9%</p>
        <p class="text-sm text-gray-300">Continuidad Operativa (Oracle RAC)</p>
      </div>
      <div>
        <p class="text-3xl font-bold text-cyan-400">20+ años</p>
        <p class="text-sm text-gray-300">Defensa, Banca, Salud Pública</p>
      </div>
      <div>
        <p class="text-3xl font-bold text-cyan-400"><50ms</p>
        <p class="text-sm text-gray-300">Latencia Determinística</p>
      </div>
    </div>
    
    <!-- CTA Buttons -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="px-8 py-4 bg-cyan-500 hover:bg-cyan-600 text-white font-bold rounded-lg transition">
        Solicitar Consultoría
      </button>
      <button class="px-8 py-4 border-2 border-cyan-400 text-cyan-400 hover:bg-cyan-400 hover:text-slate-900 font-bold rounded-lg transition">
        Ver Arquitectura Técnica
      </button>
    </div>
  </div>
</section>
```

## Patrones de Optimización (Web Vitals)

1. **LCP (Largest Contentful Paint):** Hero debe ser viewport-critical. Usa `fetchpriority="high"` en imágenes de fondo.
2. **CLS (Cumulative Layout Shift):** Declara alturas explícitas en métricas para evitar reflow.
3. **Paleta de Colores:** Mantén contraste WCAG AA mínimo (4.5:1). Uso de degradados azul-slate refuerza autoridad tech.

## Variaciones Dinámicas Recomendadas

- **A/B Testing:** Rota entre las 3 opciones de titulares. Mide engagement con analytics.
- **Personalization by Role:** Detecta si visitante es CTO (muestra opción 2), CFO (opción 3), o genérico (opción 1).
- **Animación Sutil:** Fade-in del titular + desfase de 0.2s para subtítulo (evita motion sickness).

## Integración con Resto de Site

Este hero desemboca naturalmente en:
- **Agitación (Pain Points Section):** "Fragmentación por IA", "Costos de Nube", "Riesgos SPDP".
- **Autoridad (Metrics Bar):** 325K transacciones, 1.2M usuarios, 20+ años.
- **Soluciones (Services Section):** A+B de modernización y Rust.

## Checklist de Implementación

- [ ] Elegir titular base (o rotar dinámicamente)
- [ ] Validar contraste WCAG AA en paleta
- [ ] Medir LCP en Lighthouse (target: <2.5s)
- [ ] Añadir tracking de CTA clicks
- [ ] Implementar fallback CSS si JS falla
- [ ] Testear responsive en móvil (<480px ancho)