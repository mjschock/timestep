<template>
  <q-page padding>
    <q-card>
      <q-card-section>
        Signed out
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'SignOutPage',
  setup () {
    const router = useRouter()

    setTimeout(() => {
      router.push('/')
    }, 2_500)
  }
})
</script>
