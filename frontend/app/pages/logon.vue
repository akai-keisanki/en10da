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
      <div class=max-500>
        <div class=input>
          <label for=handle>Identificador</label>
          <input id=handle type=text placeholder=identificador required v-model=handle>
        </div>
        <div class=input>
          <label for=email>E-mail</label>
          <input id=email type=email placeholder=e-mail required v-model=birthday>
        </div>
        <div class=input>
          <label for=birthday>Aniversário</label>
          <input id=birthday type=date placeholder=aniversário required v-model=birthday>
        </div>
        <div class=input>
          <label for=role>Cargo</label>
          <select id=role required v-model=role>
            <option v-for='r in roles' :key=r :value=r>
              {{r}}
            </option>
          </select>
        </div>
        <button type=submit class=highlight>Cadastrar</button>
      </div>
    </form>
  </page>
</template>
