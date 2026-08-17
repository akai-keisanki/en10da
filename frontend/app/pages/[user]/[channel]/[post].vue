<script setup>
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel
  const post = route.params.post

  const {get} = useAPI()

  const pstDataStatus = ref("LOADING")
  const pstData = ref({})
  const title = computed(() => pstData.value?.title ?? '')
  const content = computed(() => pstData.value?.content ?? '')
  const channelName = computed(() => pstData.value?.channel?.name ?? '')
  const authorName = computed(() => pstData.value?.author?.name ?? '')

  async function requestPstData() {
    try {
      pstDataStatus.value = "LOADING"
      pstData.value = (await get(`post/${user}/${channel}/${post}`)).data
      pstDataStatus.value = "AVAILABLE"
    } catch (error) {
      pstDataStatus.value = error.message
    }
  }

  requestPstData()
</script>

<template>
  <page :title=title :subtitle='`${user}/${channel}/${post}`'>
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
      <en10da-post v-if='pstDataStatus === "AVAILABLE"' :content=content ></en10da-post>
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
