<script setup>
  const {token, signIn, getSession} = useAuth
  const {post} = useAPI()

  const emailLogin = ref(false)

  const handle = ref('')
  const password = ref('')
  const emailCode = ref('')

  const error = ref(null)

  async function makeLogin() {
    try {
      let resp = null

      if (emailLogin)
        resp = await signIn(
          {
            handle,
            email_code: emailCode
          },
          {
            redirect: false,
            endpoint: {path: 'user/login/email', method: 'post'}
          }
        )
      else
        resp = await signIn(
          {handle, password},
          {redirect: false}
        )

      if (!resp || resp.error)
        error.value = 'Erro no login! Confira o identificador e a senha.'
    } catch (e) {
      error.value = 'Erro de requisição.'
      console.log(e)
    }
  }
</script>

<template>
  <page title=Login>
    <NuxtLink to=/logon><div class='infobox link'>
      <h4>
        Você é nov@ no En10da?
      </h4>
      <p>
        Caso não possua uma conta, clique aqui para encaminhar-se à página de logon.
      </p>
    </div></NuxtLink>
    <form @submit.prevent='makeLogin()'>
      <div class=max-500>
        <div class=input>
          <label for=handle>Identificador</label>
          <input id=handle type=text placeholder=identificador required v-model=handle>
        </div>
        <div class=horinput>
          <label for=email_login>Login pelo e-mail</label>
          <input id=email_login type=checkbox v-model=emailLogin>
        </div>
        <Transition name=fade>
          <div class='input' v-show=!emailLogin>
            <label for=password>Senha</label>
            <input id=password type=password placeholder=******** required  v-model=password>
          </div>
        </Transition>
        <Transition name=fade>
          <NuxtLink to=/send-email-code><div class='infobox link' v-show=emailLogin>
            <p>
              Caso não possua um código de e-mail, clique aqui para encaminhar-se ao formulário de envio deste código.
            </p>
          </div></NuxtLink>
        </Transition>
        <Transition name=fade>
          <div class='input' v-show=emailLogin>
            <label for=email_code>Código do e-mail</label>
            <input id=email_code placeholder=... v-model=emailCode>
          </div>
        </Transition>
        <button type=submit class=highlight>Login</button>
      </div>
    </form>
  </page>
</template>
