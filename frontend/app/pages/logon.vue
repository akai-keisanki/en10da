<script setup>
  const {token, signIn, getSession} = useAuth
  const {get, post} = useAPI()

  const rolesStatus = ref('LOADING')
  const roles = ref([])

  async function requestRoles() {
    try {
      rolesStatus.value = 'LOADING'
      roles.value = (await get('user/roles')).data.user_roles
      rolesStatus.value = 'AVAILABLE'
    } catch (error) {
      rolesStatus.value = error.message
    }
  }

  const emailLogin = ref(false)

  const handle = ref('')
  const email = ref('')
  const birthday = ref('')
  const role = ref('')

  const error = ref('')

  async function makeLogon() {
  }

  requestRoles()
</script>

<template>
  <page title=Logon subtitle='cadastro de usuário'>
    <form @submit.prevent=makeLogon>
      <div class=max-500>
        <div class=input>
          <label for=handle>Identificador</label>
          <input id=handle type=text placeholder=identificador required v-model=handle>
        </div>
        <div class='infobox'>
          <p>
            O identificador é um nome composto somente por letras (minúsculas (a-z) e maiúsculas (A-Z)) sem acentuação gráfica, dígitos (1-9) e os caracteres underline (_) e hífen (-), sem espaços.
          </p>
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
            <option value='' disabled hidden selected v-if='rolesStatus === "AVAILABLE"'>Selecione um cargo...</option>
            <option value='' disabled hidden selected v-else-if='rolesStatus === "LOADING"'>Carregando...</option>
            <option value='' disabled hidden selected v-else>Erro ao carregar cargos.</option>
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
