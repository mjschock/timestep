<template>
  <q-card-actions vertical>
    <q-btn
      color="primary"
      icon="mdi-github"
      label="Continue with GitHub"
      no-caps
      type="button"
      :disable="true"
    />
    <q-btn
      color="primary"
      icon="mdi-google"
      label="Continue with Google"
      no-caps
      type="button"
      :disable="true"
    />
    <q-btn
      color="primary"
      icon="mdi-facebook"
      label="Continue with Facebook"
      no-caps
      type="button"
      :disable="true"
    />
  </q-card-actions>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { nhost } from 'src/boot/nhost';

export default defineComponent({
  name: 'OAuthLinks',
  setup (props) {
    // console.log('props', props)
    return {}
  }
})
</script>
