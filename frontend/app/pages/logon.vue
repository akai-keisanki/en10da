<script setup>
  const {token, signIn, getSession} = useAuth
  const api = useAPI()

  const emailLogin = ref(false)

  const handle = ref('')
  const email = ref('')
  const birthday = ref('')
  const role = ref('')
</script>

<template>
  <page title=Logon>
    <form @submit.prevent=makeLogon>
      <input id=handle type=text placeholder=identificador required v-model=handle>
      <input id=email type=email placeholder=e-mail required v-model=birthday>
      <input id=birthday type=date placeholder=aniversário required v-model=birthday>
      <select id=role required v-model>
      </select>
      <button type=submit class=highlight></button>
    </form>
  </page>
</template>
