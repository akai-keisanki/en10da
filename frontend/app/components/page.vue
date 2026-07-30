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
  <main>
    <navbar></navbar>
    <page-title :title=title :subtitle=subtitle></page-title>
    <slot />
  </main>
</template>
