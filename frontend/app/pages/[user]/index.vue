<script setup>
  const route = useRoute()
  const user = route.params.user
  await navigateTo(`/${user}/${user}`)
</script>
