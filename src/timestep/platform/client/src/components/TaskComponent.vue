<template>
  <li>{{ task.input }}</li>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { Task } from 'agent-protocol'

export default defineComponent({
  name: 'TaskComponent',
  props: {
    task: {
      required: true,
      type: Object as () => Task
    }
  }
})
</script>
