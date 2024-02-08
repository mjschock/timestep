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
  name: 'AgentsPage',

  components: {
    TaskComponent
  },

  setup () {
    return {
      tasks: [
        { input: 'Agent 1', task_id: '1' },
        { input: 'Agent 2', task_id: '2' },
        { input: 'Agent 3', task_id: '3' }
      ] as Task[]
    }
  }
})
</script>
