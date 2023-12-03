<template>
  <!-- <q-page padding> -->
    <oauth-links />
    <q-separator />
    <q-card-actions vertical>
      <q-btn
        color="primary"
        icon="mdi-lock"
        label="Continue with passwordless email"
        to="/signup/passwordless"
        type="button"
      />
      <q-btn
        color="primary"
        label="Continue with email + password"
        to="/signup/email-password"
        type="button"
      />
    </q-card-actions>
  <!-- </q-page> -->
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import OauthLinks from 'src/components/OAuthLinks.vue'

export default defineComponent({
  name: 'SignUpMain',
  components: {
    OauthLinks
  },
  setup () {
    return {}
  }
})
</script>
