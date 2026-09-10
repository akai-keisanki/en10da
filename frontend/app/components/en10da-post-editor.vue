<script setup>
  const model = defineModel({
    type: String,
    required: true
  })
</script>

<template>
  <textarea 
    class=post-editor
    v-model=model
    placeholder='Write your post here...'
  ></textarea>
</template>
