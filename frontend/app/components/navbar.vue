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
      {{userData.handle}}
    </div>
    <div class=right v-if='width/height > 1'>
      <page-buttons></page-buttons>
    </div>
    <div class=right v-else>
      <NuxtLink to=/pages><button>
        <Icon name="mdi:hamburger-menu" />
      </button></NuxtLink>
    </div>
  </nav>
</template>
