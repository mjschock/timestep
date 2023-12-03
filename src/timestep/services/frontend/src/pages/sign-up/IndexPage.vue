<template>
  <q-page padding>
    <q-card>
      <q-tabs v-model="tab">
        <q-tab label="Sign in" name="sign-in" to="/signin"/>
        <q-tab label="Sign up" name="sign-up" to="/signup"/>
      </q-tabs>
      <q-card-section>
        <router-view />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'SignUpPage',
  setup () {
    return {
      tab: ref('sign-up')
    }
  }
})
</script>
