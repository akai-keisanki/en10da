<script setup>
  const config = useRuntimeConfig()
  const {signIn} = useAuth()
  const {post} = useAPI()

  const emailLogin = ref(false)

  const handle = ref('')
  const password = ref('')
  const emailCode = ref('')

  const error = ref(null)

  async function makeLogin() {
    try {
      let resp = null

      if (emailLogin.value)
      {
        const signInPath = config.public.auth.provider.endpoints.signIn.path
        try {
          config.public.auth.provider.endpoints.signIn.path = '/user/login/email'

          resp = await signIn(
            {
              handle: handle.value.trim(),
              email_code: emailCode.value.trim()
            },
            {redirect: false}
          )
        } finally {
          config.public.auth.provider.endpoints.signIn.path = signInPath
        }
      }
      else
        resp = await signIn(
          {
            handle: handle.value.trim(),
            password: password.value
          },
          {redirect: false}
        )

      if (!resp || resp.error)
        error.value = 'Erro no login! Confira o identificador e a senha.'
      else
        error.value = 'Login completo com sucesso!'
    } catch (e) {
      console.log(e)
      if (e.response)
        error.value = `${e.response.status}\n${e.response.data}`
      else
        error.value = e
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
    <form @submit.prevent=makeLogin()>
      <div class=max-500>
        <Transition name=fade>
          <div class='infobox' v-show=error>
            <p>
              {{error}}
            </p>
          </div>
        </Transition>
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
            <input id=password type=password placeholder=******** :required='emailLogin ? null : true' v-model=password>
          </div>
        </Transition>
        <Transition name=fade>
          <NuxtLink to=/send_email_code><div class='infobox link' v-show=emailLogin>
            <p>
              Caso não possua um código de e-mail, clique aqui para encaminhar-se ao formulário de envio deste código.
            </p>
          </div></NuxtLink>
        </Transition>
        <Transition name=fade>
          <div class='input' v-show=emailLogin>
            <label for=email_code>Código do e-mail</label>
            <input id=email_code placeholder=... :required='emailLogin ? true : null' v-model=emailCode>
          </div>
        </Transition>
        <button type=submit class=highlight>Login</button>
      </div>
    </form>
  </page>
</template>
