import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';

export default defineConfig({
  site: 'https://da-tica.com',
  integrations: [vue()],
  output: 'static',
  trailingSlash: 'always',
  vite: {
    server: {
      watch: {
        usePolling: false,
      },
    },
  },
});
