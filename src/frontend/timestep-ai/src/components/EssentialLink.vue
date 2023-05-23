<template>
  <q-item
    clickable
    tag="a"
    target="_blank"
    :href="link"
  >
    <q-item-section
      v-if="icon"
      avatar
    >
      <!-- <q-icon :name="icon" /> -->
      <q-skeleton type="QAvatar" />
    </q-item-section>

    <q-item-section>
      <q-item-label>
        <!-- {{ title }} -->
        <q-skeleton type="text" width="35%" />
      </q-item-label>
      <q-item-label caption>
        <!-- {{ caption }} -->
        <q-skeleton type="text" />
      </q-item-label>
    </q-item-section>
  </q-item>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'EssentialLink',
  props: {
    title: {
      type: String,
      required: true
    },

    caption: {
      type: String,
      default: ''
    },

    link: {
      type: String,
      default: '#'
    },

    icon: {
      type: String,
      default: ''
    }
  }
});
</script>
