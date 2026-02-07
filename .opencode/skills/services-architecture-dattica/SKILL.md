---
name: services-architecture-dattica
description: Catálogo de 4 servicios productized (Modernización Legacy, Ultra-Baja Latencia Rust, IA Soberana RAG, Auditoría KNIME) con arquitectura técnica, ROI y pricing boutique premium.
license: MIT
---

# Skill: Services Architecture — Catálogo de Soluciones Productized

## Propósito Estratégico

Transformar la propuesta de valor en soluciones concretas, tangibles y con ROI cuantificado. Cada servicio está diseñado como "productized service" (no custom consulting), lo que acelera la venta y ejecución.

## Los 4 Servicios Obligatorios

### SERVICIO A: Modernización de Legacy & Oracle Convergente

**Tagline:** "De Java Monolítico a Oracle 26ai nativa en 6-12 meses"

**Problema que resuelve:**
- Sistema Java legacy con 15+ años, deuda técnica insostenible
- Datos en silos (DataWarehouse desacoplado de transaccional)
- IA desconectada de la verdad corporativa

**Solución Técnica:**
1. **Análisis de Dependencias:** Scanner de código + mapeo de data flows (Semana 1-2)
2. **Refactorización Gradual:** Migración de tablas a Oracle 26ai con búsqueda vectorial nativa (Mes 2-4)
3. **Convergencia de Datos:** Data Lakehouse pattern con Oracle como single source of truth (Mes 5-8)
4. **IA Soberana:** Integración de RAG auditada, con pre/in/post-filtrado bajo ACID (Mes 9-12)

**Stack Técnico:**
- Oracle 23ai → 26ai (upgrade guiado)
- Oracle Active Data Guard (replicación sincrónica)
- Oracle Vector Database (búsqueda nativa)
- PL/SQL Advanced Optimization
- Kubernetes para orquestación (opcional)

**ROI Esperado:**
- **Año 1:** 30% reducción en OPEX (menos servidores Java, menos data silos)
- **Año 2:** 60% aumento en velocidad de feature releases (monolito modularizado)
- **Año 3+:** IA competitiva integrada; retención de talento técnico

**Inversión Estimada:**
$250K - $500K USD (Boutique Premium: $75-110/hora × 3500-6700 horas)

**Duración:** 6-12 meses (según complejidad)

**Entregables:**
- ✅ Arquitectura convergente documentada
- ✅ Pipeline de migración de datos automatizado
- ✅ Modelo RAG auditado en producción
- ✅ Runbooks operacionales
- ✅ Training para DBA + DevOps team

---

### SERVICIO B: Ingeniería de Ultra-Baja Latencia (Rust)

**Tagline:** "4x menos RAM, <50ms garantizado. Tu infraestructura, 10x más ágil."

**Problema que resuelve:**
- Microservicios Java con GC pauses (50-200ms cada 30s)
- Costo de nube escalando 40-50% YoY sin crecimiento de tráfico
- Latencia predecible = imposible (variable según GC)

**Solución Técnica:**
1. **Profiling Selectivo:** Identificar servicios críticos donde latencia importa (Semana 1)
2. **Reescritura en Rust:** Traducción gradual con tests exhaustivos (Mes 2-6, según líneas de código)
3. **Zero-Copy Serialization:** Protobuf/Bincode para eficiencia máxima
4. **Deployment Canary:** Roll-out gradual con monitoring de latencia en P99, P95 (Mes 7-8)

**Stack Técnico:**
- Rust + Tokio (async runtime)
- gRPC + Protocol Buffers
- Prometheus + Grafana (latency tracking)
- Kubernetes + Istio (service mesh)
- Load testing con k6 / Locust

**ROI Esperado:**
- **Año 1:** 40-50% reducción en OPEX cloud (fewer pods needed)
- **Latencia:** P99 <50ms garantizado (vs. 200ms+ con Java)
- **Experiencia Usuario:** 15-25% aumento en conversion rate (percepción de velocidad)

**Inversión Estimada:**
$150K - $350K USD (según número de servicios a reescribir)

**Duración:** 3-8 meses (servicios pequeños vs. monolitos grandes)

**Entregables:**
- ✅ Código Rust en producción (canary + monitored)
- ✅ Benchmarks públicos (latencia Rust vs. Java)
- ✅ Runbooks de troubleshooting
- ✅ Training para equipo backend

---

### SERVICIO C: IA Soberana & Arquitectura RAG Auditada

**Tagline:** "IA explicable, bajo control absoluto. Sin cajas negras. Sin fugas de dato."

**Problema que resuelve:**
- Equipos usan ChatGPT directamente; datos corporativos expuestos a terceros
- IA responde cosas incorrectas porque no ve datos corporativos
- Zero audit trail = riesgo regulatorio

**Solución Técnica:**
1. **Arquitectura RAG de 3 Niveles:**
   - **Pre-filtrado:** Control de acceso basado en roles SQL
   - **In-filtrado:** Búsqueda vectorial ultra-rápida (Oracle 26ai HNSW/IVF)
   - **Post-filtrado:** Reglas de negocio + fact-checking antes de LLM

2. **Implementación:**
   - Vector embeddings: locales (sentence-transformers) o Azure OpenAI (EU instance)
   - LLM: Llama 2 (privado) o Claude (con contrato de privacidad)
   - Audit Log: Cada prompt + respuesta queda registrada en Oracle

3. **Governance:**
   - Data lineage automático (qué dato usó la IA)
   - Explicabilidad: "Basado en documentos X, Y, Z"
   - Trazabilidad regulatoria (SPDP-ready)

**Stack Técnico:**
- Oracle 26ai (Vector Database)
- LangChain / LlamaIndex (RAG orchestration)
- Sentence Transformers o Azure OpenAI Embeddings
- Audit table en Oracle con trigger automation
- Kafka (opcional) para logging distribuido

**ROI Esperado:**
- **Año 1:** 20-30% aumento en productividad (IA asiste, no reemplaza)
- **Cumplimiento:** 100% preparado para auditoría SPDP
- **Talento:** Reclutamiento de especialistas en GenAI (competitive advantage)

**Inversión Estimada:**
$100K - $250K USD

**Duración:** 3-6 meses

**Entregables:**
- ✅ Pipeline RAG funcional en producción
- ✅ Dashboard de governance (quién preguntó, qué datos usó)
- ✅ Audit report template para reguladores
- ✅ Documentation de arquitectura
- ✅ Training: uso responsable de IA

---

### SERVICIO D: Auditoría Proactiva & Gobernanza C-Suite (KNIME)

**Tagline:** "Auditoría completa en 2 semanas. Cero sorpresas regulatorias. 85% reducción de tiempo."

**Problema que resuelve:**
- Auditorías manuales: 6+ meses, caras, muestras (no población)
- Incumplimiento SPDP detectado en inspección regulatoria = multas
- No hay visibilidad real de quién accede a qué dato, cuándo, por qué

**Solución Técnica:**
1. **Auditoría de Población Completa:**
   - KNIME workflows analizan 100% de datos, no muestras
   - Ley de Benford para detectar anomalías estadísticas
   - Clustering de patrones de acceso anómalo

2. **Anonimización Automática:**
   - Microsoft Presidio (NER + regex) para identificar PII
   - Masking contextual: nombres → "USER_XXX", DNI → "DNI_XXXX"
   - GDPR/LOPDP-ready

3. **Governance Dashboard:**
   - Quién accedió a qué dato, cuándo, por qué (lineage completo)
   - Alerts automáticos: accesos anómalos, violaciones de políticas
   - Reports templated para reguladores

**Stack Técnico:**
- KNIME Analytics Platform (workflows visuales)
- Python scripts (para custom logic)
- Microsoft Presidio (PII detection)
- SQL (análisis de access logs)
- Grafana (dashboards)

**ROI Esperado:**
- **Cumplimiento:** 100% SPDP + GDPR verified
- **Tiempo Auditoría:** De 6 meses → 2 semanas
- **Costos:** 85% reducción en horas de auditoría
- **Riesgo Legal:** Multas potenciales evitadas ($5-50M)

**Inversión Estimada:**
$80K - $180K USD

**Duración:** 2-4 meses (setup + workflow design + deployment)

**Entregables:**
- ✅ KNIME workflows en producción (orchestrado con cron/Airflow)
- ✅ Governance dashboard accesible 24/7
- ✅ Reports automáticos (mensuales / trimestrales)
- ✅ Runbooks de escalación
- ✅ Training para compliance team

---

## Matriz de Combinaciones (Bundles)

Para acelerar venta y maximizar ROI acumulado, ofrecer bundles:

| Bundle | Servicios | Inversión | Timeline | Ideal Para |
|--------|-----------|-----------|----------|-----------|
| **Starter** | C + D | $180K-430K | 5-10 meses | Empresas reguladas sin IA aún |
| **Growth** | A + B + C | $500K-1.1M | 9-18 meses | Midmarket con legacy + ambición cloud |
| **Complete** | A + B + C + D | $630K-1.3M | 12-24 meses | Enterprise transformación digital |

---

## Pricing: Boutique Premium

**Tarifa Horaria Base:** $75 - $110 USD/hora (benchmarks Latinoamérica 2026)

**Justificación:**
- Vs. consultoras grandes (McKinsey, Accenture): 60% menor
- Vs. consultoras locales genéricas: 50% premium (especialización)
- ROI positivo en 12-18 meses (ahorro OPEX > inversión)

**Modelo de Facturación:**
- Fixed-price por servicio (predictibilidad)
- Hito-based: pagos al completar arquitectura, MVP, producción
- SLA incluido: respuesta en 24h, uptime 99.9%

---

## Estructura HTML/Tailwind para Página Web

```html
<section class="services py-20 px-6 bg-white">
  <div class="max-w-6xl mx-auto">
    
    <h2 class="text-4xl font-black text-slate-900 mb-4 text-center">
      Soluciones Productized para 2026
    </h2>
    <p class="text-center text-gray-600 mb-16 max-w-2xl mx-auto">
      Cada servicio es un bloque de arquitectura. Combínalos según tu roadmap.
    </p>

    <!-- Grid de 4 Servicios -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">

      <!-- Service A -->
      <article class="service-card bg-gradient-to-br from-blue-50 to-blue-100 rounded-lg p-8 border-2 border-blue-200">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-4xl">🏛️</span>
          <h3 class="text-2xl font-bold text-slate-900">Modernización Legacy</h3>
        </div>
        <p class="text-gray-700 mb-6">
          De Java monolítico a Oracle 26ai convergente. IA soberana integrada en 6-12 meses.
        </p>
        <ul class="space-y-2 mb-6 text-sm text-gray-700">
          <li>✅ Análisis de dependencias completo</li>
          <li>✅ Migración de datos gradual</li>
          <li>✅ Oracle Active Data Guard</li>
          <li>✅ IA nativa + RAG auditada</li>
        </ul>
        <div class="mb-6 p-4 bg-blue-200 rounded text-sm">
          <p class="font-bold text-blue-900">ROI Esperado:</p>
          <p class="text-blue-800">30% OPEX Año 1 | 60% velocity Año 2</p>
        </div>
        <p class="font-bold text-blue-700 mb-4">$250K - $500K | 6-12 meses</p>
        <button class="w-full px-4 py-2 bg-blue-600 text-white font-bold rounded hover:bg-blue-700">
          Ver Detalles
        </button>
      </article>

      <!-- Service B -->
      <article class="service-card bg-gradient-to-br from-green-50 to-green-100 rounded-lg p-8 border-2 border-green-200">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-4xl">⚡</span>
          <h3 class="text-2xl font-bold text-slate-900">Ultra-Baja Latencia</h3>
        </div>
        <p class="text-gray-700 mb-6">
          Reescritura selectiva en Rust. 4x menos RAM. &lt;50ms garantizado.
        </p>
        <ul class="space-y-2 mb-6 text-sm text-gray-700">
          <li>✅ Profiling de servicios críticos</li>
          <li>✅ Reescritura en Rust + Tokio</li>
          <li>✅ Deployment canary monitoreado</li>
          <li>✅ Benchmarks públicos</li>
        </ul>
        <div class="mb-6 p-4 bg-green-200 rounded text-sm">
          <p class="font-bold text-green-900">ROI Esperado:</p>
          <p class="text-green-800">40-50% OPEX cloud | +15% conversion</p>
        </div>
        <p class="font-bold text-green-700 mb-4">$150K - $350K | 3-8 meses</p>
        <button class="w-full px-4 py-2 bg-green-600 text-white font-bold rounded hover:bg-green-700">
          Ver Detalles
        </button>
      </article>

      <!-- Service C -->
      <article class="service-card bg-gradient-to-br from-purple-50 to-purple-100 rounded-lg p-8 border-2 border-purple-200">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-4xl">🧠</span>
          <h3 class="text-2xl font-bold text-slate-900">IA Soberana & RAG</h3>
        </div>
        <p class="text-gray-700 mb-6">
          IA explicable, bajo control. Sin cajas negras. Auditoría integrada.
        </p>
        <ul class="space-y-2 mb-6 text-sm text-gray-700">
          <li>✅ Arquitectura RAG 3-niveles</li>
          <li>✅ Embeddings + búsqueda vectorial</li>
          <li>✅ Audit trail automático</li>
          <li>✅ Cumplimiento SPDP</li>
        </ul>
        <div class="mb-6 p-4 bg-purple-200 rounded text-sm">
          <p class="font-bold text-purple-900">ROI Esperado:</p>
          <p class="text-purple-800">20-30% productividad | 100% SPDP-ready</p>
        </div>
        <p class="font-bold text-purple-700 mb-4">$100K - $250K | 3-6 meses</p>
        <button class="w-full px-4 py-2 bg-purple-600 text-white font-bold rounded hover:bg-purple-700">
          Ver Detalles
        </button>
      </article>

      <!-- Service D -->
      <article class="service-card bg-gradient-to-br from-yellow-50 to-yellow-100 rounded-lg p-8 border-2 border-yellow-200">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-4xl">📊</span>
          <h3 class="text-2xl font-bold text-slate-900">Auditoría Proactiva</h3>
        </div>
        <p class="text-gray-700 mb-6">
          KNIME + Benford. Auditoría completa en 2 semanas. 85% menos tiempo.
        </p>
        <ul class="space-y-2 mb-6 text-sm text-gray-700">
          <li>✅ Análisis de población completa</li>
          <li>✅ Detección de anomalías</li>
          <li>✅ Anonimización con Presidio</li>
          <li>✅ Dashboard gobernanza 24/7</li>
        </ul>
        <div class="mb-6 p-4 bg-yellow-200 rounded text-sm">
          <p class="font-bold text-yellow-900">ROI Esperado:</p>
          <p class="text-yellow-800">100% cumplimiento | $5-50M multas evitadas</p>
        </div>
        <p class="font-bold text-yellow-700 mb-4">$80K - $180K | 2-4 meses</p>
        <button class="w-full px-4 py-2 bg-yellow-600 text-white font-bold rounded hover:bg-yellow-700">
          Ver Detalles
        </button>
      </article>

    </div>

    <!-- Bundles Section -->
    <div class="bg-slate-100 rounded-lg p-12 text-center">
      <h3 class="text-2xl font-bold text-slate-900 mb-8">Bundles: Combina Servicios</h3>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white rounded-lg p-6 border-2 border-slate-300">
          <p class="font-bold text-slate-900 mb-2">Starter</p>
          <p class="text-sm text-gray-600">Servicios C + D</p>
          <p class="text-lg font-bold text-slate-900 mt-4">$180K - $430K</p>
        </div>
        <div class="bg-white rounded-lg p-6 border-2 border-blue-400 shadow-lg">
          <p class="font-bold text-slate-900 mb-2">Growth ⭐ Popular</p>
          <p class="text-sm text-gray-600">Servicios A + B + C</p>
          <p class="text-lg font-bold text-slate-900 mt-4">$500K - $1.1M</p>
        </div>
        <div class="bg-white rounded-lg p-6 border-2 border-slate-300">
          <p class="font-bold text-slate-900 mb-2">Complete</p>
          <p class="text-sm text-gray-600">Servicios A + B + C + D</p>
          <p class="text-lg font-bold text-slate-900 mt-4">$630K - $1.3M</p>
        </div>
      </div>
    </div>

  </div>
</section>
```

## Dinámicas de Interacción

- **Accordion Expandible:** Cada servicio expandible con detalles técnicos
- **Calculadora de ROI:** Input (líneas de código, usuarios, OPEX actual) → Output (ahorro estimado)
- **Comparison Table:** Servicio A vs. B vs. C vs. D (features, timeline, cost)
- **CTA Contextual:** "Ver detalles" → modal con documentación técnica + case study

## Integración con Flujo de Página

**Secuencia Natural:**
1. Hero (Promesa)
2. Pain Points (Agitación)
3. Authority Metrics (Credibilidad)
4. **Services** (Soluciones específicas) ← AQUÍ
5. Thought Leadership (Educación)
6. Contact / CTA Final

## Checklist

- [ ] Documentar stack técnico completo para cada servicio
- [ ] Crear case studies (anonimizados) por servicio
- [ ] Implementar calculadora de ROI interactiva
- [ ] Testing A/B: orden de servicios (impacto vs. timeline)
- [ ] Medir engagement: clicks en "Ver detalles"
- [ ] SEO: cada servicio en su propia página (/services/legacy, /services/rust, etc.)
- [ ] Pricing: validar con benchmarks locales de mercado

## Notas Comerciales

- **Flexibilidad:** Servicios se venden individuales O en bundle (10-15% descuento)
- **Contrato:** SLA de 99.9% uptime para infraestructura desplegada
- **Soporte:** 12 meses de SLA incluido; después, modelo retainer opcional ($10K-30K/mes)
- **Escalación:** Si proyecto excede timeline/budget en 20%, se revisa scope (no sobrecostos sorpresa)