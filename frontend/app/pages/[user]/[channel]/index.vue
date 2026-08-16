<script setup>
  const {data: userData} = useAuth()
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel

  const {get} = useAPI()

  const chResp = await get(`channel/${user}/${channel}`)
  const {name, author: {name: authorName}} = chResp.data

  const pstResp = await get(`post/search`, {
    params: {
      author_handle: user,
      channel_handle: channel,
      order_by_oldest: true
    }
  })
  const posts = pstResp.data.posts
</script>

<template>
  <page :title=name :subtitle='`${user}/${channel}`'>
    <div class=post-list>
      <div class=max-500>
        <post-sum
          v-for='post in posts'
          :key=post.id
          :data=post
        ></post-sum>
      </div>
    </div>
  </page>
</template>
