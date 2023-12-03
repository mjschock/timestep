<template>
  <email-passwordless />
  <q-card-actions vertical>
    <q-btn
      color="primary"
      label="&#8592; Other Sign up Options"
      to="/signup"
    />
  </q-card-actions>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import EmailPasswordless from 'src/components/EmailPasswordlessForm.vue'

export default defineComponent({
  name: 'SignUpEmailPaswordless',
  components: {
    EmailPasswordless
  },
})
</script>
