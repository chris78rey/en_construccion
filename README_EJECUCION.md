# Da-TIca - Astro + Vue

## 1) Instalar dependencias
```bash
npm install
```

## 2) Ejecutar en desarrollo
```bash
npm run dev
```

## 3) Generar build de producción
```bash
npm run build
```

## 4) Probar build localmente
```bash
npm run preview
```

## 5) Docker
```bash
docker build -t datica-astro-vue .
docker run --rm -p 8080:8080 datica-astro-vue
```

## 6) Rutas principales
- /
- /sitios-web/
- /data-mining/
- /cursos/

## 7) Ajustes rápidos
- Correo: `src/data/site.js`
- Enlaces del menú: `src/data/site.js`
- Textos principales: `src/pages/*.astro`
- Colores y estilos globales: `src/styles/global.css`
