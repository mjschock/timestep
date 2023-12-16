<template>
  <q-card-actions vertical>
    <q-form @submit="signUp">
      <q-card-actions vertical>
        <q-input
          v-model="email"
          label="Email"
          type="email"
        />
        <q-input
          v-model="password"
          label="Password"
          type="password"
        />
        <q-btn
          color="primary"
          label="Sign up"
          no-caps
          type="submit"
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>
  <!-- <q-separator /> -->
  <!-- <oauth-links/> -->
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { nhost } from 'src/boot/nhost';
import { useQuasar } from 'quasar'

export default defineComponent({
  name: 'SignUpPage',
  setup () {
    const email = ref('')
    const isPwd = ref(true)
    const password = ref('')
    const $q = useQuasar()

    const signUp = async (e: Event) => {
      e.preventDefault()

      const notif = $q.notify({
        group: false, // required to be updatable
        position: 'top',
        timeout: 0, // we want to be in control when it gets dismissed
        spinner: true,
        message: 'Signing up...',
        // caption: '0%'
      })

      const params: SignUpParams = {
        email: email.value,
        password: password.value,
      }
      const resp: NhostSessionResponse = await nhost.auth.signUp(params)
      const error: AuthErrorPayload | null = resp.error
      const session: NhostSession | null = resp.session

      if (error) {
        // console.log('error', error)
        // submitResult.value.error = error.error
        // submitResult.value.message = error.message
        // submitResult.value.status = error.status
        // $q.notify({
        //   color: 'negative',
        //   message: error.message,
        //   position: 'top',
        //   icon: 'report_problem',
        // })
        notif({
          color: 'negative',
          message: error.message,
          position: 'top',
          icon: 'report_problem',
          spinner: false,
          timeout: 5000,
        })
      } else {
        // $q.notify({
        //   color: 'positive',
        //   multiLine: true,
        //   message: 'Please click the link in the email we sent you to verify your account',
        //   position: 'top',
        //   icon: 'check_circle',
        // })
        notif({
          color: 'positive',
          multiLine: true,
          message: 'Please click the link in the email we sent you to verify your account',
          position: 'top',
          icon: 'check_circle',
          spinner: false,
          timeout: 5000,
        })
      }

      // if (session) {
      //   console.log('session', session)
      // }
    }

    return {
      email,
      isPwd,
      password,
      signUp,
    }
  }
})
</script>
