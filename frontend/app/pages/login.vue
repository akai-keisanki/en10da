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
    <div class=infobox>
      <h4>
        Você é nov@ no En10da?
      </h4>
      <p>
        Caso não possua uma conta, crie uma na página de <NuxtLink to=/logon class=link>logon</NuxtLink>.
      </p>
    </div>
    <form @submit.prevent=makeLogin>
      <div class=max-500>
        <div class=input>
          <label for=handle>Identificador</label>
          <input id=handle type=text placeholder=identificador required v-model=handle>
        </div>
        <div class=input>
          <label for=password>Senha</label>
          <input id=password type=password placeholder=senha required v-if=!emailLogin v-model=password>
        </div>
        <div class=input>
          <label for=email_code>Código do e-mail</label>
          <input id=email_code v-if=emailLogin v-model=email_code>
        </div>
        <button type=submit class=highlight></button>
      </div>
    </form>
  </page>
</template>
