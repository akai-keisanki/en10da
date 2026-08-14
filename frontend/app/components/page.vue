<script setup>
const props = defineProps({
  title: {
    type: String,
    required: false,
    default: null
  },
  subtitle: {
    type: String,
    required: false,
    default: null
  }
})
</script>

<template>
  <main>
    <navbar></navbar>
    <page-title
      v-if="title !== null"
      :title="title"
      :subtitle="subtitle"
    ></page-title>
    <slot />
    <app-footer></app-footer>
  </main>
</template>
