<template>
  <div class="faq-list">
    <article v-for="(item, index) in items" :key="index" class="faq-item">
      <button class="faq-question" type="button" @click="toggle(index)">
        <span>{{ item.question }}</span>
        <span class="faq-icon" aria-hidden="true">{{ openIndex === index ? '−' : '+' }}</span>
      </button>
      <div v-if="openIndex === index" class="faq-answer">
        <p>{{ item.answer }}</p>
      </div>
    </article>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  items: {
    type: Array,
    default: () => [],
  },
});

const openIndex = ref(0);

const toggle = (index) => {
  openIndex.value = openIndex.value === index ? -1 : index;
};
</script>
