# Da-TIca - Migración a Astro + Vue

## 1) Requisitos
- Node.js 22.12.0 o superior
- npm

## 2) Instalar dependencias
```bash
npm install
```

## 3) Ejecutar en desarrollo
```bash
npm run dev
```

## 4) Generar build de producción
```bash
npm run build
```

## 5) Probar build localmente
```bash
npm run preview
```

## 6) Docker
```bash
docker build -t datica-astro-vue .
docker run --rm -p 8080:8080 datica-astro-vue
```

## 7) Rutas principales
- /
- /sitios-web/
- /data-mining/
- /cursos/

## 8) Ajustes rápidos
- Correo y enlaces: `src/data/site.js`
- Textos principales: `src/pages/*.astro`
- Colores y estilos: `src/styles/global.css`
- Proxy Nginx: `nginx/default.conf`
