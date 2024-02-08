<template>
  <q-header
    elevated
    :class="$q.dark.isActive ? 'bg-secondary' : 'bg-black'"
  >
    <q-toolbar>
      <q-btn
        flat
        round
        dense
        icon="menu"
        @click="($event) => onMenuButtonClick($event)"
      />

      <q-toolbar-title
        class="cursor-pointer q-hoverable"
        @click="onTitleClick"
      >
        {{ title }}
      </q-toolbar-title>

      <!-- <div>Quasar v{{ $q.version }}</div> -->
      <sign-out-component v-if="isSignedIn" />
    </q-toolbar>
  </q-header>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import SignOutComponent from 'src/components/SignOutComponent.vue'

export default defineComponent({
  name: 'HeaderComponent',

  components: {
    SignOutComponent
  },

  props: {
    isSignedIn: {
      required: true,
      type: Boolean
    },

    onMenuButtonClick: {
      required: true,
      type: Function
    },

    onTitleClick: {
      required: true,
      type: Function
    },

    title: {
      required: true,
      type: String
    }
  }
})
</script>
