export const site = {
  brand: 'Da-TIca',
  email: 'crrb@da-tica.com',
  youtube: 'https://www.youtube.com/@Da-Tica',
  whatsapp: 'https://wa.me/593000000000',
  headline: 'Sitios web, Data Mining e IA aplicada con una estructura clara y ligera.',
  description:
    'Consultoría digital orientada a presencia web, análisis de datos, automatización e inteligencia artificial aplicada para negocios, profesionales y proyectos que necesitan comunicar mejor y operar con más claridad.',
};

export const nav = [
  { href: '/', label: 'Inicio' },
  { href: '/sitios-web/', label: 'Sitios web' },
  { href: '/data-mining/', label: 'Data Mining' },
  { href: '/cursos/', label: 'Cursos' },
];

export const services = [
  {
    index: '01',
    href: '/sitios-web/',
    label: 'Sitios web',
    title: 'Presencia web profesional para negocio, consultorio o marca personal',
    description:
      'Sitios claros, rápidos y pensados para que el visitante entienda el servicio, encuentre contacto y perciba una imagen profesional desde la primera visita.',
    bullets: ['Diseño limpio', 'SEO base', 'Carga rápida'],
  },
  {
    index: '02',
    href: '/data-mining/',
    label: 'Data Mining',
    title: 'Información útil para detectar patrones, problemas y oportunidades',
    description:
      'Servicios orientados a limpieza, exploración y entendimiento de datos para apoyar decisiones, priorizar mejoras y preparar automatización o IA aplicada.',
    bullets: ['Análisis útil', 'Hallazgos', 'Decisiones'],
  },
  {
    index: '03',
    href: '/cursos/',
    label: 'Cursos',
    title: 'Formación práctica en datos, automatización, prompts e IA aplicada',
    description:
      'Una línea de contenidos orientada a uso real, no solo teoría, para ayudar a aprender herramientas que generen valor desde etapas tempranas.',
    bullets: ['Aplicación real', 'Explicación clara', 'Próximamente'],
  },
];

export const faqSitios = [
  {
    question: '¿Astro y Vue sirven para un sitio profesional?',
    answer:
      'Sí. Astro deja la mayor parte del sitio como HTML estático muy rápido y Vue se puede usar solo en los bloques que necesitan interacción, como menús, preguntas frecuentes o widgets de contacto.',
  },
  {
    question: '¿El sitio puede seguir siendo liviano en VPS?',
    answer:
      'Sí. Esta estructura está pensada para generar archivos estáticos y enviar poco JavaScript al navegador. Eso reduce consumo de CPU, memoria y ancho de banda frente a una app pesada.',
  },
  {
    question: '¿Se puede mantener el sitio actual y luego crecer?',
    answer:
      'Sí. La base queda lista para sumar más páginas, blog, landing pages, formularios o integraciones sin tener que rehacer toda la estructura desde cero.',
  },
  {
    question: '¿Qué se necesita para publicarlo?',
    answer:
      'Dominio, hosting o VPS y el build final del proyecto. Si ya existe un Nginx sirviendo estáticos, la salida de Astro se puede publicar sin necesidad de backend adicional.',
  },
];

export const faqData = [
  {
    question: '¿Qué tipo de datos se pueden trabajar?',
    answer:
      'Tablas de Excel, CSV, exportaciones de sistemas, registros operativos y bases que necesiten limpieza, revisión o interpretación para tomar decisiones con más claridad.',
  },
  {
    question: '¿Sirve aunque los datos estén desordenados?',
    answer:
      'Sí. Una parte clave del trabajo es ordenar, depurar y estructurar los datos antes de buscar patrones o generar conclusiones útiles.',
  },
  {
    question: '¿Esto ayuda a preparar automatización o IA?',
    answer:
      'Sí. Cuando la información se organiza bien, luego es más fácil crear dashboards, reglas automáticas, reportes y soluciones con inteligencia artificial aplicada.',
  },
];
