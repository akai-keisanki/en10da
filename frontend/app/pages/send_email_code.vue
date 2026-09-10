<script setup>
  const {post} = useAPI()

  const handle = ref('')
  const email = ref('')

  const error = ref(null)

  async function requestEmail() {
    try {
      const request = await post('user/request-email-code',
          {
            handle: handle.value,
            email: email.value
          }
        )
      console.log(request)
      error.value = request.data.msg
    } catch (e) {
      console.log(e)
      error.value = e
    }
  }
</script>

<template>
  <page title='Send Email'>
    <form @submit.prevent=requestEmail()>
      <div class=max-500>
        <Transition name=fade>
          <div class=infobox v-show=error>
            <p>
              {{error}}
            </p>
          </div>
        </Transition>
        <div class=input>
          <label for=handle>Identificador</label>
          <input id=handle type=text placeholder=identificador required v-model=handle>
        </div>
        <div class=input>
          <label for=email>E-mail</label>
          <input id=email type=email placeholder=e-mail required v-model=email>
        </div>
        <button type=submit class=highlight>Enviar código</button>
      </div>
    </form>
  </page>
</template>
