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
      <h3>
        Você é nov@ no En10da?
      </h3>
      <p>
        Caso não possua uma conta, crie uma na página de <NuxtLink to=/logon class=link>logon</NuxtLink>.
      </p>
    </div>
    <form @submit.prevent=makeLogin>
      <input id=handle type=text placeholder=identificador required v-model=handle>
      <input id=password type=password placeholder=senha required v-if=!emailLogin v-model=password>
      <input id=email_code v-if=emailLogin v-model=email_code>
      <button type=submit class=highlight></button>
    </form>
  </page>
</template>
