<template>
  <q-table
    title="Agents"
    :rows="agents"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />

  <q-card-actions vertical>
    <q-form @submit="createAgent">
      <q-card-actions vertical>
        <q-btn
          color="primary"
          disable
          label="Create agent"
          no-caps
          type="submit"
        />
      </q-card-actions>
    </q-form>
  </q-card-actions>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { api } from 'boot/axios'
import { nhost } from 'src/boot/nhost';
import { useQuasar } from 'quasar'
import { on } from 'events';

export default defineComponent({
  name: 'AgentsPage',
  setup () {
    const columns = [
      {
        align: 'left',
        field: agent => agent.name,
        label: 'Name',
        name: 'name',
        sortable: true
      },
    ]
    const agents = ref([])
    const selected = ref([])
    const $q = useQuasar()

    const createAgent = async (e: Event) => {
      e.preventDefault()

      const notif = $q.notify({
        group: false, // required to be updatable
        position: 'top',
        timeout: 0, // we want to be in control when it gets dismissed
        spinner: true,
        message: 'Creating agent...',
        // caption: '0%'
      })

      api.post(
        `/agents`,
        {},
        {
          headers: {
            'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
          },
        },
      )
        .then((response) => {
          notif({
            color: 'positive',
            message: 'Agent created',
            position: 'top',
            icon: 'check_circle',
            spinner: false,
            timeout: 5000,
          })
        })
        .catch((error) => {
          notif({
            color: 'negative',
            message: error.message,
            position: 'top',
            icon: 'report_problem',
            spinner: false,
            timeout: 5000,
          })
        })
    }
  
    const getAgents = async () => {
      api.get(
        `/agents`,
        {
          headers: {
            'Authorization': `Bearer ${nhost.auth.getAccessToken()}`,
          },
        },
      )
        .then((response) => {
          // agents.value = response.data
          console.log(response.data)
          agents.value = response.data.agents

        })
        .catch((error) => {
          console.log(error)
          // notif({
          //   color: 'negative',
          //   message: error.message,
          //   position: 'top',
          //   icon: 'report_problem',
          //   spinner: false,
          //   timeout: 5000,
          // })
        })
    }

    onMounted(() => {
      getAgents()
    })

    return {
      columns,
      createAgent,
      agents,
      selected,
      getSelectedString () {
        // return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${documents.length}`
        return selected.value.length === 0 ? '' : `${selected.value.length} agent${selected.value.length > 1 ? 's' : ''} selected of ${agents.value.length}`
      },
    }
  }
})
</script>
