<script setup>
  const {data: userData} = useAuth()
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel

  const {get} = useAPI()

  const chDataStatus = ref('LOADING')
  const chData = ref({})
  const name = computed(() => chData.value ? chData.value.name : '')
  const authorName = computed(() => chData.value ? chData.value.author.name : '')

  async function requestChData() {
    chDataStatus.value = 'LOADING'
    try {
      chData.value = (await get(`channel/${user}/${channel}`)).data
      chDataStatus.value = 'AVAILABLE'
    } catch (error) {
      chDataStatus.value = error.message
    }
  }

  const pstDataStatus = ref('LOADING')
  const pstData = ref({})
  const posts = computed(() => pstData.value ? pstData.value.posts : '')
  async function requestPstData() {
    try {
      pstDataStatus.value = 'LOADING'
      pstData.value = (await get(`post/search`, {
          params: {
            author_handle: user,
            channel_handle: channel,
            order_by_oldest: true
          }
        })).data
      pstDataStatus.value = 'AVAILABLE'
    } catch (error) {
      pstDataStatus.value = error.message
    }
  }

  requestChData()
  requestPstData()
</script>

<template>
  <page :title=name :subtitle='`${user}/${channel}`'>
    <div class=centercol>
      <div class=max-500 v-if='pstDataStatus === "AVAILABLE"'>
        <post-sum
          v-for='post in posts'
          :key=post.id
          :data=post
        ></post-sum>
      </div>
      <div class='max-500 infobox' v-else-if='pstDataStatus === "LOADING"'>
        <h4>
          Carregando...
        </h4>
      </div>
      <div class='max-500 infobox' v-else>
        <h4>
          Erro!
        </h4>
        <p>
          {{pstDataStatus}}
        </p>
      </div>
    </div>
  </page>
</template>
