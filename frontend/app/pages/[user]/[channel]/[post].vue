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
    <div class=post-dt>
      <post-sum-secdata :data=resp.data></post-sum-secdata>
      <div>
        Canal: <NuxtLink :to='`/${user}/${channel}`' class=link>{{resp.data.channel.name}}</NuxtLink>
      </div>
      <div>
        Autor@: <NuxtLink :to='`/${user}`' class=link>{{resp.data.author.name}}</NuxtLink>
      </div>
    </div>
    <en10da-post :content=content></en10da-post>
  </page>
</template>
