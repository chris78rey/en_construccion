<template>
  <button
    class="theme-toggle"
    type="button"
    :aria-label="isDark ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro'"
    @click="toggleTheme"
  >
    <span aria-hidden="true">{{ isDark ? '☀️' : '🌙' }}</span>
  </button>
</template>

<script setup>
import { onMounted, ref } from 'vue';

const key = 'datica-theme';
const isDark = ref(false);

const applyTheme = (theme) => {
  document.documentElement.dataset.theme = theme;
  isDark.value = theme === 'dark';
};

const toggleTheme = () => {
  const nextTheme = isDark.value ? 'light' : 'dark';
  localStorage.setItem(key, nextTheme);
  applyTheme(nextTheme);
};

onMounted(() => {
  const current = document.documentElement.dataset.theme || 'light';
  applyTheme(current);
});
</script>
