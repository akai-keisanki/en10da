<script setup>
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel
  const post = route.params.post

  const {get} = useAPI()

  const resp = await get(`post/${user}/${channel}/${post}`)
  const {title, content} = resp.data
</script>

<template>
  <page :title=title :subtitle='`${user}/${channel}/${post}`'>
    <en10da-post :content=content></en10da-post>
  </page>
</template>
