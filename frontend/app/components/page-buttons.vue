<script setup>
  const props = defineProps({
    withNames: {
      type: Boolean,
      required: false,
      default: false
    }
  })
</script>

<template>
  <NuxtLink to=/welcome><button>
    <Icon name=mdi:home size=15px />
    <div v-show=withNames>
      Início
    </div>
  </button></NuxtLink>
  <button>
    <Icon name=mdi:magnify size=15px />
    <div v-show=withNames>
      Pesquisa
    </div>
  </button> <!-- WIP -->
  <NuxtLink to=/login><button>
    <Icon name=mdi:login size=15px />
    <div v-show=withNames>
      Login
    </div>
  </button></NuxtLink>
</template>
