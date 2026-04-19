Paquete final limpio para entregar al programador.

Archivos a copiar dentro de la carpeta web/ del proyecto:
- styles.css
- index.html
- sitios-web.html
- data-mining.html
- cursos.html

Notas:
1. No hace falta tocar Docker ni docker-compose si los enlaces usan .html.
2. Si el despliegue actual sigue apuntando a la carpeta web/, estos archivos quedan servidos por nginx al hacer rebuild.
3. Las imágenes siguen apuntando a:
   - web/img/hero-data-center.png
   - web/img/services-data-flow.png
   - web/img/ai-governance-shield.png
