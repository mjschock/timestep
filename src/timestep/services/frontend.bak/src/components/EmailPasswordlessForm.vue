<template>
  <q-form @submit="handleSignIn">
    <q-card-actions vertical>
      <q-input v-model="email" label="Email" type="email" />
      <q-btn
        color="primary"
        label="Continue with email"
        type="submit"
        :disabled="isLoading"
        :loading="isLoading"
      />
    </q-card-actions>
  </q-form>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import {
  AuthErrorPayload,
  Mfa,
  NhostSession,
  SignInParams,
  SignInResponse,
} from '@nhost/nhost-js';

import { nhost } from 'src/boot/nhost';

const router = useRouter();

export default defineComponent({
  name: 'SignInEmailPaswordlessForm',
  setup() {
    const email = ref('');

    const handleSignIn = async (e: Event) => {
      e.preventDefault();

      const params: SignInParams = {
        email: email.value,
      };
      const resp: SignInResponse = await nhost.auth.signIn(params);
      const error: AuthErrorPayload | null = resp.error;
      const mfa: Mfa | null = resp.mfa;
      const session: NhostSession | null = resp.session;

      if (error) {
        console.log('error', error);
        // submitResult.value.error = error.error
        // submitResult.value.message = error.message
        // submitResult.value.status = error.status
      }

      if (mfa) {
        console.log('mfa', mfa);
      }

      if (session) {
        console.log('session', session);
      }
    };

    return {
      email,
      handleSignIn,
    };
  },
});
</script>
