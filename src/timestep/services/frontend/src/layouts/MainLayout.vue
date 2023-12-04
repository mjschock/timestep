<template>
  <q-layout view="hHh LpR fFf">
    <q-header>
      <q-toolbar>
        <q-toolbar-title class="cursor-pointer q-hoverable" @click="toolbarOnclick">
          Timestep AI
        </q-toolbar-title>
        <!-- <q-breadcrumbs active-color="grey">
          <q-breadcrumbs-el label="envs" to="/envs" />
          <q-breadcrumbs-el :label="envId" :to="`/envs/${envId}`" :visible="false" />
          <q-breadcrumbs-el label="agents" :to="`/envs/${envId}/agents`"/>
          <q-breadcrumbs-el :label="agentId" />
        </q-breadcrumbs> -->
        <SignOutComponent v-if="isAuthenticated"/>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer>
      <q-toolbar>
        <q-toolbar-title>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

// import SignInComponent from 'src/components/SignInComponent.vue';
// import SignUpComponent from'src/components/SignUpComponent.vue';
import SignOutComponent from 'src/components/SignOutComponent.vue';

import { AuthChangeEvent, AuthChangedFunction, AuthErrorPayload, ChangePasswordParams, ChangePasswordResponse, Mfa, NhostClient, NhostSession, NhostSessionResponse, RedirectOption, ResetPasswordParams, ResetPasswordResponse, SendVerificationEmailParams, SendVerificationEmailResponse, SignInParams, SignInResponse, SignUpParams } from '@nhost/nhost-js'

import { nhost } from 'src/boot/nhost';

export default defineComponent({
  name: 'MainLayout',

  components: {
    SignOutComponent,
  },

  setup() {
    const router = useRouter();
    const isAuthenticated = ref(false)
    const isLoading = ref(false)
    const envId = computed(() => (router.currentRoute.value.params.envId || '').toString())
    const agentId = computed(() => (router.currentRoute.value.params.agentId || '').toString())
    // const { isAuthenticated, isLoading } = nhost.auth.getAuthenticationStatus()

    nhost.auth.onAuthStateChanged((event: AuthChangeEvent, session: NhostSession | null) => {
      console.log(
        `The auth state has changed. State is now ${event} with session: ${session}`
      )

      if (event === "SIGNED_IN") {
        isAuthenticated.value = true
      } else {
        isAuthenticated.value = false
      }
    })

    const toolbarOnclick = () => {
      router.push('/')
    }

    return {
      agentId,
      envId,
      isAuthenticated,
      isLoading,
      toolbarOnclick,
    }
  }
});
</script>
