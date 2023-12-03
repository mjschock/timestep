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
import { computed, defineComponent } from 'vue';
import { useRouter } from 'vue-router';

// import SignInComponent from 'src/components/SignInComponent.vue';
// import SignUpComponent from'src/components/SignUpComponent.vue';
import SignOutComponent from 'src/components/SignOutComponent.vue';

import { nhost } from 'src/boot/nhost';

export default defineComponent({
  name: 'MainLayout',

  components: {
    SignOutComponent,
  },

  setup() {
    const router = useRouter();

    const envId = computed(() => (router.currentRoute.value.params.envId || '').toString())
    const agentId = computed(() => (router.currentRoute.value.params.agentId || '').toString())
    const { isAuthenticated, isLoading } = nhost.auth.getAuthenticationStatus()

    nhost.auth.onAuthStateChanged((event, session) => {
      console.log(
        `The auth state has changed. State is now ${event} with session: ${session}`
      )
    })

    const toolbarOnclick = () => {
      router.push('/')
    }

    return {
      agentId,
      envId,
      isAuthenticated,
      toolbarOnclick,
    }
  }
});
</script>
