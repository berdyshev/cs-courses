import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

const isProd = process.env.GITHUB_ACTIONS === 'true';

export default defineConfig({
  site: 'https://berdyshev.github.io',
  base: isProd ? '/pgz-plan' : '/',
  markdown: {
    shikiConfig: {
      theme: 'github-light',
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
