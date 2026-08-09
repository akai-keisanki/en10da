<script setup>
  const {token, signIn, getSession} = useAuth
  const api = useAPI()

  const emailLogin = ref(false)

  const handle = ref('')
  const password = ref('')
  const email_code = ref('')
</script>

<template>
  <page title=Login>
    <form @submit.prevent=makeLogin>
      <input id=handle type=text placeholder=identificador required v-model=handle>
      <input id=password type=password placeholder=senha required v-if=!emailLogin v-model=password>
      <input id=email_code v-if=emailLogin v-model=email_code>
      <button type=submit class=highlight></button>
    </form>
  </page>
</template>
