<template>
  <div>
    <q-btn label="Sign out" type="button" color="primary" @click="signOutHandler" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

import { nhost } from 'src/boot/nhost';

export default defineComponent({
  name: 'SignOutComponent',

  setup() {
    const router = useRouter()
    const signOutHandler = async () => {
      console.log('signOutHandler')
      await nhost.auth.signOut({all: true})
      router.replace('/')
    }

    return {
      signOutHandler,
    }
  }
})
</script>
