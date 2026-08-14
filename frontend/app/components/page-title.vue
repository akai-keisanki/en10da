<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String,
    required: false,
    default: null
  }
})
</script>

<template>
  <header class="page_title">
    <h1>{{ title }}</h1>
    <h2 v-if="subtitle !== null">{{ subtitle }}</h2>
  </header>
</template>
