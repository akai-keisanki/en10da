<script setup>
  const props = defineProps({
    data: {
      type: Object,
      required: true
    },
  })
</script>

<template>
  <NuxtLink :to='`/${data.author.handle}/${data.channel.handle}/${data.handle}`'><div class=post-sum>
    <div class='cttcol_l'>
      <h4>{{data.title}}</h4>
      <div class=path>{{data.author.handle}}/{{data.channel.handle}}/{{data.handle}}</div>
    </div>
    <div class=cttcol_r>
      <post-sum-secdata :data=data></post-sum-secdata>
    </div>
  </div></NuxtLink>
</template>
