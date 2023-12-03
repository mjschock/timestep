<template>
  <!-- <q-page padding> -->
  <q-tab-panel name="sign-in">
    <oauth-links />
    <q-separator />
    <q-card-actions vertical>
      <q-btn
        color="primary"
        icon="mdi-lock"
        label="Continue with passwordless email"
        to="/signin/passwordless"
        type="button"
      />
      <q-btn
        color="primary"
        label="Continue with email + password"
        to="/signin/email-password"
        type="button"
      />
    </q-card-actions>
  </q-tab-panel>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import OauthLinks from 'src/components/OAuthLinks.vue'

export default defineComponent({
  name: 'SignInMain',
  components: {
    OauthLinks
  },
  setup (props) {
    console.log('props', props)
    return {}
  }
})
</script>
