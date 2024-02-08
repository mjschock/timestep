<template>
  <q-page>
    <div class="q-pa-md">
      <q-card
        v-if="!isSignedIn"
        class="my-card"
        flat
        bordered
      >
        <q-tabs v-model="tab">
          <q-tab
            label="Sign in"
            name="sign-in"
          />
          <q-tab
            label="Sign up"
            name="sign-up"
          />
        </q-tabs>

        <q-separator />

        <q-tab-panels
          v-model="tab"
        >
          <q-tab-panel name="sign-in">
            <sign-in-component />
          </q-tab-panel>

          <q-tab-panel name="sign-up">
            <sign-up-component />
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import { AuthChangeEvent } from '@nhost/nhost-js'

import { nhost } from 'src/boot/nhost'
import SignInComponent from 'src/components/SignInComponent.vue'
import SignUpComponent from 'src/components/SignUpComponent.vue'

export default defineComponent({
  name: 'IndexPage',

  components: {
    SignInComponent,
    SignUpComponent
  },

  setup () {
    const isSignedIn = ref(false)

    const { isAuthenticated } = nhost.auth.getAuthenticationStatus()

    isSignedIn.value = isAuthenticated

    nhost.auth.onAuthStateChanged((event: AuthChangeEvent) => {
      isSignedIn.value = event === 'SIGNED_IN'
    })

    return {
      isSignedIn,
      tab: ref('sign-in')
    }
  }
})
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
</style>
