<script setup>
  const {token, signIn, getSession} = useAuth
  const {get, post} = useAPI()

  let roles = await get('user/roles')
  roles = roles.data.user_roles

  const emailLogin = ref(false)

  const handle = ref('')
  const email = ref('')
  const birthday = ref('')
  const role = ref('')
</script>

<template>
  <page title=Logon subtitle='cadastro de usuário'>
    <form @submit.prevent=makeLogon>
      <input id=handle type=text placeholder=identificador required v-model=handle>
      <input id=email type=email placeholder=e-mail required v-model=birthday>
      <input id=birthday type=date placeholder=aniversário required v-model=birthday>
      <select id=role required v-model=role>
        <option v-for='r in roles' :key=r :value=r>
          {{r}}
        </option>
      </select>
      <button type=submit class=highlight>Cadastrar</button>
    </form>
  </page>
</template>
