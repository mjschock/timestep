<template>
  <!-- <q-page padding> -->
    <q-form @submit="handleSignIn">
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
          label="Sign in"
          type="submit"
          :disabled="isLoading"
          :loading="isLoading"
        />
      </q-card-actions>
    </q-form>
    <q-card-actions vertical>
      <q-btn
        color="primary"
        label="&#8592; Other Sign-in Options"
        to="/signin"
      />
    </q-card-actions>
  <!-- </q-page> -->
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { AuthErrorPayload, Mfa, NhostSession, SignInParams, SignInResponse } from '@nhost/nhost-js';

import { nhost } from 'src/boot/nhost'

export default defineComponent({
  name: 'SignInEmailPasword',
  setup () {
    const email = ref('')
    const password = ref('')

    const handleSignIn = async (e: Event) => {
      e.preventDefault()

      const params: SignInParams = {
        email: email.value,
        password: password.value,
      }
      const resp: SignInResponse = await nhost.auth.signIn(params)
      const error: AuthErrorPayload | null = resp.error
      const mfa: Mfa | null = resp.mfa
      const session: NhostSession | null = resp.session

      if (error) {
        console.log('error', error)
        // submitResult.value.error = error.error
        // submitResult.value.message = error.message
        // submitResult.value.status = error.status
      }

      if (mfa) {
        console.log('mfa', mfa)
      }

      if (session) {
        console.log('session', session)
      }
    }

    return {
      email,
      handleSignIn,
      password
    }
  }
})
</script>
