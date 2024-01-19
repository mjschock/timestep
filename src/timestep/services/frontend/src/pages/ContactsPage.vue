<template>
  <q-table
    title="Contacts"
    :rows="contacts"
    :columns="columns"
    row-key="id"
    :selected-rows-label="getSelectedString"
    selection="single"
    v-model:selected="selected"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'ContactsPage',
  setup () {
    const columns = [
      {
        align: 'left',
        field: contact => contact.name,
        label: 'Name',
        name: 'name',
        sortable: true
      },
    ]
    const contacts = ref([])
    const selected = ref([])

    return {
      columns,
      contacts,
      selected,
      getSelectedString () {
        // return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${documents.length}`
        return selected.value.length === 0 ? '' : `${selected.value.length} contact${selected.value.length > 1 ? 's' : ''} selected of ${accounts.value.length}`
      },
    }
  }
})
</script>
