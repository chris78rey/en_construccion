---
name: web-integration-implementation-dattica
description: Guía práctica para integrar todos los 6 skills en la página web da-tica.com. Incluye estructura HTML, personalization logic, testing checklist y deployment en Coolify.
license: MIT
---

# Skill: Web Integration & Implementation Guide

## Propósito
Transformar los 6 skills (hero, pain-points, authority-metrics, services, thought-leadership, ICP) en una página web cohesiva, personalizada y optimizada para conversión.

## Overview: Flujo de la Página

```
┌─────────────────────────────────────────────────────────┐
│ Hero Section                                             │
│ (3 opciones titulares: soberanía, latencia, legacy)    │
│ CTA: "Solicitar Arquitectura"                          │
└──────────────┬──────────────────────────────────────────┘
               ↓
┌─────────────────────────────────────────────────────────┐
│ Pain Points Section (Agitación)                         │
│ - Fragmentación por IA                                  │
│ - Costos Cloud Insostenibles                            │
│ - Riesgos SPDP 2026                                     │
│ CTA: "Diagnosticar tu Infraestructura"                 │
└──────────────┬──────────────────────────────────────────┘
               ↓
┌─────────────────────────────────────────────────────────┐
│ Authority Metrics (Credibilidad)                        │
│ - 325K transacciones / 40s                             │
│ - 1.2M usuarios simultáneos                             │
│ - 20+ años en defensa/banca/salud                       │
│ - 85% reducción auditoría                              │
└──────────────┬──────────────────────────────────────────┘
               ↓
┌─────────────────────────────────────────────────────────┐
│ Services (4 Soluciones)                                 │
│ - Modernización Legacy                                  │
│ - Ultra-Baja Latencia (Rust)                            │
│ - IA Soberana RAG                                       │
│ - Auditoría KNIME                                       │
│ CTA individual por servicio                            │
└──────────────┬──────────────────────────────────────────┘
               ↓
┌─────────────────────────────────────────────────────────┐
│ Thought Leadership Blog Teaser                          │
│ (Últimos 3 artículos)                                   │
│ CTA: "Ver todos los artículos"                         │
└──────────────┬──────────────────────────────────────────┘
               ↓
┌─────────────────────────────────────────────────────────┐
│ Contact / CTA Final                                     │
│ - Formulario contacto                                   │
│ - Calendly para agendar                                │
│ - FAQ                                                   │
└─────────────────────────────────────────────────────────┘
```

## Key Integration Points (Skills → Website)

### 1. Hero Section Integration
**Skill:** `hero-section-dattica`
- Implementar 3 variantes de titulares (A/B test)
- Conectar hero metrics con datos reales (325K, 1.2M, 20+, 85%)
- CTAs abren formulario contacto O calendario Calendly

### 2. Pain Points Integration
**Skill:** `pain-points-section-dattica`
- 3 tarjetas (IA, Costos, SPDP) con iconos
- Cada tarjeta tiene botón CTA específico
- Tracking: registrar cuál pain point genera más engagement

### 3. Authority Metrics Integration
**Skill:** `authority-metrics-dattica`
- 4 métrica cards con números animados (counter)
- Al scroll, iniciar animación "count-up" desde 0 → número final
- Lazy-load para evitar impacto de performance

### 4. Services Integration
**Skill:** `services-architecture-dattica`
- 4 service cards (expandibles en móvil)
- CTAs por servicio redirigen a formulario + topic específico
- Matriz de bundles debajo (Starter, Growth, Complete)

### 5. Thought Leadership Integration
**Skill:** `thought-leadership-content-dattica`
- Teaser de últimos 3 artículos
- Links a `/blog` para artículos completos
- RSS feed (opcional) para suscriptores

### 6. ICP Personalization Integration
**Skill:** `ideal-customer-profile-dattica`
- Detectar persona (CTO vs CFO) automáticamente
- Mostrar/ocultar secciones según persona
- Personalizar CTAs ("sesión técnica" vs "ROI calculator")

## Estructura HTML Base

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>da-tica: Ingeniería de Misión Crítica | Modernización + Rust + IA Soberana</title>
  <meta name="description" 
    content="Modernización legacy, Rust ultra-baja latencia, IA soberana, auditoría KNIME. 
    20+ años en defensa, banca, salud. Eliminamos latencia y recuperamos soberanía de datos.">
  <meta property="og:title" content="da-tica: Ingeniería de Alto Rendimiento">
  <meta property="og:description" content="325K transacciones/40s, 1.2M usuarios, 99.9% uptime">
  <meta property="og:image" content="https://da-tica.com/og-image.png">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet">
  
  <!-- Styles -->
  <link rel="stylesheet" href="/styles/main.css">
  <link rel="stylesheet" href="/styles/hero.css">
  <link rel="stylesheet" href="/styles/pain-points.css">
  <link rel="stylesheet" href="/styles/authority.css">
  <link rel="stylesheet" href="/styles/services.css">
  <link rel="stylesheet" href="/styles/contact.css">
  
  <!-- Scripts (deferred for performance) -->
  <script src="/js/persona-detection.js" defer></script>
  <script src="/js/cta-tracking.js" defer></script>
  <script src="/js/counters.js" defer></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_ID');
  </script>
</head>
<body>

  <!-- Navigation (Sticky) -->
  <header id="header-sticky" class="header-sticky">
    <div class="header-content">
      <a href="/" class="logo">da-tica</a>
      <nav class="nav-main">
        <a href="#servicios" class="nav-link">Servicios</a>
        <a href="#blog" class="nav-link">Blog</a>
        <a href="#contacto" class="nav-link">Contacto</a>
      </nav>
      <button class="btn-contact btn-primary" data-cta="header-cta">
        Solicitar Auditoría
      </button>
    </div>
  </header>

  <!-- Main Content -->
  <main role="main">

    <!-- Hero Section (from skill: hero-section-dattica) -->
    <section id="hero" class="hero" role="banner">
      <div class="hero-container">
        <div class="hero-content">
          <h1 class="hero-title">Recupere la Soberanía de sus Datos</h1>
          <p class="hero-subtitle">Ingeniería de Alto Rendimiento para la Era de la IA Empresarial</p>
          
          <div class="hero-metrics">
            <div class="metric" data-value="99.9">
              <strong class="metric-number">99.9%</strong>
              <small class="metric-label">Continuidad Operativa</small>
            </div>
            <div class="metric" data-value="50">
              <strong class="metric-number">&lt;50ms</strong>
              <small class="metric-label">Latencia Determinística</small>
            </div>
            <div class="metric" data-value="20">
              <strong class="metric-number">20+</strong>
              <small class="metric-label">Años en Misión Crítica</small>
            </div>
          </div>

          <div class="hero-actions">
            <button class="btn btn-primary btn-lg" data-cta="solicitar-arquitectura">
              Solicitar Arquitectura
            </button>
            <button class="btn btn-secondary btn-lg" data-cta="ver-caso-exito">
              Ver Caso de Éxito
            </button>
          </div>
        </div>

        <aside class="hero-alert" data-persona-cto>
          <h3>⚠️ El 2026 Exige Blindaje</h3>
          <p>Tres crisis convergen en tu infraestructura. Aquí está cómo resolverlas.</p>
          <ul>
            <li>325K transacciones en 40 segundos</li>
            <li>1.2M usuarios simultáneos sin degradación</li>
            <li>Blindaje de 20+ años en defensa</li>
          </ul>
        </aside>
      </div>
    </section>

    <!-- Pain Points Section (from skill: pain-points-section-dattica) -->
    <section id="pain-points" class="pain-points" role="region" aria-label="Puntos de dolor críticos 2026">
      <div class="container">
        <h2 class="section-title">El Triángulo de la Crisis de 2026</h2>
        <p class="section-subtitle">Tres presiones simultáneas amenazan la estabilidad operativa</p>

        <div class="pain-grid">
          <!-- Pain Point 1: Fragmentación IA -->
          <article class="pain-card" data-pain="fragmentacion-ia">
            <div class="pain-icon">⚡</div>
            <h3 class="pain-title">Fragmentación por IA</h3>
            <p class="pain-desc">Bases vectoriales aisladas debilitan ACID. Oracle 26ai integra bajo garantía de integridad.</p>
            <ul class="pain-list">
              <li>✓ Silos de datos debilitan auditoría</li>
              <li>✓ Inconsistencia entre AI y core</li>
              <li>✓ Violaciones de ACID</li>
            </ul>
            <p class="pain-metric">⚠️ 85% brechas en IA vienen de separación de capas</p>
            <button class="btn btn-outline" data-cta="diagnosticar-fragmentacion">
              Diagnosticar fragmentación →
            </button>
          </article>

          <!-- Pain Point 2: Costos Cloud -->
          <article class="pain-card" data-pain="costos-cloud">
            <div class="pain-icon">💰</div>
            <h3 class="pain-title">Costos de Nube Insostenibles</h3>
            <p class="pain-desc">Factura AWS crece 40-50% YoY. Reescritura en Rust = 4x menos RAM, ROI en 6 meses.</p>
            <ul class="pain-list">
              <li>✓ 325K transacciones vs overhead GC</li>
              <li>✓ 4x densidad en Kubernetes</li>
              <li>✓ Latencias <50ms garantizadas</li>
            </ul>
            <p class="pain-metric">📊 50 pods Java → 12 pods Rust</p>
            <button class="btn btn-outline" data-cta="calcular-ahorro-opex">
              Calcular ahorro OPEX →
            </button>
          </article>

          <!-- Pain Point 3: Riesgos SPDP -->
          <article class="pain-card" data-pain="riesgo-spdp">
            <div class="pain-icon">⚖️</div>
            <h3 class="pain-title">Riesgos SPDP 2026</h3>
            <p class="pain-desc">Resolución exige explicabilidad. Incumplimiento = multas hasta 1% volumen de negocio.</p>
            <ul class="pain-list">
              <li>✓ 70% bases deben estar gobernadas</li>
              <li>✓ Auditoría manual = 6 meses</li>
              <li>✓ 85% reducción con KNIME</li>
            </ul>
            <p class="pain-metric">🛡️ Auditoría completa en 2 semanas</p>
            <button class="btn btn-outline" data-cta="evaluar-exposicion-spdp">
              Evaluar exposición regulatoria →
            </button>
          </article>
        </div>

        <!-- CTA: From Pain to Solution -->
        <div class="pain-cta">
          <h3>¿Cuál es tu prioridad inmediata?</h3>
          <div class="pain-cta-buttons">
            <button class="btn btn-primary" data-cta="auditoria-linea-base">
              Auditar tu Infraestructura Ahora
            </button>
            <button class="btn btn-secondary" data-cta="ver-roadmap-modernizacion">
              Ver Roadmap de Modernización
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Authority Metrics (from skill: authority-metrics-dattica) -->
    <section id="authority" class="authority-metrics" role="region" aria-label="Métricas de autoridad técnica">
      <div class="container">
        <h2 class="section-title">Autoridad Técnica Comprobada</h2>
        <p class="section-subtitle">20+ años optimizando el núcleo de infraestructuras de misión crítica</p>

        <div class="metrics-grid">
          <div class="metric-card" data-metric="transacciones">
            <div class="metric-number" data-target="325000">0</div>
            <p class="metric-unit">transacciones / 40 segundos</p>
            <p class="metric-detail">PL/SQL avanzado + Oracle RAC</p>
          </div>

          <div class="metric-card" data-metric="usuarios">
            <div class="metric-number" data-target="1200000">0</div>
            <p class="metric-unit">usuarios simultáneos</p>
            <p class="metric-detail">Disponibilidad 99.9% sin degradación</p>
          </div>

          <div class="metric-card" data-metric="anos">
            <div class="metric-number" data-target="20">0</div>
            <p class="metric-unit">años en misión crítica</p>
            <p class="metric-detail">Defensa, banca, salud pública</p>
          </div>

          <div class="metric-card" data-metric="auditoria">
            <div class="metric-number" data-target="85">0</div>
            <p class="metric-unit">% reducción tiempo auditoría</p>
            <p class="metric-detail">KNIME + Ley de Benford</p>
          </div>
        </div>

        <div class="authority-statement">
          <blockquote>
            "Estas métricas no son marketing. Son el resultado de decisiones arquitectónicas inamovibles, 
            donde el costo de fallar es medido en vidas humanas o millones de dólares. 
            Tu infraestructura merece el mismo nivel de ingeniería."
          </blockquote>
        </div>
      </div>
    </section>

    <!-- Services (from skill: services-architecture-dattica) -->
    <section id="servicios" class="services" role="region" aria-label="Servicios productized">
      <div class="container">
        <h2 class="section-title">Soluciones Productized para 2026</h2>
        <p class="section-subtitle">Cuatro servicios, módularmente arquitectados. Combínalos según tu roadmap.</p>

        <div class="services-grid">
          <!-- Service A: Modernización -->
          <article class="service-card" data-service="modernizacion-legacy">
            <div class="service-icon">🏛️</div>
            <h3 class="service-title">Modernización Legacy</h3>
            <p class="service-desc">De Java monolítico a Oracle 26ai convergente. 6-12 meses.</p>
            
            <div class="service-features">
              <h4>Incluye:</h4>
              <ul>
                <li>✓ Arquitectura Oracle RAC HA</li>
                <li>✓ Migración segura sin downtime</li>
                <li>✓ Integración vectorial Oracle 26ai</li>
                <li>✓ IA nativa + RAG auditada</li>
              </ul>
            </div>

            <div class="service-roi">
              <p><strong>ROI:</strong> 30% OPEX Año 1 | 60% velocity Año 2</p>
              <p class="service-price">$250K - $500K | 6-12 meses</p>
            </div>

            <button class="btn btn-outline" data-cta="solicitar-diagnostico-modernizacion">
              Solicitar Diagnóstico
            </button>
          </article>

          <!-- Service B: Ultra-Baja Latencia -->
          <article class="service-card" data-service="ultra-baja-latencia">
            <div class="service-icon">⚡</div>
            <h3 class="service-title">Ultra-Baja Latencia (Rust)</h3>
            <p class="service-desc">4x menos RAM, &lt;50ms garantizado. Tu OPEX, 10x más ágil.</p>
            
            <div class="service-features">
              <h4>Incluye:</h4>
              <ul>
                <li>✓ Profiling de microservicios críticos</li>
                <li>✓ Reescritura selectiva en Rust</li>
                <li>✓ Benchmarks vs implementación anterior</li>
                <li>✓ Monitoring + observabilidad</li>
              </ul>
            </div>

            <div class="service-roi">
              <p><strong>ROI:</strong> 40-50% OPEX cloud | +15% conversion</p>
              <p class="service-price">$150K - $350K | 3-8 meses</p>
            </div>

            <button class="btn btn-outline" data-cta="calcular-ahorro-opex-rust">
              Calcular Ahorro OPEX
            </button>
          </article>

          <!-- Service C: IA Soberana -->
          <article class="service-card" data-service="ia-soberana">
            <div class="service-icon">🧠</div>
            <h3 class="service-title">IA Soberana & RAG</h3>
            <p class="service-desc">IA explicable, bajo control. Sin cajas negras. Auditoría integrada.</p>
            
            <div class="service-features">
              <h4>Incluye:</h4>
              <ul>
                <li>✓ Arquitectura RAG 3-niveles</li>
                <li>✓ Embeddings + búsqueda vectorial</li>
                <li>✓ Audit trail automático</li>
                <li>✓ Cumplimiento SPDP</li>
              </ul>
            </div>

            <div class="service-roi">
              <p><strong>ROI:</strong> 20-30% productividad | 100% SPDP-ready</p>
              <p class="service-price">$100K - $250K | 3-6 meses</p>
            </div>

            <button class="btn btn-outline" data-cta="disenar-arquitectura-rag">
              Diseñar Arquitectura RAG
            </button>
          </article>

          <!-- Service D: Auditoría KNIME -->
          <article class="service-card" data-service="auditoria-knime">
            <div class="service-icon">📊</div>
            <h3 class="service-title">Auditoría Proactiva (KNIME)</h3>
            <p class="service-desc">KNIME + Benford. Auditoría completa en 2 semanas. 85% menos tiempo.</p>
            
            <div class="service-features">
              <h4>Incluye:</h4>
              <ul>
                <li>✓ Análisis de población completa</li>
                <li>✓ Detección de anomalías (Benford)</li>
                <li>✓ Anonimización con Presidio</li>
                <li>✓ Dashboard gobernanza 24/7</li>
              </ul>
            </div>

            <div class="service-roi">
              <p><strong>ROI:</strong> 100% cumplimiento | $5-50M multas evitadas</p>
              <p class="service-price">$80K - $180K | 2-4 meses</p>
            </div>

            <button class="btn btn-outline" data-cta="auditoria-linea-base">
              Auditoría de Línea Base
            </button>
          </article>
        </div>

        <!-- Service Bundles -->
        <div class="service-bundles">
          <h3>Bundles: Combina Servicios para Máximo Impacto</h3>
          <div class="bundles-grid">
            <div class="bundle">
              <h4>Starter</h4>
              <p class="bundle-services">Servicios C + D</p>
              <p class="bundle-price">$180K - $430K</p>
              <p class="bundle-desc">IA soberana + auditoría automática para regulados</p>
            </div>
            <div class="bundle featured">
              <h4>Growth ⭐ Popular</h4>
              <p class="bundle-services">Servicios A + B + C</p>
              <p class="bundle-price">$500K - $1.1M</p>
              <p class="bundle-desc">Modernización completa: legacy → cloud-native + IA</p>
            </div>
            <div class="bundle">
              <h4>Complete</h4>
              <p class="bundle-services">Servicios A + B + C + D</p>
              <p class="bundle-price">$630K - $1.3M</p>
              <p class="bundle-desc">Transformación digital end-to-end</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Thought Leadership / Blog Teaser -->
    <section id="blog" class="blog-teaser" role="region" aria-label="Liderazgo de pensamiento">
      <div class="container">
        <h2 class="section-title">Liderazgo de Pensamiento 2026</h2>
        <p class="section-subtitle">Educar, no vender. Aquí está nuestro conocimiento abierto.</p>

        <div class="blog-grid">
          <article class="blog-card">
            <h3 class="blog-title">Rust vs Java en Sector Financiero</h3>
            <p class="blog-date">📅 Enero 2026</p>
            <p class="blog-excerpt">Memory safety elimina vulnerabilidades. Latencia <50ms determinística. ROI en 6 meses.</p>
            <a href="/blog/rust-vs-java" class="blog-link">Leer artículo →</a>
          </article>

          <article class="blog-card">
            <h3 class="blog-title">Guía: Modelo Técnico Gran Escala Ecuador</h3>
            <p class="blog-date">📅 Febrero 2026</p>
            <p class="blog-excerpt">SPDP-2026-0005-R explicada. Checklist de cumplimiento. Auditoría automática.</p>
            <a href="/blog/spdp-ecuador" class="blog-link">Leer artículo →</a>
          </article>

          <article class="blog-card">
            <h3 class="blog-title">Optimización Oracle RAC para GenAI</h3>
            <p class="blog-date">📅 Marzo 2026</p>
            <p class="blog-excerpt">Oracle 26ai nativa. Vector database sin silos. Migration path sin downtime.</p>
            <a href="/blog/oracle-genai" class="blog-link">Leer artículo →</a>
          </article>
        </div>

        <div class="blog-cta">
          <a href="/blog" class="btn btn-secondary">Ver todos los artículos</a>
        </div>
      </div>
    </section>

    <!-- Contact / Final CTA -->
    <section id="contacto" class="contact-section" role="region" aria-label="Formulario de contacto">
      <div class="container">
        <h2 class="section-title">¿Cuál es tu siguiente paso?</h2>

        <!-- Persona-Specific CTAs -->
        <div data-persona-cto class="cta-block">
          <h3>Para CTOs: Sesión Técnica Profunda</h3>
          <p>30 minutos con especialista. Diagnóstico arquitectónico sin compromiso.</p>
          <button class="btn btn-primary btn-lg" data-cta="agendar-sesion-tecnica">
            Agendar sesión técnica
          </button>
        </div>

        <div data-persona-cfo class="cta-block">
          <h3>Para CFOs: ROI Calculator + Propuesta</h3>
          <p>Calcula tu ahorro. Recibe propuesta personalizada en 24h.</p>
          <button class="btn btn-primary btn-lg" data-cta="descargar-roi-calculator">
            Descargar ROI Calculator
          </button>
        </div>

        <!-- General Contact Form -->
        <div class="cta-block cta-form">
          <h3>Solicitud de Información</h3>
          <form id="contact-form" method="POST" action="/api/contact">
            <div class="form-group">
              <label for="name">Nombre completo</label>
              <input type="text" id="name" name="name" required aria-required="true">
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" required aria-required="true">
            </div>

            <div class="form-group">
              <label for="role">Rol</label>
              <select id="role" name="role" required aria-required="true">
                <option value="">Selecciona tu rol</option>
                <option value="cto">CTO / VP Engineering</option>
                <option value="cfo">CFO / VP Finance</option>
                <option value="compliance">CISO / Compliance Officer</option>
                <option value="other">Otro</option>
              </select>
            </div>

            <div class="form-group">
              <label for="challenge">¿Cuál es tu mayor reto ahora?</label>
              <textarea id="challenge" name="challenge" rows="4" required aria-required="true"></textarea>
            </div>

            <button type="submit" class="btn btn-primary btn-lg">Enviar</button>
            <p class="form-privacy">Respetamos tu privacidad. <a href="/privacy">Leer política.</a></p>
          </form>
        </div>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h4>da-tica</h4>
          <p>Ingeniería de misión crítica desde 2004.</p>
        </div>
        <div class="footer-section">
          <h4>Enlaces</h4>
          <ul>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/servicios">Servicios</a></li>
            <li><a href="/contacto">Contacto</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Legal</h4>
          <ul>
            <li><a href="/privacy">Privacy Policy</a></li>
            <li><a href="/terms">Terms of Service</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Redes</h4>
          <ul>
            <li><a href="https://linkedin.com/company/da-tica" target="_blank">LinkedIn</a></li>
            <li><a href="https://github.com/da-tica" target="_blank">GitHub</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 da-tica.com. Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>

  <!-- Hidden: Calendly Modal -->
  <div id="calendly-modal" class="modal" style="display:none;">
    <div class="modal-content">
      <button class="modal-close" aria-label="Close">×</button>
      <div id="calendly-embed"></div>
    </div>
  </div>

</body>
</html>
```

## JavaScript Integration Files

### persona-detection.js
```javascript
// Detect visitor persona (CTO vs CFO) based on behavior
const personaDetector = {
  signals: {
    cto: ['rust', 'latencia', 'performance', 'architecture', 'kubernetes', 'microservices'],
    cfo: ['roi', 'spdp', 'cost', 'compliance', 'audit', 'budget']
  },

  detect() {
    const visitedPages = JSON.parse(sessionStorage.getItem('visitedPages') || '[]');
    const downloads = JSON.parse(sessionStorage.getItem('downloads') || '[]');
    
    let ctoScore = 0, cfoScore = 0;
    
    visitedPages.forEach(page => {
      this.signals.cto.forEach(sig => { if (page.includes(sig)) ctoScore++; });
      this.signals.cfo.forEach(sig => { if (page.includes(sig)) cfoScore++; });
    });
    
    if (ctoScore > cfoScore) return 'cto';
    if (cfoScore > ctoScore) return 'cfo';
    return 'both';
  },

  apply(persona) {
    localStorage.setItem('persona', persona);
    
    document.querySelectorAll('[data-persona-cto]').forEach(el => {
      el.style.display = (persona === 'cto' || persona === 'both') ? 'block' : 'none';
    });
    
    document.querySelectorAll('[data-persona-cfo]').forEach(el => {
      el.style.display = (persona === 'cfo' || persona === 'both') ? 'block' : 'none';
    });
    
    if (window.gtag) {
      gtag('event', 'persona_detected', { persona });
    }
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const persona = personaDetector.detect();
  personaDetector.apply(persona);
});
```

### cta-tracking.js
```javascript
// Track all CTA interactions
const ctaTracker = {
  track(ctaName) {
    const persona = localStorage.getItem('persona') || 'unknown';
    
    if (window.gtag) {
      gtag('event', 'cta_click', {
        cta_name: ctaName,
        persona: persona,
        page: window.location.pathname
      });
    }
    
    this.handle(ctaName);
  },

  handle(ctaName) {
    const handlers = {
      'solicitar-arquitectura': () => this.scrollToForm('arquitectura'),
      'agendar-sesion-tecnica': () => this.openCalendly('sesion-tecnica'),
      'descargar-roi-calculator': () => this.downloadFile('roi-calculator.xlsx'),
      'calcular-ahorro-opex': () => this.scrollToSection('#roi-section'),
      'ver-caso-exito': () => this.scrollToSection('#case-studies'),
      'header-cta': () => this.openCalendly('header')
    };
    
    (handlers[ctaName] || (() => {}))(ctaName);
  },

  scrollToForm(topic) {
    document.getElementById('contact-form').scrollIntoView({ behavior: 'smooth' });
  },

  openCalendly(type) {
    const modal = document.getElementById('calendly-modal');
    modal.style.display = 'flex';
    
    // Load Calendly embed if not already loaded
    if (!window.Calendly) {
      const script = document.createElement('script');
      script.src = 'https://assets.calendly.com/assets/external/calendar.js';
      document.body.appendChild(script);
    }
    
    setTimeout(() => {
      window.Calendly?.showPopupWidget('https://calendly.com/da-tica/sesion-tecnica');
    }, 500);
  },

  downloadFile(filename) {
    const link = document.createElement('a');
    link.href = `/resources/${filename}`;
    link.download = filename;
    link.click();
  },

  scrollToSection(selector) {
    document.querySelector(selector)?.scrollIntoView({ behavior: 'smooth' });
  }
};

// Attach to all CTA buttons
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-cta]').forEach(btn => {
    btn.addEventListener('click', () => {
      ctaTracker.track(btn.getAttribute('data-cta'));
    });
  });
  
  // Track visited pages
  const visitedPages = JSON.parse(sessionStorage.getItem('visitedPages') || '[]');
  visitedPages.push(window.location.pathname);
  sessionStorage.setItem('visitedPages', JSON.stringify([...new Set(visitedPages)]));
});
```

### counters.js
```javascript
// Animate number counters on scroll
const countersInit = {
  init() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
          this.animateCounter(entry.target);
          entry.target.dataset.animated = 'true';
        }
      });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('[data-target]').forEach(el => observer.observe(el));
  },

  animateCounter(el) {
    const target = parseInt(el.dataset.target);
    const duration = 2000; // 2 seconds
    const increment = target / (duration / 16); // 16ms per frame
    let current = 0;
    
    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        el.textContent = target.toLocaleString();
        clearInterval(timer);
      } else {
        el.textContent = Math.floor(current).toLocaleString();
      }
    }, 16);
  }
};

document.addEventListener('DOMContentLoaded', () => countersInit.init());
```

## Deployment in Coolify

Use el archivo `docker-compose.yml` existente. Solo asegurar:

```yaml
services:
  web:
    image: nginx:1.26.3-alpine
    build:
      context: ./web
      dockerfile: Dockerfile
    expose:
      - "8080"
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:8080/"]
      interval: 10s
      timeout: 5s
      retries: 3
    restart: unless-stopped
```

## Testing Checklist

- [ ] Page Load Performance (LCP <2.5s, CLS <0.1)
- [ ] Responsive Design (mobile 480px, tablet 768px, desktop 1200px+)
- [ ] All CTAs functional and tracked
- [ ] Persona detection working (localStorage check)
- [ ] Counters animating on scroll
- [ ] Form submission working
- [ ] Contact email being sent
- [ ] SEO (meta tags, h1-h6 hierarchy, internal links)
- [ ] Accessibility (WCAG AA contrast, keyboard nav, ARIA labels)
- [ ] Security (HTTPS, no exposed credentials, CSP headers)

## KPIs Post-Launch

- **Engagement:** Avg session 4+ minutes
- **Conversion:** 3-8% form completion
- **Persona:** 60% CTO, 40% CFO traffic
- **CTAs:** Top 3 performing by persona
- **Blog:** 50+ visits/day in 6 months
- **SEO:** Top 10 for 5 primary keywords

## Checklist de Implementación Final

- [ ] Mergear HTML de los 6 skills
- [ ] Implementar JS (persona-detection, cta-tracking, counters)
- [ ] CSS cleanup y optimización
- [ ] Build Docker image
- [ ] Test en Coolify staging
- [ ] User testing (10+ personas)
- [ ] Deploy a producción
- [ ] Monitoreo (Sentry, Datadog, Healthchecks)
- [ ] Publicar blog articles (cronograma)
- [ ] A/B test: titulares hero, orden pain points
