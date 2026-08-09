<script setup>
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel
  const post = route.params.post
</script>

<template>
  <page :title=post :subtitle='`${user}/${channel}/${post}`'>
    This is a post.
  </page>
</template>
