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
  name: 'AccountsPage',

  components: {
    TaskComponent
  },

  setup () {
    return {
      tasks: [
        { input: 'Account 1', task_id: '1' },
        { input: 'Account 2', task_id: '2' },
        { input: 'Account 3', task_id: '3' }
      ] as Task[]
    }
  }
})
</script>
