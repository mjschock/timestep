<template>
  <q-page padding>
    <!-- <h1>Tasks</h1> -->
    <ol>
      <TaskComponent
        v-for="task in tasks"
        :key="task.task_id"
        :task="task"
      />
    </ol>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { Task } from 'agent-protocol'

import TaskComponent from 'components/TaskComponent.vue'

export default defineComponent({
  name: 'ArtifactsPage',

  components: {
    TaskComponent
  },

  setup () {
    return {
      tasks: [
        { input: 'Do the laundry', task_id: '1' },
        { input: 'Wash the dishes', task_id: '2' },
        { input: 'Clean the bathroom', task_id: '3' }
      ] as Task[]
    }
  }
})
</script>
