<script setup>
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel

  const pstData = reactive({
    creation_datetime: stdDatetimeFormatter.format(new Date()),
    like_count: 0,
    dislike_count: 0,
    content: ''
  })
</script>

<template>
  <page title='New Post' :subtitle='`${user}/${channel}/...`'>
    <div class=post-dt>
      <post-sum-secdata :data=pstData></post-sum-secdata>
      <div>
        Canal: <NuxtLink :to='`/${user}/${channel}`' class=link>{{channelName}}</NuxtLink>
      </div>
      <div>
        Autor@: <NuxtLink :to='`/${user}`' class=link>{{authorName}}</NuxtLink>
      </div>
    </div>
    <div class=centercol>
      <en10da-post-editor v-model=pstData.content></en10da-post-editor>
      <en10da-post :content=pstData.content ></en10da-post>
    </div>
  </page>
</template>
