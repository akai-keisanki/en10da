<script setup>
  const props = defineProps({
    data: {
      type: Object,
      required: true
    },
  })
</script>

<template>
  <div class=lndl>
    <div class=likes>
      <button><Icon name=mdi:thumb-up size=20px /></button>
      +{{data.like_count}}
    </div>
    <div class=dislikes>
      <button><Icon name=mdi:thumb-down size=20px /></button>
      -{{data.dislike_count}}
    </div>
  </div>
  <div class=datetime>{{data.creation_datetime}}</div>
</template>
