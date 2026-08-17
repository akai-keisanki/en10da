<script setup>
  import {useWindowSize} from '@vueuse/core'

  const {width, height} = useWindowSize()
  const {data: userData} = useAuth()
</script>

<template>
  <nav>
    <div class=left>
      <img src=/favicon.ico class=navico />
      En10da
    </div>
    <div class=center v-if=userData>
      <Icon name=mdi:account size=20px />
      {{userData.handle}}
    </div>
    <div class=right v-if='width/height > 1'>
      <page-buttons></page-buttons>
    </div>
    <div class=right v-else>
      <NuxtLink to=/pages><button>
        <Icon name=mdi:menu size=20px />
      </button></NuxtLink>
    </div>
  </nav>
</template>
