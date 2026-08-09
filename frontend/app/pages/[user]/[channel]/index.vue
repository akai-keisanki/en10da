<script setup>
  const route = useRoute()
  const user = route.params.user
  const channel = route.params.channel
  await navigateTo(`/${user}/${channel}/sobre`)
</script>
